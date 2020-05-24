import random
if __name__ == '__main__':


    s = 0
    sum = 0
    b = True
    while b  :
        print("Welcom to dices game!")
        a=input("Enter the number of dices you want to roll: ")
        if a.isdigit():
            a = int(a)
            if a <= 8 and a >= 1:
                if a == 1 :
                    s = random.randint( 1 , 6 )
                    sum += s
                    print(f"RESULT: {sum}")
                    break

                for i in range(1 , a+1) :
                    s = random.randint( 1 , 6 )
                    sum += s
                    print( f"Dice {i} : {s}")

                print("==========")
                print(f"RESULT: {sum}")
                print("==========")
                break

            else:
                print("USAGE: the number must be between 1 and 8")
                continue

        else:
            print("USAGE: the number must be between 1 and 8")
            continue



