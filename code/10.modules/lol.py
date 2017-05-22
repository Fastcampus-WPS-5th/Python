#import game
import sys
from functions.game import play_game, title as game_title
from functions.shop import buy_item, title as shop_title
#from friends.chat import send_message
from friends import chat
title = 'Main Module'
def turn_on():
    print('= Start game =')
    while True:
        choice = input('What would you like to do?\n  1: Go Shop\n  2: Play Game\n  3: Send Message\n  0: Exit\n    Input : ')
        if choice == '0':
            break
        elif choice == '1':
            buy_item()
        elif choice == '2':
            play_game()
        elif choice == '3':
            chat.send_message()
        else:
            print('Choice not exist')
        print('-----------------------')
    print('= End game =')

if __name__ == '__main__':
    turn_on()
