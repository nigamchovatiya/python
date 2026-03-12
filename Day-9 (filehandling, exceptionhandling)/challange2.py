"""
  simple log writer that append timestemp entries 
  to a log file.
"""

#-----------------------------------------------------------

import datetime

#-----------------------------------------------------------

def write_log(message: str) -> None:
    """
    Args:
        message(str): log message

    Return:
        None: None     
    """

    # hour-minute-second store 
    time_str = datetime.datetime.now().strftime("%H:%M:%S")

    try:
        with open('data.log', 'a') as file:
            file.write(f"[{time_str}] {message}\n")

    except FileNotFoundError:
        print("Error: file not found.")        

    except PermissionError:
        print("Error: not permission on append file.")    

    finally:
        print("append operation completed..")        


#------------------------------------------------------------

def main() -> None:
    """main program to run"""

    write_log("this is message for program start.")
    write_log("log in..")
    write_log("log out.")
    write_log("this is message for end.")


#------------------------------------------------------------

if __name__ == "__main__":
    main()     
