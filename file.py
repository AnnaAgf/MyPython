import random

world_list = ('way', 'oil', 'cosmic', 'plan', 'library', 'washer', 'olimpia')


def print_users_word(arg):
    print(''.join(arg))
    #return True


secret_word = random.choice(world_list)
print(secret_word)

users_word = ['*'] * len(secret_word)
print_users_word(users_word)

users_word[1] = 's'
print_users_word(users_word)
