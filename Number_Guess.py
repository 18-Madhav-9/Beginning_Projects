import random 

# Taking input from user if the user wants to play
play = input("Do you want to Play the Game (Enter Yes or No ):")

# Infinite conditional loop if user wants to play many times  
while play.lower() == "yes":

    #variable for counting the tries taken by user
    count = 0

    # upper limit and lower limit input from user
    upper_limit = int(input("Enter Upper Limit :"))
    lower_limit = int(input("Enter Lower Limit :"))
    
    # using random.randrange to randomly decide a NUMBER between the limits
    system_guess = random.randrange(lower_limit,upper_limit)

    # infinite loop for tries which we can break later 
    while True :
        
        #taking guess from user
        user_guess = int(input("Enter Your Guess :"))

        # if user guess is correct  
        if user_guess == system_guess :

            # increase counter by 1 
            count +=1 
            print("Your Guess is correct and tries taken is :",count)
            #break the infinite loop for tries
            break

        # if user guess is incorrect 
        elif user_guess != system_guess :
            
            if user_guess < system_guess :
                print("Your Guess is too small ")
            else :
                print("your guess is too big")
            #increase tries counter
            count += 1
            continue

        else :
            print("Something is wrong ")

    # if the user wants to play another game
    play = input("Do You want to play again :")

    # if yes then continue the infinite loop for play  else break it 
    if play.lower() == "yes" :
        continue
    else :
        break
