#!/usr/bin/python

from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse
import testCommands
import time

# Open an interface
with DMXInterface("FT232R") as interface:
    # Create a universe
    universe = DMXUniverse()

    # Define a light
    lightA = DMXLight3Slot(address=0)
    lightB = DMXLight3Slot(address=3)

    # Add the light to a universe
    universe.add_light(lightA)
    universe.add_light(lightB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound256LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound256LoopPolyLockedB)

    print("Playing sound 256, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound257LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound257LoopPolyLockedB)

    print("Playing sound 257, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound258LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound258LoopPolyLockedB)

    print("Playing sound 258, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound259LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound259LoopPolyLockedB)

    print("Playing sound 259, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound260LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound260LoopPolyLockedB)

    print("Playing sound 260, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound261LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound261LoopPolyLockedB)

    print("Playing sound 261, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound262LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound262LoopPolyLockedB)

    print("Playing sound 262, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound263LoopPolyLockedA)
    lightB.set_colour(testCommands.PlaySound263LoopPolyLockedB)

    print("Playing sound 263, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a Stop All
    lightA.set_colour(StopAllCommandA)
    lightB.set_colour(StopAllCommandB)

    print("Sending a Stop All, sound should stop")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()