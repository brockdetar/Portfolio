"""
Programming Exam: Develop a collection of four different rules for generating
the terms of a sequence. Generate a program for randomly selecting a rule,
and a starting point. Give the user the first four terms of the sequence,
and ask them for the fifth. Tell them if they were correct or not.
"""
import random


def rule_one():
    print('First rule')
    #first sequence is (n1/2) + n2
    numtoprint = 4
    start_num = random.randint(1,10)
    for index in range(numtoprint):
        next_num = (start_num / 2) + start_num
        print(next_num)
        start_num = next_num
    correct_answer = (start_num / 2) + start_num
    #print (correct_answer)
    return correct_answer
    

def rule_two():
    print('Second rule')
    numtoprint = 3
    start_num = random.randint(1,5)
    n2 = random.randint(2,5)
    for index in range(numtoprint):
        print(start_num)
        next_num =(start_num * (n2))
        start_num = next_num
    print(start_num)
    correct_answer = start_num *n2
    return(correct_answer)
    #print ('correct answer' , correct_answer)
    

def rule_three():
    print('Rule 3')
    numtoprint = 4
    start_num = 1
    for index in range(numtoprint):
        cube = start_num * start_num * start_num
        next_num = start_num + 1
        start_num = next_num
        print(cube)
    correct_answer = start_num * start_num * start_num
    return correct_answer
    

def rule_four():
    print('Rule 4')
    numtoprint = random.randint(4,10)
    n1 = 0
    n2 = 1
    for index in range(numtoprint):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        print (nth)
    correct_answer = (nth+n1)
    return correct_answer
    #print('correct' , correct_answer)


rule = random.randint(1,4)

if rule == 1:
    correct_answer = rule_one()
elif rule == 2:
    correct_answer = rule_two()
elif rule == 3:
    correct_answer = rule_three()
elif rule == 4:
    correct_answer = rule_four()

#print('What is the next term in the sequence?')
user_guess = int(float(input('What is the next term? ')))

if user_guess == correct_answer:
    print('You were correct! The next term in the sequence is', correct_answer)
if user_guess != correct_answer:
    print('Oops, you were not correct. The correct answer was' , correct_answer)
    
    

