from time import sleep
from os import system


def red_patterns():
    for i in range(10):
        print("\033[1;31;40m*" * 25)

def  yellow_patterns():
    for i in range(10):
        print("\033[1;33;40m*" * 25)

def green_patterns():
    for i in range(10):
        print("\033[1;32;40m*" * 25)


while True:
    #Red
    red_patterns()
    sleep(5)
    system("cls")

    #Yellow
    yellow_patterns()
    sleep(5)
    system("cls")
    
    #Green
    green_patterns()
    sleep(5)
    system("cls")
    for _ in range(4):
        sleep(0.5)
        green_patterns()
        sleep(0.5)
        system("cls")
        

