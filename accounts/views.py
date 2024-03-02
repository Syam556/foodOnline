from django.views.decorators.csrf import csrf_protect



from django.shortcuts import render,redirect
from vendor.forms import VendorForm
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages,auth
from django.contrib.auth import authenticate


@csrf_protect

def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in!')
        return redirect('dashboard')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #Create the user using the form
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # user.save()
            
            #Create the user using create_user method
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            messages.success(request, 'Your account has been registered successfully')
            
            
            # print('User is created')
                        
            return redirect('registerUser')
            # Redirect to a success page or do something else
        else:
            print('Invalid form')
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)





def registerVendor(request):
    
    # Initialize UserForm and VendorForm instances
    form = UserForm()
    v_form = VendorForm()
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in!')
        return redirect('dashboard')
    elif request.method == 'POST':
        # Bind POST data to form instances
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)

        # Check if both forms are valid
        if form.is_valid() and v_form.is_valid():
            # Create a new user
            user = form.save(commit=False)
            user.role = User.VENDOR
            user.save()

            # Create a new vendor associated with the user
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()

            # Display success message
            messages.success(request, 'Your account has been registered successfully! Please wait for the approval')
            return redirect('registerVendor')
        else:
            # If either form is invalid, print errors for debugging
            print(form.errors)
            print(v_form.errors)

    # Render the template with the form instances
    context = {
        'form': form,
        'V_form': v_form,
    }
    return render(request, 'accounts/registerVendor.html', context)



def login(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in!')
        return redirect('dashboard')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        
        
        user=auth.authenticate(email=email,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credential')
            return redirect('login')

    return render(request,'accounts/login.html')





# def login(request):
#     if request.user.is_authenticated:
#         messages.warning(request, 'You are already logged in!')
#         return redirect('dashboard')
#     elif request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Authenticate user
#         user = authenticate(email=email, password=password)
        
#         if user is not None:
#             # Check if the authenticated user is a vendor
#             if user.role == User.VENDOR:
#                 login(request, user)
#                 messages.success(request, 'You are now logged in as a vendor.')
#                 return redirect('vendor_dashboard')  # Redirect to vendor dashboard
#             else:
#                 # If not a vendor, login as a regular user
#                 login(request, user)
#                 messages.success(request, 'You are now logged in.')
#                 return redirect('dashboard')  # Redirect to user dashboard
#         else:
#             messages.error(request, 'Invalid login credentials')
#             return redirect('login')
#     return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'You have been logged out.')
    return redirect('login')

def dashboard(request):
    return render(request,'accounts/dashboard.html')