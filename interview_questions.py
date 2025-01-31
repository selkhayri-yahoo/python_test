#Function that reverses a string
def reverse_string(word):
    return ''.join(reversed(word))

# Test. Verification of reverse_string function
def test_reverse_string():
    input_str = "TripleTen"

    # Perform the reverse operation
    reversed_str = reverse_string(input_str)

      # Check if the reversed string matches the expected output
    assert reversed_str == "neTelpirT"

    print("\n\nTest Passed! " + input_str + "'s reverse is " + reversed_str)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def test_factorial():
    assert factorial(5) == 120
