file = open('/proc/1901/stat')
line = file.readline()
words = line.split()
i = 0
for word in words:
    i += 1
print(i)   