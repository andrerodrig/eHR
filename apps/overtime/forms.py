
from django.forms import ModelForm

from .models import OvertimeRegister
from apps.employee.models import Employee


class OvertimeRegisterForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(OvertimeRegisterForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(
            company=user.employee.company)

    class Meta:
        model = OvertimeRegister
        fields = ['reason', 'employee', 'hours']
