import glob
import os
import pandas as pd
import main 

"""

In the original extraction, Eric's material contained genuine grid-in questions. 
For these no multiple-choice answers were available. The answer key that was 
extracted at the same time as the individual questions contains the correct answer 
verbatim (instead of a letter indicating the correct answer choice as is the case 
for all other questions).

The question file itself carries o record of the correct answer, it is only 
contained in the answer key. With this script, I will include the correct answer 
for the grid-in problems into the question file.

For all other questions (multiple-choice questions), I will copy the correct answer 
from the SAT section to the grid-in section.

"""

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def extract_correct_answer(question,answer_choice):
    """
        Extract the verbatim correct answer from the 
        multiple choice SAT part and include it in 
        the gridin section
    """
    with open(file,'r') as f:
        lines = f.readlines()
    flag = False
    start_recording = False
    answer_choices_string = ''
    for idx,line in enumerate(lines):
        if '\ifsat' in line:
            flag = True
        if flag and '\else' in line:
            flag = False
        if flag and '\\begin{enumerate}' in line:
            start_recording = True
            continue
        if flag and '\\end{enumerate}' in line:
            start_recording = False
        if start_recording:
            answer_choices_string = answer_choices_string + line
    print answer_choices_string
    answer_choices = answer_choices_string.split('\item')[1:]
    for tmp_answer in answer_choices:
        if (tmp_answer.strip()[-1] == '%' and 
                tmp_answer.strip()[-2:] != '\%'):
            answer = tmp_answer
    # if answer_choice == 'A':
    #     answer =  answer_choices[0]       
    # if answer_choice == 'B':
    #     answer =  answer_choices[1]       
    # if answer_choice == 'C':
    #     answer =  answer_choices[2]       
    # if answer_choice == 'D':
    #     answer =  answer_choices[3]       
    return answer


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

answer_key_file_00 = os.path.join('..','support','answer_key.txt')
answer_key_00 = pd.read_csv(answer_key_file_00,sep=',')
answer_key_00 = answer_key_00.dropna()
answer_key_00.columns = answer_key_00.columns.str.rstrip()

answer_key_file_01 = os.path.join('..','support','answer_key_1000_plus.txt')
answer_key_01 = pd.read_csv(answer_key_file_01,sep=';')
answer_key_01 = answer_key_01.dropna()
answer_key_01.columns = answer_key_01.columns.str.rstrip()

answer_key_file_02 = os.path.join('..','support','answer_key_2000_plus.txt')
answer_key_02 = pd.read_csv(answer_key_file_02,sep=',')
answer_key_02 = answer_key_02.dropna()
answer_key_02.columns = answer_key_02.columns.str.rstrip()

frames = [answer_key_00, answer_key_01, answer_key_02]

answer_key = pd.concat(frames)

questions = answer_key['question'].tolist()

# Identify grid-in question via the answer key

print 'Do you really want to run this?'
#print bla

questions = glob.glob(os.path.join('..','questions','jc_question_b*.tex'))
for question in questions:
    answer = (answer_key['SAT']
        [answer_key['question'] ==  question]
        .tolist()[0])
    # Test is answer is a letter
    file = os.path.join('..','questions',question)

    if os.path.isfile(file):
        if not answer.isalpha():
            # read problem
            with open(file,'r') as f:
                lines = f.readlines()
            outfile = open(file,'w')
            # Loop through lines
            for line in lines:
                outfile.write(line)
                if '\\ifgridin' in line:
                    outfile.write(answer+'\n')

            outfile.close()
        else:
            # For all non-grid-in questions, write the correct answer verbatim into the 
            # grid-in section
            correct_answer = main.find_correct_answer(file)
            #print correct_answer
            #print correct_answer['\ifsat']
            # Find answer string
            print question
            print correct_answer
            print correct_answer['\ifsat']
            answer_text = extract_correct_answer(file,correct_answer['\ifsat'])
            print answer_text
            # read problem
            with open(file,'r') as f:
                lines = f.readlines()
            outfile = open(file,'w')
            # Loop through lines
            for line in lines:
                outfile.write(line)
                if '\\ifgridin' in line:
                    outfile.write(answer_text+'\n')

            outfile.close()
    else:
        pass




