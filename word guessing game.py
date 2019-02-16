"""import random
import game
#Name = input('Enter your name: ')
Name = 'Safi'
print('\n',Name,' Welcome to the guess the four-lettered word game!\n')
print('------------------------------------------------------------\n')
con = 'y' # var for check the to continue the game
print('The rules are simple...\nYou must a guess a four letter word and you have 15 chances to do so :P')
print('\n Sounds easy right? Lets get on with it!\n')

def getwords():
    fobj = open(r"filename.txt","r+")""*
    
    
import random
import game
#Name = 'Safi' Testing i/p
check=True
rcount=6
print('\t\t\tGUESS GAME\n')
while check == True and rcount != 0 :

    print('Log in to continue\n')
    uname=input('User name: ')
    pwd=input('Password:')
    if uname == 'critical' and pwd == '1234':
        Name = input('Enter your name: ')
        print('\n', Name, ' Welcome to the guess the four-lettered word game!\n')
        print('------------------------------------------------------------\n')
        con = 'y'  # var for check the to continue the game
        print('The rules are simple...\nYou must a guess a four letter word and you have 15 chances to do so :P')
        print('\n Sounds easy right? Lets get on with it!\n')


        def getwords():
            fobj = open(r"filename.txt", "r+")
            get = fobj.read().splitlines()
            return get


        get = getwords()
        game.play(con, get, Name)
        # print(get) #check if the words are fetched from file

    else:
        print('User name or password wrong')
        rcount-=1
        print('Remaining attempts ',rcount,'\n\n')




 



