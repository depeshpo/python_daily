"""
As soon as the hiker moves down from initial (sea level) valley starts
"""

if __name__ == "__main__":
    data = "DDUUDDUDUUUD"
    initial_level = 0
    prev_level = 0
    number_of_valleys = 0
    for item in data.upper():
        prev_level = initial_level
        if item == 'U':
            initial_level += 1
        elif item == 'D':
            initial_level -= 1
        if initial_level == -1 and prev_level == 0:
            number_of_valleys += 1

    print(number_of_valleys)
