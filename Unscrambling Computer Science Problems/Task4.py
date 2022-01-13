"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

#get the distinct number of phone numbers from texts list
distinct_texters = []
text_receivers = []
for text in texts:
    if text[0] not in distinct_texters:
        distinct_texters.append(text[0])
    if text[1] not in text_receivers:
        text_receivers.append(text[1])

distinct_callers = []
call_receivers = []
#get the distinct number of records from calls
for call in calls:
    if call[0] not in distinct_callers:
        distinct_callers.append(call[0])
    if call[1] not in call_receivers:
        call_receivers.append(call[1])

#calls who have either never received one, sent or received a text
telemarketers = set(distinct_callers) - set(call_receivers) - set(distinct_texters) - set(text_receivers)

tele = [telemarketers]
tele.sort()

print('These numbers could be telemarketers: ')
for t in tele[0]:
    print(t)