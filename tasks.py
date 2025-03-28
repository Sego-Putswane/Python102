# Task 1: Sum of Squares
def sum_of_squares(n):
    """
    Calculate the sum of squares of the first `n` natural numbers.
    Example: If n = 3, return 1² + 2² + 3² = 14.
    """
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result
        
# Task 2: Fibonacci Sequence
def fibonacci(n):
    """
    Generate the first `n` numbers in the Fibonacci sequence.
    Return the sequence as a list.
    Example: If n = 5, return [0, 1, 1, 2, 3].
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    
    return sequence

# Task 3: Prime Number Check
def is_prime(num):
    """
    Check if a number is prime.
    Return True if the number is prime, otherwise False.
    Example: is_prime(7) → True, is_prime(10) → False.
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Task 4: Largest Number in List
def find_largest(numbers):
    """
    Find the largest number in a list of numbers.
    Return the largest number.
    Example: find_largest([3, 7, 2, 9]) → 9.
    """
    largest = max(numbers)
    return largest

# Task 5: Reverse a Number
def reverse_number(num):
    """
    Reverse the digits of a number.
    Return the reversed number.
    Example: reverse_number(123) → 321.
    """
    
    if num < 0:
        sign = -1
    else:
        sign = 1

        num *= sign #change number to a positive number if negative
        reversed_num = 0
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10
        return sign * reversed_num

# Task 6: Leap Year Check
def is_leap_year(year):
    """
    Check if a year is a leap year.
    Return True if it is a leap year, otherwise False.
    A leap year is divisible by 4 but not by 100, unless it is also divisible by 400.
    Example: is_leap_year(2000) → True, is_leap_year(1900) → False.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False #NEED TO FIX HERE

# Task 7: Count Vowels
def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    Return the count.
    Example: count_vowels("hello") → 2.
    """
    vowel_count = 0
    for char in text:
        if char in ["a","e","i","o","u","A","E","I","O","U"]:
            vowel_count += 1
    return vowel_count

# Task 8: Factorial
def factorial(n):
    if n < 0:
        return "number(n) should be greater than 0. Try again."
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(factorial(-5))

# Task 9: Grade Calculator
def calculate_grade(score):
    """
    Calculate the grade based on a score:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: Below 60
    Return the grade as a string.
    Example: calculate_grade(85) → "B".
    """
    pass

# Task 10: Password Validator
def validate_password(password):
    """
    Validate a password based on the following rules:
    - At least 8 characters long.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.
    - Contains at least one special character (!@#$%^&*).
    Return True if the password is valid, otherwise False.
    Example: validate_password("Pass123!") → True.
    """
    pass
