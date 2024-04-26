import random 


play = input("Do you want to Play the Game (Enter Yes or No ):")
while play.lower() == "yes":
    count = 0
    upper_limit = int(input("Enter Upper Limit :"))
    lower_limit = int(input("Enter Lower Limit :"))
    system_guess = random.randrange(lower_limit,upper_limit)
    while True :
        user_guess = int(input("Enter Your Guess :"))
        if user_guess == system_guess :
            count +=1 
            print("Your Guess is correct and tries taken is :",count)
            break
        elif user_guess != system_guess :
            if user_guess < system_guess :
                print("Your Guess is too small ")
            else :
                print("your guess is too big")
            count += 1
        else :
            print("Something is wrong ")
    play = input("Do You want to play again :")

    if play.lower() == "yes" :
        continue
    else :
        break
