from machine import Pin
import utime
trigger = Pin(4, Pin.OUT)
echo = Pin(1, Pin.IN)
power= Pin(15,Pin.OUT)
motor=Pin(19,Pin.OUT) 
def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
   if 130<distance<150 :
       motor.on()
   if 20<distance<40 :
       motor.off()
   utime.sleep(1)
while True:
   power.on()
   utime.sleep(1)
   ultra()
   power.off()
   utime.sleep(5)