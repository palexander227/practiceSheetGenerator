import os
from scripts import main 
from datetime import datetime
from time import gmtime, strftime
import subprocess

# +++++++++++++++++++++++++++++++++++
# Read user input
# +++++++++++++++++++++++++++++++++++
user_input = os.path.join('input','user_input.txt')
test_flavor, test_kind, test_infile = main.read_user_input(user_input)

# +++++++++++++++++++++++++++++++++++
# Run consistency checks on user input
# +++++++++++++++++++++++++++++++++++
main.check_user_input(test_flavor, test_kind, test_infile)

# +++++++++++++++++++++++++++++++++++
# Set current time
# +++++++++++++++++++++++++++++++++++
time_now = datetime.now()
time_now_string = time_now.strftime("%Y%m%d_%H%M%S")
time_now_fancy = time_now.strftime("%a, %d %b %Y at %H:%M:%S")

# +++++++++++++++++++++++++++++++++++
# Open target file in current directory
# +++++++++++++++++++++++++++++++++++
tmp_flavor = test_flavor.lower()
if '-' in test_kind: 
    tmp_kind = test_kind.replace('-','')
else:
    tmp_kind = test_kind
outfile = tmp_flavor+'_'+tmp_kind+'_'+time_now_string+'.tex'
out = open(outfile,'w')

# +++++++++++++++++++++++++++++++++++
# Write header
# +++++++++++++++++++++++++++++++++++
out.write('% Created '+time_now_fancy+' \n')
out.write('\n')
if test_flavor == 'SAT':
    main.write_sat_header(out)
else:
    main.write_act_header(out)

# +++++++++++++++++++++++++++++++++++
# Read problem list
# +++++++++++++++++++++++++++++++++++
qlist = main.read_input_file(test_infile)

# +++++++++++++++++++++++++++++++++++
# Write questions
# +++++++++++++++++++++++++++++++++++
if test_flavor == 'ACT':
	answer_key = main.write_act_questions(out,qlist)
else:
	answer_key = main.write_sat_questions(out,qlist,test_kind)

# +++++++++++++++++++++++++++++++++++
# Add answer key
# +++++++++++++++++++++++++++++++++++
if test_flavor == 'ACT':
	main.write_act_answer_key(out,answer_key)
else:
	main.write_sat_answer_key(out,answer_key,test_kind)

# +++++++++++++++++++++++++++++++++++
# Close target file
# +++++++++++++++++++++++++++++++++++
out.close()

# +++++++++++++++++++++++++++++++++++
# Compile latex 
# +++++++++++++++++++++++++++++++++++
subprocess.call(['pdflatex',outfile])

# +++++++++++++++++++++++++++++++++++
# Clean-up
# +++++++++++++++++++++++++++++++++++
# Move TEX and PDF
subprocess.call(['mv',outfile,os.path.join('final','.')])
pdf_file = outfile.replace('.tex','.pdf')
subprocess.call(['mv',pdf_file,os.path.join('final','.')])
# Remove TEX supplemental compilation files (.aux, .log)
supp_file_extensions = ['.aux','.log']
for supp_ext in supp_file_extensions:
	supp_file = outfile.replace('.tex',supp_ext)
	subprocess.call(['rm',supp_file])
# Miscellaneous files to be removed
misc_files = ['longdiv.aux']
for misc_file in misc_files:
	if os.path.isfile(misc_file):
		subprocess.call(['rm',misc_file])



