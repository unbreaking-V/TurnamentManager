from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Team,Coach,Stadium,Players,Event_organizer,Team_manager,Request,Match_history,Budget, Box_office, Employee

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class CoachForm(ModelForm):
    phone_number = PhoneNumberField(region="PL")
    class Meta:
         model = Coach
         fields = '__all__'

class StadiumForm(ModelForm):
     class Meta:
         model = Stadium
         fields = '__all__'

class PlayersForm(ModelForm):
     phone_number = PhoneNumberField(region="PL")
     class Meta:
         model = Players
         fields = '__all__'

class OrganizerForm(ModelForm):
    phone_number =  PhoneNumberField(region="PL")
    class Meta:
        model = Event_organizer
        fields = '__all__'

class TeamManagerForm(ModelForm):
    phone_number = PhoneNumberField(region="PL")
    class Meta:
        model = Team_manager
        fields = '__all__'

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

class MatchForm(ModelForm):
    class Meta:
        model = Match_history
        fields = '__all__'

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'

class BoxOfficeForm(ModelForm):
    class Meta:
        model = Box_office
        fields = '__all__'

class EmployeeForm(ModelForm):
    phone_number = PhoneNumberField(region="PL")
    class Meta:
        model = Employee
        fields = '__all__'

