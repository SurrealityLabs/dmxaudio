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
    lightA.set_colour(testCommands.PlaySound1LoopMonoA)
    lightB.set_colour(testCommands.PlaySound1LoopMonoB)

    print("Playing sound 1, looping, moderate volume - did you hear it?")

    # Update the interface's frame to be the universe's current state
    interface.set_frame(universe.serialise())

    # Send an update to the DMX network
    interface.send_update()

    time.sleep(5)

    # Send a pause
    lightA.set_colour(testCommands.MasterVolumeUpCommandA)
    lightB.set_colour(testCommands.MasterVolumeUpCommandB)

    print("Sending a Master Volume Up command, volume should increase")

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

    lightA.set_colour(testCommands.MasterVolumeNormalCommandA)
    lightB.set_colour(testCommands.MasterVolumeNormalCommandB)

    print("Sending a Master Volume Normal command, volume should return")

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
