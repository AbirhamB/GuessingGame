secret_word='Abay'
guess=''
guess_count=0
guess_limit=3
is_out_of_guess=False
while guess!=secret_word and not(is_out_of_guess):
    if guess_count < guess_limit:
        guess=input('Guess here: ')
        guess_count+=1
    else:
        is_out_of_guess = True

if is_out_of_guess:
    print("you are out of guessing limit, you lose!")
else:
    print('congrats, you win!')
