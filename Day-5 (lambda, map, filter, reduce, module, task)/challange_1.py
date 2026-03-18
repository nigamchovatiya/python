"""
  Here i performed using map and lembda to apply a 10%
  discount on all price.
"""

# -----------------------------------------------------------------

# Function of user_sort 


def total_discount(user_list: list) -> None:
    """
    This perform map and lambda to discount on a total
    price and print a final price

    Args:
        user_list(list) : Take a list of user items  

    Return:
        None : Print discount price   
    """

    # discountprice = totalPrice * 0.1
    # finalprice = totalprice - discountprice

    product_discount_price = list(
        map(lambda x: x['price'] - (x['price'] * 0.1), user_list)
    )
    
    # Print discount data
    print("total price:", user_list) # before discount price
    # After discount price
    print("Discount on total price:", product_discount_price)    
   

# -----------------------------------------------------------------

def main() -> None:
    """main function run the program"""

    user_list = []

    n = int(input("Enter a number you want to add a item."))

    # Iterate through total number of item
    for i in range(n):
        name = input("enter a name of item: ")
        price = float(input("enter a price of item: "))

        user_list.append({"name": name, "price": price})

    # Function call
    total_discount(user_list) 
  

# -----------------------------------------------------------------

if __name__ == "__main__":
    main()

  