from __future__ import print_function

import random

GREETINGS = [
    'Hiiii testing3, y\'ALL',
    'G\'day, mate! New branch',
]

def greeting():
    return random.choice(GREETINGS)

if __name__ == '__main__':
    print(greeting())
