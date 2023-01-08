# Change 1 - Assigmnet was removed to improve readablity 
def mergeSort(list_to_sort_by_merge):
    # Change 2 - Embedded the original if statement within 
    # the following to check if all items are integers 
    if all([isinstance(item, float) for item in my_list]) == True:
        # Change 3 - Check if the list has more than one element
        # < 1 and != 0 removed cause > 1 is sufficient
        if len(list_to_sort_by_merge) > 1:
            # Divide the list into two halves 
            mid = len(list_to_sort_by_merge) // 2
            left = list_to_sort_by_merge[:mid]
            right = list_to_sort_by_merge[mid:]

            # Sort the left and right halves
            mergeSort(left)
            mergeSort(right)

            # Merge the sorted left and right halves
            l = 0
            r = 0
            i = 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    # ASSIGNMENT was removed add replaced by the following
                    list_to_sort_by_merge[i] = left[l]
                    l += 1
                else:
                    # ASSIGNMENT was removed add replaced by the following
                    list_to_sort_by_merge[i] = right[r]
                    r += 1
                i += 1

            # Add any remaining elements from the left half
            while l < len(left):
                list_to_sort_by_merge[i] = left[l]
                l += 1
                i += 1

            # Add any remaining elements from the right half
            while r < len(right):
                list_to_sort_by_merge[i] = right[r]
                r += 1
                i += 1
        else:
            print('There are 0 values in the list')
            return
    else:
        print('Either no integers were given or one of the values is not an integer.')
        return
    

import matplotlib.pyplot as plt

# Initialize the list to sort
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot the original list
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()

# Sort the list
mergeSort(my_list)

# Plot the sorted list
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
