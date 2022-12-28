from django_tables2 import tables, TemplateColumn
from .models import Team, Coach, Stadium, Players, Event_organizer, Team_manager, Request, Match_history, Budget, Box_office,Employee

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
            "player_id": lambda record: record.pk
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
            "manager_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['manager_id','team_id','first_name', 'last_name', 'phone_number', 'edit', 'delete']
    edit = TemplateColumn(template_name='master/team_manager_update_column.html')
    delete = TemplateColumn(template_name='master/team_manager_delete_column.html')

class RequestTable(tables.Table):
    class Meta:
        model = Request
        row_attrs = {
            "request_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['request_id','create_date', 'salary', 'manager_id', 'organizer_id','edit', 'delete']
    edit = TemplateColumn(template_name='master/request_update_column.html')
    delete = TemplateColumn(template_name='master/request_delete_column.html')

class MatchTable(tables.Table):
    class Meta:
        model = Match_history
        row_attrs = {
            "match_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = ['match_id', 'team_id', 'team_score', 'match_date', 'stadium_id','edit', 'delete']
    edit = TemplateColumn(template_name='master/match_update_column.html')
    delete = TemplateColumn(template_name='master/match_delete_column.html')

class BudgetTable(tables.Table):
   class Meta:
       model = Budget
       row_attrs = {
           "organizer_id": lambda record: record.pk
        }
       attrs = {'class': "table table-striped thead-dark",
                 'thead' : {'class': 'thead-dark' }}
       fields = ['organizer_id', 'prize_fund', 'balance', 'expenses', 'profit','edit','delete']
   edit = TemplateColumn(template_name='master/budget_update_column.html')
   delete = TemplateColumn(template_name='master/budget_delete_column.html')

class BoxOfficeTable(tables.Table):
  class Meta:
      model = Box_office
      row_attrs = {
          "window_id": lambda record: record.pk
       }
      attrs = {'class': "table table-striped thead-dark",
                'thead' : {'class': 'thead-dark' }}
      fields = ['window_id', 'window_name','stadium_id', 'number_of_tickets', 'ticket_price','edit','delete']
  edit = TemplateColumn(template_name='master/box_office_update_column.html')
  delete = TemplateColumn(template_name='master/box_office_delete_column.html')

class EmployeeTable(tables.Table):
  class Meta:
      model = Employee
      row_attrs = {
          "employee_id": lambda record: record.pk
       }
      attrs = {'class': "table table-striped thead-dark",
                'thead' : {'class': 'thead-dark' }}
      fields = ['employee_id', 'organizer_id', 'window_id','first_name','last_name', 'phone_number','edit','delete']
  edit = TemplateColumn(template_name='master/employee_update_column.html')
  delete = TemplateColumn(template_name='master/employee_delete_column.html')

