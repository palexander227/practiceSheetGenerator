import os
import glob

def read_user_input(user_input):
    with open(user_input,'r') as f:
        lines = f.readlines()
    for line in lines:
        if line[0] == '#':
            pass
        else:
            if 'flavor' in line:
                test_flavor = line.split('=')[-1].strip()
            if 'kind' in line:
                test_kind = line.split('=')[-1].strip()
            if 'infile' in line:
                test_infile = line.split('=')[-1].strip()
                test_infile = os.path.join('input',test_infile)
    return test_flavor, test_kind, test_infile

def read_input_file(infile):
    with open(infile,'r') as f:
        lines = f.readlines()
    qlist = []
    for line in lines:
        if len(line.strip()) > 0:
            qlist.append(line.strip())   
    return qlist

def check_number_match(flavor,kind,infile):
    # Count number of questions
    n_questions = len(read_input_file(infile))
    # Check consistency with requested format
    if kind == 'in-class':
        if n_questions != 10:
            raise ValueError('Incorrect number of questions ({nquest}) for selected kind of test ({kind})'
                .format(nquest=repr(n_questions),kind=repr(kind)))
        else:
            pass
    else:
        if flavor == 'ACT' and n_questions == 60:
            pass
        elif flavor == 'SAT' and n_questions == 58:
            pass
        else:
            raise ValueError('Incorrect number of questions ({nquest}) for selected kind of test ({flavor})'
                .format(nquest=repr(n_questions),flavor=repr(flavor)))

def check_user_input(flavor,kind,infile):
    # Choices
    flavor_choices = ['ACT','SAT']
    kind_choices = ['in-class','homework']
    # Check flavor
    if flavor.strip() in flavor_choices:
        pass
    else:
        raise ValueError('Wrong flavor: {foo}, please check your input'
            .format(foo=repr(flavor)))
    # Check kind
    if kind.strip() in kind_choices:
        pass
    else:
        raise ValueError('Wrong kind: {foo}, please check your input'
            .format(foo=repr(kind)))
    # Check if input file exists at expected location
    if os.path.isfile(infile):
        pass
    else:
        raise ValueError('Input file {foo} not found at expected location!'
            .format(foo=repr(infile)))
    # Check that question numbers match requested format
    check_number_match(flavor,kind,infile)

def write_act_header(outfile):
    outfile.write('\documentclass[10pt]{article}\n')
    outfile.write('\input{support/flex_act_2016_supplements.tex}\n')
    outfile.write('\\acttrue\n')
    outfile.write('\usepackage{palatino}\n')
    outfile.write('\usepackage[left=10mm,right=17mm,bottom=8mm,includefoot]{geometry}\n')
    outfile.write('\setlength{\\voffset}{-1in+20mm} \n')
    outfile.write('\setlength{\headheight}{15mm} \n')
    outfile.write('\setlength{\headsep}{3mm} \n')
    outfile.write('\setlength{\columnsep}{8mm} \n')
    outfile.write('\setlength{\\textheight}{225mm}  \n')
    outfile.write('\setlength{\\footskip}{10mm}  \n')
    outfile.write('\\begin{document}\n')
    outfile.write('\pagestyle{fancy}\n')
    outfile.write('\n')
    outfile.write('% Change inter word spacing to avoid lines running onto the margins \n')
    outfile.write('% with \hyphenenalty10000 \n')
    outfile.write('% http://tex.stackexchange.com/questions/19236/how-to-change-the-interword-spacing \n')
    outfile.write('\spaceskip=1.5\\fontdimen2\\font plus 3.5\\fontdimen3\\font \n')
    outfile.write('minus 1.5\\fontdimen4\\font \n')
    outfile.write('\n')
    outfile.write('\\begin{center} \n')
    outfile.write('\\fontfamily{phv}\selectfont{ {\large \n')
    outfile.write('\\hspace*{8mm} \n')
    outfile.write('\\textbf{MATHEMATICS IN-CLASS TEST} \\\\[0.9ex]\n')
    outfile.write('\n')
    outfile.write('\\hspace*{8mm} \n')
    outfile.write('\\textit{10 Minutes\,---\,10 Questions}} \n')
    outfile.write('\n')
    outfile.write('\\vspace*{5mm} \n')
    outfile.write('\n')
    outfile.write('\hyphenpenalty10000 \n')
    outfile.write('\hspace*{1mm} \n')
    outfile.write('{\\normalsize \n')
    outfile.write('\\begin{tabularx}{1.02\\textwidth}{XX} \n')
    outfile.write('\parbox[t]{0.47\columnwidth}{\\textbf{DIRECTIONS:} Solve each problem, choose the correct answer, ')
    outfile.write('and then fill in the corresponding oval on your answer document.\\\\[0.9ex] \n')
    outfile.write('Do not linger over problems that take too much time. Solve as many ')
    outfile.write('as you can; then return to the others in the time you have left for this test.\\\\[0.9ex]  \n')
    outfile.write('You are permitted to use a calculator on this test. You may use your calculator ')
    outfile.write(' for any problems you choose,} & \n')
    outfile.write('\parbox[t]{0.48\columnwidth}{but some of the problems may best be done without using a calculator. \\\\[0.9ex] \n')
    outfile.write('Note: Unless otherwise stated, all of the following should be assumed. \\\\ \n')
    outfile.write('\\vspace*{-5.3mm} \n')
    outfile.write('\\begin{enumerate}[itemsep=-1.4mm,leftmargin=4.7mm] \n')
    outfile.write('\item Illustrative figures are NOT necessarily drawn to scale.  \n')
    outfile.write('\item Geometric figures lie in a plane. \n')
    outfile.write('\item The word \\textit{line} indicates a straight line. \n')
    outfile.write('\item The word \\textit{average} indicates arithmetic mean. \n')
    outfile.write('\end{enumerate}} \\\\ \n')
    outfile.write('\end{tabularx}} \n')
    outfile.write('} \n')
    outfile.write('\end{center} \n')
    outfile.write('\\vspace*{-1mm} \n')
    outfile.write('\hspace*{4mm}\\rule{0.99\\textwidth}{1pt} \n')
    outfile.write('\\begin{multicols}{2}\n')
    outfile.write('\\begin{enumerate}[label=\\textbf{\\arabic*}.] \n')
    outfile.write('\n')
    outfile.write('\n')

def write_sat_header(outfile):
    outfile.write('\documentclass[10pt,twoside]{article}\n')
    outfile.write('\input{support/flex_sat_2016_supplements.tex}\n')
    outfile.write('\sattrue\n')
    outfile.write('\usepackage{palatino}\n')
    outfile.write('\usepackage[top=6mm,inner=18mm,bottom=6mm,outer=12mm,includehead,includefoot]{geometry}\n')
    outfile.write('\setlength{\headheight}{16mm} \n')
    outfile.write('\setlength{\headsep}{15mm} \n')
    outfile.write('\setlength{\columnsep}{12mm} \n')
    outfile.write('\setlength{\\textheight}{204mm}  \n')
    outfile.write('\setlength{\\footskip}{30mm}  \n')
    outfile.write('\\begin{document}\n')
    outfile.write('\pagestyle{fancy}\n')
    outfile.write('\n')

def find_correct_answer(question):
    """
        Find the correct answer in the question file.
        The correct answer is indicated by a trailing '%' sign.
    """
    correct_answer_choices = {
        '\ifsat': ['A','B','C','D'],
        '\ifactodd': ['A','B','C','D','E'],
        '\ifacteven': ['F','G','H','J','K'],
    }
    file = question
    with open(file, 'r') as f:
        lines = f.readlines()
    flag = False
    start_recording = False
    tests = ['\ifsat','\ifactodd','\ifacteven','\ifgridin']
    correct_answer = {}
    for version in tests:
        correct_answer[version] = ''
        answer_choices_string = ''
        if version == '\ifgridin':
            for line in lines:
                if version in line:
                    start_recording = True
                    continue
                if '\else' in line:
                    start_recording = False
                if start_recording:
                    if (len(line.strip()) >= 2 and
                        line.rstrip()[-1] == '%' and 
                        line.rstrip()[-2:] != '\%'):
                        line = line.rstrip()[0:-1]
                    answer_choices_string = answer_choices_string + line.rstrip()
            correct_answer[version] = answer_choices_string
        else:
            for line in lines:
                if version in line:
                    flag = True
                if flag and '\else' in line:
                    flag = False
                if flag and '\\begin{enumerate}' in line:
                    start_recording = True
                    continue
                if flag and '\\end{enumerate}' in line:
                    start_recording = False
                    continue
                if start_recording:
                    if 'setcounter' in line or 'addtocounter' in line:
                        pass
                    else:
                        answer_choices_string = answer_choices_string + line
            answer_choices = answer_choices_string.split('\item')[1:]
            for idx,tmp_answer in enumerate(answer_choices):
                if (tmp_answer.strip()[-1] == '%' and 
                        tmp_answer.strip()[-2:] != '\%'):
                    answer = tmp_answer
                    correct_answer[version] = \
                        correct_answer_choices[version][idx]
    return correct_answer



def write_sat_questions(outfile,question_list,kind):
    questions_per_column = 0
    answer_key = []
    if kind == 'in-class':
        outfile.write('\\begin{multicols*}{2}\n')
    for nquestion,tmp_file in enumerate(question_list):
        tmp_answers = find_correct_answer(os.path.join('questions',tmp_file))
        if (nquestion >= 15 and nquestion < 20) or (nquestion >=50): 
            tmp_answer = tmp_answers['\\ifgridin']
        else:
            tmp_answer = tmp_answers['\\ifsat']
        answer_key.append(tmp_answer)
        if  nquestion == len(question_list)-1:
            outfile.write('\\nocontinuetrue \n')
        if kind == 'homework':
            if nquestion < 15:
                if nquestion == 0:
                    outfile.write('\calcofftrue\n')
                    outfile.write('\input{support/sat_calcoff_cover.tex}\n')
                    outfile.write('\\begin{multicols*}{2}\n')
                    questions_per_column = 0
                outfile.write('\calcofftrue\n')
            if nquestion >= 15 and nquestion < 20:
                if nquestion == 15:
                    outfile.write('\end{multicols*}\n')
                    outfile.write('\\newpage\n')
                    outfile.write('\calcofftrue\n')
                    outfile.write('\input{support/sat_calcoff_grid-in_cover.tex}\n')
                    outfile.write('\\begin{multicols*}{2}\n')
                    outfile.write('\n')
                    outfile.write('\n')
                    questions_per_column = 0
                outfile.write('\calcofftrue\n')
                outfile.write('\satfalse\n')
                #outfile.write('\gridintrue\n')
            if nquestion >=20 and nquestion < 50:
                if nquestion == 20:
                    outfile.write('\end{multicols*}\n')
                    outfile.write('\\newpage\n')
                    outfile.write('\calcofffalse\n')
                    outfile.write('\calcontrue\n')
                    outfile.write('\input{support/sat_calcon_cover.tex}\n')
                    outfile.write('\\begin{multicols*}{2}\n')
                    outfile.write('\n')
                    outfile.write('\satquestionnumber=0 \n')
                    outfile.write('\n')
                    questions_per_column = 0
                outfile.write('\calcontrue\n')
            if nquestion >=50:
                if nquestion == 50:
                    outfile.write('\end{multicols*}\n')
                    outfile.write('\\newpage\n')
                    outfile.write('\calcontrue\n')
                    outfile.write('\input{support/sat_calcon_grid-in_cover.tex}\n')
                    outfile.write('\\begin{multicols*}{2}\n')
                    outfile.write('\n')
                    outfile.write('\n')
                    questions_per_column = 0
                outfile.write('\calcontrue\n')
                outfile.write('\satfalse\n')
                #outfile.write('\gridintrue\n')
            tmp_name = tmp_file
            outfile.write('\\noindent\hspace*{2mm}\\begin{minipage}{\columnwidth-0.5\columnsep}\n')
            outfile.write('\\noindent\satquestion\n')
            outfile.write('\n')
            outfile.write('\input{questions/'+tmp_name+'}\n')
            outfile.write('\n')
            outfile.write('\\vspace{30mm} \n')
            outfile.write('\end{minipage}\n')
            outfile.write('\\vfill\n')
            outfile.write('\n')
            questions_per_column += 1
            if questions_per_column == 2 and nquestion:
                questions_per_column = 0
        else:
            if nquestion < 4:
                outfile.write('\gridinfalse\n')
                outfile.write('\calconfalse\n')
                outfile.write('\calcofftrue\n')
            if nquestion >= 4 and nquestion < 10:
                if nquestion == 4:
                    outfile.write('\end{multicols*}\n')
                    outfile.write('\\newpage\n')
                    outfile.write('\calcofffalse\n')
                    outfile.write('\calcontrue\n')
                    outfile.write('\\begin{multicols*}{2}\n')
                    outfile.write('\n')
                    outfile.write('\n')
                    questions_per_column = 0
                outfile.write('\calcofffalse\n')
                outfile.write('\calcontrue\n')
                outfile.write('\gridinfalse\n')
            tmp_name = tmp_file
            outfile.write('\\noindent\hspace*{2mm}\\begin{minipage}{\columnwidth-0.5\columnsep}\n')
            outfile.write('\\noindent\satquestion\n')
            outfile.write('\n')
            outfile.write('\input{questions/'+tmp_name+'}\n')
            outfile.write('\n')
            outfile.write('\\vspace{30mm} \n')
            outfile.write('\end{minipage}\n')
            outfile.write('\\vfill\n')
            outfile.write('\n')
            questions_per_column += 1
            if questions_per_column == 2 and nquestion:
                questions_per_column = 0
    #
    outfile.write('\end{multicols*} \n')
    outfile.write('\clearpage \n')
    return answer_key


def write_act_questions(outfile,question_list):
    answer_key = []
    for nquestion,tmp_file in enumerate(question_list):
        tmp_answers = find_correct_answer(os.path.join('questions',tmp_file))
        if nquestion%2 == 0:
            outfile.write('\\actevenfalse\n')
            outfile.write('\\actoddtrue\n')
            tmp_answer = tmp_answers['\\ifactodd']
        else:
            outfile.write('\\actoddfalse\n')
            outfile.write('\\acteventrue\n')
            tmp_answer = tmp_answers['\\ifacteven']
        answer_key.append(tmp_answer)
        tmp_name = tmp_file
        outfile.write('\\noindent\hspace*{2mm}\\begin{minipage}{\columnwidth-0.5\columnsep}\n')
        outfile.write('\item \n')
        outfile.write('\n')
        outfile.write('\parbox[t]{\columnwidth-0.5\columnsep}{\input{questions/'+tmp_name+'}} \n')
        outfile.write('\n')
        outfile.write('\end{minipage}\n')
        outfile.write('\\vfill\n')
        outfile.write('\n')
    outfile.write('\end{enumerate} \n')
    outfile.write('\end{multicols} \n')
    outfile.write('\\nocontinuetrue \n')
    outfile.write('\\vfill \n')
    outfile.write('\hfill \parbox{1\\textwidth}{\\flushright \\fontfamily{phv}\selectfont\\textbf{END OF TEST\\\\ \n')
    outfile.write('STOP! DO NOT TURN THE PAGE UNTIL TOLD TO DO SO.\\\\ \n')
    outfile.write('DO NOT RETURN TO THE PREVIOUS TEST.}} \n')
    outfile.write('\clearpage \n')
    return answer_key



def write_act_answer_key(outfile,answer_key):
    outfile.write('\\vspace*{10mm} \n')
    outfile.write('\\begin{center} \n')
    outfile.write('\underline{{\LARGE Answer Key}} \n')
    outfile.write('\end{center} \n')
    outfile.write('\\begin{multicols}{2} \n')
    outfile.write('\\begin{center} \n')
    outfile.write('\\begin{tabularx}{0.6\columnwidth}{p{1cm}X} \n')
    if len(answer_key) > 10:
        outfile.write('\multicolumn{2}{l}{Question $1 -30$} \\\\ \n')
    else:        
        outfile.write('\multicolumn{2}{l}{Question $1 -10$} \\\\ \n')
    outfile.write('\\toprule \n')
    for index in range(len(answer_key)):
        nq = index + 1
        if index == 30:
            outfile.write('\\bottomrule \n')
            outfile.write('\end{tabularx} \n')
            outfile.write('\end{center} \n')
            outfile.write('\\vfill\n')
            outfile.write('\columnbreak\n')
            outfile.write('\\begin{center} \n')
            outfile.write('\\begin{tabularx}{0.6\columnwidth}{p{1cm}X} \n')
            outfile.write('\multicolumn{2}{l}{Question $31 -60$} \\\\ \n')
            outfile.write('\\toprule \n')
        outfile.write(str(nq)+' & '+answer_key[index]+' \\\\'+' \n')
    outfile.write('\\bottomrule \n')
    outfile.write('\end{tabularx} \n')
    outfile.write('\end{center} \n')
    outfile.write('\end{multicols} \n')
    outfile.write('\end{document} \n')


def write_sat_answer_key(outfile,answer_key,kind):
    if kind == 'homework':
        outfile.write('\calconfalse \n')
        outfile.write('\calcofffalse \n')
        outfile.write('\\nocontinuetrue \n')
        outfile.write('\\vspace*{-10mm} \n')
        outfile.write('\\begin{center} \n')
        outfile.write('\underline{{\LARGE Answer Key}} \n')
        outfile.write('\end{center} \n')
        outfile.write('\\begin{multicols}{2} \n')
        outfile.write('\\begin{center} \n')
        outfile.write('\\begin{tabularx}{0.6\columnwidth}{p{1cm}X} \n')
        outfile.write('\multicolumn{2}{l}{Calculator Off} \\\\ \n')
        outfile.write('\\toprule \n')
        for index in range(len(answer_key)):
            nq = index + 1
            if index >= 20:
                nq = nq - 20
            if index == 20:
                outfile.write('\\bottomrule \n')
                outfile.write('\end{tabularx} \n')
                outfile.write('\end{center} \n')
                outfile.write('\\vfill\n')
                outfile.write('\columnbreak\n')
                outfile.write('\\begin{center} \n')
                outfile.write('\\begin{tabularx}{0.6\columnwidth}{p{1cm}X} \n')
                outfile.write('\multicolumn{2}{l}{Calculator On} \\\\ \n')
                outfile.write('\\toprule \n')
            outfile.write(str(nq)+' & '+answer_key[index]+' \\\\'+' \n')
            if index == 14 or index == 49:
                outfile.write('\midrule \n')
        outfile.write('\\bottomrule \n')
        outfile.write('\end{tabularx} \n')
        outfile.write('\end{center} \n')
        outfile.write('\end{multicols} \n')
        outfile.write('\end{document} \n')
    if kind == 'in-class':
        outfile.write('\calconfalse \n')
        outfile.write('\calcofffalse \n')
        outfile.write('\\nocontinuetrue \n')
        outfile.write('\\vspace*{-10mm} \n')
        outfile.write('\\begin{center} \n')
        outfile.write('\underline{{\LARGE Answer Key}} \n')
        outfile.write('\end{center} \n')
        outfile.write('\\begin{multicols}{2} \n')
        outfile.write('\\begin{center} \n')
        outfile.write('\\begin{tabularx}{0.6\columnwidth}{p{1cm}X} \n')
        outfile.write('\multicolumn{2}{l}{Calculator Off} \\\\ \n')
        outfile.write('\\toprule \n')
        for index in range(len(answer_key)):
            nq = index + 1
            if index == 4:
                outfile.write('\\bottomrule \n')
                outfile.write('\end{tabularx} \n')
                outfile.write('\end{center} \n')
                outfile.write('\\vfill\n')
                outfile.write('\columnbreak\n')
                outfile.write('\\begin{center} \n')
                outfile.write('\\begin{tabularx}{0.6\columnwidth}{p{1cm}X} \n')
                outfile.write('\multicolumn{2}{l}{Calculator On} \\\\ \n')
                outfile.write('\\toprule \n')
            outfile.write(str(nq)+' & '+answer_key[index]+' \\\\'+' \n')

        outfile.write('\\bottomrule \n')
        outfile.write('\end{tabularx} \n')
        outfile.write('\end{center} \n')
        outfile.write('\end{multicols} \n')
        outfile.write('\end{document} \n')



