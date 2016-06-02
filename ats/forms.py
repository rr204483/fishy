from django.forms import ModelForm
from utils.models import School

#just a test

class SchoolForm(ModelForm):
    '''state = forms.CharField(widget=forms.TextInput(
                                          attrs={'readonly': ' readonly'}))
    '''

    class Meta:
        model = School
        fields = ('name', 'board', 'address', 'city', 'state', 'country',
				  'phone1', 'phone2', 'fax', 'email', 'website')

