from gettext import translation
from django.shortcuts import render,redirect,HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile,Student_detail,Batch,FeedbackRes




def Home(request):
    return render(request,'home/index.html')
# def Login(request):
#     return render(request,'home/login.html')
def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create the user
           
            user = form.save()

            # Additional fields specific to UserProfile
            name = form.cleaned_data.get('name')

            # Check if 'name' is not empty before creating the UserProfile
            if name:
                # Create UserProfile instance
                user_profile = UserProfile(user=user, name=name, designation=form.cleaned_data['designation'])
                user_profile.save()
            else:
                # Handle the case where 'name' is empty (provide appropriate error handling or redirect)
                print("Error: 'name' cannot be empty")

            messages.success(request,"Account has been created")

            # Log the user in
        

            # Redirect to a success page or home page
            return redirect('Login')
        else:
            # Form is not valid, handle errors or log them for debugging
            print(form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'home/register.html', {'form': form})
       
def Loginview(request):
    form = RegistrationForm()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return render(request, 'home/login.html',)

def Logoutview(request):
    logout(request)
    return redirect('Home')     



@login_required
def profile(request):
     user = request.user
     if user.is_authenticated:
        return render(request, 'home/profile.html', {'user': user})
     else:
        # Handle the case when the user is not authenticated
        return render(request, 'home/profile.html')

   
    
# @login_required
# def feedback_view(request):
#     subjects = None
#     obj1 = Batch.objects.all()
#     labs=None

#     if request.method == 'POST':
#         selected_batch_year = request.POST.get('year')
#         selected_department = request.POST.get('department')

#         subjects = Student_detail.objects.filter(Batch__Batchyear=selected_batch_year, Batch__department=selected_department,sub_type='SUBJECT')
#         labs=Student_detail.objects.filter(
#             Batch__Batchyear=selected_batch_year,
#             Batch__department=selected_department,
#             sub_type='LABORATORY'
#         )
        
    
#     return render(request, 'home/test.html', {'results': obj1, 'subjects': subjects,'labs':labs})
    

    

def test(request):
    subjects = None
    labs = None
    obj1 = Batch.objects.all()

    if request.method == 'POST':
        selected_batch_year = request.POST.get('year')
        selected_department = request.POST.get('department')

        subjects = Student_detail.objects.filter(Batch__Batchyear=selected_batch_year, Batch__department=selected_department, sub_type='SUBJECT')
        labs = Student_detail.objects.filter(Batch__Batchyear=selected_batch_year, Batch__department=selected_department, sub_type='LABORATORY')

        for sub in subjects:
            for i in range(1, 11):  # Assuming 10 questions per subject
                field_name = f"P{i}{sub.id}"
                # print(field_name)
                ans = request.POST.get(field_name)
                print(ans)
                print(f"Field name: {field_name}, Answer: {ans}")
                
                if ans:
                    FeedbackRes.objects.create(
                        year=selected_batch_year,
                        department=selected_department,
                        res=int(ans),
                        Qno=i
                    )
        for lab in labs:
            for i in range(1, 11):  # Assuming 10 questions per lab
                field_name = f"L{i}{lab.id}"
                ans = request.POST.get(field_name)
                if ans:
                    FeedbackRes.objects.create(
                        year=selected_batch_year,
                        department=selected_department,
                        res=int(ans),
                        Qno=i
                    )

    print("Feedback saved successfully.")

    return render(request, 'home/test.html', {'results': obj1, 'subjects': subjects, 'labs': labs})
    
    
def submit(request):
    return render(request,'home/test.html')