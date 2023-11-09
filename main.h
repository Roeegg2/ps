struct basic_proc_info {
    unsigned int pid;
    char tty[10];
    struct run_time {
        unsigned int nano_sec;
        unsigned int sec;
        unsigned int min;
    };
    char cmd[50];
};

struct extended_proc_info {
    char state;
    unsigned int uid;
    unsigned int ppid;
    float cpu_util;
    short priority;
    short nice_val;
    unsigned long long addr;
    unsigned long long vsize;
    char wchan[50];

    struct basic_proc_info* bpi;
};