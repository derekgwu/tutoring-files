
#given arr of two elements, sort them
def sort_two(arr):
    return 0

#given an arr find two elements that add up to the target sum return the two element as an arr
#return [] if there are no possible elements
def two_sum(arr, target):
    return 0

#givne an arr, shift every element to the right by one, and shift the last element to the beginning
def shift():
    return 0

#given an arr, return true if there is a duplicate element, else return flase
def contains_dup(arr):
    return 0

#given an 2-d arr, return true if it contains the target
def contains(arr, target):
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
    asserter(1.1, [1,2], sort_two, [2,1])
    asserter(1.2, [1,2], sort_two, [1,2])
    asserter(1.3, [0,0], sort_two, [0,0])
    asserter(2.1, [2,3], two_sum, [1,2,3,5], 5)
    asserter(2.2, [5,6], two_sum, [1,5,7,3,9,6], 11)
    asserter(3.1, [5,1,2,3,4], shift, [1,2,3,4,5])
    asserter(3.2, [3,2,1], shift, [2,1,3])
    asserter(3.3, [1,2], shift, [2,1])
    asserter(4.1, True, contains_dup, [1,2,3,4,1])
    asserter(4.2, False, contains_dup, [1,2,3,4])
    asserter(5.1, True, contains, [[1,2,3], [4,5,6], [7,8,9]], 5)
    asserter(5.2, False, contains, [[1,2,3], [4,5,6], [7,8,9]], 10)

run_tests()

    

