from machine import Pin
import utime

trigger = Pin(2, Pin.OUT)
echo = Pin(4, Pin.IN)
power = Pin(15, Pin.OUT)
motor = Pin(14, Pin.OUT)
status = Pin(25, Pin.OUT)

def ultra():
    print('hello')
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(20)
    trigger.low()
    
    # Set timeout period in microseconds
    timeout = 30000  # 30 ms timeout to detect an echo (adjust if needed)
    
    # Initialize signalon and signaloff
    signaloff = utime.ticks_us()
    signalon = signaloff
    
    # Measure the time until echo goes high, with timeout
    start = utime.ticks_us()
    while echo.value() == 0 and utime.ticks_diff(utime.ticks_us(), start) < timeout:
        signaloff = utime.ticks_us()
        
    # If timeout reached and echo did not go high, consider no echo detected
    if utime.ticks_diff(utime.ticks_us(), start) >= timeout:
        print("No echo detected, retrying...")
        return  # Exit the function and retry in the next loop
    
    # Measure the time until echo goes low, with timeout
    start = utime.ticks_us()
    while echo.value() == 1 and utime.ticks_diff(utime.ticks_us(), start) < timeout:
        signalon = utime.ticks_us()
        
    # If timeout reached and echo did not go low, consider no echo detected
    if utime.ticks_diff(utime.ticks_us(), start) >= timeout:
        print("No echo detected, retrying...")
        return  # Exit the function and retry in the next loop
    
    # Calculate time passed and distance
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ", distance, "cm")
    
    # Control motor based on distance
    if 95 < distance < 120:
        motor.on()
    elif distance > 120:
        motor.off()
    if 20 < distance < 26:
        motor.off()
        
    utime.sleep(1)

while True:
    power.on()
    status.on()
    utime.sleep(1)
    ultra()
    power.off()
    status.off()
    utime.sleep(5)

