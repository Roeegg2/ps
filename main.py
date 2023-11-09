import os
import sys
import time



status_entries = ['Name:', 'State:']

def func(pid, filename):
    with open('/proc/' + pid + filename) as file: 
        for line in file:
                 

def get_entry_value(line):
    words = line.split()
    if words[0] in status_entries:
        return ''.join(words[1:])

def main():
    entries = os.listdir('/proc')
    for entry in entries:
        if (entry.isdigit()):
            func(entry, '/status')


main()