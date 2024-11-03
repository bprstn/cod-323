# Brian Preston
# csd-325
# Module3.2
# Changes that are requested:
# Updated input prompts to use my initials"BPP:".
# I Increased the house fee to 12%.
# Added a notice that is about a 10 mon bonus for dice totals of 2 or 7
# then I created a a bonus check, awarding 10mon and displaying a message if triggered.

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

**Notice**: If the total dice roll is a 2 or 7, you get a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('BPP: ')  # Changed input prompt to "BPP:"
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll_total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('BPP: ').upper()  # Changed input prompt to "BPP:"
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Check for the 2 or 7 bonus:
    if roll_total == 2 or roll_total == 7:
        print(f'You rolled a total of {roll_total}! You get a 10 mon bonus!')
        purse += 10  # Add the 10 mon bonus to the purse.

    # Determine if the player won:
    rollIsEven = (roll_total) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot  # Add the pot to player's purse.
        print('The house collects a', pot * 12 // 100, 'mon fee.')  # House fee is now 12%
        purse -= (pot * 12 // 100)  # Subtract the 12% house fee.
    else:
        purse -= pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
