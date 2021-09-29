from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration,SearchStudent
from .models import Student
# Create your views here.


def delete_data(request,id):
	if request.method=='POST':
		pi =Student.objects.get(pk=id) 
		pi.delete()
		return HttpResponseRedirect('/')


def model_form(request):
	stu = Student.objects.all()
	if request.method=='POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			print('form validated')
			nm = fm.cleaned_data['name']
			em = fm.cleaned_data['email']
			pw = fm.cleaned_data['password']
			print(nm)
			reg =Student(name=nm,email=em,password=pw)
			reg.save()
			return render(request,'enroll/modelform.html',{'form':fm,'st':stu})
	else:
		fm = StudentRegistration()
		print('yeh page modelform ke get method se aaya hai')
	return render(request,'enroll/modelform.html',{'form':fm,'st':stu})

def edit_data(request,id):
	if request.method=='POST':
		pi = Student.objects.get(pk=id)
		gm =  StudentRegistration(request.POST,instance=pi)
		sm = SearchStudent(request.POST)
		if gm.is_valid():
			gm.save()
		elif sm.is_valid() or gm.is_valid():
			stu = Student.objects.all()
			name = sm.cleaned_data['name']
			# print(name)
			print('search chalu hai')
			for data in stu:
				# print(data.name)
				if data.name==name:
					print('successfull')
					print("you search : ",data.name)
					return render(request,'enroll/edit.html',{'form':gm,'searchform':sm,'da':data})
				
	else:
		gm = StudentRegistration()
		sm = SearchStudent()
		print('yeh page editdata ke get method se aaya hai')
	return render(request,'enroll/edit.html',{'form':gm,'searchform':sm,'myid':id})


