dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged) #{'a': 1, 'b': 3, 'c': 4}

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common) #[3, 4]

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("The fox jumps over the lazy dog"))  # jumps

# binary search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))  # 2

# Write a Python program to find the intersection of two sets
def intersectionSet(set1, set2):
    return set1 & set2

print(intersectionSet({1, 2, 3}, {2, 3, 4}))

