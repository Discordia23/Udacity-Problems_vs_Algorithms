import os

def find_files(suffix, path):
    #loop through all items in main path
    if os.path.isfile(path):
        if path.endswith(suffix):
            path_files.append(path)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            # if item ends with suffix, append the path + item to the path_files list
            if item.endswith(suffix):
                path_files.append(os.path.join(path, item))
            # define new path for recursion call
            new_path = os.path.join(path, item)
            # if item is a directory, recursion call
            if os.path.isdir(new_path):
                find_files(suffix, new_path)
    else:
        return "Path is not existing"
    return path_files

# Test 1 - returns 4 paths
path_files = list()
print('Test 1:\n', find_files(".c", './testdir'))
print('Should return 4 paths ending with .c\n')

# Test 2 - edge case, no file found, list should be empty
path_files = list()
print('Test 2:\n', find_files(".ccc", './testdir'))
print('List should be empty\n')

# Test 3 - edge case, path is not existing
path_files = list()
print('Test 3:\n', find_files(".c", './testdir/subdir6'))
print("Should return 'Path is not existing'\n")

# Test 4 - path is a file, not a directory
path_files = list()
print('Test 4:\n', find_files(".c", './testdir/subdir1/a.c'))
print('Should return 1 path ending with .c\n')
