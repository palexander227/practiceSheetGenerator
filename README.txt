+++++++++++++++++++++++++++++++++++++++++++++++++++++++

			README 

			 for 
	
	Flex ‘Practice Sheet Generator’

+++++++++++++++++++++++++++++++++++++++++++++++++++++++

This collection of folders and scripts will allow you to generate either full 
SAT and ACT test sheets (58 questions for SAT and 60 questions for ACT).

Alternatively, you can choose to create 10-question test sheets in ACT or SAT 
format. 

At the end of each test sheet an answer key will be provided.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Folder structure:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

Practice Sheet Generator

	practice_sheet_generator.py - the main executable
	/input - user input
	/scripts - main and auxiliary scripts
	/questions - the repository of questions
	/support - supporting files for compiling the latex source


+++++++++++++++++++++++++++++++++++++++++++++++++++++++
The ‘/input’ folder contains two files:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

	user_input.txt - choose which version you want to create
	my_list.txt - provide a list of questions (from the ‘questions’ directory) 
		that you wish to use to create the files

	Important note: You will have to order the file names in the ‘my_list.txt’
		as yu want them to appear in the final document. You also need to 
		make sure you provide the correct number of questions for the selected
		format. The main executable will run a few consistency test and prompt
		you for possible issues.


+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Important note on the files contained in ’/questions’:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

	These were initially a straight copy of the ‘/Questions’ folder of the 
	‘Flex Supporting Content’. However, a few changes were made to make them 
	sufficiently different. A potential cause for confusion could be that the 
	naming scheme was unchanged.

	However, in the current ‘/questions’ folder, certain changes have been 
	applied to the questions:

		‘/scripts/switch_location_supporting.py’

		This script changed the location of any supplemental files 
		referenced inside the ‘.tex’ questions files (e.g., tables 
		or images) to reflect the new layout.

		‘/scripts/insert_gridin_answers.py’

		This script identified the correct answer for each question
		and included it into the ‘\ifgridin’ section of the raw latex 
		code of the question.

	Since the changes of these two scripts are applied in addition to what is 
	already there, you need to make sure that they are only run once. If, by 
	accident, they are run twice, copy the questions from the ‘/Questions’ 
	directory in the ‘Flex Supporting Content’ again and apply the changes 
	one time.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Adding new problems:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

	New questions can simply be added by placing them in the ‘/questions’ folder. 
	Then they can be chosen as part of ‘my_list.txt’ for generating tests.

	Newly added problems will have to satisfy strict formatting guidelines, in 
	particular with respect to the coding of the answer choices.  	

+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Issue tracker:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

	‘question_1202.tex’ has been moved to ‘/questions/issues/‘ because it has 
	no answers indicated anywhere in the file. This potentially comes from the 
	extraction and may have to be fixed by hand.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Installing on Windows:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1. Go to: https://www.latex-project.org/get/
 2. Download MiKTeX for windows and install
 3. During MiKTeX installation check the box to not prompt you to install additional packages
 4. Open up MiKTeX Console and go to Settings->Directories and folder path of this project
 5. Run practice_sheet_generator.py
 6. If you run into issues then try opening up a command prompt and navigate to this projects directory. Then
 run pdflatex with one of the .tex files. This will make pdflatex install any missing packages that it needs. You can
 do this by typing: pdflatex sat_homework_20160904_153609.tex
