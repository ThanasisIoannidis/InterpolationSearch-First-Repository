# importing libraries
import math
import numpy as np

# creating a random array
randomArray = np.random.randint(1, 150, 10)
APArray = []

# sorting the random array
randomArray = sorted(randomArray, reverse=False)
# creating a variable to use for input validation
correct = False
# loop for input validation
while correct == False:
    # giving the user a message on how to use the programme
    randomOrCreate = input(("You can use a randomly created progressive array or create one.(for random press 'r' and "
                            "to create press 'c') "))
    # assigning the random array as the default
    if randomOrCreate == 'r':
        array = randomArray
        correct = True
    # creating a new array and assigning it as the default
    if randomOrCreate == 'c':
        array = array = list(map(int, input("Create an array: ").split()))
        correct = True

# Enable this to create an Arithmetic progressional array (uniformly distributed)
# for x in range(0, 2000, 5):
#    APArray.append(x)
# array = APArray
# print(array)

print(array)
print()
left = 0
right = (len(array) - 1)

# asking the user the element he wants to find and storing it inside a variable
x = int(input("What is the key of the item you want to search for? "))
print()

# Creating a function for Interpolated Search
def interpolationSearch(arr, left, right, x, comparisons):
    # making sure the array is sorted
    if (left <= right and x >= arr[left] and x <= arr[right]):
        # applying the interpolated search formula (The equation is divided into parts because it can not be
        # understood by the computer when it is in one part)
        TopBottom = right - left
        kVbottom = x - arr[left]
        VtopVbottom = arr[right] - arr[left]
        kVbottomDividedVtopVbottom = kVbottom / VtopVbottom
        pos = TopBottom * kVbottomDividedVtopVbottom + left
        pos = math.floor(pos)

        # if the target is found
        if arr[pos] == x:
            comparisons = comparisons + 1
            print("Number of comparisons made: " + str(comparisons))
            return pos

        # If x is larger, x is in right subarray
        if arr[pos] < x:
            comparisons = comparisons + 1
            return interpolationSearch(arr, pos + 1,
                                       right, x, comparisons)

        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            comparisons = comparisons + 1
            return interpolationSearch(arr, left,
                                       pos - 1, x, comparisons)

    return -1


# Driver code
# comparisons variable is for counting the comparisons made until the element we are searching is found
comparisons = 0
# calling the function
index = interpolationSearch(array, left, right, x, comparisons)

# printing the index that the wanted element was found
if index != -1:
    print("Element found at index", index)
# in case element is not found
else:
    print("Element not found")
