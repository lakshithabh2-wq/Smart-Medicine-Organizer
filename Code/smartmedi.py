import time
from gpiozero import LED, Buzzer

# Pins for LEDs and Buzzer
LED_PINS = [2, 3, 4, 5]
BUZZER_PIN = 17

leds = [LED(pin) for pin in LED_PINS]
buzzer = Buzzer(BUZZER_PIN)

BLINK_DURATION = 30  # seconds

def trigger_alarm(compartment_index):
    if not (0 <= compartment_index < len(leds)):
        return

    active_led = leds[compartment_index]
    start_time = time.time()

    # Beep 3 times at the start
    for _ in range(3):
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(0.1)

    # Blink LED for 30 seconds
    while time.time() - start_time < BLINK_DURATION:
        active_led.toggle()
        time.sleep(0.5)

    # Turn off LED
    active_led.off()

# Example: Alert for Compartment 1
trigger_alarm(0)
