
def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    """Subtracting b from a and if the result is 0, a mod b is 0. 
    If it goes below 0, a mod b is the previous result of a - b."""
    
    #Base step.
    if a - b == 0:
        return a - b
    
    elif a - b < 0:
        return a

    #Recursive step.
    return modulus((a-b), b)        

def how_many(lis1, lis2):
    """Checking lis1 first element membership in lis2 and incrementing by slicing lis1 to
    check all off its elements against lis2, returning 1 for each hit."""

    #Base step.
    if len(lis1) == 0:
        return 0
    
    #Recursive step.
    if lis1[0] in lis2:
        return 1 + how_many(lis1[1:], lis2)
    else:
        return how_many(lis1[1:], lis2)

def test_modulus(num1, num2):
    print("The modulus of " + str(num1) + " and " + str(num2) + " is " + str(modulus(num1, num2)))

def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1) + " are also in " + str(lis2))

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15) 

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])


if __name__ == "__main__":
    run_recursion_program()