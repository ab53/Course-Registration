from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Course, CourseDetail

# Create your views here.

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], 
								password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated \'successfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form': form})

#def user_logout(request):
#	logout(request,logout ,'account/logged_out.html')

def status_course(request):

	if request.user.is_authenticated():
		queryset = CourseDetail.objects.all()
		context = {
			'course_list' : queryset,
		}
		return render(request,"account/status.html",context)
	
	else:
		return redirect('dashboard')

def detail(request,id=None):

	if request.user.is_authenticated():

		course_obj = get_object_or_404(CourseDetail,id=id)
		queryset = Course.objects.filter(code=course_obj.coursecode)
		context = {
			'course_list' : queryset,
			'course_title' : course_obj.coursetitle,
		}

		return render(request,"account/detail.html",context)

	else:
		return HttpResponseRedirect(reverse('dashboard'))

@login_required
def dashboard(request):
	
	queryset = Course.objects.filter(owner=request.user.username)
	context = {
		'course_list' : queryset,
	}

	return render(request,'account/dashboard.html',context)

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(
				user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			return render(request,
				'account/register_done.html',
				{'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	
	return render(request,'account/register.html',{'user_form': user_form})

def add_course(request):

	if request.user.is_authenticated:
		queryset = CourseDetail.objects.all()
		context = {
			'course_list' : queryset,
		}
	
	return render(request,"account/add.html",context)

def new_course(request,id=None):

	if request.user.is_authenticated():
		newcourse = get_object_or_404(CourseDetail,id=id)
		current_user = request.user
		if not (Course.objects.filter(code=newcourse.coursecode).filter(owner=current_user.username).exists()): 
			Course.objects.create(owner=current_user.username, title = newcourse.coursetitle ,code = newcourse.coursecode )

	return HttpResponseRedirect(reverse('dashboard'))	

	