puzzle = open("input.txt", "r").read().splitlines()

cwd = '/'
size_dict = dict()  # key: directory, value: size


def get_cwd(_cwd, target):
    if target == '..':
        return '/'.join(_cwd.split('/')[:-1])
    elif target == '/':
        return '/'
    return f"{_cwd}{target}/"


def parse_filesize(size):
    """Add the size to size_dict using the cwd, and the parent directories, as the keys"""
    cf = ''  # current folder
    for folder in cwd.split('/'):
        if folder == '' and cf != '':
            continue
        cf += f"{folder}/"  # add folder to current folder
        size_dict[cf] = int(size) + size_dict.get(cf, 0)


# Iterate through each line in the puzzle
for line in puzzle:
    match line.split():
        case ['$', 'cd', args]:
            cwd = get_cwd(cwd, args)
        case ['$' | 'dir', *args]:
            pass  # ignore dir, use directory path as key instead
        case [num, filename]:
            parse_filesize(num)


# Part 1
total = sum(size for size in size_dict.values() if size <= 100000)
print(f'The sum (size) of all directories up to 100000: {total}')

# Part 2
total_space = 70000000
update_size = 30000000
used_space = size_dict['/']
available_space = total_space - used_space
missing_space = update_size - available_space


total = min(size for size in size_dict.values() if size >= missing_space)
print(f'The smallest directory to clear up enough space: {total}')