import random
import datetime
def play(con,get,Name,check,is_New_Name):   
    fobj = open(r"C:\Safi T\Projects\Github\Shared\Playerscore.txt","a+")
    fp = open(r"C:\Safi T\Projects\Github\Shared\Players.txt","a+")
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
                    fobj.close()
                    

             
                score = 0
                show=input('Do you want to know the secret word which make you lose this game(y/n): ')
                if show == 'y':
                    print('The secret word is  ' + s_word)
                con = input('Do you want to continue the game(y/n): ')
                score = 0
                if con == 'n':
                    print('\nThank you for playing the game ;-) ')
                    break
    print()#C_S:Even I don't know WHAT THE HELL IS THIS DOING HERE!!!