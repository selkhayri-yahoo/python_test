# This test calculates the total sum and checks if the test has passed or failed.
def test_sum():
    sum = 2 + 2
    assert sum == 4

def test2_sum():
    sum = 2 + 2
    assert sum == 5

# Test 1. Verification of multiplication function
# Positive test

def test_multiply():
    # Define the first number
    a = 2
    # Define the second number
    b = 3
    # Perform the multiplication operation
    multiply = a * b
    # Check if the user gets the expected
    assert multiply == 6
