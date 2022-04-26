"""
0 - zero
1 - one
....
9 - nine
10 - ten
11 - eleven
..
19 - nineteen
20 - twenty
21 - twenty - one
..
30 - thirty - one
100 - one hundred
101 - one hundred and one
..
999 - nine hundred and ninety nine
1000 - one thousand
1001 - one thousand and one

last 2 digits:
    if last two numbers are under 20 -> special case
    if last digit == 0 -> special case

every 3 digits:
    if > 99, find hundreds conversion
"""

# constants
num_dict = {
    0  : "zero",
    1  : "one",
    2  : "two",
    3  : "three",
    4  : "four",
    5  : "five",
    6  : "six",
    7  : "seven",
    8  : "eight",
    9  : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30  : "thirty",
    40  : "fourty",
    50  : "fifty",
    60  : "sixty",
    70  : "seventy",
    80  : "eighty",
    90  : "ninety",
}

endings = {
    1 : "thousand",
    2 : "million",
    3 : "billion"
}

three_digit_ending = "hundred"
space = ' '

def english_int(num: int) -> str:
    if num in num_dict:
        return num_dict[num]
    
    index = 0
    english = ''
    three_digit_eng = ''

    # break in < 1000 chunks but ignore zeros
    while(num > 0):        
        mark = endings[index] if index in endings else ''
       
        three_digit_eng = return_three_digit_english(num % 1000)
        index += 1
        num = int(num / 1000)

        if (three_digit_eng == num_dict[0]):
            continue
        
        english = three_digit_eng + space + mark + space + english
        
    return english


def return_three_digit_english(num: int) -> str:
    '''
    Returns the three digit english equivalent
    '''
    if num in num_dict:
        return num_dict[num]

    if num > 99:
        hundreds_digit = num_dict[int(num / 100)] + space + three_digit_ending
        two_digit_remainder = int(num % 100)
        if two_digit_remainder == 0:
            return hundreds_digit
        return hundreds_digit + space + retrun_two_digit_english(two_digit_remainder)
    
    return retrun_two_digit_english(num)


def retrun_two_digit_english(two_digit_remainder: int) -> str:
    '''
    Returns the two digit english equivalent
    '''
    if two_digit_remainder in num_dict:
        return num_dict[two_digit_remainder]

    tens_digit = num_dict[int(two_digit_remainder / 10) * 10]
    ones_digit = num_dict[two_digit_remainder % 10]
    return tens_digit + space + ones_digit

# TODO: Add unit tests to validate instead
print(english_int(3), 3)
print(english_int(33), 33)
print(english_int(313), 313)
print(english_int(333), 333)
print(english_int(340), 340)
print(english_int(1333), 1333)
print(english_int(31313), 31313)
print(english_int(31), 31)
print(english_int(1340), 1340)
print(english_int(35313), 35313)
print(english_int(100333), 100333)
print(english_int(23340), 23340)
print(english_int(31000), 31000)