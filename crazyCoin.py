# Crazy habit is a tool for forming habits and getting things done.
    # The concept is based off of completing a task that is relatively simple. Then flipping the crazy coin.
    # If you WIN the flip you get to do a "crazy" task of your choice (ex 20 min of gaming)
    # If you LOSE the flip you have to do a work task. I guess you can pick the task.
    # Should probably have an options thing so I can correct it.
# The goal here is to motivate you to do tasks. Playing on psychology of varied rewards and habit forming.


title_art = "░█████╗░██████╗░░█████╗░███████╗██╗░░░██╗  ░█████╗░░█████╗░██╗███╗░░██╗\n██╔══██╗██╔══██╗██╔══██╗╚════██║╚██╗░██╔╝  ██╔══██╗██╔══██╗██║████╗░██║\n██║░░╚═╝██████╔╝███████║░░███╔═╝░╚████╔╝░  ██║░░╚═╝██║░░██║██║██╔██╗██║\n██║░░██╗██╔══██╗██╔══██║██╔══╝░░░░╚██╔╝░░  ██║░░██╗██║░░██║██║██║╚████║\n╚█████╔╝██║░░██║██║░░██║███████╗░░░██║░░░  ╚█████╔╝╚█████╔╝██║██║░╚███║\n░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ░╚════╝░░╚════╝░╚═╝╚═╝░░╚══╝"

import random as rand
import time
import os

work_list = []
crazy_list = []

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def menu_screen():
    clear_screen()
    print("\n" + title_art + "\n")
    #This can probably be a loop + function
    while(True):
        print("Crazy Coin: What work task have you completed?")
        work_task = input("You: ")
        work_list.append(work_task)
        print("Crazy Coin: Good job. Lets give it a flip.")

        #Flip the coin.
        flip = rand.randint(0,1)
        if(flip == 0):
            print("*The coin lands on heads*")
            print("Crazy Coin: It was heads. Sorry pal. Do another work task and we can flip again.")
        else:
            print("*The coin lands on crazy face*")
            print("Crazy Coin: LETS PARTY! What do you want to do?")
            crazy_task = input("Enter your crazy task: ")
            crazy_list.append(crazy_task)
            print("Crazy Coin: Enjoy your fun. Once you're done, comlete a work task and we can flip again.")
        
        print(crazy_list)
        print(work_list)

# Loads in the instructions with a little animation. (old school computer)
# Press Enter to continue.
def instructions_screen():
    clear_screen()
    time.sleep(1)
    print("\n" + title_art + "\n")
    time.sleep(0.05)
    clear_screen()
    time.sleep(0.5)
    print("\n" + title_art + "\n")
    time.sleep(0.3)
    clear_screen()
    time.sleep(0.05)
    print("\n" + title_art + "\n")
    time.sleep(0.9)
    print("- First complete a work task. Enter it and then wait for the crazy coin to flip.")
    time.sleep(0.35)
    print("- If HEADS, you skip the reward and must do another work tast to earn a flip.")
    time.sleep(0.35)
    print("- If CRAZY FACE, then you can do any task of your choice.")
    time.sleep(0.35)
    print("- Repeat. Quit when finished to get a summary.")
    time.sleep(0.35)
    user_input = input("\nPress Enter to continue\n\n")
    menu_screen()


#Flips a virtual coin with 50/50 odds. Returns True for heads and False for tails.

# MAKE THIS MORE THEATRIC. ADD A TIME DELAY AND STUFF SO YOU WAIT FOR AND ANTICIPATE THE OUTCOME.
def flip_coin():
    flip = rand.randint(0,1)
    if flip==0:
        return(False)
    else:
        return(True)

def main():
    instructions_screen()
    while(True):
        user_input = input("Your choice: ").lower() # User selects their guess.

main()