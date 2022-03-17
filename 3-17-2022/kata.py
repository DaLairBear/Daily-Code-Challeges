# 8 kyu
# We need a function that can transform a number into a string.

# What ways of achieving this do you know?

# Examples:
# 123 --> "123"
# 999 --> "999"

def number_to_string(num):
    # Return a string of the number here!
    return str(num)



# 8 kyu
# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since midnight in milliseconds.

# Example:
# h = 0
# m = 1
# s = 1

# result = 61000
# Input constraints:

# 0 <= h <= 23
# 0 <= m <= 59
# 0 <= s <= 59

def past(h, m, s):
    # Good Luck!
    import datetime
    timepast = datetime.timedelta(hours=h, minutes=m, seconds=s)
    return timepast.total_seconds()*1000



# 8 kyu 
# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples:

# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!

def rps(p1, p2):
    #your code here
    if p1 == p2:
        return 'Draw!'
    else:
        if p1 == 'rock':
            if p2 == 'scissors':
                return "Player 1 won!"
            else:
                return "Player 2 won!"
        elif p1 == 'scissors':
            if p2 == 'paper':
                return "Player 1 won!"
            else:
                return "Player 2 won!"
        elif p1 == 'paper':
            if p2 == 'rock':
                return "Player 1 won!"
            else:
                return "Player 2 won!"




# 8 kyu 
# Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    #your code here
    return x.replace(" ", "")