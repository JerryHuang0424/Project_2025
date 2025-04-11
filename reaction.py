from gpiozero import LED, Button
from time import sleep
from random import uniform
import time


def ready(time = 5):
     print("Both players need to press their buttons to get ready.")
     player1_ready = False
     player2_ready = False
     start_time = time.time()
     while time.time() - start_time < time:
         if right_button.is_pressed:
             player1_ready = True
             print("Player 1 is ready!")
         if left_button.is_pressed:
             player2_ready = True
             print("Player 2 is ready!")
         if player1_ready and player2_ready:
             return True
         if right_button.is_pressed or left_button.is_pressed:
            sleep(0.5)
     print("Time is up!")
    

def main_play():

    def pressed(button):
        if button.pin.number == 14:
            print(left_name + ' won the game')
        else:
            print(right_name + ' won the game')

    left_name = input('Enter the name of the left player: ')
    right_name = input('Enter the name of the right player: ')

    led.on()
    sleep(uniform(5,10))
    led.off()
    start_time = time.time()
    while time.time() - start_time < 3:
        right_button.when_pressed = pressed()
        left_button.when_pressed = pressed()
        if right_button.is_pressed or left_button.is_pressed:
            sleep(0.5)

def reset(timeout=10):
    print("Press the reset button to play again.")
    player1_reset = False
    player2_reset = False
    start_time = time.time()
    while time.time() - start_time < timeout:  # 添加超时机制
        if right_button.is_pressed:
            player1_reset = True
            print("Player 1 has reset the game!")
        if left_button.is_pressed:
            player2_reset = True
            print("Player 2 has reset the game!")
        if player1_reset and player2_reset:
            return True
        if right_button.is_pressed or left_button.is_pressed:
            sleep(0.5)
    print("Reset timed out!")
    return False



def play():
    
    while True:
        if ready() == True:
            print("Both players are ready!")
            main_play()

        if reset():
            break

if __name__ == "__main__":
    led = LED(4)
    right_button = Button(15)
    left_button = Button(14)
    play()






