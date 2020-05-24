
if __name__ == '__main__':

    b = True
    while b :
        print("Please enter your amount:")
        amn = input()
        if amn.isdigit():
            amn = int(amn)
        else:
            print("Number is incorrect, try again.")
            continue

        c = True
        while c:
            print("Please enter your tax rate:")
            rate = input()
            if rate.isdigit():
                rate = int(rate)
                if rate < 100 :
                    break
                else:
                   print("Rate is incorrect, try again.")
                   continue
            else:
                print("Number is incorrect, try again.")
                continue
        sum1 = amn * rate / 100
        sum2 = amn - sum1
        print("===== ===== ===== =====")
        print(f"AMOUNT: {amn}$")
        print(f"RATE: {rate}%")
        print("===== ===== ===== =====")
        print(f"TAX: {sum1}$")
        print(f"NET: {sum2:.2f}$")
        print("===== ===== ===== =====")

        b = False


