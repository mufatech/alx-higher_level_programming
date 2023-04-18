#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    R1 = Rectangle(10, 2)
    print(R1.id)

    R2 = Rectangle(2, 10)
    print(R2.id)

    R3 = Rectangle(10, 2, 0, 0, 12)
    print(R3.id)

