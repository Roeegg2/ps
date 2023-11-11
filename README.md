# Some notes:

1. WCHAN value 0 means the process isnt waiting in a kernel function.
2. I made the filename a parameter in the get_file_values and just used a '/stat' const to add support for later expansion (idk analyzing statm for more memory information and such)
3. I initially added analsys for the 'status' file to get the UID's and GID's but was a pain in the ass to extract the values out, I dont want to waste my time on it. (but what is important is that I get the concept - it resides in the 'status' file in a process's directory)
4. Utime and Stime are displayed in clock ticks.



# Explanation of each of the fields displayed:

PID 0 - the ID of the process
Comm 1 - the name assosiacted with the process
State 2 - the current state of the process
PPID 3 - the ID of the parent of the process
Utime 13 - the amount of time the process has been scheduled in user mode (in CPU ticks)
Stime 14 - the amount of time the process has been scheduled in kernel mode (in CPU ticks)
Priority 17 - the actual priority of the process the kernel sees
Nice 18 - 'how nice the process is' this value affects the Priority value of the process. (from what I understand it differs between different kernel versions)
Threads 19 - the number of threads the process has
RSS 23 - the number of pages the process has in real memory

Uid - status file - real, effective and saved uid
Gid - status file - real, effective and saved gid
Wchan - wchan file - the address of the kernel function the process is blocked in
Tty - fd/0 symlink - the tty device the process is running on

