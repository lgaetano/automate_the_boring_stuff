#! python3
# randomQuizGenerator.py - Creates quizzes with questions
# and answers in random order, along with answer key.

import random

# Quiz data
capitals = {'Alabama': 'Montgomery',
            'Alaska': 'Juneau',
            'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock',
            'California': 'Sacramento',
            'Colorado': 'Denver'
}

# Generate 5 quiz files
for i in range(5):
    # Create the quiz and answer key files
    quiz_file = open(f'quiz{i + 1}.txt', 'w')
    ans_file = open(f'quiz{i + 1}Ans.txt', 'w')

    # Write out the header for the quiz
    quiz_file.write('Name:\n\nDatae:n\n\Period:\n\n')
    quiz_file.write(f'State Capitol Quiz Form {i+1}')
    quiz_file.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all states, making a question for each
    for i in range(len(states)):
        quiz_file.write(f'{i + 1}: What is the capital of {states[i]}\n')
        ans_file.write(f'{i + 1}: {capitals[states[i]]}\n')

    quiz_file.close()
    ans_file.close()
