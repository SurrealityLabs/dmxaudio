#pragma once

typedef enum {
  DMX_AUDIO_COMMAND_NOP = 0x00, // do nothing
  DMX_AUDIO_COMMAND_STOP_ALL = 0x01, // immediately stop all playing tracks
  DMX_AUDIO_COMMAND_PLAY_ONCE_POLY = 0x02, // play a track with no repetition, leaving all other playing tracks playing. evict the oldest unlocked track. if no track is available, abort.
  DMX_AUDIO_COMMAND_PLAY_LOOP_POLY = 0x03, // play a track with repetition, leaving all other playing tracks playing. evict the oldest unlocked track. if no track is available, abort.
  DMX_AUDIO_COMMAND_PLAY_ONCE_MONO = 0x04, // play a track with no repetition. stop all other tracks.
  DMX_AUDIO_COMMAND_PLAY_LOOP_MONO = 0x05, // play a track with repetition. stop all other tracks.
  DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED = 0x06, // play a track with no repetition. do not allow the track to be evicted.
  DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED = 0x07, // play a track with repetition. do not allow the track to be evicted.
  DMX_AUDIO_COMMAND_STOP = 0x08, // stop the specified track, if playing
  DMX_AUDIO_COMMAND_PAUSE = 0x09, // pause the specified track, if playing
  DMX_AUDIO_COMMAND_RESUME = 0x0A, // resume the specified track, if playing
  DMX_AUDIO_COMMAND_TRACK_VOLUME = 0x0B, // set the volume of the specified track
  DMX_AUDIO_COMMAND_MASTER_VOLUME = 0x0C, // set the master volume
  NUM_DMX_AUDIO_COMMANDS
} dmxAudioCommands_t;
