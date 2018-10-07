# This python script gets input from a DHT11, measuring temperature and humidity.
# The temperature and humidity is then get displayed on an lcm1602 iic v1
import lcddriver
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 4
display = lcddriver.lcd()
display.lcd_clear()
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#counter = 0

try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        #display.lcd_clear()
        '''
        if counter % 2 == 0:
            display.backlight_off()
        if counter % 2 == 1:
            display.backlight_on()
        '''
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        #print("Writing to display  Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature,humidity))
        #print(counter)
        if humidity is not None and temperature is not None:
            display.lcd_display_string("Temp={0:0.1f}*C".format(temperature), 1)
            display.lcd_display_string("Humidity={0:0.1f}%".format(humidity), 2)
        else:
            display.lcd_display_string("Failed!", 1)
        #counter += 1
        time.sleep(2)
        
        
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
