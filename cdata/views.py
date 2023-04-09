from django.shortcuts import render
from .models import Students
from .forms import StudentForm

# Create your views here.
def home(request):
    if request.method=="POST":
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            cl=form.cleaned_data['cl']
            roll=form.cleaned_data['roll']
            pro_img=form.cleaned_data['pro_img']

            reg=Students(name=name,cl=cl,roll=roll,pro_img=pro_img)
            reg.save()
            
    else:
        form=StudentForm()
    all_data=Students.objects.all()
    return render(request,'home.html',{'form':form,'all_data':all_data})