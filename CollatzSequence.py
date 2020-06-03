import time

print('Enter number:')
    
def collatz():
    global number, loopNum
    number = int(number)                # Integer check
    if number % 2 == 0:                 # Even Check
        loopNum = number // 2
        number = loopNum
        print(loopNum)
        time.sleep(0.1)
    elif number % 2 == 1:               # Odd Check
        loopNum = (number * 3) + 1
        print(loopNum)
        time.sleep(0.1)

def loop():
    global loopNum
    while True:
        if loopNum == 1:
            break
        elif loopNum % 2 == 0:
            loopNum = loopNum // 2
            print(loopNum)
            time.sleep(0.1)
        else:
            loopNum = (loopNum * 3) +1
            print(loopNum)
            time.sleep(0.1)
    
while True:
    number = input()
    try:
        collatz()
        loop()
    except ValueError:
        print('Please type in an integer')
    

