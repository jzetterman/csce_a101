# 4. Magic 8 ball

import random

def main():
    # Open the 8 Ball Response file.
    response_file = open('8_ball_responses.txt', 'r')

    # Read the file contents into a list.
    responses = response_file.readlines()

    # Close the file.
    response_file.close()

    # Strip the newline from each element.
    for i in range(len(responses)):
        responses[i] = responses[i].rstrip('\n')

    # Get the user's question.
    question = input('Enter your question: ')

    # Display a random response.
    print(responses[random.randint(0, len(responses))])

# Call the main function.
if __name__ == '__main__':
    main()