from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
    # print(RegisterationForm())
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            login(request, user)
            # print(form.__dict__)
            # print(request.POST)
            if form.is_valid():
                user = form.save()
                # authenticate(user)

                return redirect('/1')
            else:
                # print("PROBLEM")
                # print(form.errors)
                return render(request, 'accounts/signup.html',{"errors":form.errors})
        return render(request, 'accounts/signup.html')
    return redirect('/')

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    else:
                        return redirect('/')
        return render(request, 'accounts/signin.html')
    return redirect('/')

def logout1(request):
    logout(request)
    return redirect('/')