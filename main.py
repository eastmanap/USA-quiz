# Apollos Eastman
# Nov 15 2024
# Quiz Game

# Function to ask question
def ask_quest(question,answer):
    user_ans = input(question+'')
    if user_ans.lower() == answer.lower():
        return True
    else:
        return False

# Funtion to run quiz
def run_quiz():
    questions = [('How many different presidents has the US had?\n', '46'), 
                 ('Which state is the smallest in the US?\n', 'Rhode Island'), 
                 ('Which state has the highest population in the US?\n', 'California'), 
                 ('How many US presidents have been assasinated?\n', '4'),
                 ('How many US states are there?\n', '50'),
                 ('Which US state has the Grand Canyon in it?\n', 'Arizona')
                 ]

    # Loop through questions
    score = 0
    for q in questions:
        if ask_quest(q[0], q[1]):
            print('Correct! You get +1 points!\n')
            score += 1
        else:
            print('Incorrect, sorry!\n')
            print('You can try again for a half point')
           
            if ask_quest(q[0], q[1]):
                print('Correct! You get +0.5 points!\n')
                score += .5
            else:
                print('Incorrect, sorry!\n')

# calculate score percentage
    print(f'\nYour final score is: {score}/{len(questions)}')
    percentage = (score / len(questions)) * 100
    print(f'You scored: {percentage:.1f}%')
    print('Thanks for playing, Goodbye!')

# Main function
def main():
    print('\nWelcome to my US quiz!\n')
    run_quiz()

# Start game
if __name__ == '__main__':
    main()
