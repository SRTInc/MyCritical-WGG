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
    