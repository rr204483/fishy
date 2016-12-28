from django.forms import ModelForm
from utils.models import Staff

#just a test

class StaffForm(ModelForm):
    '''state = forms.CharField(widget=forms.TextInput(
                                          attrs={'readonly': ' readonly'}))
    '''

    class Meta:
        model = Staff
        fields = ('title','first_name','last_name', 'gender', 'staff_type', 'dob', 'doj', 'phone1', 'phone2', 'email', 'address', 'city', 'state', 'country',
				   'qualification', 'experience', 'photo', 'emergencycontact', 'major_subjects', 'school_id')

