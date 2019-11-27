from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from scripts.main import receive_respond
import os
import sys


sys_type=os.name
work_dir=os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
html_file=work_dir+r'\newsbot\index.html'


def accept(request):
    ctx={'default':'only for testing'}
    if request.POST:
        ctx['user_message']=request.POST['q']
        ctx['bot_message']=receive_respond(request.POST['q'])
    return render(request,html_file,ctx)