from datetime import datetime
file = open("laptop.txt", "r")
mydict = {}
laptop_id = 1

for line in file:
    line = line.replace("\n", "")
    mydict.update({laptop_id: line.split(",")})
    laptop_id += 1

def Buy():
    name = input("**Enter your name**: ")
    phone = input("**Enter your phone number**: ")
    print("******************************************************************************************************")
    print("S.N    \tName    \t\tBrand\t\t Price\t\t Quantity\tGeneration   \tModel")
    print("******************************************************************************************************")
    a = 1
    file = open("laptop.txt", "r")
    for line in file:
        print(a ,"\t"+line.replace(",","\t"))
        a += 1
   
    

    valid_id = int(input("Please provide the id of the laptop that you want to purchase: "))

    while valid_id <= 0 or valid_id > len(mydict):
        print("\n************************************************************************")
        print("     ***** Wrong Input  *****   ")
        print(" ****Please enter a  Valid input!!****")
        print("************************************************************************\n")

    get_quantity = int(mydict[valid_id][3])
    user_quantity = int(input("****Enter quantity of laptop****: "))

    while user_quantity <= 0 or user_quantity > get_quantity:
        print("\n************************************************************************")
        print("      ****Laptop is out of stock !! ****    ")
        print("\n************************************************************************")

    mydict[valid_id][3] = int(get_quantity) - int(user_quantity)
    delivery_cost = input("Can i get my Product delivered ?(y/n): ").lower()
    if delivery_cost == "y":
        print("\n*****************************************************************************")
        print("                        Thank You for delivering my Product                    ")
        print("*****************************************************************************\n")
    else:
        print("\n*****************************************************************************")
        print("                   *****Thank You for your Service*****                        ")
        print("\n*****************************************************************************")


    Track_order = input("*****Do you want to track your order ?(y/n):*****").lower()

    if Track_order == "y":
        print("\n*****************************************************************************")
        print("       ****Your product has picked by one of our delivery Agent****            ")
        print("*****************************************************************************\n")

    else:
        print("\n*****************************************************************************")
        print("                   ****We will Contact You soon ***                            ")
        print("\n*****************************************************************************")
    
    print("         Here is the Bill Of the products that you purchased           ")

    name_of_product = mydict[valid_id][0]
    quantity_selected_by_user = user_quantity
    unit_price = mydict[valid_id][2]
    price_of_selected_item = mydict[valid_id][2].replace("$",'')
    total_price = int(price_of_selected_item)*int(quantity_selected_by_user)
    vatAmount = 0.13 *total_price
    grossAmount = total_price +vatAmount
    dateandtime = datetime.now()
    brandName = mydict[valid_id][1]
    bill_Number = datetime.now()

    user_purchased_laptops = []
    user_purchased_laptops.append([name_of_product,quantity_selected_by_user,unit_price,price_of_selected_item,total_price,vatAmount,grossAmount])


    print("\n")
    print("****TechMax City****", "\t\t\t\t\t\t\t\t" " Date: ",
          dateandtime.strftime("%d" " " "%b"",""%Y"))
    print("Kumaripati - Lalitpur ", "\t\t\t\t\t\t\t\t" "   " "Time:",
          dateandtime.strftime("%I" ":" "%M" "%p"))
    print("techmax096@gmail.com")
    print("015343457")

    print("\n")
    print("Bill Number:" + str(dateandtime.strftime("%f")))

    print("******************************************************************************************")
    print("S.N", "\t\t", "Product's Name", "\t", "Brand",
          "\t\t  ", "Quantity", "\t\t", "Amount")
    print("******************************************************************************************")
    print(" 1 ", "\t\t" + str(name_of_product), "\t\t" + str(brandName),
          "\t""\t" + str( quantity_selected_by_user) + "\t" + str(unit_price))
    print("\n")
    print("\n")
    print("*****************************************************************************************************")
    print("Net Amount:", "\t\t\t\t\t\t\t\t\t\t", "$" + str(total_price))
    print("Vat Amount:", "\t\t\t\t\t\t\t\t\t\t", "$" + str(vatAmount))
    print("*****************************************************************************************************")
    print("Gross Amount:", "\t\t\t\t\t\t\t\t\t\t", "$" + str(grossAmount))
    print("******************************************************************************************")
    print("\n")
    print("Terms & Conditions" "\t\t\t\t\t\t\t" + "Bank Details")
    print("Payment is due within 20 days." "\t\t\t\t\t" "    " "Nepal Investment Mega Bank")
    print("\t\t\t\t\t\t\t\t", "Account Number:05205030262927")
    print("\n")
    print("******************************************************************************************")
    print("\t\t\t\t""  ", "Thank You for your order.")
    print("******************************************************************************************")
    print("\n")
