#!/usr/bin/python

from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse

DMX_AUDIO_COMMAND_NOP = 0x00
DMX_AUDIO_COMMAND_STOP_ALL = 0x01
DMX_AUDIO_COMMAND_PLAY_ONCE_POLY = 0x02
DMX_AUDIO_COMMAND_PLAY_LOOP_POLY = 0x03
DMX_AUDIO_COMMAND_PLAY_ONCE_MONO = 0x04
DMX_AUDIO_COMMAND_PLAY_LOOP_MONO = 0x05
DMX_AUDIO_COMMAND_PLAY_ONCE_POLY_LOCKED = 0x06
DMX_AUDIO_COMMAND_PLAY_LOOP_POLY_LOCKED = 0x07
DMX_AUDIO_COMMAND_STOP = 0x08
DMX_AUDIO_COMMAND_PAUSE = 0x09
DMX_AUDIO_COMMAND_RESUME = 0x0A
DMX_AUDIO_COMMAND_TRACK_VOLUME = 0x0B
DMX_AUDIO_COMMAND_MASTER_VOLUME = 0x0C

NOPCommand = Colour(DMX_AUDIO_COMMAND_NOP, 0, 0)
PlaySound0OnceMono = Colour(DMX_AUDIO_COMMAND_PLAY_ONCE_MONO, 0, 127)

# Open an interface
with DMXInterface("FT232R") as interface:
    # Create a universe
    universe = DMXUniverse()

    # Define a light
    light = DMXLight3Slot(address=0)

    # Add the light to a universe
    universe.add_light(light)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    light.set_colour(PLaySound0OnceMono)

    print("Playing sound 0, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()