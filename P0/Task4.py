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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_telemarketers = []


def get_possible_telemarketers():

    for call in calls:
        add_caller(call.sending_number)

    for call in calls:
        reciever = call.recieving_number
        remove_telemarketer(reciever)

    for text in texts:
        remove_telemarketer(text.sending_number)
        remove_telemarketer(text.recieving_number)

    return possible_telemarketers


def remove_telemarketer(number):
    if number in possible_telemarketers:
        possible_telemarketers.remove(number)


def add_caller(number):
    if number not in possible_telemarketers:
        possible_telemarketers.append(number)


def print_telemarketers():
    template = "These numbers could be telemarketers:"
    sorted_numbers = sorted(get_possible_telemarketers())
    print(template)
    print("\n".join(sorted_numbers))


print_telemarketers()
