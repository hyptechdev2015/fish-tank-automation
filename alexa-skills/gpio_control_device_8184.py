#!/usr/bin/env python
"""
This script using:
https://github.com/erik/alexandra
"""

import alexandra
import RPi.GPIO as GPIO
import logging

app = alexandra.Application()
name_map = {}

GPIO.setmode(GPIO.BCM)

@app.launch
def launch_handler():
    return alexandra.reprompt('What would you like to do?')

"""
@app.intent('MyNameIs')
def set_name_intent(slots, session):
    name = slots['Name']
    name_map[session.user_id] = name

    return alexandra.respond("Okay, I won't forget you, %s" % name)

@app.intent('WhoAmI')
def get_name_intent(slots, session):
    name = name_map.get(session.user_id)

    if name:
        return alexandra.respond('You are %s, of course!' % name)

    return alexandra.reprompt("We haven't met yet! What's your name?")

@app.intent('Tell')
def set_name_intent(slots, session):
    name = slots['Name']
    name_map[session.user_id] = name

    return alexandra.respond("Okay, I won't forget you, %s" % name)
"""

@app.intent('FishTankPhraseIntent')	
def get_name_intent(slots, session):
    phrase = slots['phrase']
    name_map[session.user_id] = phrase
    pinNum = 18
    GPIO.setup(pinNum, GPIO.OUT)
    if phrase == 'feed the fish' or phrase == 'feed the fishes' or phrase == 'feed my fish' or phrase == 'feed my fishes' or phrase.find('fish') > 0 or phrase.find('feed') > 0:
        GPIO.output(pinNum, GPIO.HIGH)	
        return alexandra.respond('The fish feeder in online.')			
    else:
        return alexandra.respond('Sorry, command not understood')	

@app.intent('FishTankDeviceIntent')
def get_name_intent(slots, session):
    status = slots['status']
    device = slots['device']
    try:
        pinNum = int(getPinDevice(device))
    except Exception as e:
        return alexandra.respond('Pin number for ' + device + ' not valid.')

    GPIO.setup(pinNum, GPIO.OUT)

    if pinNum == 5 or pinNum == 6 or pinNum == 26 or pinNum == 27:
        if status in ['on', 'high']:
            GPIO.output(pinNum, GPIO.LOW)
        if status in ['off', 'low']:
            GPIO.output(pinNum, GPIO.HIGH)
    else:
        if status in ['on', 'high']:
            GPIO.output(pinNum, GPIO.HIGH)
        if status in ['off', 'low']:
            GPIO.output(pinNum, GPIO.LOW) 	

    return alexandra.respond('Turning device {} {}'.format(device, status))	

@app.intent('GPIOControlIntent')
def get_name_intent(slots, session):
    status = slots['status']
    pin = slots['pin']
    try:
        pinNum = int(pin)
    except Exception as e:
        return statement('Kevin, Pin number not valid.')

    GPIO.setup(pinNum, GPIO.OUT)

    if pinNum == 5 or pinNum == 6 or pinNum == 26 or pinNum == 27:
        if status in ['on', 'high']:
            GPIO.output(pinNum, GPIO.LOW)
        if status in ['off', 'low']:
            GPIO.output(pinNum, GPIO.HIGH)
    else:
        if status in ['on', 'high']:
            GPIO.output(pinNum, GPIO.HIGH)
        if status in ['off', 'low']:
            GPIO.output(pinNum, GPIO.LOW)

    return alexandra.respond('Turning pin {} {}'.format(pin, status))

#getPinDevice
def getPinDevice(dev):
    pin = ''
    if dev == 'feeder' or dev == 'the feeder' or dev == 'fish feeder' or dev == 'the fish feeder':
        pin = 18
    elif dev == 'light 1' or dev == 'daylight' or dev == 'day light'  or  dev.find('day') > 0 or  dev.find('bright') > 0 or dev.find('pride') > 0  or dev == 'bright light' or dev == 'bright' or dev == 'the bright light' or dev == 'brightlight':
        pin = 5
    elif dev == 'light 2' or dev.find('dim') > 0 or dev == 'dim light' or dev == 'dim' or dev == 'the dim light' or dev == 'dimlight':
        pin = 26
    elif dev == 'light 3' or dev.find('night') > 0 or dev == 'night light' or dev == 'night' or dev == 'the night light' or dev == 'nightlight':
        pin = 6
    elif dev == 'light 4' or dev.find('heater') > 0 or dev == 'heater light' or dev == 'heater' or dev == 'the heater':
        pin = 27
    return pin

if __name__ == '__main__':
    app.run('0.0.0.0', 8184, debug=False)
