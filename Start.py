def start_game(Name,game,check,is_New_Name):
    print('\n', Name, ' Welcome to the guess the four-lettered word game!\n')
    print('------------------------------------------------------------\n')
    con = 'y'  # var for check the to continue the game
    print('The rules are simple...\nYou must a guess a four letter word and you have 15 chances to do so :P')
    print('\n Sounds easy right? Lets get on with it!\n')


    def getwords():
        fobj = open(r"C:\Safi T\Projects\Github\Shared\Randwords.txt", "r+")
        get = fobj.read().splitlines()
        fobj.close()
        return get


    get = getwords()
    game.play(con, get, Name, check,is_New_Name)
    # print(get) #check if the words are fetched from file