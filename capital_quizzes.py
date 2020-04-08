import random,os
from capital_dictionary import capital
from pathlib import Path
os.chdir('/home/uriel/Documents/test')
#create quiz files and answer files
for quiznum in range(1,31):
    quiz = open(Path.cwd() / f'quiz_{quiznum}','w')
    quizans = open(Path.cwd() / f'quiz_{quiznum}_answers','w')
    quiz.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz.write((' ' * 20) + f'State Capitals Quiz (Form {quiznum + 1})')
    quiz.write('\n\n')
    quizans.write((' ' * 20) + f'State Capitals Answers (Form {quiznum + 1})')
    quizans.write('\n\n')
    #make a list of all the state names
    states = list(capital.keys())
    #mix up the state names
    random.shuffle(states)
    #now to write the questions
    #the states will be the indices for the questions
    for state in states:
        quiz.write(f'\n{states.index(state)+1}. What is the capital of ' + state + '?\n\n')
        answer = capital[state]
        #make list of wrong answer by deleting right answer from all answers
        wrong_answers = list(capital.values())
        del wrong_answers[wrong_answers.index(answer)]
        #select 3 wrong answers
        wrong_answers = random.sample(wrong_answers,3)
        #3 wrong answers plus the right answer
        answer_options = wrong_answers + [answer]
        #mix up the options
        random.shuffle(answer_options)

        # now to arrange the options
        for i in range(4):
            quiz.write(f"{'ABCD'[i]} "+ answer_options[i] + '\n')
        quizans.write(f"{states.index(state)+1}. The answer is " +
                      f"{'ABCD'[answer_options.index(answer)]}. "
                      + 'The capital of '+ state+ ' is ' + answer +'.' + '\n\n')
#close both files
    quiz.close()
    quizans.close()


