#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>
#include <sys/types.h>

#define DELIMITERS " \n\t"
#define STATUS_entry_COUNT 1

const char STATUS_entries[6][10] = {"Name"}; // not sure its the right order (both the size and the entries)

// current problem: need to use a data scructure like a list (or mark the struct fields with indices) to store all the values of the entries

int main(){
    DIR* proc_dir;
    struct dirent *entry;

    proc_dir = opendir("/proc");

    while ((entry = readdir(proc_dir)) != NULL){
        if (entry->d_name[0] >= '0' && entry->d_name[0] <= '9'){
            // get_entry_value(strcat("/proc", entry->d_name), "/status", STATUS_entry_COUNT, STATUS_entries);
        }
    }

    return 0;
}

/* place the raw entry values from a file in the proc_info struct */
int iterate_over_all_entries(char* pid_path, char* filename, int entry_count, char** entries){
    FILE* stat_file;
    char* token, entry_value;
    char line[256];

    stat_file = fopen(strcat(pid_path, filename), "r");

    for (int i = 0; i < entry_count; i++){
        fgets(line, 256, stat_file);
        token = strtok(line, DELIMITERS);

        if (strcmp(token, entries[i])){
            parse_entry_value(get_entry_value(token));
        }
    }
}

/* parse the entry value as needed*/
int parse_entry_value(char* entry_value){

}

/* get the raw entry value from a certain entry*/
char* get_entry_value(char* token){
    char* entry_value;

    strtok(NULL, DELIMITERS);
    entry_value = (char*)calloc(strlen(token), sizeof(char));

    while (token != NULL){
        strtok(NULL, DELIMITERS);
        strcat(entry_value, " ");
        strcat(entry_value, token);
    }

    return entry_value;
}

int print_basic(struct basic_proc_info* bpi){

}
int print_extended(struct extended_proc_info* epi){

}

/** 
 * end result i am looking for:
 * 1. 2 printing options, one full detail and one short detail
*/


/**
 * main:
 * 1. open the /proc directory
 * 2. read each entry in the directory
 * 3. check if the entry is a directory, specifically if the name is a number meaning it is a process
 * get_entry_value: (call with status, stat, cmdline, etc)
 * 4.   open the file
 * 5.   read each line in the file
 * 6.   check if the line is one of the entries we are looking for
 * 7.   if it is, add the value to the return string
 * 8.   return the string
 * main:
 * 9. pass the string to parse_entry_value
 * parse_entry_value:
 * 10. parse the string as needed, and 
 * 10. add the returned value to the proc_info struct
 * 11. print the proc_info struct
 * 
*/