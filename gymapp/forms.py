from django.contrib.auth.forms import UserCreationForm
from django import forms

from gymapp.models import Login, Customer, Physician, Instructor, CustMembership, CustomerDoubts, \
    CustomerComplaint, GymServices, Membership, Idietadd, HealthDetails, Membershipjoin, Fee


class LoginReg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ("username", "password1", "password2")


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'
        exclude = ("user",)

        class DateInput(forms.DateInput):
            input_type = 'date'


class PhysicianForm(forms.ModelForm):
    class Meta:
        model = Physician
        fields = '__all__'
        exclude = ("user1",)

        class DateInput(forms.DateInput):
            input_type = 'date'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ("user2",)


# class EquipmentForm(forms.ModelForm):
#     class Meta:
#         model = Equipments
#         fields = '__all__'



# class FirstaidForm(forms.ModelForm):
#     class Meta:
#         model = FirstAid
#         fields = '__all__'

class Custmembershipform(forms.ModelForm):
    class Meta:
        model = CustMembership
        fields = '__all__'


class CustomerDoubtsUserForm(forms.ModelForm):
    class Meta:
        model=CustomerDoubts

        exclude=('user4','reply')
class CustomerDoubtsPhyForm(forms.ModelForm):
    class Meta:
        model = CustomerDoubts
        exclude = ('user4',)
class CustomerComplaintUserForm(forms.ModelForm):
    class Meta:
        model = CustomerComplaint

        exclude = ('user5','reply',)

class CustomerComplaintAdminForm(forms.ModelForm):
     class Meta:
         model = CustomerComplaint

         exclude = ('user5',)


class GymServicesForm(forms.ModelForm):
    class Meta:
        model = GymServices
        fields = '__all__'



class AdminReplyForm(forms.ModelForm):
    class Meta:
        model= CustomerComplaint
        fields=('user5','complaints','reply')






class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'


class MembershipJoinForm(forms.ModelForm):
    # duration = forms.CharField(max_length=100)
    class Meta:
        model= Membershipjoin

        fields='__all__'

class DietaddForm(forms.ModelForm):
    class Meta:
        model= Idietadd
        fields = '__all__'


class HealthDetailsForm(forms.ModelForm):
    class Meta:
        model = HealthDetails
        fields = '__all__'

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'