from __future__ import print_function

import random

GREETINGS = [
    'Hi, y\'all',
    'G\'day, mate!',
]

def greeting():
    return random.choice(GREETINGS)

if __name__ == '__main__':
    print(greeting())
