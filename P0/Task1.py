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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_numbers = []


def get_unique_numbers():

    for record in calls:
        add_number_if_unique(record.sending_number)
        add_number_if_unique(record.recieving_number)

    for record in texts:
        add_number_if_unique(record.sending_number)
        add_number_if_unique(record.recieving_number)
    return len(unique_numbers)


def add_number_if_unique(number):
    if number not in unique_numbers:
        unique_numbers.append(number)


def print_message():
    template = "There are {} different telephone numbers in the records."
    message = template.format(get_unique_numbers())
    print(message)


print_message()
