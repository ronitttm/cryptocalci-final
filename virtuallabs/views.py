from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserImageForm , CodeForm
from .models import UserImage , Code
from django.contrib.sessions.models import Session

# Create your views here.
def home(request):
    return render(request,"home.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('signin')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, "Passwords do not match. Please try again.")
            return redirect('signup')

        # Check if a user with the same username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "A user with the same username or email already exists. Please Login")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been created")
        return redirect('signin')

    return render(request, 'signup.html')



def signout(request):
    logout(request)
    messages.success(request , "Logged out Sucessfully")
    return redirect('home')

@login_required
def exp_list(request):
    return render(request,"exp_list.html")

def display_image_and_code1(request):
    user = request.user
    session_key = request.session.session_key
    try:
        latest_image = UserImage.objects.filter(session_key=session_key).latest('created_at')
    except UserImage.DoesNotExist:
        latest_image = None

    # Retrieve the code for the currently logged-in user
    user = request.user
    try:
        latest_code = Code.objects.filter(user=user).latest('created_at')
    except Code.DoesNotExist:
        latest_code = None

    return render(request, 'Experiment 1.html', {'latest_image': latest_image, 'latest_code': latest_code ,'user': user})

def display_image_and_code2(request):
    user = request.user
    session_key = request.session.session_key
    try:
        latest_image = UserImage.objects.filter(session_key=session_key).latest('created_at')
    except UserImage.DoesNotExist:
        latest_image = None

    # Retrieve the code for the currently logged-in user
    user = request.user
    try:
        latest_code = Code.objects.filter(user=user).latest('created_at')
    except Code.DoesNotExist:
        latest_code = None

    return render(request, 'Experiment 2.html', {'latest_image': latest_image, 'latest_code': latest_code ,'user': user})

def display_image_and_code3(request):
    user = request.user
    session_key = request.session.session_key
    try:
        latest_image = UserImage.objects.filter(session_key=session_key).latest('created_at')
    except UserImage.DoesNotExist:
        latest_image = None

    # Retrieve the code for the currently logged-in user
    user = request.user
    try:
        latest_code = Code.objects.filter(user=user).latest('created_at')
    except Code.DoesNotExist:
        latest_code = None

    return render(request, 'Experiment 3.html', {'latest_image': latest_image, 'latest_code': latest_code ,'user': user})

def display_image_and_code4(request):
    user = request.user
    session_key = request.session.session_key
    try:
        latest_image = UserImage.objects.filter(session_key=session_key).latest('created_at')
    except UserImage.DoesNotExist:
        latest_image = None

    # Retrieve the code for the currently logged-in user
    user = request.user
    try:
        latest_code = Code.objects.filter(user=user).latest('created_at')
    except Code.DoesNotExist:
        latest_code = None

    return render(request, 'Experiment 4.html', {'latest_image': latest_image, 'latest_code': latest_code ,'user': user})


def exp1(request):
    if request.method == 'POST':
        code_form = CodeForm(request.POST)
        image_form = UserImageForm(request.POST, request.FILES)

        if code_form.is_valid() and image_form.is_valid():
            # Get the currently logged-in user
            user = request.user
            code = code_form.cleaned_data['code']
            
            # Create a Code instance and link it to the user
            Code.objects.create(user=user, code=code)

            # Attach the session key to the image before saving
            image = image_form.save(commit=False)
            image.session_key = request.session.session_key
            image.save()

            # Redirect to a success page or perform other actions
            return redirect('exp1')
    else:
        code_form = CodeForm()
        image_form = UserImageForm()

    return render(request, 'exp1.html', {'code_form': code_form, 'image_form': image_form})

def exp2(request):
    if request.method == 'POST':
        code_form = CodeForm(request.POST)
        image_form = UserImageForm(request.POST, request.FILES)

        if code_form.is_valid() and image_form.is_valid():
            # Get the currently logged-in user
            user = request.user
            code = code_form.cleaned_data['code']
            
            # Create a Code instance and link it to the user
            Code.objects.create(user=user, code=code)

            # Attach the session key to the image before saving
            image = image_form.save(commit=False)
            image.session_key = request.session.session_key
            image.save()

            # Redirect to a success page or perform other actions
            return redirect('exp2')
    else:
        code_form = CodeForm()
        image_form = UserImageForm()
    return render(request, 'exp2.html', {'code_form': code_form, 'image_form': image_form})

def exp3(request):
    if request.method == 'POST':
        code_form = CodeForm(request.POST)
        image_form = UserImageForm(request.POST, request.FILES)

        if code_form.is_valid() and image_form.is_valid():
            # Get the currently logged-in user
            user = request.user
            code = code_form.cleaned_data['code']
            
            # Create a Code instance and link it to the user
            Code.objects.create(user=user, code=code)

            # Attach the session key to the image before saving
            image = image_form.save(commit=False)
            image.session_key = request.session.session_key
            image.save()

            # Redirect to a success page or perform other actions
            return redirect('exp3')
    else:
        code_form = CodeForm()
        image_form = UserImageForm()
    return render(request, 'exp3.html', {'code_form': code_form, 'image_form': image_form})

def exp4(request):
    if request.method == 'POST':
        code_form = CodeForm(request.POST)
        image_form = UserImageForm(request.POST, request.FILES)

        if code_form.is_valid() and image_form.is_valid():
            # Get the currently logged-in user
            user = request.user
            code = code_form.cleaned_data['code']
            
            # Create a Code instance and link it to the user
            Code.objects.create(user=user, code=code)

            # Attach the session key to the image before saving
            image = image_form.save(commit=False)
            image.session_key = request.session.session_key
            image.save()

            # Redirect to a success page or perform other actions
            return redirect('exp4')
    else:
        code_form = CodeForm()
        image_form = UserImageForm()
    return render(request, 'exp4.html', {'code_form': code_form, 'image_form': image_form})
    

def exp5(request):
    return render(request,"exp5.html")

def exp6(request):
    return render(request,"exp6.html")

def exp7(request):
    return render(request,"exp7.html")

def exp8(request):
    return render(request,"exp8.html")

def exp9(request):
    return render(request,"exp9.html")

def exp10(request):
    return render(request,"exp10.html")



def upload_image(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_display')
    else:
        form = UserImageForm()
    return render(request, 'upload_image.html', {'form': form})

