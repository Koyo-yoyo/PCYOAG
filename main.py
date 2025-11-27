import time, sys, pygame

pygame.init()

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

try:
    potion_sound = pygame.mixer.Sound("potion-sound.wav")
    sharkdolphin_sound = pygame.mixer.Sound("shark&dolphin.wav")
    stayhome_sound = pygame.mixer.Sound("stay-home.wav")
    wentout_sound = pygame.mixer.Sound ("went-out.wav")

    bg_sound = pygame.mixer.music.load("Big-Day-Out.mp3")
    pygame.mixer.music.play(-1)
except:
    raise(UserWarning, "could not load or play soundfiles in 'media' folder :-(")




def chooseOption(numberOfOptions):
    choice = 0
    while choice < 1 or choice > numberOfOptions:
        print('1 to ' + str(numberOfOptions) + '> ', end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
            choice = 0
        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
            choice = int(choice)
        print('\n\n')
    return choice


def pause():
    input('Press enter to continue!\n')


def game_explanation():
    print('\u001b[31m<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\u001b[0m')
    print("Please read the story since the choices you make will effect your ending! :)")
    print('\u001b[31m<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\u001b[0m \n\n')
    time.sleep(3)
    start()


def start():
    print(
        "You are a jellyfish living in the ocean! You wanna leave home and meet new friends, but you're a little scared.")
    print("Will you leave or not?\n")
    time.sleep(1)

    pause()
    print("1 - Adventure into the unknown!")
    print("2 - Stay in the safety of your home…")
    print("3 - Go to the sea witch and ask for advice!!!!")
    print("4 - Eat something :p")

    choice = chooseOption(4)
    if choice == 1:
        adventure()
    elif choice == 2:
        stayHome()
    elif 3 == choice:
        seaWitch()
    elif 4 == choice:
        eat()
    else:
        print("Error!")

    # Adventure into the unknown!


def adventure():
    print("You leave home and adventure into the unknown to find some friends.")
    print("As you swim, you encounter a shark and a dolphin!")
    sharkdolphin_sound.play()
    print("They look like they are fighting…\n")
    print("You wonder if either one of them would want to be your friend!\n")
    print("You swim over and see whats going on.")
    print("Turns out they were fighting over who would win a race.")
    print("They turn to you suddenly and ask for your opinion!\n")

    print('Who would win?')
    print(" 1 - The shark!")
    print(" 2 - The dolphin!")
    print(" 3 - It would be a tie!")
    print(" 4 - Neither of them!")

    choice = chooseOption(4)
    if 1 == choice:
        shark()
    elif 2 == choice:
        dolphin()
    elif 3 == choice:
        tie()
    elif 4 == choice:
        neither()
    else:
        print("Error!")


def shark():
    print("The shark looks like a good choice!")
    print("They are big and look like very strong swimmer.")
    print("The dolphin gets upset at that and swims away in frustration.")
    print("You and the shark become good friends after that.")
    print("Even though they look a little scary, they are always kind to you and put you first.")


def dolphin():
    print("The dolphin looks like a good choice!")
    print("They are fast and look like they could beat the shark.")
    print("The shark gets upset at that and swims away in frustration.")
    print("You and the dolphin become good friends after that.")
    print("Even though they can be mean sometimes, they still care about you.")


def tie():
    print("You panic and say that it would be a tie!")
    print("The two of them stop fighting and agree, a little reluctantly, that you might be right.")
    print("The three of you become friends after you continue to talk to each other for a little longer!")
    print("They are both good friends and you enjoy their company.")


def neither():
    print("You dont know what to say, and you start to panic before swimming away as fast as you can!")

    # Stay in the safety of your home...


def stayHome():
    stayhome_sound.play()
    print("The ocean is a scary place that you're not ready for! You'd rather stay home where its safe.")

    # Go to the sea witch and ask for advice!!!


def seaWitch():
    print(
        "The sea witch gives you a potion and says that the other ocean dwellers are meanies and that you should go on land to make friends!")
    print(ASCII_ART1)
    potion_sound.play()
    print("\u001b[31mITEM OBTAINED!\u001b[0m\n")
    print("She hands you the potion and says that you can't turn back into a jellyfish if you drink it! D:")
    print("But you really wanna make new friends…")
    print("Will you drink it?...\n")

    choice = chooseOption(2)
    if 1 == choice:
        dontTrust()
    elif 2 == choice:
        trust()
    else:
        print("Error!")


def dontTrust():
    print(
        "You decide not to trust the witch. She seemed a little fishy...Instead, you decide to go home and give up on making new friends.")
    print("A bit disappointing, but it might be for the best.")


def trust():
    print("You thank the witch and head to the surface, and end up close to a beach.")
    print("You chug the potion in one go and become a human!!")
    print("You try out your new legs and find it quite fun to run in the sand.")
    print("After walking for a little while, you meet a few people building a tower using sand.")
    print("You ask if you can join, and they say yes!\n")
    print("\u001b[31m time skip \u001b[0m\n")
    print("Its been 5 years since you became a human.")
    print("You have a job, a home and great friends!")
    print("You're very happy that you took the sea witches advice.")

    # Eat something :p


def eat():
    print("All this thinking is making you hungry.")
    print("You decide to eat something, but after the meal you start to feel drowsy and wanna take a nap.")

    choice = chooseOption(2)
    if 1 == choice:
        nap()
    elif 2 == choice:
        noNap()
    else:
        print("Error!")


def nap():
    print("You wake up a little while later and dont feel the motivation to go out now.")
    print("You decide to go explore tomorrow.")


def noNap():
    wentout_sound.play()
    print("You push through the tiredness and adventure out.")
    print("After swimming for a while, you end up falling asleep!")
    print("You wake up only to find yourself lost after the currents took you somewhere.")
    print("After a while of swimming, you start to give up before another jellyfish comes up to you and asks what's wrong.")
    print("You explain what happened, and the other jellyfish decides to help you out.")
    print("The other jellyfish lets you stay at their house, where the two of you get along and become friends!")
    print("After figuring out how to get home and having made a new friend, you feel very satisfied with your day!")
    print("You cant wait for tomorrow to see your new friend again.")


ASCII_ART1 = r"""                                                                                                    
    **+                                                        
   *+++-                                                    
   :+**## :...                                                 
     +###     --                                               
  ####*     ===-:                                              
%### :    ====---:                                             
%%   ------------:                                             
     ---:-------:                                              
      -:------::
        ******
"""

###################### THE MAIN GAME LOOP ############################
# --------------------------- Game Loop -------------------------------
# Don't mess with this unless you really know what you are doing!!
while True:

    # Start the game
    game_explanation()

    # "Play again" user option
    print('\nWould you like to play again? Y/N')
    playAgain = input()
    if playAgain == 'Y' or playAgain == 'y':
        continue  # continue loop
    elif playAgain == 'N' or playAgain == 'n':
        break  # leave while loop
    break

# You've exited the loop, so end the game...
# snd.quitScript()
print("Quitting...")
sys.exit(0)

quit()


