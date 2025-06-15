
my_list = [8, 15, 4, 2]
           
def swap(input_list, index_1, index_2):
    """
    Swaps the elements at index_1 and index_2 in input_list.
    """
    temp = input_list[index_1]
    input_list[index_1] = input_list[index_2]
    input_list[index_2] = temp
    return input_list

lowest_index = 0

for i in range(len(my_list)):
    if my_list[i] < my_list[lowest_index]:
        lowest_index = i

my_list = swap(my_list, lowest_index, 0)
print(my_list)