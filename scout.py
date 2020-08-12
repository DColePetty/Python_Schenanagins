# Path traversal script to try and find files that have certain priviledges on the host
import os
import os.path
import sys

# this is a better print statement. tell is four letters, and no extra newlines or shenanagins.
def tell(message):
    sys.stdout.write(str(message))

all_files = []
all_directories = []

disallowed_directories = []
read_allowed_files = [] #if we can't read the file, we don't know it exists. Refer to all_files
write_allowed_files = []
execute_allowed_files = []

def list(file_path, depth_of_structure=10, show_hidden_files = False, depth_limit=4321):
    # this try is to catch permissions errors when reading the passed directory
    try:
        for name in os.listdir(file_path):
            current_file_or_directory = str(str(file_path) + "/" + str(name))
            # check for directory, call "list" method on it
            # check for file, check permissions associated with it
            if os.path.isfile(current_file_or_directory):
                if(show_hidden_files==False and name.startswith(".")):
                    continue
                for i in range(0, depth_of_structure):
                    tell("  ")
                tell("-" + str(name) + "  " +  "\n")
                if os.access(str(current_file_or_directory), os.R_OK):
                    read_allowed_files.append(str(current_file_or_directory))
                if os.access(str(current_file_or_directory), os.W_OK):
                    write_allowed_files.append(str(current_file_or_directory))
                if os.access(str(current_file_or_directory), os.X_OK):
                    execute_allowed_files.append(str(current_file_or_directory))
                all_files.append(current_file_or_directory)
                continue
            elif os.path.isdir(current_file_or_directory):
                for i in range(0, depth_of_structure):
                    tell("  ")
                tell(">" + str(name) + "\n")
                list(current_file_or_directory, depth_of_structure + 1)
                all_directories.append(current_file_or_directory)
                continue
            #done
        #done
    except PermissionError as perm_error:
        disallowed_directories.append(str(file_path))


from os.path import expanduser
home = expanduser("~")

#list(home, 0)
#list(expanduser("/etc"), 0)
list(expanduser("."), 0, show_hidden_files=True)
'''
tell("Disallowed_directories" + str(disallowed_directories) + " \n\n")

tell("read_allowed_files" + str(read_allowed_files) + " \n\n")

tell("write_allowed_files" + str(write_allowed_files) + " \n\n")

tell("execute_allowed_files" + str(execute_allowed_files) + " \n\n")
'''
