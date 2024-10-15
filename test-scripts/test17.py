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

    # Stop sound 256
    lightA.set_colour(testCommands.Stop256CommandA)
    lightB.set_colour(testCommands.Stop256CommandB)

    print("Stopping sound 256, it should stop")

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

    # Stop sound 257
    lightA.set_colour(testCommands.Stop257CommandA)
    lightB.set_colour(testCommands.Stop257CommandB)

    print("Stopping sound 257, it should stop")

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

    # Stop sound 258
    lightA.set_colour(testCommands.Stop258CommandA)
    lightB.set_colour(testCommands.Stop258CommandB)

    print("Stopping sound 258, it should stop")

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

    # Stop sound 259
    lightA.set_colour(testCommands.Stop259CommandA)
    lightB.set_colour(testCommands.Stop259CommandB)

    print("Stopping sound 259, it should stop")

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

    # Stop sound 260
    lightA.set_colour(testCommands.Stop260CommandA)
    lightB.set_colour(testCommands.Stop260CommandB)

    print("Stopping sound 260, it should stop")

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

    # Stop sound 261
    lightA.set_colour(testCommands.Stop261CommandA)
    lightB.set_colour(testCommands.Stop261CommandB)

    print("Stopping sound 261, it should stop")

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
    lightA.set_colour(testCommands.Stop271CommandA)
    lightB.set_colour(testCommands.Stop271CommandB)

    print("Stopping sound 271, it should stop")

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

    # 1Stop sound 263
    lightA.set_colour(testCommands.Stop263CommandA)
    lightB.set_colour(testCommands.Stop263CommandB)

    print("Stopping sound 263, it should stop")

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
