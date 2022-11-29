answer = "mazda miata"
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = (input('Guess: '))
    guess_count += 1
    if guess == answer:
        print ('Miata is always the answer')
        break
else:
    print('Wrong, try again')
    