import random

MAX_ERRORS = 8

world_list = ('way', 'oil', 'cosmic', 'plan', 'library', 'washer', 'olimpia')


def print_users_word(arg):
    print(''.join(arg))
    #return True


secret_word = random.choice(world_list)
print(secret_word)

users_word = ['*'] * len(secret_word)
print_users_word(users_word)

#users_word[1] = 's'
#print_users_word(users_word)


errors_counter = 0
while True:
    letter = raw_input("vvedi bukvu ")

    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        for idx, char in enumerate(secret_word):
            if char == letter:
                users_word[idx] = letter
            idx += 1
        if '*' not in users_word:
            print('win ;)')
            break

    else:
        errors_counter += 1
        print('mistakes are ', errors_counter)
        if errors_counter == MAX_ERRORS:
            print('loser')
            break
    print_users_word(users_word)
print('Bye!')

    #print(letter)

