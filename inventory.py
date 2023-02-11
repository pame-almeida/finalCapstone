
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country=country
        self.code=code
        self.product=product
        self.cost=cost
        self.quantity=quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        shoe_cost={}
        k,v=self.product,self.cost
        shoe_cost[k]=v
        return shoe_cost

    def get_quantity(self):
        #Return the quantity of the shoes.
        shoe_quantity={}
        k,v=self.product,self.quantity
        shoe_quantity[k]=v
        return shoe_quantity

    def __str__(self): 
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        #Open inventory data
        with open ("inventory.txt") as f1:
            #Create variable to conain text from inventory.txt skipping the first line
            data=f1.readlines()[1:]
            count=0
            #For each line in the variable data, separate the items by the comma and then create a new variale with class "Shoe" and apply the class parameters to the corresponding sections
            for num, line in enumerate(data):
                section=line.strip().split(",")
                count+=1
                locals()[f"shoe_file_{count}"]=Shoe(section[0],section[1],section[2],section[3],section[4])
                #Append new variable to list shoe_list
                shoe_list.append(locals()[f"shoe_file_{count}"])
    #Pring warning if file does not exist
    except FileNotFoundError:
        print("\nFile not found\n.")

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    input_country=input("Enter the country of the item: ")
    input_code=input("Enter the code of the item: ")
    input_product=input("Enter the name of the item: ")
    input_cost=input("Enter the cost of the item: ")
    input_quantity=input("Enter the quantity of items: ")

    #Use the input to assign the class characteristics
    shoe_caputre=Shoe(input_country,input_code,input_product,input_cost,input_quantity)
    #Append new item to list
    shoe_list.append(shoe_caputre)

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. 
    '''
    read_shoes_data()
    for shoe in shoe_list:
        print(f"{shoe}\n")

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    read_shoes_data()
    #Create dictionary to store the name of the product and its quantity
    shoe_stock={}
    for shoe in shoe_list:
        shoe_stock[shoe.product]=int(shoe.quantity)
    #Sort by value (lowest woul dbe first item in dictionary)
    shoe_stock=sorted(shoe_stock.items(), key=lambda item:item[1])
    #Create list variable with lowest item
    lowest=list(shoe_stock[0])

    print(f"The shoe with the lowest quantity is {lowest[0]} with {lowest[1]} items in existence.")

    #Ask user if they want to update the quantity of the item
    add_shoes=input("\nWould you like to update the quantity this item? (yes/no): ")
    add_shoes.lower()

    if add_shoes=="yes":
        #New quantity
        new_quantity=input("\nEnter the new quantity for the item: ")
        #Change quantity in list
        for shoe in shoe_list:
            if shoe.product==lowest[0]:
                shoe.quantity=new_quantity

            #Save updated list to file
            with open ("inventory.txt", "w") as f2:
                for shoe in shoe_list:
                    f2.write(f"{shoe}\n")

    elif add_shoes=="no":
        main_menu()


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    read_shoes_data()
    #Ask user for the code of the item they are searching for
    input_code=input("Enter the code of the item: ")
    #Match the input to the shoes available in the list
    for shoe in shoe_list:
        if shoe.code==input_code:
            print (shoe)


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    read_shoes_data()
    #Create dictiornary to store the  name of the product and the total value
    shoe_value={}
    for shoe in shoe_list:
        #Cast values to integers
        cost=int(shoe.cost)
        quant=int(shoe.quantity)
        #Fill in dictionary with relevant variables
        shoe_value[shoe.product]=int(cost*quant)
    
    print(shoe_value)


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    read_shoes_data()
    #Create dictionary to store the name of the product and its quantity
    shoe_qty={}
    for shoe in shoe_list:
        shoe_qty[shoe.product]=int(shoe.quantity)
    #Sort by value (highest would be last item in dictionary)
    shoe_qty=sorted(shoe_qty.items(), key=lambda item:item[1])
    #Create list variable with highest item
    highest=list(shoe_qty[-1])

    print(f"\nThe shoe {highest[0]} is for sale")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

def main_menu():
    while True:
        try:
            menu = int(input('''
            Select one of the following options below:
            1 - View all inventory
            2 - View inventory for specific product
            3 - View inventory value
            4 - View product in sale 
            5 - Add new product to inventory
            6 - Re-stock product
            7 - Exit
            : '''))

            if menu == 1:
                view_all()
            elif menu == 2:
                search_shoe()
            elif menu == 3:
                value_per_item()
            elif menu == 4:
                highest_qty()
            elif menu == 5:
                capture_shoes()
            elif menu == 6:
                re_stock()
            elif menu == 7:
                print("\nGoodbye!\n")
                break
            else:
                print("Wrong input. Please try again.")

        except ValueError:
            print ("Wrong input. Please try again.")


main_menu()