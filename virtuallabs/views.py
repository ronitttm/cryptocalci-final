from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserImageForm , CodeForm, addQuestionform
from .models import Code, UploadedImage, QuesModel, QuizScore, ExperimentSubmission, Experiments
from django.contrib.sessions.models import Session
from django.conf import settings
import pyrebase
from virtuallabs import urls
import random

firebase_config = settings.FIREBASE_CONFIG

firebase = pyrebase.initialize_app(firebase_config)
storage = firebase.storage()

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


def admin_dashboard(request):
    submissions = ExperimentSubmission.objects.all()
    context = {
        'submissions': submissions
    }
    return render(request, 'dashboard.html', context)

def user_dashboard(request):
    if request.user.is_staff:
        return admin_dashboard(request)
    else:
        user = request.user
        experiments = ExperimentSubmission.objects.filter(user=user)
        experiment_count = experiments.count()
        experiment_names = [experiment.experiment_name for experiment in experiments]
        context = {
            'experiment_count': experiment_count,
            'experiment_names': experiment_names
        }
        return render(request, 'dashboard.html', context)


def display_image_and_code1(request):
    user = request.user
    
    # Fetch the latest uploaded image
    latest_image = UploadedImage.objects.last()
    # Fetch the latest code for the currently logged-in user
    latest_code = Code.objects.filter(user=user).latest('created_at')
    # Fetch quiz scores for the current user
    quiz_scores = QuizScore.objects.filter(user=user).last()
    # Fetch information about the experiment
    experiment = get_object_or_404(Experiments, pk=1)
    # Fetch submissions for the current user related to the experiment
    submissions = ExperimentSubmission.objects.filter(user=user, experiment_id=1)

    return render(request, 'Experiment 1.html', {
        'latest_image': latest_image,
        'latest_code': latest_code,
        'user': user,
        'quiz_scores': quiz_scores,
        'experiment': experiment,
        'submissions': submissions
    })



def display_image_and_code2(request):
    user = request.user
    
    # Fetch the latest uploaded image
    latest_image = UploadedImage.objects.last()
    # Fetch the latest code for the currently logged-in user
    latest_code = Code.objects.filter(user=user).latest('created_at')
    # Fetch quiz scores for the current user
    quiz_scores = QuizScore.objects.filter(user=user).last()
    # Fetch information about the experiment
    experiment = get_object_or_404(Experiments, pk=2)
    # Fetch submissions for the current user related to the experiment
    submissions = ExperimentSubmission.objects.filter(user=user, experiment_id=2)

    return render(request, 'Experiment 2.html', {
        'latest_image': latest_image,
        'latest_code': latest_code,
        'user': user,
        'quiz_scores': quiz_scores,
        'experiment': experiment,
        'submissions': submissions
    })

   

def display_image_and_code3(request):
    user = request.user
    
    # Fetch the latest uploaded image
    latest_image = UploadedImage.objects.last()
    # Fetch the latest code for the currently logged-in user
    latest_code = Code.objects.filter(user=user).latest('created_at')
    # Fetch quiz scores for the current user
    quiz_scores = QuizScore.objects.filter(user=user).last()
    # Fetch information about the experiment
    experiment = get_object_or_404(Experiments, pk=3)
    # Fetch submissions for the current user related to the experiment
    submissions = ExperimentSubmission.objects.filter(user=user, experiment_id=3)

    return render(request, 'Experiment 3.html', {
        'latest_image': latest_image,
        'latest_code': latest_code,
        'user': user,
        'quiz_scores': quiz_scores,
        'experiment': experiment,
        'submissions': submissions
    })

def display_image_and_code4(request):
    user = request.user
    
    # Fetch the latest uploaded image
    latest_image = UploadedImage.objects.last()
    # Fetch the latest code for the currently logged-in user
    latest_code = Code.objects.filter(user=user).latest('created_at')
    # Fetch quiz scores for the current user
    quiz_scores = QuizScore.objects.filter(user=user).last()
    # Fetch information about the experiment
    experiment = get_object_or_404(Experiments, pk=4)
    # Fetch submissions for the current user related to the experiment
    submissions = ExperimentSubmission.objects.filter(user=user, experiment_id=4)

    return render(request, 'Experiment 4.html', {
        'latest_image': latest_image,
        'latest_code': latest_code,
        'user': user,
        'quiz_scores': quiz_scores,
        'experiment': experiment,
        'submissions': submissions
    })


def exp1(request):
    if request.method == 'POST':
        code_form = CodeForm(request.POST)
        image_form = UserImageForm(request.POST, request.FILES)

        if code_form.is_valid() and image_form.is_valid():
            user = request.user
            code = code_form.cleaned_data['code']
            image = request.FILES['image']

            # Save code to the database
            Code.objects.create(user=user, code=code)

            # Upload image to cloud storage (Replace this with your actual code to upload to Firebase Storage)
            filename = image.name  # Assuming you're using the filename as the object name
            storage.child("images/" + filename).put(image)
            # Get the download URL of the uploaded image
            image_url = storage.child("images/" + filename).get_url(None)
            
            # Save the image URL into the database
            image_instance = UploadedImage.objects.create(url=image_url)
            image_instance.save()

            # Get the experiment
            experiment = Experiments.objects.get(pk=1)

            submission = ExperimentSubmission.objects.filter(user=user, experiment=experiment).first()

            if submission:
            # Increment submission count if already submitted
                submission.submission_count += 1
                submission.link = image_url  # Update the link with the image URL
                submission.code = code
                submission.save()
            else:
                # Create a new submission if not already submitted
                submission = ExperimentSubmission.objects.create(
                    user=user, 
                    experiment=experiment,
                    experiment_name = 'Experiment 1 - Implement Ceaser/Additive Cipher Using Python' ,
                    code = code,
                    image = image_url,
                    submission_count=1)
                submission.save()
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
            user = request.user
            code = code_form.cleaned_data['code']
            image = request.FILES['image']

            # Save code to the database
            Code.objects.create(user=user, code=code)

            # Upload image to cloud storage (Replace this with your actual code to upload to Firebase Storage)
            filename = image.name  # Assuming you're using the filename as the object name
            storage.child("images/" + filename).put(image)
            # Get the download URL of the uploaded image
            image_url = storage.child("images/" + filename).get_url(None)
            
            # Save the image URL into the database
            image_instance = UploadedImage.objects.create(url=image_url)
            image_instance.save()

            # Get the experiment
            experiment = Experiments.objects.get(pk=2)

            submission = ExperimentSubmission.objects.filter(user=user, experiment=experiment).first()

            if submission:
            # Increment submission count if already submitted
                submission.submission_count += 1
                submission.link = image_url  # Update the link with the image URL
                submission.code = code
                submission.save()
            else:
                # Create a new submission if not already submitted
                submission = ExperimentSubmission.objects.create(
                    user=user, 
                    experiment=experiment,
                    experiment_name = 'Experiment 2 - Implement Multiplicative Cipher Using Python' ,
                    code = code,
                    image = image_url,
                    submission_count=1)
                submission.save()
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
            user = request.user
            code = code_form.cleaned_data['code']
            image = request.FILES['image']

            # Save code to the database
            Code.objects.create(user=user, code=code)

            # Upload image to cloud storage (Replace this with your actual code to upload to Firebase Storage)
            filename = image.name  # Assuming you're using the filename as the object name
            storage.child("images/" + filename).put(image)
            # Get the download URL of the uploaded image
            image_url = storage.child("images/" + filename).get_url(None)
            
            # Save the image URL into the database
            image_instance = UploadedImage.objects.create(url=image_url)
            image_instance.save()

            # Get the experiment
            experiment = Experiments.objects.get(pk=3)

            submission = ExperimentSubmission.objects.filter(user=user, experiment=experiment).first()

            if submission:
            # Increment submission count if already submitted
                submission.submission_count += 1
                submission.link = image_url  # Update the link with the image URL
                submission.code = code
                submission.save()
            else:
                # Create a new submission if not already submitted
                submission = ExperimentSubmission.objects.create(
                    user=user, 
                    experiment=experiment,
                    experiment_name = 'Experiment 3 - Implement Affine Cipher Using Python' ,
                    code = code,
                    image = image_url,
                    submission_count=1)
                submission.save()
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
            user = request.user
            code = code_form.cleaned_data['code']
            image = request.FILES['image']

            # Save code to the database
            Code.objects.create(user=user, code=code)

            # Upload image to cloud storage (Replace this with your actual code to upload to Firebase Storage)
            filename = image.name  # Assuming you're using the filename as the object name
            storage.child("images/" + filename).put(image)
            # Get the download URL of the uploaded image
            image_url = storage.child("images/" + filename).get_url(None)
            
            # Save the image URL into the database
            image_instance = UploadedImage.objects.create(url=image_url)
            image_instance.save()

            # Get the experiment
            experiment = Experiments.objects.get(pk=4)

            submission = ExperimentSubmission.objects.filter(user=user, experiment=experiment).first()

            if submission:
            # Increment submission count if already submitted
                submission.submission_count += 1
                submission.link = image_url  # Update the link with the image URL
                submission.code = code
                submission.save()
            else:
                # Create a new submission if not already submitted
                submission = ExperimentSubmission.objects.create(
                    user=user, 
                    experiment=experiment,
                    experiment_name = 'Experiment 4 - Implement Rail Fence Transposition Cipher Using Python' ,
                    code = code,
                    image = image_url,
                    submission_count=1)
                submission.save()
            # Redirect to a success page or perform other actions
            return redirect('exp4')
    else:
        code_form = CodeForm()
        image_form = UserImageForm()

    return render(request, 'exp4.html', {'code_form': code_form, 'image_form': image_form})
   
    

def exp5(request):
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
            image = request.FILES['image']
            filename = image.name
            storage.child("images/" + filename).put(image)
            # Get the download URL of the uploaded image
            image_url = storage.child("images/" + filename).get_url(None)
            
            # Save the image URL into the database
            uploaded_image = UploadedImage.objects.create(url=image_url)
            uploaded_image.save()

            # Redirect to a success page or perform other actions
            return redirect('exp5')
    else:
        code_form = CodeForm()
        image_form = UserImageForm()
    return render(request, 'exp5.html', {'code_form': code_form, 'image_form': image_form})

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



# def upload_image(request):
#     if request.method == 'POST':
#         form = UserImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('image_display')
#     else:
#         form = UserImageForm()
#     return render(request, 'upload_image.html', {'form': form})

def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('addquestion')
        context={'form':form}
        return render(request,'addQuestion.html',context)
    else: 
        return redirect('home') 
    
def quiz1(request):
    if request.method == 'POST':
        # Process quiz submission
        questions = QuesModel.objects.filter(experiment_id=1)
        total = questions.count()  # Calculate total number of questions for experiment_id 1
        score = 0
        wrong = 0
        correct = 0
        for q in questions:
            answer = request.POST.get(str(q.id))
            if answer:
                if q.Answer == answer:
                    score += 10
                    correct += 1
                else:
                    wrong += 1
        
        # Calculate percent
        if total != 0:
            percent = (score / (total * 10)) * 100
        else:
            percent = 0
        
        # Save quiz score to database
        quiz_score = QuizScore.objects.create(
            user=request.user,
            score=score,
            time_taken=int(request.POST.get('timer', 0)),
            correct_answers=correct,
            wrong_answers=wrong,
            percent_correct=percent,
            total_questions=total
        )


        # Redirect to display_image_and_code1 view
        return redirect('generate1')
    else:
        # Render the quiz page
        questions = list(QuesModel.objects.filter(experiment_id=1))  # Convert queryset to a list
        total = len(questions)  # Calculate total number of questions for experiment_id 1

        # Randomize the order of questions every time the page loads
        random.shuffle(questions)

        # Select any 5 random questions
        selected_questions = questions[:5]

        context = {
            'questions': selected_questions,  # Pass the selected questions to the template
            'total': total
        }
        return render(request, 'quiz1.html', context)
    
    
    
def quiz2(request):
    if request.method == 'POST':
        # Process quiz submission
        questions = QuesModel.objects.filter(experiment_id=2)
        total = questions.count()  # Calculate total number of questions for experiment_id 1
        score = 0
        wrong = 0
        correct = 0
        for q in questions:
            answer = request.POST.get(str(q.id))
            if answer:
                if q.Answer == answer:
                    score += 10
                    correct += 1
                else:
                    wrong += 1
        
        # Calculate percent
        if total != 0:
            percent = (score / (total * 10)) * 100
        else:
            percent = 0
        
        # Save quiz score to database
        quiz_score = QuizScore.objects.create(
            user=request.user,
            score=score,
            time_taken=int(request.POST.get('timer', 0)),
            correct_answers=correct,
            wrong_answers=wrong,
            percent_correct=percent,
            total_questions=total
        )

        # Redirect to display_image_and_code1 view
        return redirect('generate2')
    else:
        questions = list(QuesModel.objects.filter(experiment_id=2))  # Convert queryset to a list
        total = len(questions)  # Calculate total number of questions for experiment_id 1

        # Randomize the order of questions every time the page loads
        random.shuffle(questions)

        # Select any 5 random questions
        selected_questions = questions[:5]

        context = {
            'questions': selected_questions,  # Pass the selected questions to the template
            'total': total
        }
        return render(request, 'quiz2.html', context)
    
def quiz3(request):
    if request.method == 'POST':
        # Process quiz submission
        questions = QuesModel.objects.filter(experiment_id=3)
        total = questions.count()  # Calculate total number of questions for experiment_id 1
        score = 0
        wrong = 0
        correct = 0
        for q in questions:
            answer = request.POST.get(str(q.id))
            if answer:
                if q.Answer == answer:
                    score += 10
                    correct += 1
                else:
                    wrong += 1
        
        # Calculate percent
        if total != 0:
            percent = (score / (total * 10)) * 100
        else:
            percent = 0
        
        # Save quiz score to database
        quiz_score = QuizScore.objects.create(
            user=request.user,
            score=score,
            time_taken=int(request.POST.get('timer', 0)),
            correct_answers=correct,
            wrong_answers=wrong,
            percent_correct=percent,
            total_questions=total
        )

        # Redirect to display_image_and_code1 view
        return redirect('generate3')
    else:
        questions = list(QuesModel.objects.filter(experiment_id=3))  # Convert queryset to a list
        total = len(questions)  # Calculate total number of questions for experiment_id 1

        # Randomize the order of questions every time the page loads
        random.shuffle(questions)

        # Select any 5 random questions
        selected_questions = questions[:5]

        context = {
            'questions': selected_questions,  # Pass the selected questions to the template
            'total': total
        }
        return render(request, 'quiz3.html', context)
    
def quiz4(request):
    if request.method == 'POST':
        # Process quiz submission
        questions = QuesModel.objects.filter(experiment_id=4)
        total = questions.count()  # Calculate total number of questions for experiment_id 1
        score = 0
        wrong = 0
        correct = 0
        for q in questions:
            answer = request.POST.get(str(q.id))
            if answer:
                if q.Answer == answer:
                    score += 10
                    correct += 1
                else:
                    wrong += 1
        
        # Calculate percent
        if total != 0:
            percent = (score / (total * 10)) * 100
        else:
            percent = 0
        
        # Save quiz score to database
        quiz_score = QuizScore.objects.create(
            user=request.user,
            score=score,
            time_taken=int(request.POST.get('timer', 0)),
            correct_answers=correct,
            wrong_answers=wrong,
            percent_correct=percent,
            total_questions=total
        )

        # Redirect to display_image_and_code1 view
        return redirect('generate4')
    else:
        questions = list(QuesModel.objects.filter(experiment_id=4))  # Convert queryset to a list
        total = len(questions)  # Calculate total number of questions for experiment_id 1

        # Randomize the order of questions every time the page loads
        random.shuffle(questions)

        # Select any 5 random questions
        selected_questions = questions[:5]

        context = {
            'questions': selected_questions,  # Pass the selected questions to the template
            'total': total
        }
        return render(request, 'quiz4.html', context)




# Sandbox Views 

def sandbox(request):
    return render(request,"sandbox/sandbox.html")


def additive(request):
    return render(request,"sandbox/additive.html")


def multiplicative(request):
    return render(request,"sandbox/multiplicative.html")


def affine(request):
    return render(request,"sandbox/Affine.html")


def caeser(request):
    return render(request,"sandbox/caeser.html")


def vignere(request):
    return render(request,"sandbox/vignere.html")


def hill(request):
    return render(request,"sandbox/hill.html")


def playfair(request):
    return render(request,"sandbox/Playfair.html")


def aes(request):
    return render(request,"sandbox/aes.html")


def des(request):
    return render(request,"sandbox/des.html")


def rc4(request):
    return render(request,"sandbox/rc4.html")


def rsa(request):
    return render(request,"sandbox/rsa.html")


def elgamal(request):
    return render(request,"sandbox/elgamal.html")


def sha256(request):
    return render(request,"sandbox/sha256.html")
