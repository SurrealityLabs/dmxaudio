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
    lightA.set_colour(testCommands.PlaySound256LoopPolyA)
    lightB.set_colour(testCommands.PlaySound256LoopPolyB)

    print("Playing sound 256, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound257LoopPolyA)
    lightB.set_colour(testCommands.PlaySound257LoopPolyB)

    print("Playing sound 257, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound258LoopPolyA)
    lightB.set_colour(testCommands.PlaySound258LoopPolyB)

    print("Playing sound 258, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound259LoopPolyA)
    lightB.set_colour(testCommands.PlaySound259LoopPolyB)

    print("Playing sound 259, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound260LoopPolyA)
    lightB.set_colour(testCommands.PlaySound260LoopPolyB)

    print("Playing sound 260, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound261LoopPolyA)
    lightB.set_colour(testCommands.PlaySound261LoopPolyB)

    print("Playing sound 261, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound262LoopPolyA)
    lightB.set_colour(testCommands.PlaySound262LoopPolyB)

    print("Playing sound 262, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound263LoopPolyA)
    lightB.set_colour(testCommands.PlaySound263LoopPolyB)

    print("Playing sound 263, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound264LoopPolyA)
    lightB.set_colour(testCommands.PlaySound264LoopPolyB)

    print("Playing sound 264, looping, moderate volume - it should replace 256")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound265LoopPolyA)
    lightB.set_colour(testCommands.PlaySound265LoopPolyB)

    print("Playing sound 265, looping, moderate volume - it should replace 257")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound266LoopPolyA)
    lightB.set_colour(testCommands.PlaySound266LoopPolyB)

    print("Playing sound 266, looping, moderate volume - it should replace 258")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound267LoopPolyA)
    lightB.set_colour(testCommands.PlaySound267LoopPolyB)

    print("Playing sound 267, looping, moderate volume - it should replace 259")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound268LoopPolyA)
    lightB.set_colour(testCommands.PlaySound268LoopPolyB)

    print("Playing sound 268, looping, moderate volume - it should replace 260")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound269LoopPolyA)
    lightB.set_colour(testCommands.PlaySound269LoopPolyB)

    print("Playing sound 269, looping, moderate volume - it should replace 261")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound270LoopPolyA)
    lightB.set_colour(testCommands.PlaySound270LoopPolyB)

    print("Playing sound 270, looping, moderate volume - it should replace 262")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Play the sound
    lightA.set_colour(testCommands.PlaySound271LoopPolyA)
    lightB.set_colour(testCommands.PlaySound271LoopPolyB)

    print("Playing sound 271, looping, moderate volume - it should replace 263")

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