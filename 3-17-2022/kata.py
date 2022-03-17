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