# Brian Preston
# CSD-325
# Module 1.3

# User Input: The program asks the user for the number of bottles.
# Countdown Function: The function countdown_bottles takes the input and manages the countdown.
# Singular vs. Plural: When the number of bottles is greater than 1, it will then use plural ("bottles"), 
# and when it reaches 1, it switches to just bottle
# Final Message: After the countdown ends, it reminds the user to buy more beer.

def countdown_bottles(bottle_count):
    # Loop from the number of bottles down to 1
    while bottle_count > 0:
        if bottle_count > 1:
            print(f"{bottle_count} bottles of beer on the wall, {bottle_count} bottles of beer.")
            bottle_count -= 1
            print(f"Take one down and pass it around, {bottle_count} bottle(s) of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            bottle_count -= 1
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
    
    # Reminder to buy more beer
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy more, 99 bottles of beer on the wall!")

# Main Program
def main():
    # Ask the user for the number of bottles
    bottle_count = int(input("Enter the number of bottles: "))
    
    # here we will Call the countdown function
    countdown_bottles(bottle_count)

# not forgetting to Run the program
if __name__ == "__main__":
    main()
