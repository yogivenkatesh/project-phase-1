# motor_control.py
import RPi.GPIO as GPIO
import time

# Define GPIO pins for motor control
motor_enable_pin = 18  # Enable pin for the motor driver
motor_forward_pin = 23  # Forward direction pin
motor_backward_pin = 24  # Backward direction pin
motor_pwm_pin = 12      # PWM pin for speed control

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins
GPIO.setup(motor_enable_pin, GPIO.OUT)
GPIO.setup(motor_forward_pin, GPIO.OUT)
GPIO.setup(motor_backward_pin, GPIO.OUT)
GPIO.setup(motor_pwm_pin, GPIO.OUT)

# Create PWM object
pwm = GPIO.PWM(motor_pwm_pin, 100)  # 100 Hz frequency

# Initialize motor driver
GPIO.output(motor_enable_pin, GPIO.HIGH)  # Enable the motor driver
pwm.start(0)  # Start PWM with 0% duty cycle (motor stopped)

def set_motor_speed(speed):
    """Sets the motor speed (0-100)."""
    pwm.ChangeDutyCycle(speed)

def move_forward():
    GPIO.output(motor_forward_pin, GPIO.HIGH)
    GPIO.output(motor_backward_pin, GPIO.LOW)

def move_backward():
    GPIO.output(motor_forward_pin, GPIO.LOW)
    GPIO.output(motor_backward_pin, GPIO.HIGH)

def stop_motor():
    GPIO.output(motor_forward_pin, GPIO.LOW)
    GPIO.output(motor_backward_pin, GPIO.LOW)
    set_motor_speed(0)

try:
    # Example usage
    print("Moving forward...")
    move_forward()
    set_motor_speed(50)  # Set speed to 50%
    time.sleep(2)

    print("Moving backward...")
    move_backward()
    set_motor_speed(30)
    time.sleep(1)

    print("Stopping...")
    stop_motor()

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    print("Cleaning up...")
    stop_motor()
    GPIO.cleanup()  # Clean up GPIO pins

# Run this script:  sudo python motor_control.py
