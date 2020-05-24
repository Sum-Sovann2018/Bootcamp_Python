
def main():
    # 1 print("Welcome to kirirom!")

     # 2 print("what is your name?")
     # name=input()
     # print("Hello "+name)


     # 3number=input("Enter a number")#'-333'
     # if(number.isdigit()):
     #     number=int(number)
     #     for i in range(number):
     #         print("Hello world")
     # else:
     #     print("nothing to display")


    #4 num=input("Enter first number:")
    # numb=input("Enter second number:")
    # if num>numb:
    #     print(num+" > "+numb)
    # elif num == numb:
    #     print(num+" = "+numb)
    # elif num<numb:
    #     print(numb+" > "+num)


    # 5num=input("Enter first number:")
    # numb=input("Enter second number:")
    # if num>numb:
    #  print(numb+" < ",num)
    # elif num == numb:
    #  print(num+" = ",numb)
    # elif num<numb:
    #  print(num+" < ",numb)



   #6 b=1
   # while b>0:
   #  num=input("Enter a number : ")
   #  if(num.isdigit()):
   #      num=int(num)
   #      if num%2==0:
   #          print("Even number")
   #      else:
   #          print("Odd number")
   #  elif(num.isalpha()):
   #      num=num
   #      if(num=="Exit" or num=="exit"):
   #          print("")
   #          break
   #      else:
   #       print("it not number")
   #       continue

     # 7c=0
     # total=0
     # while c==0:
     #    num=input("Enter number: ")
     #    if num.isdigit():
     #        num=int(num)
     #        total=total+num
     #        print(f"Total: {total}")
     #        continue
     #    elif num.isalpha():
     #        num=num
     #        if(num=="exit"):
     #            break
     #        else:
     #            print("Total: ",total)
     #            continue


      #8 print (random.randint(1,100))

      #9 for x in range(3):
      #     print(random.randint(1,100))


      # 10str=input("Ënter string")
      # if str.isalpha():
      #     print(len(str))
      # else:
      #     print(" this is not a string")


      # 11str=input("Enter a string")
      # if str.isalpha():
      #     print(str.upper())
      # else:
      #     print("this is not a string")


    # 12str=input("Enter a string")
    # if str.isalpha():
    #     print(str.lower())
    # else:
    #     print("this is not a string")


    # 13str=input("Enter a string")
    # print(''.join(reversed(str)))


     #14 s=input("Enter a title: ")
     # print(f"<h1>{s}</h1>")



    # 15b= True
    # v=""
    # while(b):
    #     s=input("Enter a string")
    #     if s=="Generate" or s=="generate":
    #         b=False
    #     else:
    #         v=v+"<p>"+s+"</p>\n"
    #
    # print(v)


    # 16s=input("Enter a string")
    # if len(s)>0:
    #     print(s[0])
    # else:
    #     print("Empty")



    # 18s=input("Enter a string: ")
    # if s.isalpha():
    #     s = str(s)
    #     if len(s)>0:
    #         l = len(s)
    #         for i in range(l):
    #             if s[i].isupper():
    #                 print( s[i].lower() , end="" )
    #             elif s[i].islower():
    #                 print( s[i].upper() , end="" )
    #
    #     else:
    #         print("Empty")
    # else:
    #     print("Empty")


    s=input("Enter a string: ")
    v = ""
    if s.isalpha() :
        s = str(s)
        if len(s) > 0 :
            l=len(s)
            for i in range(l) :
                if s.cho(i) >= 65 and s.cho(i) <= 77 or s.cho(i) >= 97 and s.cho(i) >=109 :
                    v = s.chr(i) - 13
                    print( v )







import random
if __name__ == '__main__':
    main()
