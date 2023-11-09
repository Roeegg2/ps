import os

title = ['PID', 'Comm', 'State', 'PPID', 'Terminal', 'Priority', 'Nice', 'Threads', 'Wchan', 'CPU', 'Time']
#in order: PID, Comm, State, PPID, Controlling termianl, Priority, Nice, Num of threads, Wchan. missing CPU and time 
indices = [0, 1, 2, 3, 6, 17, 18, 19, 34]

def get_file_values(pid, filename):
    values = []
    file = open('/proc/' + pid + filename)
    try:
        i = 0
        line = file.readline()
        words = line.split()
        for word in words:
            if (i in indices):
                values.append(word)
            i += 1

    except:
        print("Error: unable to read process: {pid}'s file")
    finally:
        file.close()
    
    return values

def main():
    objects = os.listdir('/proc')
    print("{:<6} {:<37} {:<6} {:<6} {:<8} {:<8} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*title))
    for object in objects:
        if (object.isdigit()):
            values = get_file_values(object, '/stat')
            # print(values)
            print("{:<6} {:<37} {:<6} {:<6} {:<8} {:<8} {:<10} {:<10} {:<10}".format(*values))
            # {:<10} {:<10}

main()
