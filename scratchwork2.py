import random

def debuggy():
    #this code is trying to swap two values in variables
    val_1 = "im in value 1"
    val_2 = "im in value 2"

    #put value val1 in val2
    val_2 = val_1

    #do the same again...
    val_1 = val_2

    print(val_1)
    print(val_2)


#given a string of binary, flip each 0 to a 1 and flip each 1 to a 0
def binary_flip(num):
    ret = ""
    for i in num:
        if i == "1":
            ret += "0"
        else:
            ret += "1"
    return ret
    


#given a string of binary, determine if there are more 0's than 1's
def binary_count(num):
    count1 = 0
    count0 = 0
    for i in num:
        if i == "1":
            count1 += 1
        else:
            count0 += 1
    if count0 > count1:
        return True
    else:
        return False

#HARD 
#given two strings of binary, add the two binary strings together and return the sum, you can assume the strings are
#the same length but you must account for carry over
def add_binary(num1, num2):
    result = ""
    carry = "0"
    for i in range(len(num1)- 1, -1, -1):
        if (num1[i] == "1" and num2[i] == "0") or (num1[i] == "0" and num2[i] == "1"):
            if carry == "1":
               
                result = "0" + result
                carry = "1"
            else:
                result = "1" + result
                carry = "0"
        elif (num1[i] == "0" and num2[i] == "0"):
            if carry == "1":
                result = "1" + result
                carry = "0"
            else:
                result = "1" + result
                carry = "0"
        else:
            if carry == "1":
                result = "1" + result
                carry = "1"
            else:
                carry = "1"
                result = "0" + result
      
    if carry == "1":
        result = "1" + result
    
    return result




#homework
#given a string of binary, reorganize the string such that all the 0's are on the left and all the 1 on the right
#example: given "011011", return "001111"
def binary_rearrange(num):
    ret = ""
    for i in num:
        if i == "0":
            ret = "0" + ret
        else:
            ret += "1"
    return ret
 
#homework
#given a string of binary, check that there are no adjacent 0's or 1's, return True or False
def binary_adjancent(num):
    prev = ""
    for i in num:
        if i == prev:
            return False
        else:
            prev = i
    return True

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
    asserter(1.1, "0110", binary_flip, "1001")
    asserter(1.2, "1111", binary_flip, "0000")
    asserter(1.3, "01010101", binary_flip, "10101010")
    asserter(2.1, False, binary_count, "1101")
    asserter(2.2, True, binary_count, "0001110")
    asserter(3.1, "111", add_binary, "000", "111")
    asserter(3.2, "1111", add_binary, "1010", "0101")
    asserter(3.3, "1000", add_binary, "001", "111")
    asserter(4.1, "001111", binary_rearrange, "110011")
    asserter(4.2, "000111", binary_rearrange, "111000")
    asserter(5.1, True, binary_adjancent, "01010")
    asserter(5.2, False, binary_adjancent, "101001")
    asserter(5.3, True, binary_adjancent, "0")
    

run_tests()