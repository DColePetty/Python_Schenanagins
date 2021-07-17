'''
input = [[0, 0, 0, 1, 1, 1],
 [0, 0, 0, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1]]

output = [[0, 0, 0, 1, 1, 1],
 [0, 0, 0, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1]]
'''
input = [
 [0, 0, 0, 0, 0, 1],
 [0, 0, 0, 1, 1, 1],
 [1, 1, 1, 0, 0, 1],
 [1, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1]]

# has (row, col) as key and we'll set it to true for placeholder.
safe_dict = {}
def check_safe_one(input_array, row_indices, column_indices):
    # check we were passed the correct types
    row_indices = int(row_indices)
    column_indices = int(column_indices)
    # check if we are in bounds
    if row_indices >= 0  and row_indices < len(input_array[0]) + 1 and column_indices >= 0 and column_indices < len(input_array) + 1:
        # if it's on row borders (row 0 and max, col 0 and col max) make it true
        # check it's a 1
        if input_array[row_indices][column_indices] == 1:
            if row_indices == 0 or row_indices == len(input_array):
                safe_dict[(row_indices, column_indices)] = True
            if column_indices == 0 or column_indices == len(input_array[0]):
                safe_dict[(row_indices, column_indices)] = True
            # going to create our moving indices and check for them being in range
            # if it's safe then we go ahead with yes.
            above = row_indices - 1
            below = row_indices + 1
            left = column_indices - 1
            right = column_indices + 1
            if above in range(0, len(input_array)):
                if (above, column_indices) in safe_dict:
                    safe_dict[(row_indices, column_indices)] = True
            if below in range(0, len(input_array)):
                if (below, column_indices) in safe_dict:
                    safe_dict[(row_indices, column_indices)] = True
            if left in range(0, len(input_array[0])):
                if (row_indices, left) in safe_dict:
                    safe_dict[(row_indices, column_indices)] = True
            if right in range(0, len(input_array[0])):
                if (row_indices, right) in safe_dict:
                    safe_dict[(row_indices, column_indices)] = True
            # elif neither then check if it's touching a safe-one by lookup.

# check each row/col for valid values
for row in range(0, len(input)):
    for column in range(0, len(input[0])):
        check_safe_one(input, int(row), int(column))

# do it again, backwards this time. That way we get any straggling rows
# since the checks are only in a up-down-left-right, we need this to traverse all combinations.
for row in range(0, len(input))[::-1]:
    for column in range(0, len(input[0]))[::-1]:
        check_safe_one(input, int(row), int(column))

# print the mappings of safe indices
for val in safe_dict.keys():
    print(str(val) + " : " + str(safe_dict[val]))

# print the output based on the safe_dict
output = input
for row in range(0, len(input)):
    for column in range(0, len(output[0])):
        if (row, column) in safe_dict:
            print(str(" 1 "), end = "")
        else:
            print(str(" 0 "), end = "")
    print()
# find all 1's that are adjacemt to borders.
# add them to "safe 1's"
# pass over deleting the unsafe 1's
