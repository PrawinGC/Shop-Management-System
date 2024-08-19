import Selling
import Buying

file = open("laptop.txt", "r")
mydict = {}
laptop_id = 1

for line in file:
    line = line.replace("\n", "")
    mydict.update({laptop_id: line.split(",")})
    laptop_id += 1

file = open("name.txt","r")
name_dict = {}
name_id = 1

for line in file:
    line = line.replace("\n","")
    name_dict.update({name_id: line.split(",")})
    name_id += 1

print("\n")
print("\n*****************************************************************************************************")
print("               ** Techmax City **             ")
print("               ** Kumaripati - Lalitpur**     ")
print("*******************************************************************************************************")
print("\n*****************************************************************************************************")
print("               Welcome to Tech max City            ")
print("*******************************************************************************************************")
print("               Please select below options         ")
print("*******************************************************************************************************")

continueloop = True
while continueloop == True:
    print("\n")
    print("1) Press 1 For Selling a Laptop.")
    print("2) Press 2 for Purchasing a Laptop.")
    print("3) Press 3 to retreat.")
    print("\n")
    userinput = int(input("**Select from above mentioned options**: "))

    if userinput == 1:
        Selling.sell()

    elif userinput == 2:
        Buying.Buy()
       
    elif userinput == 3:
        print("\n\n***************************************************************************")
        print("               Thank you for Choosing Us.         ")
        print("                  Have a great day!!              ")
        print("            Hope you will like the product       ")
        print("*****************************************************************************\n")

    else:
          print("\n*****************************************************************************")
          print("      Wrong Input     ")
          print(" Please enter a  Valid input!!")
          print("*****************************************************************************\n")



        
  


