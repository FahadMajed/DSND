"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

callersDurations = {}


def get_most_consuming_caller():

    for call in calls:
        increment_caller_duration(call.sending_number, call.duration)
        increment_caller_duration(call.recieving_number, call.duration)

    return max(callersDurations, key=callersDurations.get)


def increment_caller_duration(number, duration):
    try:
        callersDurations[number] += int(duration)
    except KeyError:
        callersDurations[number] = int(duration)


def print_message():
    template = "{} spent the longest time, {} seconds, on the phone during September 2016."
    most_consuming_caller = get_most_consuming_caller()
    message = template.format(most_consuming_caller,
                              callersDurations[most_consuming_caller])
    print(message)


print_message()
