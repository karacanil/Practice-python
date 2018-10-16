#Exercise 25
#Guessing game

def guessGame(domain):
    
    #Creating a counter variable to count the number of guesses
    counter=0
    
    while True:
        counter+=1
        
        #Creating a optimal guess according to the current domain
        guess = domain[len(domain)//2]
        
        print('\nMy guess is ->%d<-'%(guess))
        print(
            '''
Write down (correct) if my guess is correct
Write down (greater) if your number is greater than my guess
Write down (lower) if your number is lower than my guess
            '''
            )
        info = input('\n')
        
        #Checking if user has entered a valid answer
        if(info=='correct' or info=='greater' or info=='lower'):
            if info=='correct':
                print('It took me %d guesses to find it out'%(counter))
                break
            #Adjusting the domain according to the user's answer
            elif info=='greater':
                domain = domain[(domain.index(guess))+1:]
            else:
                domain = domain[:domain.index(guess)]
        else:
            counter-=1

#Defining the domain list
l = list(range(101))

#Checking if user has entered a valid input
confirmation = ''
while(confirmation!='done'):  
    confirmation = input("Pick a number between 0 and 100(0 and 100 included) and than type 'done':")

#Calling the guessGame function
guessGame(l)
