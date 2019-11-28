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
    ctx={'default':'only for testing','user_message':'hi'}
    hidden_info=None
    if request.POST:
        hidden_info=request.POST['hidden']
        ctx['user_message']=request.POST['q']
    print(ctx)
    curr_step=int(hidden_info or 0)
    print(curr_step)
    obj=State.objects.get(timestep=curr_step)
    state,intent,addition=0,'',''
    if obj:
        state,intent,addition=obj.state,obj.intent,obj.addition
    answer,state,search_sequence=receive_respond(message=ctx['user_message'],state=state,search_sequence=(intent,addition))
    print((answer,state,search_sequence,curr_step))
    intent,addition=search_sequence or '',''
    ctx['bot_message']=answer
    State.objects.get_or_create(timestep=curr_step+1)[0].update(answer=answer,state=state,intent=intent,addition=addition)
    return render(request,html_file,ctx)

def home(request):
    return render(request,html_file,{})