my_list = [8, 15, 4, 2, 4, 2]

def swap(input_list, index_1, index_2):
  # Write swap and test it!
    temp = input_list[index_1]
    input_list[index_1] = input_list[index_2]
    input_list[index_2] = temp
    return input_list 
# The lowest index before we begin the for loop is 0
# Step 2: Write the for loop that finds the lowest index in the list
# Step 3: After finding the lowest index, use swap() to put the lowest value at the start of the list
for j in range(len(my_list)):
    lowest_index = j
    for i in range(j, len(my_list)):
        if my_list[i] < my_list[lowest_index]:
            lowest_index = i
    my_list = swap(my_list, lowest_index, j)

print(my_list)

