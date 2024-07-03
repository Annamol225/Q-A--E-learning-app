from django.shortcuts import redirect, render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages
# Create your views here.
 
def home(request):
    sub_obj=subject.objects.all()
    return render(request,'home1.html',{"sub_obj":sub_obj})



def learn(request):
    sub_obj=subject.objects.all() 
    return render(request,'learn.html',{"sub_obj":sub_obj})



def indo(request,in_id):
    if not request.user.is_authenticated:
        messages.info(request,'please login to access that page')
        return redirect('/account/login')
    sub=subject.objects.all()
    sub_obj=subject.objects.get(id=in_id) 

    sub_ob = get_object_or_404(subject, id=in_id)
    sy = syllabus.objects.filter(sub_name=sub_ob)
    return render(request,'indo.html',{"sub_obj":sub_obj,"sub_ob":sub_ob, 'sy':sy,'sub':sub})


def indo1(request,in_id):
    if not request.user.is_authenticated:
        messages.info(request,'please login to access that page')
        return redirect('/account/login')
    sub=subject.objects.all()
    sub_obj=subject.objects.get(id=in_id) 

    sub_ob = get_object_or_404(subject, id=in_id)
    sy = syllabus.objects.filter(sub_name=sub_ob)
    return render(request,'indo1.html',{"sub_obj":sub_obj,"sub_ob":sub_ob, 'sy':sy,'sub':sub})


def qa(request,q_id):
    su=subject.objects.all()
    sl=syllabus.objects.all()

    sy= get_object_or_404(syllabus, id=q_id)
    qa = Qa.objects.filter(sy_list=sy).select_related('sub_name', 'sy_list')
    return render(request,'qa.html',{"qa":qa,'sy':sy,'su':su,'sl':sl})

def qa1(request,q_id):
    su=subject.objects.all()
    sl=syllabus.objects.all()

    sy= get_object_or_404(syllabus, id=q_id)
    qa = Qa.objects.filter(sy_list=sy).select_related('sub_name', 'sy_list')
    return render(request,'qa1.html',{"qa":qa,'sy':sy,'su':su,'sl':sl})

 
def search(request):
    if request.method=='POST':
        search1=request.POST.get('search')
        # res=Qa.objects.filter(sub_name__icontains=search1)
        return render(request,'search.html',{'search1':search1})
    else:
        return render(request,'search.html',{})

