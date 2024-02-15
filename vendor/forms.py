# from django import forms
# from .models import vendor

# class VendorForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = vendor
#         fields = ['vendor_name', 'vendor_license']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['vendor_name'].widget = forms.TextInput(attrs={'placeholder': 'Vendor Name'})
#         self.fields['vendor_license'].widget = forms.FileInput(attrs={'accept': 'image/*'})



from django import forms
from .models import vendor

class VendorForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = vendor
        fields = ['vendor_name', 'vendor_license']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendor_name'].widget = forms.TextInput(attrs={'placeholder': 'Vendor Name'})
        self.fields['vendor_license'].widget = forms.FileInput(attrs={'accept': 'image/*', 'placeholder': 'Upload Image'})
