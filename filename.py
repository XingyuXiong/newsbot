import os
import sys

sys_type=os.name
work_dir=os.path.abspath(os.path.dirname(sys.argv[0]))
if sys_type=='nt':
    work_dir=work_dir+'\\'
elif sys_type=='posix':
    work_dir=work_dir+'/'


spacy_model_name='spacy_model'