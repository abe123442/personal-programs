import random
import sys


class error(Exception):
    pass

class Exit(error):
    pass

def rand_pass():
    simple_pass = list("abcdefghijklmnopqrstuvwxyz") 
    normal_pass = list("abcdefghijklmnopqrstuvwxyz1234567890")
    advanced_pass = list("ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstvxyz1234567890!@#$%^&*()")
    options = input("Do you want to generate a password? (Yes, No or Q) ").lower()
    
    if options == "yes":
        pass
    elif options == "no":
        sys.tracebacklimit = 0
        raise Exit()
    elif options == "q":
        sys.tracebacklimit = 0
        raise Exit()
    else:
        print("Invalid Input")
        return()

    user_input = input("Do you want a simple password (s), a normal password (n) or an advanced password (a)? ")

    if user_input == "s":
        gen = random.sample(simple_pass, 8)
        pwd = ",".join(str(x) for x in gen).replace(",","",len(",".join(str(x) for x in gen)))
        print(pwd)

    elif user_input == "n":
        gen = random.sample(normal_pass, 10)
        pwd = ",".join(str(x) for x in gen).replace(",","",len(",".join(str(x) for x in gen)))
        print(pwd)


    elif user_input == "a":
        gen = random.sample(advanced_pass, 12)
        pwd = ",".join(str(x) for x in gen).replace(",","",len(",".join(str(x) for x in gen)))
        print(pwd)

    else:
        print("Invalid input!")
        return()

while 0 < 1:
    rand_pass()
