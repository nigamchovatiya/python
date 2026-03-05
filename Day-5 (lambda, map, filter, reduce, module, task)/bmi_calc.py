"""
  Here i performed Checks BMI(Body Mass Index) in user given 
  height and weight for user and return Status
  
"""

# --------------------------------------------------------------

# Function of check_bmi 


def check_bmi(height: float, weight: float) -> float:
    """
    This perform height and weight according bmi calculate
    and return result

    Args:
        height(float) : user input for height   
        weight(float) : user input for weight   

    Return:
        Float : calculate bmi number    
    """

    if height <= 0 or weight <= 0:
        return None
    
    # convert height in meter. 
    elif height > 0:
        height = height / 100
    
    # BMI formula = weight / (height**2)
    bmi = weight / (height ** 2)
    return bmi


# result_bmi 


def result_bmi(result: float) -> None:
    """
    This perform check bmi range according user input.

    Args:
        result(float) : BMI result get  

    Return:
        None : Range according print output    
    """

    print(f"Your BMI: {result} range is below :")

    if result is None:
        print("Invalid Bmi")

    elif result < 18.5:
        print("Under weight....")    

    elif result < 25:
        print("Noraml weight...")

    elif result < 30:
        print("Over weight...")

    else:
        print("Obese..")               
        

# --------------------------------------------------------------

def main() -> None:
    """main function run the program"""

    height = float(input("Enter your height in centimeter: "))
    weight = float(input("Enter your weight in kilograms: "))

    result = check_bmi(height,weight) # store bmi value
    result_bmi(result) # print result
  

# ---------------------------------------------------------------

if __name__ == "__main__":
    main()
