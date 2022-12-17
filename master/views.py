from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Coach,Stadium,Team,Players,Event_organizer,Team_manager,Request,Match_history,Budget,Box_office,Employee

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TeamForm
from .tables import TeamTable
def home(response):
    num_team = Team.objects.all().count()
    team_name = [elem for elem in list(Team.objects.all().values_list('team_name', flat=True))]
    return render(response, "master/home.html", {"num_team":num_team,"team_name":team_name})

def AllViews(response):
    return render(response, 'master/all_views.html')

def AllCreate(response):
     return render(response, 'master/all_create.html')

def AllUpdate(response):
    return render(response,"master/all_update.html")
#-------------------------------------------------------------
                        #TEAM


def TeamListView(response,pk):
    team = get_object_or_404(Team, team_id=pk)
    table = TeamTable(Team.objects.all())
    return render(response, "master/team_list.html", {
        "table": table, "team":team})

#def TeamListView(response):
#    team_list = Team.objects.all()
#    return render(response, 'master/team_list.html', locals())

def TeamCreate(response):

    form = TeamForm()
    if response.method == 'POST':
        form = TeamForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('create/')

    contex = {'form':form}
    return  render(response, 'master/team_form.html', contex)


def TeamUpdate(response,pk):
    team = Team.objects.get(team_id=pk)
    form = TeamForm(instance=team)
    contex = {'form':form}

    if response.method == 'POST':
         form = TeamForm(response.POST)
         if form.is_valid():
             form.save()
             return redirect('home/')



    return  render(response, 'master/team_form.html', contex)

def TeamDelete(response,pk):
    team = Team.objects.get(team_id=pk)
    if response.method == "POST":
        team.delete()
        return redirect("/home")
    contex = {"item":team}

    return render(response,'master/team_delete.html', contex)

#class TeamCreate(CreateView):
#    model = Team
#    fields = ['team_id', 'team_name', 'rating', 'coach_id','stadium_id']


#class TeamUpdate(UpdateView):
#    model = Team
#    fields = '__all__'


#-------------------------------------------------------------
                         #COACH
def CoachListView(response):
     coach_list = Coach.objects.all()
     return render(response, 'master/coach_list.html', locals())

class CoachCreate(CreateView):
     model = Coach
     fields = ['coach_id', 'first_name', 'last_name', 'phone_number']

class CoachUpdate(UpdateView):
    model = Coach
    fields = ['coach_id', 'first_name', 'last_name', 'phone_number']


#-------------------------------------------------------------
                         #Stadium
def StadiumListView(response):
     stadium_list = Stadium.objects.all()
     return render(response, 'master/stadium_list.html', locals())

class StadiumCreate(CreateView):
     model = Stadium
     fields = ['stadium_id', 'adres', 'number_of_seats']


#-------------------------------------------------------------
                         #Players
def PlayersListView(response):
     players_list = Players.objects.all()
     return render(response, 'master/players_list.html', locals())

class PlayersCreate(CreateView):
     model = Players
     fields = ['player_id','team_id','first_name', 'last_name', 'phone_number']


#-------------------------------------------------------------
                    #EVENT_ORGANIZER
def EventOrganizerListView(response):
     event_organizer_list = Event_organizer.objects.all()
     return render(response, 'master/event_organizer_list.html', locals())

class EventOrganizerCreate(CreateView):
     model = Event_organizer
     fields = ['organizer_id','stadium_id','first_name', 'last_name', 'phone_number']


#-------------------------------------------------------------
                    #TEAM_MANAGER
def TeamManagerListView(response):
     team_manager_list = Team_manager.objects.all()
     return render(response, 'master/team_manager_list.html', locals())

class TeamManagerCreate(CreateView):
     model = Team_manager
     fields = ['manager_id','team_id','first_name', 'last_name', 'phone_number']


#-------------------------------------------------------------
                        #REQUEST
def RequestListView(response):
     request_list = Request.objects.all()
     return render(response, 'master/request_list.html', locals())

class RequestCreate(CreateView):
     model = Request
     fields = ['create_data', 'salary', 'manager_id', 'organizer_id']

#-------------------------------------------------------------
                         #MATCH_HISTORY
def MatchHistoryListView(response):
     match_history_list = Match_history.objects.all()
     return render(response, 'master/match_history_list.html', locals())

class MatchHistoryCreate(CreateView):
     model = Match_history
     fields = ['match_id', 'team_id', 'team_score', 'match_date', 'stadium_id']

#-------------------------------------------------------------
                         #BUDGET
def BudgetListView(response):
     budget_list = Budget.objects.all()
     return render(response, 'master/budget_list.html', locals())

class BudgetCreate(CreateView):
     model = Budget
     fields = ['budget_id', 'prize_fund', 'balance', 'expenses', 'profit']

#-------------------------------------------------------------
                         #BOX_OFFICE
def BoxOfficeListView(response):
     box_office_list = Box_office.objects.all()
     return render(response, 'master/box_office_list.html', locals())

class BoxOfficeCreate(CreateView):
     model = Box_office
     fields = ['window_id', 'employee_id', 'stadium_id', 'number_of_tickets', 'ticket_price']

#-------------------------------------------------------------
                         #EMPLOYEE
def EmployeeListView(response):
     employee_list = Employee.objects.all()
     return render(response, 'master/employee_list.html', locals())

class EmployeeCreate(CreateView):
     model = Employee
     fields = ['employee_id', 'organizer_id', 'window_id','first_name','last_name', 'phone_number']


