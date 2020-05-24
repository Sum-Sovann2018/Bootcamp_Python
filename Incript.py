

if __name__ == '__main__':
    key = input("Enter the number of key: ")
    string = input("Enter the string to encrypt: ")


    if len(string) > 0:
        for i in string:
            if  ord(i) >= 97 and ord(i) <= 122:
                str1 = ""
                str1 += chr((((ord(i)+key)-97)%26)+97)
                print(str1.upper())


    else:
        print("Nothing to encrypt.")