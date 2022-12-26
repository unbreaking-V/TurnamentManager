from django.forms import ModelForm
from .models import Team, Coach, Stadium, Players,Event_organizer,Team_manager

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class CoachForm(ModelForm):
     class Meta:
         model = Coach
         fields = '__all__'

class StadiumForm(ModelForm):
     class Meta:
         model = Stadium
         fields = '__all__'

class PlayersForm(ModelForm):
     class Meta:
         model = Players
         fields = '__all__'

class OrganizerForm(ModelForm):
    class Meta:
        model = Event_organizer
        fields = '__all__'

class TeamManagerForm(ModelForm):
    class Meta:
        model = Team_manager
        fields = '__all__'




