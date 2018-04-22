from __future__ import print_function

import random

GREETINGS = [
    'Hiiii, y\'ALL',
    'G\'day, mate!',
]

def greeting():
    return random.choice(GREETINGS)

if __name__ == '__main__':
    print(greeting())
