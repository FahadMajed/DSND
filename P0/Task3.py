"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from text_record import TextRecord
from call_record import CallRecord
from typing import List


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts: List[TextRecord] = []
    for record in reader:
        texts.append(TextRecord(record))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls: List[CallRecord] = []
    for record in reader:
        calls.append(CallRecord(record))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

telemarketer_prefix = "140"


def get_numbers_prefixes_called_by_bangalore():
    prefixes = []
    for call in calls:
        if caller_is_bangalorian(call.sending_number):

            prefix = get_prefix(call.recieving_number)

            if prefix not in prefixes:
                prefixes.append(prefix)
    return prefixes


def caller_is_bangalorian(number):
    return "(080)" in number


def get_prefix(number):
    prefix = ""
    if reciever_is_fixed_line(number):
        prefix = get_fixed_line_prefix(number)
    elif reciever_is_mobile(number):
        prefix = get_mobile_prefix(number)
    else:
        prefix = telemarketer_prefix
    return prefix


def reciever_is_fixed_line(number):
    return number[0] == "("


def reciever_is_mobile(number):
    return len(number) == 11


def get_fixed_line_prefix(number):
    prefix = ""
    for char in number:
        if char != ")":
            prefix += char
        else:
            prefix += ")"
            break

    return prefix


def get_mobile_prefix(number):
    return number[0:4]


def print_prefixes():
    template = "The numbers called by people in Bangalore have codes: {}"
    message = template.format(get_numbers_prefixes_called_by_bangalore())
    print(message)


print_prefixes()

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
bangalore_prefix = "(080)"
bangalorian_calls = {}


def get_precantage_of_bangalore_to_bangalore():

    for call in calls:
        if (caller_is_bangalorian(call.sending_number)):
            add_call(call.recieving_number)

    calls_to_bangalore = bangalorian_calls[bangalore_prefix]
    total_calls = get_total_bangalorian_calls()
    return calculate_percantage(calls_to_bangalore, total_calls)


def add_call(number):
    try:
        bangalorian_calls[get_prefix(number)] += 1
    except KeyError:
        bangalorian_calls[get_prefix(number)] = 1


def get_total_bangalorian_calls():
    total = 0
    for call in bangalorian_calls:
        total += bangalorian_calls[call]
    return total


def calculate_percantage(calls_to_bangalore, total_calls):
    return round(calls_to_bangalore/total_calls, 2)


def print_percantage():
    template = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
    message = template.format(get_precantage_of_bangalore_to_bangalore())
    print(message)


print_percantage()
