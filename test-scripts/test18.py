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
    lightA.set_colour(testCommands.PlaySound260LoopPolyA)
    lightB.set_colour(testCommands.PlaySound260LoopPolyB)

    print("Playing sound 260, looping, moderate volume - did you hear it?")

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
    lightA.set_colour(testCommands.PlaySound261LoopPolyA)
    lightB.set_colour(testCommands.PlaySound261LoopPolyB)

    print("Playing sound 261, looping, moderate volume - did you hear it?")

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
    lightA.set_colour(testCommands.PlaySound271LoopPolyA)
    lightB.set_colour(testCommands.PlaySound271LoopPolyB)

    print("Playing sound 271, looping, moderate volume - did you hear it?")

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
    lightA.set_colour(testCommands.PlaySound263LoopPolyA)
    lightB.set_colour(testCommands.PlaySound263LoopPolyB)

    print("Playing sound 263, looping, moderate volume - did you hear it?")

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
	
    # Stop sound 264
    lightA.set_colour(testCommands.Stop264CommandA)
    lightB.set_colour(testCommands.Stop264CommandB)

    print("Stopping sound 264, nothing should happen")

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
    # Stop sound 265
    lightA.set_colour(testCommands.Stop265CommandA)
    lightB.set_colour(testCommands.Stop265CommandB)

    print("Stopping sound 265, nothing should happen")

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
	
    # Stop sound 266
    lightA.set_colour(testCommands.Stop266CommandA)
    lightB.set_colour(testCommands.Stop266CommandB)

    print("Stopping sound 266, nothing should happen")

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

    # Stop sound 267
    lightA.set_colour(testCommands.Stop267CommandA)
    lightB.set_colour(testCommands.Stop267CommandB)

    print("Stopping sound 267, nothing should happen")

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

    # Stop sound 268
    lightA.set_colour(testCommands.Stop268CommandA)
    lightB.set_colour(testCommands.Stop268CommandB)

    print("Stopping sound 268, nothing should happen")

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

    # Stop sound 269
    lightA.set_colour(testCommands.Stop269CommandA)
    lightB.set_colour(testCommands.Stop269CommandB)

    print("Stopping sound 269, nothing should happen")

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

    # Stop sound 270
    lightA.set_colour(testCommands.Stop270CommandA)
    lightB.set_colour(testCommands.Stop270CommandB)

    print("Stopping sound 270, nothing should happen")

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

    # Stop sound 262
    lightA.set_colour(testCommands.Stop262CommandA)
    lightB.set_colour(testCommands.Stop262CommandB)

    print("Stopping sound 262, nothing should happen")

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

    # Send a Stop All
    lightA.set_colour(testCommands.StopAllCommandA)
    lightB.set_colour(testCommands.StopAllCommandB)

    print("Sending a Stop All, sound should stop")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()
