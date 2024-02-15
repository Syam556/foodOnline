from django.shortcuts import render,redirect
from vendor.forms import VendorForm
from .forms import UserForm
from .models import User
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
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

# def registerVendor(request):
#     form=UserForm()
#     v_form=VendorForm()
    
    
#     context={
#         'form':form,
#         'v_form':v_form
#     }
#     return render(request,'accounts/registerVendor.html',context)

def registerVendor(request):
    form=UserForm()
    if request.method == 'POST':
        v_form = VendorForm(request.POST, request.FILES)
        if v_form.is_valid():
            # Process the form data if it's valid
            # Redirect or perform other actions
            pass
        else:
            # If the form is not valid, handle the errors
            print(v_form.errors)  # Print the form errors to the console for debugging
            # You can also pass the form with errors to the template context if needed
            context = {
                'v_form': v_form,
            }
            return render(request, 'accounts/registerVendor.html', context)
    else:
        # If it's a GET request, initialize a new form
        v_form = VendorForm()

    # Render the template with the form
    context = {
        'form':form,
        'V_form': v_form,
    }
    return render(request, 'accounts/registerVendor.html', context)
