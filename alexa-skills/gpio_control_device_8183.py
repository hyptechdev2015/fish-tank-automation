#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.intent('FishTankPhraseIntent', mapping={'phrase': 'phrase'})
def phrase_control(phrase):
    pinNum = 18
    GPIO.setup(pinNum, GPIO.OUT)

    if phrase == 'feed the fish' or phrase == 'feed the fishes' or phrase == 'feed my fish' or phrase == 'feed my fishes'$
        GPIO.output(pinNum, GPIO.HIGH)
        return statement('The fish feeder in online.')
    else:
                return statement('Sorry, command not understood')


@ask.intent('FishTankDeviceIntent', mapping={'status': 'status',
            'device': 'device'})
def tank_control(status, device):
    try:
        pinNum = int(getPinDevice(device))
    except Exception, e:
        return statement('Pin number for ' + device + ' not valid.')

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

    return statement('Turning device {} {}'.format(device, status))


@ask.intent('GPIOControlIntent', mapping={'status': 'status',
            'pin': 'pin'})
def gpio_control(status, pin):
    try:
        pinNum = int(pin)
    except Exception, e:
        pinNum = int(pin)
    except Exception, e:
        return statement('Pin number not valid.')

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

    return statement('Turning pin {} {}'.format(pin, status))


def getPinDevice(dev):
    pin = ''
    if dev.find('feed') > 0 or dev == 'feeder' or dev == 'the feeder' or dev == 'fish feeder' or dev == 'the fish feeder':
        pin = 18
    elif dev == 'daylight' or dev == 'day light'  or  dev.find('day') > 0 or  dev.find('bright') > 0 or dev.find('pride')$
        pin = 5
    elif dev.find('dim') > 0 or dev == 'dim light' or dev == 'dim' or dev == 'the dim light' or dev == 'dimlight':
        pin = 26
    elif dev.find('night') > 0 or dev == 'night light' or dev == 'night' or dev == 'the night light' or dev == 'nightligh$
        pin = 6
    elif dev.find('heater') > 0 or dev == 'heater light' or dev == 'heater' or dev == 'the heater':
        pin = 27
    return pin


if __name__ == '__main__':
    port = 8183  # the custom port you want
    app.run(host='0.0.0.0', port=port)
    
