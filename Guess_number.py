import random
if __name__ == '__main__':

    print("Hello, what is your name?")
    name = input()

    b = True

    while b :
        print(f"Well {name}, try to guess the number I have in mine!")

        v = random.randint( 1 , 50 )
        for i in range(3):
            num=input()
            if num.isdigit():
                num = int( num )
                if num > v:
                    print("Too high, try again")

                elif num < v :
                    print("Too low, try again")
            else:
               print("Enter number only")

        print(f"It took you 3 turns to guess my number which was {v}!")
        c = True
        while c :
            print("Do you want to play again? [Y/N]")
            s = input()
            s = str(s)
            if s == "Y":
                c = False
                continue

            elif s == "N":
                 print(f"Ok, bye {name}! See you later")
            else:
                 print("Sorry, I did not understand. Let me repeat:")
                 continue



