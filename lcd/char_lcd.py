#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import Adafruit_CharLCD as LCD
import time
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import subprocess

#temperature


# Raspberry Pi pin configuration:
lcd_rs        = 25   # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 21 #18
lcd_d7        = 22
lcd_backlight = 4

# BeagleBone Black configuration:
# lcd_rs        = 'P8_8'
# lcd_en        = 'P8_10'
# lcd_d4        = 'P8_18'
# lcd_d5        = 'P8_16'
# lcd_d6        = 'P8_14'
# lcd_d7        = 'P8_12'
# lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

cmd = "ip addr show wlan0 | grep inet | awk '{print $2; exit}'"
def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output


# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                                   lcd_columns, lcd_rows, lcd_backlight)

#loop time and IP
while 1:
        lcd.clear()
        ipaddr = run_cmd(cmd)
        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        lcd.message('%s' % ( ipaddr ) )
        lcd.message('%s' % ( ipaddr ) )

        time.sleep(2)


        # Print a two line message
        lcd.clear()
        lcd.message('Welcome to Ngoc\nAnh Fish Tank')

        # Wait 5 seconds
        time.sleep(2)

        # Demo showing the cursor.
        #lcd.clear()
        #lcd.show_cursor(True)
        #lcd.message('It is great')

        #time.sleep(5.0)

        # Demo showing the blinking cursor.
        lcd.clear()
        lcd.blink(True)
        temp_GPU = int( subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])[5:7])
        lcd.message("Temperature\n GPU: %s " %temp_GPU + chr(176) + "C")
        time.sleep(2)

        #get number of processes
        lcd.clear()
        lcd.blink(True)
        temp_CPU_cmd = "cat /sys/class/thermal/thermal_zone0/temp | awk '{print $1/1000}'"
        temp_CPU = run_cmd(temp_CPU_cmd)
        lcd.message("CPU:\n %s" %temp_CPU + chr(176) + "C")
        time.sleep(2)

        #get number of processes
        lcd.clear()
        lcd.blink(True)
        cmd_no_proc = "ps -eo nlwp | tail -n +2 | awk '{ num_threads += $1 } END { print num_threads;exit }'"
        no_proc =  run_cmd(cmd_no_proc)
        lcd.message('# process:\n %s' %(no_proc))
        time.sleep(2)

        # Stop blinking and showing cursor.
        lcd.show_cursor(False)
        lcd.blink(False)

        # Demo scrolling message right/left.
#       lcd.clear()
#       message = 'Feeder at Pin 18'
#       lcd.message(message)
#       for i in range(lcd_columns-len(message)):
#               time.sleep(0.5)
#               lcd.move_right()
#       for i in range(lcd_columns-len(message)):
#               time.sleep(0.5)
#               lcd.move_left()
#               time.sleep(0.5)
#               lcd.move_left()

        # Demo turning backlight off and on.
#       lcd.clear()
#       lcd.message('Flash backlight\nin 5 seconds...')
#       time.sleep(5)
        # Turn backlight off.
#       lcd.set_backlight(0)
#       time.sleep(2)

        # Turn backlight on.
        lcd.set_backlight(1)

        
