#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: Februrary
# This program is rock paper scisora game against a computer

import random


def main():
    while True:
        choice_str = input("Pick One (Rock: 1, Scissors: 2, Paper: 3): ")
        comp_choice = random.randint(1, 3)
        print()
    
        try:
            choice_int = int(choice_str)
            
            if (choice_int > 3):
                print("Invalid Input")
                print()
                continue

            if (comp_choice == 1):
                print("I pick rock!")
            elif (comp_choice == 2):
                print("I pick scissors!")
            elif (comp_choice == 3):
                print("I pick paper!")

            answer = comp_choice - choice_int 

            if (answer == 0):
                print("Tie!")
            elif (answer < 0):
                if (answer == -2):
                    print("You Win!")
                else:
                    print("You Lose!")
            else:
                if (answer == 2):
                    print("You Lose!")
                else:
                    print("You Win!")
        except ValueError:
            print("Invalid Input")
            print()
            continue
        else:
            break


if __name__ == "__main__":
    main()
