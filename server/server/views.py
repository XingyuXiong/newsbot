from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
import os
import sys


sys_type=os.name
work_dir=os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
html_file=work_dir+r'\newsbot\index.html'


def accept(request):
    ctx={}
    if request.POST:
        ctx['rlt']=request.POST['q']
    return render(request,html_file,ctx)