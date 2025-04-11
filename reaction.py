from gpiozero import LED, Button
from time import sleep, time
from random import uniform


led = LED(4)
right_button = Button(15)
left_button = Button(14)


left_name = input("The left player: ")
right_name = input("The right player: ")


# Record time
led.on()
sleep(uniform(5, 10))
led.off()
led_off_time = time()


def pressed(button):
    reaction_time = time() - led_off_time 

    if button.pin.number == 14:
        print(f"{left_name} won! Reaction time is: {reaction_time:.2f} s")
    else:
        print(f"{right_name} won! Reaction time is: {reaction_time:.2f} s")


right_button.when_pressed = pressed
left_button.when_pressed = pressed


try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    print("Stop!")  # Ctrl + C 
    led.off()
