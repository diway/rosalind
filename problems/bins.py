# Binary search

def bin_search_range(arr, search_value, min_index, max_index):
    if (max_index < min_index or min_index < 0 or max_index >= len(arr)):
        return -1
    if (max_index == min_index):
        if arr[min_index] == search_value: return min_index
        else: return -1
    middle_index = (min_index + max_index) >> 1
    if (arr[middle_index] >= search_value):
        return bin_search_range(arr, search_value, min_index, middle_index)
    elif (arr[middle_index] < search_value):
        return bin_search_range(arr, search_value, middle_index+1, max_index)

# Complex O(log(n)), n - array length
def bin_search(arr, search_value):
    return bin_search_range(arr, search_value, 0, len(arr)-1)

# Test
# arr = [10, 20, 30, 40, 50]
# for search_value in [40, 10, 35, 15, 40, 20]:
#     print bin_search(arr, search_value)

input = open('/home/diway/Desktop/rosalind_bins.txt', 'r')
n = input.readline().strip()
m = input.readline().strip()
arr = input.readline().split()
search_values = input.readline().split()
input.close()

output = open('/home/diway/Desktop/rosalind_bins_out.txt', 'w')
for search_value in search_values:
    index = bin_search(arr, search_value)
    if (index >= 0):
        index += 1
    output.write(str(index) + ' ') 
output.close()