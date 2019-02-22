import random
import Start
import Leaderboard
import game

import random
import datetime

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

def start_game(Name,game,check,is_New_Name):
    print('\n', Name, ' Welcome to the guess the four-lettered word game!\n')
    print('------------------------------------------------------------\n')
    con = 'y'  # var for check the to continue the game
    print('The rules are simple...\nYou must a guess a four letter word and you have 15 chances to do so :P')
    print('\n Sounds easy right? Lets get on with it!\n')


    def getwords():
        fobj = open(r"Randwords.txt", "r+")
        get = fobj.read().splitlines()
        fobj.close()
        return get


    get = getwords()
    game.play(con, get, Name, check,is_New_Name)
    # print(get) #check if the words are fetched from file

def score_board():
    def get_the_playerscore():
            get_playerscore = open(r"Playerscore.txt",'r+')
            gs = get_playerscore.read().splitlines()
            get_playerscore.close()
            return gs
    gs = get_the_playerscore()
    print('\n\nNAME        SCORE  DATE')
    print('-----------------------')
    count=0
    for i in gs:
        print(gs[count][0:9],'  ',gs[count][10:13],' ',gs[count][13:])
        count+=1



def play(con,get,Name,check,is_New_Name):       
    fobj = open(r"Playerscore.txt","a+")
    fp = open(r"Players.txt","a+")
    found = False
    score = 0
    print('hi')
    while(con == 'y'):

        def get_random_word():
                a = random.choice(get)#selects a random string from get[] 
                return a
           
        g = get_random_word()
        #print(g) #to check whether get_random_word() works
        s_word=g
        #print(s_word)
        g_word = ''  # guess word
        g_count = 1  # this is guessing count to limit the guess
        out_of_guess = False
        
        while g_word != s_word and not (out_of_guess):  # This while is for give the chance unitl the chance are over 
            if g_count < 16:  # this if check the chance over or not if over come out

                g_word = input('Enter the guess of the secret word:   ')[:4]
                if len(g_word) < 4:
                    print('Wrong input you wasted one chance :-( ')
                    g_word ='    '
                if len(g_word) == 0:
                    g_word='    '


                if g_word == s_word:
                    no = str(g_count)  # to convert the g_count to str becoz v can't concat str and int
                    print('GREAT!!! B-) ' + Name + ' guessed word is correct, ' + Name + ' win by ' + no + '  guess')
                    found = True
                    score+=1 #Now the score is incremented by one
                    print('Now your score is ',score,'\n')
                    g_word = ''  # guess word
                    g_count = 1  # this is guessing count to limit the guess
                    s_word = get_random_word()
                    con = input('Do you want to continue the game(y/n): ')       
                    if con == 'n':
                        print('\nThank you for playing the game ;-) ')
                        break
                    continue
                    
                else:
                    for x in range(0, 4):
                        if s_word[x] == g_word[x]:  # to compare the each char of g_word and s_word
                            if x == 0:
                                k = g_word[x]
                            else:
                                k = k + g_word[x]

                        else:
                            if x == 0:
                                k = '_'
                            else:
                                k = k + '_'
                    print(k)
                    coun=0

                    for k in range(0 , 4):  # this loop is for comparing the element in all possible ways
                        boolean = True  # this boolean value is for avoid the comparing the word that already found
                        for j in range(0, 4):
                            if s_word[k] == g_word[j]:  # it filter the word that not matched

                                if j != k and boolean == True:# this filter the already finded exact  and approx. pos. of the letter(07)

                                    coun=coun+1
                                    if j == 0:
                                        ab=g_word[1:4]
                                        g_word='0'+ab

                                    elif j == 3:
                                        bc=g_word[0:3]
                                        g_word=bc+'0'
                                    else :
                                        cd=g_word[:x]
                                        de=g_word[x+1:]
                                        g_word=cd+'0'+de
                                    boolean = False  # if we find the value this change the value to false to false the if(7) condition
                    abc = str(coun)
                    print( abc + ' letter is  present in wrong position')
                    rem = 15 - g_count  # for showing remaing chance
                    rem = str(rem)
                    print('Remaining chance ' + rem)
                    g_count += 1
                    count = str(g_count)
                    print('Guessing count is ' + count)
                    if(g_count == 16):
                        found = False  # After find the value change the boolean to stop the looping
            
            elif found == False:
                g_word = ''  # guess word
                g_count = 1  # this is guessing count to limit the guess
                print('\nNice try :-) Out of chance, U lose!!! ;-P')
                print('Your score now is ',score,'\n')

                if is_New_Name == 'yes' or is_New_Name == 'no':#I screwed up real bad on this one!
                    fp.write('\n%s'%(Name))
                    x = datetime.datetime.now()
                    fobj.write("\n%s        %d  %s"%(Name,score,x))
                    
                                
                score = 0
                show=input('Do you want to know the secret word which make you lose this game(y/n): ')
                if show == 'y':
                    print('The secret word is  ' + s_word)
                
                con = input('Do you want to continue the game(y/n): ') 
                s_word = get_random_word()      
                if con == 'n':
                    print('\nThank you for playing the game ;-) ')
                    break
                
    
        
    fp.close()
    fobj.close()
