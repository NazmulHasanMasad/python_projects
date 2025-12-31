#cprint will print color text in the terminal

import random
from termcolor import cprint


QUESTION='question'
OPTIONS='options'
ANSWER='answer'

def ask_question(index, question, options):
    print(f'Question : {index}: {question}')
    for option in options:
        print(option)
    
    return input("your answer : ").upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)

    score=0

    for index, item in enumerate(quiz,1):
      answer=  ask_question(index, item[QUESTION],item[OPTIONS])

    if answer==item[ANSWER]:
          cprint('correct','green')
          score+=1
    else:
        cprint(f'wrong, The correct answer is:{item[ANSWER]}')

    print()
      
    print(f'The final score is {score} out of {len(quiz)}')


def main():
    quiz= [
        {
            QUESTION: 'What is the capital of France?',
            OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
            ANSWER: 'C'
        },
        {
            QUESTION: 'What is the capital of Italy?',
            OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
            ANSWER: 'D'
        },
        {
            QUESTION: 'What is the capital of Spain?',
            OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
            ANSWER: 'B'

        }
    ]


    run_quiz(quiz)


if __name__=='__main__':
    main()
