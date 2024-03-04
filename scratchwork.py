import random

#in the arr, all elements appear twice except for 1, return the element that appears once
def appear_twice(arr):
    for i in range(0, len(arr), 2):
        if arr[i] != arr[i+1]:
            return arr[i]
    return -1

print(appear_twice([0,1,0,2,2]))

#adds the numeric value of two strings together
def adding_str(str1, str2):
    return 0

#determines whether a string is a palindrome or not
def palindrome(str):
    return 0

#determine whether the sum of all the numbers in arr1 equal the product of all the numbers in arr2
def balanced(arr1, arr2):
    return 0
 
def asserter(test_case, exp, func, *args):
    try:
        ret = func(*args)
        if ret == exp:
            print("Test Case " + str(test_case) + " SUCCESS!")
        else:
           print("Test Case " + str(test_case) + " FAILED. We expected: " + str(exp) + " but you returned " + str(ret))
    except Exception as e:
        print("Test Case " + str(test_case) + f" had an exception: {type(e).__name__}: {e}")


def run_tests():
    asserter(1.1, "222", adding_str, "111", "111")
    asserter(1.2, "1345", adding_str, "1000", "345")
    asserter(1.3, "123", adding_str, "0", "123")
    asserter(2.1, True, palindrome, "racecar")
    asserter(2.2, True, palindrome, "i did did i")
    asserter(2.3, False, palindrome, "notpalindrome")
    asserter(2.4, False, palindrome, "rotatior")
    asserter(3.1, True, balanced, [1,2,3], [2,3])
    asserter(3.2, True, balanced, [0], [0])
    asserter(3.3, False, balanced, [1,2,3,4], [1,2,3,4])
