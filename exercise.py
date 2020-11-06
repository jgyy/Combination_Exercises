"""
Personal practice on python
"""
import random, string


def question_one(strs):
    """
    Q1) Write a program to sort the characters of a string such that the it follows following format:
    uppercase letters, lowercase letters then numbers. Punctuation is not required.
    """
    try:
        letters = [s for s in strs if s.isalpha()]
        sorted_letters = "".join(sorted(letters))
        numbers = [s for s in strs if not s.isalpha()]
        sorted_numbers = "".join(sorted(numbers))

        print("Question 1 Answers:")
        print(f"Input: {strs}")
        print(f"Output: {sorted_letters}{sorted_numbers}")
        print("")
    except TypeError as err:
        print(err, "; Skipping to the next question.")


def question_two():
    """
    Write a function to count the number of strings from the given list of strings where the strings
    must have a length more than or equal to 2 and its first and last character must match.
    """


if __name__ == "__main__":
    length = random.randint(1, 99)
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for _ in range(length))
    question_one(result_str)
