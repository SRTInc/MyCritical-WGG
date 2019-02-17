import random
import Start
import Leaderboard
import game
#Name = 'Safi' Testing i/p
check=True
def get_the_players():
    get_players = open(r"Players.txt",'r+')
    gp = get_players.read().splitlines()
    get_players.close()
    return gp
gp = get_the_players()
#print(gp) To check whether get_the_players() works
while check == True :
    print('\n\t\t\tWORD-GUESS GAME\n')
    print('Main menu')
    print('---------\n')
    print('\n\t\t1.START GAME')
    print('\n\t\t2.LEADERBOARD')
    print('\n\t\t3.EXIT') 
    choice = int(input('Enter the option:'))

    if choice==1:
        Name = input('\nEnter your name: ')
        if Name in gp:
            is_New_Name = 'no'   
            Start.start_game(Name,game,check,is_New_Name)
        else:
            is_New_Name = 'yes'
            Start.start_game(Name,game,check,is_New_Name)

    elif choice==2:
        Leaderboard.score_board()
            

    elif choice==3:
        exit(0)


#Saffi     5  2019-02-17 00:03:25.922398