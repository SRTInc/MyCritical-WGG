import random
import Start
import Leaderboard
import game

#Name = 'Safi' Testing i/p
check=True #To emulate infinite loop


def get_the_players():#this snippet is just checking whether the file functions work!
    get_players = open(r"C:\guessgame\Players.txt",'r+')
    gp = get_players.read().splitlines()
    get_players.close()
    return gp
    
gp = get_the_players()
#print(gp) To check whether get_the_players() works


while check == True :
    option = 0
    print('\n                      GUESS    GAME')
    print('                      ======   =====\n')
    print('                    _____________________')
    print('                    |   MAIN MENU       |\n                     ___________________')
    print('                    | 1)  Start         |\n                    | 2)  Score Board   |')
    print('                    | 3)  Credits       | \n                    | 4)  Exit          |')
    print('                    |___________________|')
    try:
        option=int(input('Enter your option:(1-4)>'))
    except:
        print('Genius, Enter only number,\nIf you do not know number go learn and come ;-p :\n ')
    
    if option==1:
        Name = input('\nEnter your name: ')
        if Name in gp:
            is_New_Name = 'no'   
            Start.start_game(Name,game,check,is_New_Name)
        else:
            is_New_Name = 'yes'
            Start.start_game(Name,game,check,is_New_Name)

    elif option==2:
        Leaderboard.score_board()
            
    elif option==3:
        print('''                                             CREDITS



PROGRAMMED BY:        MR.S DEEPAK (K)ISHORE (P)
                      MR.N.SAFFIUDDIN

DEBUGGED BY:          MR.N.SAFFIUDDIN

MOTIVATED BY:         MR. MOHAMED ASIF




                                      THANK YOU!!!''')
    elif option==4:
        print("THANK YOU!!!\nSEE YOU SOON")
        exit()

#Sample output for LEADERBOARD fun()
#Saffi     5  2019-02-17 00:03:25.922398