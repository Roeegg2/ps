import os

# Some notes:
# 1. I made the filname a parameter in the get_file_values and just used a '/stat' const to add support for later expansion

# titles to print
Titles = ['PID', 'Comm', 'State', 'PPID', 'Flags', 'Priority', 'Nice', 'Threads', 'BTime', 'Wchan', 'Tty (last)']
# the indices of values we want in the stat file
Stat_Indices = [0, 1, 2, 3, 8, 17, 18, 19, 21]


def get_file_values(pid, filename):
    values = []
    file = open('/proc/' + pid + filename)
    try:
        i = 0
        line = file.readline()
        words = line.split()

        for word in words:
            if (i in Stat_Indices):
                if (word[0] == '(' and word[len(word)-1] != ')'): # this and the second if statement take care of the case where the process name is split into two words
                    values.append(word + ' ' + words[i+1])
                elif (word[0] != '(' and word[len(word)-1] == ')'): #i know, disgusting if statement and logic but it works
                    i -= 1
                else:
                    values.append(word)
            i += 1

    except:
        print("Error: unable to read process: {pid}'s file")
    finally:
        file.close()
    
    return values

""" getting the wchan function name from the /proc/[pid]/wchan file """
def get_wchan(pid):
    with open('/proc/' + pid + '/wchan') as file:
        return file.readline()


""" getting the /proc/[pid]/fd/0 symlink and pasting it (its a symlink to the tty device)"""
def get_tty(pid):
    try:
        return os.readlink(f'/proc/{pid}/fd/0')
    except:
        return '?'


"""main function"""
def main():
    objects = os.listdir('/proc')
    print("{:<6} {:<37} {:<6} {:<6} {:<8} {:<8} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*Titles)) # printing the Titles

    for object in objects:
        if (object.isdigit()):
            values = get_file_values(object, '/stat') #getting the values from the stat file
            values.append(get_wchan(object)) # getting the wchan
            values.append(get_tty(object))
            print("{:<6} {:<37} {:<6} {:<6} {:<8} {:<8} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*values))

main()
