"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from text_record import TextRecord
from call_record import CallRecord

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?

Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def print_first_record_of_texts():
    record = TextRecord(texts[0])
    template = "First record of texts, {} texts {} at time {}"
    message = template.format(record.sending_number,
                              record.recieving_number, record.timestamp)
    print(message)


def print_list_record_of_calls():
    record = CallRecord(calls[-1])
    template = "Last record of calls, {} calls {} at time {}, lasting {} seconds"
    message = template.format(
        record.sending_number, record.recieving_number, record.timestamp, record.duration)
    print(message)


print_first_record_of_texts()
print_list_record_of_calls()