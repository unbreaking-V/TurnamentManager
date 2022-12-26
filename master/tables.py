from django_tables2 import tables, TemplateColumn
from .models import Team, Coach, Stadium, Players, Event_organizer, Team_manager

class TeamTable(tables.Table):
    class Meta:
        model = Team
        row_attrs = {
            "team_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['team_id','team_name','rating','coach_id','stadium_id','edit', 'delete']
    edit = TemplateColumn(template_name='master/team_update_column.html')
    delete = TemplateColumn(template_name='master/team_delete_column.html')

class CoachTable(tables.Table):
    class Meta:
        model = Coach
        row_attrs = {
            "coach_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['coach_id', 'first_name', 'last_name', 'phone_number', 'edit', 'delete']
    edit = TemplateColumn(template_name='master/coach_update_column.html')
    delete = TemplateColumn(template_name='master/coach_delete_column.html')

class StadiumTable(tables.Table):
    class Meta:
        model = Stadium
        row_attrs = {
            "stadium_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['stadium_id', 'adres', 'number_of_seats','edit', 'delete']
    edit = TemplateColumn(template_name='master/stadium_update_column.html')
    delete = TemplateColumn(template_name='master/stadium_delete_column.html')

class PlayersTable(tables.Table):
    class Meta:
        model = Players
        row_attrs = {
            "coach_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['player_id','team_id','first_name', 'last_name', 'phone_number', 'edit', 'delete']
    edit = TemplateColumn(template_name='master/players_update_column.html')
    delete = TemplateColumn(template_name='master/players_delete_column.html')

class OrganizerTable(tables.Table):
    class Meta:
        model = Event_organizer
        row_attrs = {
            "organizer_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['organizer_id','stadium_id','first_name', 'last_name', 'phone_number', 'edit', 'delete']
    edit = TemplateColumn(template_name='master/organizer_update_column.html')
    delete = TemplateColumn(template_name='master/organizer_delete_column.html')

class TeamManagerTable(tables.Table):
    class Meta:
        model = Team_manager
        row_attrs = {
            "organizer_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['manager_id','team_id','first_name', 'last_name', 'phone_number', 'edit', 'delete']
    edit = TemplateColumn(template_name='master/team_manager_update_column.html')
    delete = TemplateColumn(template_name='master/team_manager_delete_column.html')


