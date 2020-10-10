


games = 6 # This is the count of rounds you want to play,you can chage as you wish ,default rounds in a game are '6'.



import sys, termios, tty, os, time
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
import random
import time
import pyautogui
h = 0
g = 0
def scores(h, g):
    print('                                                                                                        Your score: ' + str(h))
    print('                                                                                                        Computer score ' + str(g))
a = ['Rock', 'Paper', 'Scissor']
print("Instruction: press 'r' for rock and s for scissor and p for paper")
print("10 Rounds match!")
z = input("Press Enter to play")
print("                                                      Lets Play Rock,Paper,Scissor!")
i = 1
while i <= games:
   
    time.sleep(1)
    print("                     ........................................Ready.........................................")
    time.sleep(1)

    
    print("                                                            Round -" + str(i))
    for y in a:
        time.sleep(0.5)
        print(y)
       
    t = random.choice(a)
    char = getch()
    if char == 'r':
      e = 'Rock'
    elif char == 'p':
      e = 'Paper'
    else:
      e = 'Scissor'
    
    print('                                                 ' + t + '  -  ' + e)
    if t == e:
        print("                                                Ohhh... No points")
        i += 1
    elif (e == a[0]) and (t == a[2]) or ((e == a[2]) and (t == a[1])) or ((e == a[1]) and (t == a[0])):
        print("                                             You win and 1 point for you")
        h += 1
        scores(h ,g)
        i += 1
    else:
        print("                                              Computer gets 1 point")
        g += 1
        scores(h, g)
        i += 1
if h > g:
    print("              -------------------------------------------------------YOU WON------------------------------------------------------")
elif  h < g:
    print("              ----------------------------------------------------COMPUTER WON----------------------------------------------------")
else:
    print('              -----------------------------------------------------Hurray It a Tie------------------------------------------------')


      i += 1
      print("Thank you for playing")
"""
 

 
while True:
    char = getch()
 
    if (char == "p"):
        print("Stop!")
        exit(0)
   
      
