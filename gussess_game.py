
secret_word = "youssef"
guess =""
count_guess = 0
count_limit = 3
out_of_guesses= False

guess=input("Enter Your Guessing :")
while guess != secret_word and not out_of_guesses:
    if count_guess < count_limit:
        guess=input("False, Please Try again :")
        count_guess +=1
    else:
     out_of_guesses =True

if out_of_guesses:
    print("You Lose,Out Broo")
else:
    print("Winner Winner")