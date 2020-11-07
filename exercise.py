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
        print()
    except TypeError as err:
        print(err, "; Skipping to the second question.")


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
        print()
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
        print()
    except TypeError as err:
        print(err, "; Skipping to the fourth question.")


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
        return str(err) + "; Skipping to the fifth question."


def question_five(strs):
    """
    Using a single list comprehension and lambda functions apply the math
    functions $ f(x) = x+x $ and $ g(x) = x*x $ to a list of numbers.
    """
    try:
        response = "Question 5 Answers:\n"
        fx = lambda x: 2 * x
        gx = lambda x: x ** 2
        output = [fx(x) for x in strs] + [gx(x) for x in strs]
        return response + "Input: " + str(strs) + "\nOutput: " + str(output) + "\n"

    except TypeError as err:
        return str(err) + "; Skipping to the next question."


def question_six():
    """
    The following codes loops the contents of a 2D list in a the direction from left to
    right but there are errors. Correct the errors to produce the following output.
    """
    b = (0,0,0)
    w = (255,255,255)

    right_arrow = [
        [b,b,b,w,b,b,b,b],
        [b,b,b,b,w,b,b,b],
        [b,b,b,b,b,w,b,b],
        [b,w,w,w,w,w,w,b],
        [b,w,w,w,w,w,w,b],
        [b,b,b,b,b,w,b,b],
        [b,b,b,b,w,b,b,b],
        [b,b,b,w,b,b,b,b],
    ]
    print("Question 6 Answer:\n")
    # each step of this for loop is a slice of animation for the arrow
    # use it to check that your arrow is moving in the right direction
    for i in range(0,8):
        # print the arrow
        number = str(i + 1)
        print(f"Slice Number {number}:\n")
        print_8x8(right_arrow)
        # compute the arrow's next step
        right_arrow = right(right_arrow)
        print()


def right(board):
    '''
    Function to move the contents in the matrix to the right
    '''
    b = (0,0,0)
    # init 2d array
    temp = [[b for _ in range(8)] for _ in range(8)]
    
    # swapping the last column with the first column 
    for j in range(8):
        temp[j][0] = board[j][-1]
    
    # copying the rest of the contents back
    for col in range(1,8):
        for row in range(8):
            temp[row][col] = board[row][col-1]

    return temp

def print_8x8(board):
    '''
    Function to print the matrix
    '''
    b = (0,0,0)
    for row in board:
        for col in row:
            if col == b:
                print(' -', end="")
            else:
                print(' *', end="")
        print()


def question_seven_a():
    """
    FICO® Score is one of the most well-known types of credit score in the industry.
    FICO® Scores are used by many lenders, and credit scores range from 300 to 850.
    """
    print("Question 7 Answers:\n")
    # main test driver (Do not change this cell)
    score_dict = {'Alex': 800, 'Bob':640, 'Charlie': 500}

    while True:
        if not fico(score_dict):
            break
        print("")

    print("Input:", score_dict)
    print()
    print("Output: ", end="")
    ratings_by_percent(score_dict)


def fico(score_dict):
    
    # get name input
    name = input("Enter entry's name (or enter 'q' to quit): ")
    
    # quit condition
    if name in ['q', 'Q', 'quit', 'Quit']:
        print("Bye Bye!")
        return False
    
    # get score input
    try:
        score = int(input("Enter entry's credit score: "))
    except ValueError:
        print("Invalid Credit Score")
        return False
    
    # check if score is valid
    if score < 300 or score > 850 :
        print("Invalid Credit Score")
        return False
    
    # rating logic
    if score >= 800:
        print(name, "has an Exceptional credit score")
    elif score >= 740:
        print(name, "has a Very Good credit score")
    elif score >= 670:
        print(name, "has a Good credit score")
    elif score >= 580:
        print(name, "has a Fair credit score")
    else:
        print(name, "has a Very Poor credit score")
    
    # update the dictionary of entries
    score_dict[name] = score
    return True


def ratings_by_percent(score_dict):
    """
    You are now tasked to create a function ratingsByPercent. It takes the
    dictionary of entries as input and prints the various rankings as a percentage.
    """
    length = len(score_dict)
    rate = {
        "very_poor": lambda x: 300 <= x <= 579,
        "fair": lambda x: 580 <= x <= 669,
        "good": lambda x: 670 <= x <= 739,
        "very_good": lambda x: 740 <= x <= 799,
        "exceptional": lambda x: 800 <= x <= 850,
    }
    ratings = {j: [i for i in score_dict.values() if rate[j](i)] for j in rate}
    rate_percent = {i: str(round((len(j) / length) * 100, 2)) + "%" for i, j in ratings.items()}
    print(rate_percent)
    print()


if __name__ == "__main__":
    try:
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

        result_4 = question_four(lists)
        print(result_4)
        result_5 = question_five(lists)
        print(result_5)
        question_six()
        question_seven_a()
    except KeyboardInterrupt:
        print("\nYou have choosed to exit the program\n")
