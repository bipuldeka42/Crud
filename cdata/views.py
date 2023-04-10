from django.shortcuts import render,HttpResponseRedirect
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
            form=StudentForm()
            
    else:
        form=StudentForm()
    all_data=Students.objects.all()
    return render(request,'home.html',{'form':form,'all_data':all_data})
# delete specific data from student table,
def delete_data(request,id):
    if request.method=='POST':
        e_data=Students.objects.get(id=id)
        
        e_data.delete()
    return HttpResponseRedirect('/')
def updatedata(request,id):
    if request.method=='POST':
        u_data=Students.objects.get(pk=id)
        print(u_data)
        fm=StudentForm(request.POST,instance=u_data)
        if fm.is_valid():
            fm.save()
    else:
        u_data=Students.objects.get(pk=id)
        fm=StudentForm(instance=u_data)

    return render(request,'photo.html',{'form':fm})
