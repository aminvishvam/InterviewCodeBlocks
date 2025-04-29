# def merge_sorted_lists(list1, list2):
#     """Merges two sorted lists into a single sorted list."""
#     merged_list = []
#     i, j = 0, 0 # Pointers for list1 and list2

#     # Traverse both lists while there are elements in both
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1

#     # Append any remaining elements from list1
#     while i < len(list1):
#         merged_list.append(list1[i])
#         i += 1

#     # Append any remaining elements from list2
#     while j < len(list2):
#         merged_list.append(list2[j])
#         j += 1

#     return merged_list

def mergeList(list1, list2):
    merged_list = []
    i , j = 0, 0

    while i < len(list1) and j < len(list2):
        if(list1[i] < list2[j]):
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

        

# Example usage:
list_a = [1, 2, 5, 7]
list_b = [3, 4, 6, 8, 9]
print(mergeList(list_a, list_b))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]