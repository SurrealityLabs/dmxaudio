/*
 * DMXAudio v1.0
 * by rglenn 2023-03-24
 * Copyright (c) 2023
 */

#include <TeensyDMX.h>
namespace teensydmx = ::qindesign::teensydmx;


#include "commands.h"

// DMX receiver object
teensydmx::Receiver dmxRx{Serial7};

typedef struct {
  uint32_t flags;
  uint16_t track;
  uint8_t vol;
} dmxAudioPlayer_t;

typedef enum {
  DMX_AUDIO_PLAYER_FLAG_PLAYING = 0x00000001,
  DMX_AUDIO_PLAYER_FLAG_LOCKED  = 0x00000002,
  DMX_AUDIO_PLAYER_FLAG_LOOPING = 0x00000004,
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
}

void setup() {
  // Set up serial port for debugging
  Serial.begin(115200);
  Serial.println("DMXAudio starting");

  // set up and read the device address
  address_setup();
  myAddress = address_get();
  Serial.printf("Address is %d\n", myAddress);

  players_setup();
}

void loop() {
  // put your main code here, to run repeatedly:

}
