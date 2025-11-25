import random

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
print('You have 5 chances to guess the correct number.\n')

print('Please select the difficulty level:')
print('1. Easy (10 chances)')
print('2. Medium (5 chances)')
print('3. Hard (3 chances)')

user_choice = input('Enter your choice: ')

if user_choice == '1':
    user_difficulty = 'Easy'
elif user_choice == '2':
    user_difficulty = 'Medium'
elif user_choice == '3':
    user_difficulty = 'Hard'
else:
    print('Please enter a valid number')

print(f'\nGreat! You have selected the {user_difficulty} difficulty level.')
print("Let's start the game!\n")

rand_number = random.randint(1, 100)

def number_guess_game(user_difficulty, rand_number):
    number_of_attempts = 1

    if user_difficulty == 'Easy':
        while number_of_attempts != 11:
            try:
                user_attempt = int(input('Enter your guess: '))
                if user_attempt == rand_number:
                    print(f"Congratulations! You guessed the correct number in {number_of_attempts} attempts.")
                    break
                else:
                    print(f'Incorrect! The number is {'greater' if user_attempt < rand_number else 'less'} than {user_attempt}\n')
                    number_of_attempts += 1
            except ValueError:
                print('Please enter a valid number')
    
    if user_difficulty == 'Medium':
        while number_of_attempts != 6:
            try:
                user_attempt = int(input('Enter your guess: '))
                if user_attempt == rand_number:
                    print(f"Congratulations! You guessed the correct number in {number_of_attempts} attempts.")
                    break
                else:
                    print(f'Incorrect! The number is {'greater' if user_attempt < rand_number else 'less'} than {user_attempt}\n')
                    number_of_attempts += 1
            except ValueError:
                print('Please enter a valid number')

    if user_difficulty == 'Hard':
        while number_of_attempts != 4:
            try:
                user_attempt = int(input('Enter your guess: '))
                if user_attempt == rand_number:
                    print(f"Congratulations! You guessed the correct number in {number_of_attempts} attempts.")
                    break
                else:
                    print(f'Incorrect! The number is {'greater' if user_attempt < rand_number else 'less'} than {user_attempt}\n')
                    number_of_attempts += 1
            except ValueError:
                print('Please enter a valid number')

number_guess_game(user_difficulty, rand_number)