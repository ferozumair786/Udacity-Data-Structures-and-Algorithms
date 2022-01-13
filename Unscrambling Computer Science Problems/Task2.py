"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#use a dictionary this time for addition
distinct_numbers = {}
#get the distinct number of records from calls
for call in calls:
    if call[0] not in distinct_numbers:
        distinct_numbers[call[0]] = int(call[3])
    else:
        distinct_numbers[call[0]] = int(distinct_numbers.get(call[0],0)) + int(call[3])

    if call[1] not in distinct_numbers:
        distinct_numbers[call[1]] = int(call[3])
    else:
        distinct_numbers[call[1]] = int(distinct_numbers.get(call[1],0)) + int(call[3])


max_key = max(distinct_numbers, key=distinct_numbers.get)

print('%s spent the longest time, %i seconds, on the phone during September 2016.' %(max_key, distinct_numbers.get(max_key)))