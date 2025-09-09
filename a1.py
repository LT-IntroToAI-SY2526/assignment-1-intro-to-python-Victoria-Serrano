# Assignment 1: AI-Generated Python Problems
# Name: [Victoria Serrano]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[I'm learning Python basics in a high school programming class. I have some experience with Java. Can you create 5-7 practice problems that cover loops]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Write a Python program that uses a for loop to find the sum of all even numbers between 1 and 50 (inclusive).]
use a for loop to find the sum of all even numbers between 1 and 50

total_sum = 0
for num in range(1,51):
    if num % 2 == 0:
        total_sum += num
-
- 

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""

def calculate_grade(score):
    '''
    
    '''
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "F"


start = int(input("Enter the start of the range: 1"))
end = int(input("Enter the end of the range: 50"))

total_sum = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        total_sum += num











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
print(calculate_grade(78))
print(calculate_grade(40))

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


