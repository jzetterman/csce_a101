#########################################
# John Zetterman
# Assignment 3
# Date Completed: July 28, 2025
#
# Description: This program grades driver's license exams
# Inputs: A hardcoded answer key file read from the file system and a filename
#         for the student's answers.
# Outputs: Prints out a driver's test summary including whether they passed
#          or failed, the number of correct answers, the number of incorrect
#          answers, and the question numbers that were answered incorrectly.
# Instructions: Place the answer key and the student's answers file in the
#               problem2 directory for the program to be able to read them.
#########################################

answer_key = "answer_key.txt"
test_exam = input('Please enter the filename for the student exam answers: ')

def main():
    key = []
    test_values = []
    correct_count = 0
    incorrect_count = 0
    incorrect_response_numbers = []

    with open(answer_key, 'r') as f:
        answers = f.readlines()
        key = [letter.strip() for letter in answers]

    with open(test_exam, 'r') as f:
        test_answers = f.readlines()
        test_values = [letter.strip() for letter in test_answers]

    for i, v in enumerate(key):
        if v == test_values[i]:
            correct_count += 1
        else:
            incorrect_count += 1
            incorrect_response_numbers.append(i + 1)

    if incorrect_count > 5:
        print('Result: Fail!')
    else:
        print('Result: Pass!')

    print(f'Total correctly answered questions: {correct_count}')
    print(f'Total incorrectly answered questions: {incorrect_count}')
    print('Incorrect question numbers: ')
    print(incorrect_response_numbers)


if __name__ == "__main__":
    main()
