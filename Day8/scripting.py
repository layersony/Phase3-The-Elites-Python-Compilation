#!/usr/bin/python3
import sys

def greetings(name):
    print(f"Hello and Goodmoring {name}")

if __name__ == '__main__':
    name = sys.argv[1]

    greetings(name)
