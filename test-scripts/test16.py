#!/usr/bin/python

from dmx import Colour, DMXInterface, DMXLight3Slot, DMXUniverse
import testCommands
import time

# Open an interface
with DMXInterface("FT232R") as interface:
    # Create a universe
    universe = DMXUniverse()

    # Define a light
    lightA = DMXLight3Slot(address=1)
    lightB = DMXLight3Slot(address=4)

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

    # Send a NOP
    lightA.set_colour(testCommands.NOPCommandA)
    lightB.set_colour(testCommands.NOPCommandB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound257LoopPolyA)
    lightB.set_colour(testCommands.PlaySound257LoopPolyB)

    print("Playing sound 257, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a NOP
    lightA.set_colour(testCommands.NOPCommandA)
    lightB.set_colour(testCommands.NOPCommandB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound258LoopPolyA)
    lightB.set_colour(testCommands.PlaySound258LoopPolyB)

    print("Playing sound 258, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a NOP
    lightA.set_colour(testCommands.NOPCommandA)
    lightB.set_colour(testCommands.NOPCommandB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound259LoopPolyA)
    lightB.set_colour(testCommands.PlaySound259LoopPolyB)

    print("Playing sound 259, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a NOP
    lightA.set_colour(testCommands.NOPCommandA)
    lightB.set_colour(testCommands.NOPCommandB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound260OncePolyA)
    lightB.set_colour(testCommands.PlaySound260OncePolyB)

    print("Playing sound 260, once, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(0.5)

    # Send a NOP
    lightA.set_colour(testCommands.NOPCommandA)
    lightB.set_colour(testCommands.NOPCommandB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound261OncePolyA)
    lightB.set_colour(testCommands.PlaySound261OncePolyB)

    print("Playing sound 261, once, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(0.5)

    # Send a NOP
    lightA.set_colour(testCommands.NOPCommandA)
    lightB.set_colour(testCommands.NOPCommandB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound271OncePolyA)
    lightB.set_colour(testCommands.PlaySound271OncePolyB)

    print("Playing sound 271, once, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(0.5)

    # Send a NOP
    lightA.set_colour(testCommands.NOPCommandA)
    lightB.set_colour(testCommands.NOPCommandB)

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    # Play the sound
    lightA.set_colour(testCommands.PlaySound263OncePolyA)
    lightB.set_colour(testCommands.PlaySound263OncePolyB)

    print("Playing sound 263, once, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a Stop All
    lightA.set_colour(testCommands.StopAllCommandA)
    lightB.set_colour(testCommands.StopAllCommandB)

    print("Sending a Stop All, sound should stop")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()
