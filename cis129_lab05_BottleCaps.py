# CIS129_Angel_Canez_Lab5.py
# This program converts pseusdo code to calculate the total number of bottles collected during seven days

# variables below
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0.0
keep_going = "y"

# Loop 
while keep_going.lower() == "y":
    total_bottles = 0
    total_payout = 0.0
    
    # Get number of bottles for each day
    while counter <= 7:
        print("Enter number of bottles returned for day #", counter, ":")
        today_bottles = int(input())
        total_bottles += today_bottles
        counter += 1
    
    # Calculate the total payout
    total_payout = total_bottles * 0.10
    
    # Print the number of total bottles and total payout
    print("The total number of bottles collected is", total_bottles)
    print(f"The total paid out is $ {total_payout:.2f}")

    # Prompt user if they want to enter another week's worth of data
    keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

    counter = 1  
