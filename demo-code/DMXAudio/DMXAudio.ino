/*
 * DMXAudio v1.0
 * by rglenn 2023-03-24
 * Copyright (c) 2023
 */

#include <TeensyDMX.h>
namespace teensydmx = ::qindesign::teensydmx;

#include "commands.h"

#include <Audio.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SerialFlash.h>

// GUItool: begin automatically generated code
AudioPlaySdWav           playSdWav1;     //xy=333,245
AudioPlaySdWav           playSdWav3;     //xy=334,374
AudioPlaySdWav           playSdWav2;     //xy=340,302
AudioPlaySdWav           playSdWav6;     //xy=349,613
AudioPlaySdWav           playSdWav4;     //xy=355,456
AudioPlaySdWav           playSdWav5;     //xy=361,532
AudioPlaySdWav           playSdWav7;     //xy=398,678
AudioPlaySdWav           playSdWav8;     //xy=425,739
AudioMixer4              mixer3;         //xy=761,589
AudioMixer4              mixer1;         //xy=764,288
AudioMixer4              mixer4;         //xy=776,714
AudioMixer4              mixer2;         //xy=797,401
AudioMixer4              mixer5;         //xy=1007,418
AudioMixer4              mixer6;         //xy=1010,559
AudioOutputI2S           i2s1;           //xy=1208,496
AudioConnection          patchCord1(playSdWav1, 0, mixer1, 0);
AudioConnection          patchCord2(playSdWav1, 1, mixer2, 0);
AudioConnection          patchCord3(playSdWav3, 0, mixer1, 2);
AudioConnection          patchCord4(playSdWav3, 1, mixer2, 2);
AudioConnection          patchCord5(playSdWav2, 0, mixer1, 1);
AudioConnection          patchCord6(playSdWav2, 1, mixer2, 1);
AudioConnection          patchCord7(playSdWav6, 0, mixer3, 1);
AudioConnection          patchCord8(playSdWav6, 1, mixer4, 1);
AudioConnection          patchCord9(playSdWav4, 0, mixer1, 3);
AudioConnection          patchCord10(playSdWav4, 1, mixer2, 3);
AudioConnection          patchCord11(playSdWav5, 0, mixer3, 0);
AudioConnection          patchCord12(playSdWav5, 1, mixer4, 0);
AudioConnection          patchCord13(playSdWav7, 0, mixer3, 2);
AudioConnection          patchCord14(playSdWav7, 1, mixer4, 2);
AudioConnection          patchCord15(playSdWav8, 0, mixer3, 3);
AudioConnection          patchCord16(playSdWav8, 1, mixer4, 3);
AudioConnection          patchCord17(mixer3, 0, mixer5, 1);
AudioConnection          patchCord18(mixer1, 0, mixer5, 0);
AudioConnection          patchCord19(mixer4, 0, mixer6, 1);
AudioConnection          patchCord20(mixer2, 0, mixer6, 0);
AudioConnection          patchCord21(mixer5, 0, i2s1, 0);
AudioConnection          patchCord22(mixer6, 0, i2s1, 1);
// GUItool: end automatically generated code

// DMX receiver object
teensydmx::Receiver dmxRx{ Serial7 };

typedef struct
{
	uint32_t flags;
	uint16_t track;
	uint8_t vol;
	AudioMixer4 *mixerL;
	AudioMixer4 *mixerR;
	uint8_t channel;
	AudioPlaySdWav *sdwav;
	uint32_t startStamp;
} dmxAudioPlayer_t;

typedef enum
{
	DMX_AUDIO_PLAYER_FLAG_PLAYING = 0x00000001,
	DMX_AUDIO_PLAYER_FLAG_LOCKED = 0x00000002,
	DMX_AUDIO_PLAYER_FLAG_LOOPING = 0x00000004,
	DMX_AUDIO_PLAYER_FLAG_PAUSED = 0x00000008,
} dmxAudioPlayerFlags_t;

static const uint8_t numPlayers = 8;
static uint16_t myAddress = 0;

static dmxAudioPlayer_t players[numPlayers];

static void players_setup(void)
{
	for (uint8_t i = 0; i < numPlayers; i++)
	{
		players[i].flags = 0;
		players[i].track = 0;
		players[i].vol = 0;
	}
	players[0].mixerL = &mixer1;
	players[0].mixerR = &mixer2;
	players[0].channel = 0;
	players[0].sdwav = &playSdWav1;
	players[1].mixerL = &mixer1;
	players[1].mixerR = &mixer2;
	players[1].channel = 1;
	players[1].sdwav = &playSdWav2;
	players[2].mixerL = &mixer1;
	players[2].mixerR = &mixer2;
	players[2].channel = 2;
	players[2].sdwav = &playSdWav3;
	players[3].mixerL = &mixer1;
	players[3].mixerR = &mixer2;
	players[3].channel = 3;
	players[3].sdwav = &playSdWav4;
	players[4].mixerL = &mixer3;
	players[4].mixerR = &mixer4;
	players[4].channel = 0;
	players[4].sdwav = &playSdWav5;
	players[5].mixerL = &mixer3;
	players[5].mixerR = &mixer4;
	players[5].channel = 1;
	players[6].sdwav = &playSdWav6;
	players[6].mixerL = &mixer3;
	players[6].mixerR = &mixer4;
	players[6].channel = 2;
	players[6].sdwav = &playSdWav7;
	players[7].mixerL = &mixer3;
	players[7].mixerR = &mixer4;
	players[7].channel = 3;
	players[7].sdwav = &playSdWav8;
}

uint8_t lastCommand = 0;

void setup()
{
	// Set up serial port for debugging
	Serial.begin(115200);
	Serial.println("DMXAudio starting");

	// set up and read the device address
	address_setup();
	myAddress = address_get();
	Serial.printf("Address is %d\n", myAddress);

	players_setup();

	if (!SD.begin(BUILTIN_SDCARD))
	{
		while(1)
		{
			Serial.println("SD Begin failed");
			delay(500);
		}
	}

	// Start the receiver
	dmxRx.begin();

	lastCommand = dmxRx.get(myAddress);
}

static void stopAllPlayers(void)
{
	for (uint8_t i = 0; i < numPlayers; i++)
	{
		Serial.printf("stopAllPlayers: Stopping player %d\n", i);
		players[i].sdwav->stop();
		players[i].flags = 0;
		players[i].vol = 0;
		players[i].track = 0;
	}
}

static uint8_t findAvailablePlayer(bool allowLocked)
{
	uint8_t oldestIdx;
	uint32_t oldestStamp;

	Serial.printf("findAvailablePlayer: looking for player, locked are %s\n", allowLocked ? "allowed" : "not allowed");

	for (uint8_t i = 0; i < numPlayers; i++)
	{
		if (!(players[i].flags & DMX_AUDIO_PLAYER_FLAG_PLAYING))
		{
			if (!(players[i].flags & DMX_AUDIO_PLAYER_FLAG_LOCKED))
			{
				Serial.printf("findAvailablePlayer: found player %d not playing\n", i);
				return i;
			}
		}
	}
	
	oldestIdx = 255;
	oldestStamp = UINT32_MAX;
	// otherwise find the oldest playing one, and use it
	for (uint8_t i = 0; i < numPlayers; i++)
	{
		if (!(players[i].flags & DMX_AUDIO_PLAYER_FLAG_LOCKED) || allowLocked)
		{
			if (players[i].startStamp < oldestStamp)
			{
				Serial.printf("findAvailablePlayer: found oldest unlocked player %d, started at %lu\n", i, players[i].startStamp);
				oldestStamp = players[i].startStamp;
				oldestIdx = i;
			}
		}
	}

	Serial.printf("findAvailablePlayer: found player %d to replace\n", oldestIdx);

	return oldestIdx;
}

static uint8_t findPlayerWithTrack(uint32_t track)
{
	Serial.printf("findPlayerWithTrack: Finding player with track %lu\n", track);
	for (uint8_t i = 0; i < numPlayers; i++)
	{
		if ((players[i].track == track) && (players[i].flags & DMX_AUDIO_PLAYER_FLAG_PLAYING))
		{
			Serial.printf("findPlayerWithTrack: Found player %d\n", i);
			return i;
		}
	}
	Serial.printf("findPlayerWithTrack: Did not find player\n");
	return 255;
}

void setPlayerVolume(uint8_t playerIdx, uint8_t volume)
{
	float volume_f;
	volume_f = ((float) volume) / (128.0);

	if (playerIdx != 255)
	{
		if (players[playerIdx].flags & DMX_AUDIO_PLAYER_FLAG_PLAYING)
		{
			Serial.printf("setPlayerVolume: Setting player %d volume to %d\n", playerIdx, volume);
			players[playerIdx].vol = volume;
			players[playerIdx].mixerL->gain(players[playerIdx].channel, volume_f);
			players[playerIdx].mixerR->gain(players[playerIdx].channel, volume_f);
		}
	}
}

void stopPlayer(uint8_t playerIdx)
{
	if (playerIdx != 255)
	{
		Serial.printf("stopPlayer: Stopping player %d\n", playerIdx);
		players[playerIdx].sdwav->stop();
		players[playerIdx].flags = 0;
		players[playerIdx].vol = 0;
		players[playerIdx].track = 0;
	}
}

void pausePlayer(uint8_t playerIdx)
{
	if (playerIdx != 255)
	{
		if ((players[playerIdx].flags & DMX_AUDIO_PLAYER_FLAG_PLAYING) && !(players[playerIdx].sdwav->isPaused()))
		{
			Serial.printf("pausePlayer: Pausing player %d\n", playerIdx);
			players[playerIdx].flags |= DMX_AUDIO_PLAYER_FLAG_PAUSED;
			players[playerIdx].sdwav->togglePlayPause();
		}
	}
}

void resumePlayer(uint8_t playerIdx)
{
	if (playerIdx != 255)
	{
		if ((players[playerIdx].flags & DMX_AUDIO_PLAYER_FLAG_PLAYING) && (players[playerIdx].sdwav->isPaused()))
		{
			Serial.printf("resumePlayer: Resuming player %d\n", playerIdx);
			players[playerIdx].flags &= ~DMX_AUDIO_PLAYER_FLAG_PAUSED;
			players[playerIdx].sdwav->togglePlayPause();
		}
	}
}

void startPlayer(uint8_t playerIdx, uint32_t track, uint8_t volume, uint8_t flags)
{
	char trackname[16];
	float volume_f;
	volume_f = ((float) volume) / (128.0);

	snprintf(trackname, 15, "%lu.wav", track);

	if (playerIdx != 255)
	{
		// if file does not exist, die
		if (!SD.exists(trackname))
		{
			Serial.printf("startPlayer: File %s not found\n", trackname);
			return;
		}

		Serial.printf("startPlayer: Starting file %s on player %d\n", trackname, playerIdx);
		players[playerIdx].flags = flags | DMX_AUDIO_PLAYER_FLAG_PLAYING;
		players[playerIdx].track = track;
		players[playerIdx].vol = volume;
		players[playerIdx].mixerL->gain(players[playerIdx].channel, volume_f);
		players[playerIdx].mixerR->gain(players[playerIdx].channel, volume_f);
		players[playerIdx].sdwav->play(trackname);
		players[playerIdx].startStamp = millis();
	}
}

void loop()
{
	uint8_t newCommand;
	uint16_t newTrackNum;
	uint8_t newVolume;
	uint8_t newPlayer;

	newCommand = dmxRx.get(myAddress);
	if (lastCommand != newCommand)
	{
		lastCommand = newCommand;
		newTrackNum = dmxRx.get(myAddress + 1) + (dmxRx.get(myAddress + 2) << 8);
		newVolume = dmxRx.get(myAddress + 3);

		switch (newCommand) {
			case DMX_AUDIO_COMMAND_NOP:
			{
				// do nothing
				break;
			}
			case DMX_AUDIO_COMMAND_STOP_ALL:
			{
				// stop all players
				Serial.println("loop: received STOP_ALL command");
				stopAllPlayers();
				break;
			}
			case DMX_AUDIO_COMMAND_PLAY_ONCE_POLY:
			{
				Serial.printf("loop: received PLAY_ONCE_POLY command, track is %lu, volume is %d\n", newTrackNum, newVolume);

				// find the oldest non-locked player
				newPlayer = findAvailablePlayer(false);

				if (newPlayer == 255)
				{
					break;
				}

				Serial.printf("loop: found player %d\n", newPlayer);

				// stop it if not stopped
				stopPlayer(newPlayer);

				// configure it for the specified track and volume
				startPlayer(newPlayer, newTrackNum, newVolume, 0);
				break;
			}
			case DMX_AUDIO_COMMAND_PLAY_LOOP_POLY:
			{
				Serial.printf("loop: received PLAY_LOOP_POLY command, track is %lu, volume is %d\n", newTrackNum, newVolume);

				// find the oldest non-locked player
				newPlayer = findAvailablePlayer(false);

				if (newPlayer == 255)
				{
					break;
				}

				Serial.printf("loop: found player %d\n", newPlayer);

				// stop it if not stopped
				stopPlayer(newPlayer);

				// configure it for the specified track and volume, and looping
				startPlayer(newPlayer, newTrackNum, newVolume, DMX_AUDIO_PLAYER_FLAG_LOOPING);
				break;
			}
			case DMX_AUDIO_COMMAND_PLAY_ONCE_MONO:
			{
				Serial.printf("loop: received PLAY_ONCE_MONO command, track is %lu, volume is %d\n", newTrackNum, newVolume);

				// stop all players
				stopAllPlayers();

				Serial.printf("loop: found player 0\n");

				// take player 0
				// configure it for the specified track and volume
				startPlayer(0, newTrackNum, newVolume, 0);
				break;
			}
			case DMX_AUDIO_COMMAND_PLAY_LOOP_MONO:
			{
				Serial.printf("loop: received PLAY_ONCE_LOOP command, track is %lu, volume is %d\n", newTrackNum, newVolume);

				// stop all players
				stopAllPlayers();

				Serial.printf("loop: found player 0\n");

				// take player 0
				// configure it for the specified track and volume, and looping
				startPlayer(0, newTrackNum, newVolume, DMX_AUDIO_PLAYER_FLAG_LOOPING);
				break;
			}
			case DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED:
			{
				Serial.printf("loop: received PLAY_ONCE_POLY_LOCKED command, track is %lu, volume is %d\n", newTrackNum, newVolume);

				// find the oldest non-locked player
				newPlayer = findAvailablePlayer(false);

				if (newPlayer == 255)
				{
					break;
				}

				Serial.printf("loop: found player %d\n", newPlayer);

				// stop it if not stopped
				stopPlayer(newPlayer);

				// configure it for the specified track and volume, and locked
				startPlayer(newPlayer, newTrackNum, newVolume, DMX_AUDIO_PLAYER_FLAG_LOCKED);
				break;
			}
			case DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED:
			{
				Serial.printf("loop: received PLAY_LOOP_POLY_LOCKED command, track is %lu, volume is %d\n", newTrackNum, newVolume);

				// find the oldest non-locked player
				newPlayer = findAvailablePlayer(false);

				if (newPlayer == 255)
				{
					break;
				}

				Serial.printf("loop: found player %d\n", newPlayer);

				// stop it if not stopped
				stopPlayer(newPlayer);

				// configure it for the specified track and volume, locked, and looping
				startPlayer(newPlayer, newTrackNum, newVolume, DMX_AUDIO_PLAYER_FLAG_LOCKED | DMX_AUDIO_PLAYER_FLAG_LOOPING);
				break;
			}
			case DMX_AUDIO_COMMAND_STOP:
			{
				Serial.printf("loop: received STOP command, track is %lu", newTrackNum);

				// find any player for the specified track
				uint8_t playerIdx = findPlayerWithTrack(newTrackNum);

				Serial.printf("loop: stopping track %d\n", playerIdx);

				// stop it
				stopPlayer(playerIdx);
				break;
			}
			case DMX_AUDIO_COMMAND_PAUSE:
			{
				Serial.printf("loop: received PAUSE command, track is %lu", newTrackNum);

				// find any player for the specified track
				uint8_t playerIdx = findPlayerWithTrack(newTrackNum);

				Serial.printf("loop: pausing track %d\n", playerIdx);

				// pause it
				pausePlayer(playerIdx);
				break;
			}
			case DMX_AUDIO_COMMAND_RESUME:
			{
				Serial.printf("loop: received RESUME command, track is %lu", newTrackNum);

				// find the first player for the specified track
				uint8_t playerIdx = findPlayerWithTrack(newTrackNum);

				Serial.printf("loop: resuming track %d\n", playerIdx);

				// resume it
				resumePlayer(playerIdx);
				break;
			}
			case DMX_AUDIO_COMMAND_TRACK_VOLUME:
			{
				Serial.printf("loop: received VOLUME command, track is %lu, volume is %d\n", newTrackNum, newVolume);

				// find the first player for the specified track
				uint8_t playerIdx = findPlayerWithTrack(newTrackNum);

				Serial.printf("loop: adjusting volume on track %d\n", playerIdx);

				// adjust voVolumelume
				setPlayerVolume(playerIdx, newVolume);
				break;
			}
			case DMX_AUDIO_COMMAND_MASTER_VOLUME:
			{
				Serial.printf("loop: received MASTER_VOLUME command, volume is %d\n", newVolume);

				// change master volume
				float volume_f;
				volume_f = ((float) newVolume) / (128.0);
				mixer5.gain(0, volume_f);
				mixer5.gain(1, volume_f);
				mixer5.gain(2, volume_f);
				mixer5.gain(3, volume_f);
				mixer6.gain(0, volume_f);
				mixer6.gain(1, volume_f);
				mixer6.gain(2, volume_f);
				mixer6.gain(3, volume_f);
				break;
			}
			default:
			{
				break;
			}
		}
	}

	// for each player
	for (uint8_t i = 0; i < numPlayers; i++)
	{
		// if looping, playing, and sdwav stopped, restart
		if ((players[i].flags & DMX_AUDIO_PLAYER_FLAG_PLAYING) && (players[i].flags & DMX_AUDIO_PLAYER_FLAG_LOOPING))
		{
			if (players[i].sdwav->isStopped())
			{
				Serial.printf("loop: restarting player %d\n", i);
				// restart it
				startPlayer(i, players[i].track, players[i].vol, players[i].flags);
			}
		}
		// if paused, leave it alone
		else if ((players[i].flags & DMX_AUDIO_PLAYER_FLAG_PLAYING) && (players[i].flags & DMX_AUDIO_PLAYER_FLAG_PAUSED))
		{
			// do nothing
		}
		// otherwise, if stopped, clear the player
		else if (players[i].flags & DMX_AUDIO_PLAYER_FLAG_PLAYING)
		{
			if (players[i].sdwav->isStopped())
			{
				Serial.printf("loop: stopping player %d\n", i);
				players[i].flags = 0;
				players[i].track = 0;
				players[i].vol = 0;
			}
		}
	}
}