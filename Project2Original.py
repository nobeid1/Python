# Nasim Obeid
# CS A131
# Date: March 3, 2018
# Project 
# Filename: Project2

Tax = 0.08
    # Sandwiches
Sandwiches = 0
Hamburger = 2.75
Cheeseburger = 3.25
Chicken_Sandwich = 2.50
    # Side Order
Side_Order = 0
French_Fries = 2.25
Onion_Rings = 1.75
Side_Salad = 1.50
    # Drinks
Drinks = 0
Small = 1.50
Medium = 2.25
Large = 2.75

print("*** *** *** *** Binary Burgers Order Program *** *** *** ***\n")
orders = int(input("how many orders would you like to order? "))
while orders<1:
    print("The number of orders needs to be greater than zero. Try again!")
    orders = int(input("how many orders would you like to order? "))

for x in range(1,orders+1):
   
    print("\n*************************~~~~~~~~Processing Order #",x,"~~~~~~~~*************************",sep="")
    
    Sandwiches = int(input("Enter 1 for hamburger, 2 for a cheeseburger, 3 for a chicken sandwich, or 4 for no sandwich: "))

    while Sandwiches<1 or Sandwiches>4:
        print("numbers must be between 1 and 4. Try again!")
        Sandwiches = int(input("\nEnter 1 for hamburger, 2 for a cheeseburger, 3 for a chicken sandwich, or 4 for no sandwich: "))

    Side_Orders = int(input("\nEnter 1 for French Fries, 2 for onion rings, 3 for a side salad, or 4 for no side: "))

    while Side_Orders<1 or Side_Orders>4:
        print("numbers must be between 1 and 4. Try again!")
        Side_Orders = int(input("\nEnter 1 for French Fries, 2 for onion rings, 3 for a side salad, or 4 for no side: "))

    Drinks = int(input("\nEnter 1 for Coke, 2 for Sprite, 3 for Lemonade, or 4 for a cup of water: "))
    while Drinks<1 or Drinks>4:
         print("numbers must be between 1 and 4. Try again!")
         Drinks = int(input("\nEnter 1 for Coke, 2 for Sprite, 3 for Lemonade, or 4 for a cup of water: "))
   
    if Drinks == 1 or Drinks == 2 or Drinks == 3:
             Size = int(input("\nEnter 1 for Small, 2 for Medium, 3 for Large: "))
             while Size>3 or Size<1:
                print("numbers must be between 1 and 3. Try again!")
                Size = int(input("\nEnter 1 for Small, 2 for Medium, 3 for Large: "))

    else:
        ''
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~********Total for order #",x,"********~~~~~~~~~~~~~~~~~~~~~~~~",sep="")
    ####
    if Sandwiches == 1:
        print("Hamburger                    $", format(Hamburger, '.2f'), sep='')
        Sandwiches = 2.75
    elif Sandwiches == 2:
        print("Cheeseburger                 $", format(Cheeseburger, '.2f'), sep='')
        Sandwiches = 3.25
    elif Sandwiches == 3:
        print("Chicken Sandwich             $", format(Chicken_Sandwich, '.2f'), sep='')
        Sandwiches = 2.50
    else:
        ''
        Sandwiches = 0
    #####
    if Side_Orders == 1:
        print("French Fries                 $", format(French_Fries, '.2f'), sep='')
        Side_Orders = 2.25

    elif Side_Orders == 2:
        print("Onion Rings                  $", format(Onion_Rings, '.2f'), sep='')
        Side_Orders = 1.75
    elif Side_Orders == 3:
        print("Side Salad                   $", format(Side_Salad, '.2f'), sep='')
        Side_Orders = 1.50
    else:
        ''
        Side_Orders = 0
        ####
    if Drinks == 1:
        if Size == 1:
            print("Small Coke                   $", format(Small, '.2f'), sep='')
            Drinks = 1.50
        elif Size == 2:
            print("Medium Coke                  $", format(Medium, '.2f'), sep='')
            Drinks = 2.25
        elif Size == 3:
            print("Large Coke                   $", format(Large, '.2f'), sep='')   
            Drinks = 2.75
        else:
            print("Medium Coke                  $", format(Medium, '.2f'), sep='')
            Drinks = 2.25 
    elif Drinks == 2:
        if Size == 1:
            print("Small Sprite                 $", format(Small, '.2f'), sep='')
            Drinks = 1.50
        elif Size == 2:
            print("Medium Sprite                $", format(Medium, '.2f'), sep='')
            Drinks = 2.25
        elif Size == 3:
            print("Large Sprite                 $", format(Large, '.2f'), sep='')   
            Drinks = 2.75
        else:
            print("Medium Sprite                $", format(Medium, '.2f'), sep='')
            Drinks = 2.25
    elif Drinks == 3:
        if Size == 1:
            print("Small Lemonade               $", format(Small, '.2f'), sep='')
            Drinks = 1.50
        elif Size == 2:
            print("Medium Lemonade              $", format(Medium, '.2f'), sep='')
            Drinks = 2.25
        elif Size == 3:
            print("Large Lemonade               $", format(Large, '.2f'), sep='') 
            Drinks = 2.75
 
        else:
            print("Medium Lemonade              $", format(Medium, '.2f'), sep='')
            Drinks = 2.25  
    else:
        print("Cup Of Water                       ")
        Drinks = 0
        ####
    print("----------------------------------")
    subtotal = Sandwiches + Side_Orders + Drinks
    print("Subtotal:                    $", format(subtotal, '.2f'), sep='')
    Sales_Tax = subtotal * Tax
    print("Sales Tax:                   $", format(Sales_Tax, '.2f'), sep='')
    print("Total:                       $", format((subtotal + Sales_Tax), '.2f'), sep='')



