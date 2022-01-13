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
#each of the with clauses is a loop that takes linearly in proportion to each file
#we can say that each of the 

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#first text
firsttext = texts[0]
print('First record of texts, %s texts %s at time %s' %(firsttext[0], firsttext[1], firsttext[2]))

#lastcall
lastcall = calls[-1]
print('Last record of calls, %s calls %s at time %s, lasting %s seconds' %(lastcall[0], lastcall[1], lastcall[2], lastcall[3]))