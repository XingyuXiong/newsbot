from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from scripts.main import receive_respond
from .models import State
import os
import sys


work_dir=os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
html_file=work_dir+r'\newsbot\index.html'


def accept(request):
    ctx={'default':'only for testing'}
    if request.POST:
        hidden_info=request.POST['hidden']
        ctx['user_message']=request.POST['q']
        ctx['bot_message']=receive_respond(request.POST['q'])
    answer,state,search_sequence='','',''
    intent=addition=''
    if search_sequence:
        intent,addition=search_sequence
    #state,exist=State.objects.get_or_create(answer=answer,state=state,intent=intent,addition=addition)
    return render(request,html_file,ctx)