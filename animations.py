from tools import *
from time import sleep
from rainbowio import colorwheel


def color_chase(led_obj, color, num_pixels = 30, wait = 0.1):
    for i in range(num_pixels):
        led_obj[i] = color
        sleep.sleep(wait)
        led_obj.show()
    sleep.sleep(0.5)


def rainbow_cycle(led_obj, num_pixels = 30, wait = 0.1):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            led_obj[i] = colorwheel(rc_index & 255)
        led_obj.show()
        sleep.sleep(wait)

def demo(led_obj):
    led_obj.fill(RED)
    led_obj.show()
    # Increase or decrease to change the speed of the solid color change.
    sleep.sleep(1)
    led_obj.fill(GREEN)
    led_obj.show()
    sleep.sleep(1)
    led_obj.fill(BLUE)
    led_obj.show()
    sleep.sleep(1)

    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow