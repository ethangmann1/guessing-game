i = "mazda miata"
guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == i:
        print('Miata is always the answer')
        break
else:
    print('Wrong, try again')
    