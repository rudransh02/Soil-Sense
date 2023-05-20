import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

sensor_pin = 23

running = True
textfile = open('DHT Sensor Readings.txt', 'w')

while running:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

        temperature_f = temperature * 9.0/5.0 + 32.0

        if humidity is not None and temperature is not None:
            humidity -= 45
            print(str(temperature) + " " + str(humidity))
            textfile.write(str(temperature) + " " + str(humidity) + '%\n')
            time.sleep(0.2)
        else:
            print('Failed to get reading. Try again!')
            time.sleep(1)
    except KeyboardInterrupt:
        print ('Keyboard Interrupt Encountered!')
        running = False
        textfile.close()