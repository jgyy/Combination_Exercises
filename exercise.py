"""
https://github.com/cwchong/coursework/blob/main/201106/Combination_Exercises.ipynb
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
        print(err, "; Skipping to question 2.")


def question_two(strs):
    """
    Write a function to count the number of strings from the given list of strings
    where the strings must have a length more than or equal to 2 and its first and
    last character must match.
    """
    try:
        letters = [s for s in strs if s[0] == s[-1] and len(s) >= 2]
        letters_count = str(len(letters))

        print("Question 2 Answers:")
        print(f"Input: {strs}")
        print("Filtered Output:", letters)
        print(f"String Count: {letters_count}")
        print("")
    except TypeError as err:
        print(err, "; Skipping to the third question.")


def question_three(strs):
    """
    Write a function that accepts a string, calculates the number of upper case
    letters and lower case letters and returns the values as a dictionary. The
    program (not the function) is to print the expected output defined below.
    """
    try:
        letter_lower = [s for s in strs if s.islower()]
        lower_count = str(len(letter_lower))
        letter_upper = [s for s in strs if s.isupper()]
        upper_count = str(len(letter_upper))

        print("Question 3 Answers:")
        print(f"Original String: {strs}")
        print(f"No. of Upper case characters: {lower_count}")
        print(f"No. of Lower case characters: {upper_count}")
        print("")
    except TypeError as err:
        print(err, "; Skipping to the next question.")


def question_four(strs):
    """
    Write a function to check whether a sequence of numbers have a linear, quadratic
    or cubic related number pattern and return a string stating which pattern it is.
    If there is no related pattern, return Not part of the sequence.
    """
    try:
        response = "Question 4 Answers:\n"
        def sequences(seqs):
            length = list(range(1, len(seqs)))
            sequence = [seqs[s-1] - seqs[s] for s in length]
            sequence_check = sum(sequence) / len(sequence) == sequence[0]
            return sequence, sequence_check

        linear_sequence, linear_check = sequences(strs)
        if linear_check:
            return response + "Linear Sequence: " + str(strs) + "\n"
        quad_sequence, quad_check = sequences(linear_sequence)
        if quad_check:
            return response + "Quadratic Sequence: " + str(strs) + "\n"
        _, cube_check = sequences(quad_sequence)
        if cube_check:
            return response + "Cubic Sequence: " + str(strs) + "\n"
        else:
            return response + "Not part of the sequence: " + str(strs) + "\n"

    except TypeError as err:
        return str(err) + "; Skipping to the next question."


if __name__ == "__main__":
    length_1 = random.randint(1, 99)
    letter_1 = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_1 = ''.join(random.choice(letter_1) for _ in range(length_1))
    question_one(result_1)

    length_2 = random.randint(4, 16)
    range_2 = list(range(length_2))
    letter_2 = "ab"
    result_2 = [''.join(random.choice(letter_2) for _ in range_2) for _ in range_2]
    question_two(result_2)
    question_three(result_1)

    rand = [random.randint(-1, 1) for _ in range(4)]
    line = lambda x: rand[1]*x + rand[0]
    quad = lambda x: rand[2]*x**2 + rand[1]*x + rand[0]
    cube = lambda x: rand[3]*x**3 + rand[2]*x**2 + rand[1]*x + rand[0]
    line_list = [line(r) for r in range_2]
    quad_list = [quad(r) for r in range_2]
    cube_list = [cube(r) for r in range_2]
    rand_list = [random.randint(-99, 99) for _ in range_2]
    lists = random.choice([line_list, quad_list, cube_list, rand_list])
    result = question_four(lists)
    print(result)
