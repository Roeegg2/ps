import os

# titles to print
Titles = ['PID', 'Comm', 'State', 'PPID', 'Utime', 'Stime', 'Priority', 'Nice', 'Threads', 'RSS', 'Wchan', 'Tty'] # removed 'Uid', 'Gid',

# the indices of values we want in the stat file
Stat_Indices = [0, 1, 2, 3, 13, 14, 17, 18, 19, 23]
# Status_Indices = [8, 9]

STAT_ENTRIES = 52

# some calrification:
# i - index of the current word
# si - index of the current stat value
# DIFF - the difference between the number of words and the number of stat values
""" getting the values from the /proc/[pid]/stat file """
def get_file_values(pid, filename):
    values = []
    with open('/proc/' + pid + filename) as file:
        i = si = 0
        line = file.readline()
        words = line.split()

        DIFF = len(words) - STAT_ENTRIES

        while (i < len(words)):
            if (si in Stat_Indices):
                if (words[i][0] == '('):
                    values.append(add_spaced_words(words, i))
                    i += DIFF
                else:
                    values.append(words[i])
            i += 1
            si += 1
    
    return values


""" function for getting the entry value when the file is only one line """
def get_oneline_entry(pid, filename):
    with open('/proc/' + pid + filename) as file:
        return file.readline()


""" getting the /proc/[pid]/fd/0 symlink and pasting it (its a symlink to the tty device)"""
def get_tty(pid):
    try:
        return os.readlink(f'/proc/{pid}/fd/0')
    except:
        return '?'


""" get all the words for a spaced entry"""
def add_spaced_words(words, i):
    if (words[i][-1] == ')'): # if the current word ends with a ')'
        return words[i]
    else:
        return words[i] + ' ' + add_spaced_words(words, i+1)



"""main function"""
def main():
    objects = os.listdir('/proc')
    print("{:<6} {:<37} {:<6} {:<6} {:<8} {:<8} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*Titles)) # printing the Titles

    for object in objects:
        if (object.isdigit()):
            values = get_file_values(object, '/stat') #getting the values from the stat file
            # values.extend(get_status_values(object)) # getting the values from the status file (uids and gids)
            values.append(get_oneline_entry(object, '/wchan')) # getting the wchan
            values.append(get_tty(object)) # getting the tty
            print("{:<6} {:<37} {:<6} {:<6} {:<8} {:<8} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*values))
            # {:<10} {:<10}
main()
