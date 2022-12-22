from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Coach,Stadium,Team,Players,Event_organizer,Team_manager,Request,Match_history,Budget,Box_office,Employee

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TeamForm, CoachForm, StadiumForm, PlayersForm, OrganizerForm, TeamManagerForm
from .tables import TeamTable, CoachTable, StadiumTable, PlayersTable, OrganizerTable, TeamManagerTable
def home(response):
    num_team = Team.objects.all().count()
    team_name = [elem for elem in list(Team.objects.all().values_list('team_name', flat=True))]
    return render(response, "master/home.html", {"num_team":num_team,"team_name":team_name})

def AllViews(response):
    return render(response, 'master/all_views.html')

def AllCreate(response):
     return render(response, 'master/all_create.html')
#-------------------------------------------------------------
                        #TEAM

def TeamListView(response):
    table = TeamTable(Team.objects.all())
    return render(response, "master/team_list.html", {
        "table": table})

def TeamCreate(response):
    form = TeamForm()
    if response.method == "POST":
        form = TeamForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/view')

    contex = {'form':form}
    return  render(response, 'master/team_form.html', contex)


def TeamUpdate(response,pk):
    team = Team.objects.get(team_id=pk)
    form = TeamForm(instance=team)
    contex = {'form':form}

    if response.method == "POST":
         form = TeamForm(response.POST, instance=team)
         if form.is_valid():
             form.save()
             return redirect('/view/')

    return  render(response, 'master/team_form.html', contex)

def TeamDelete(response,pk):
    team = Team.objects.get(team_id=pk)
    if response.method == "POST":
        team.delete()
        return redirect("/home")
    contex = {"item":team}

    return render(response,'master/team_delete.html', contex)
#-------------------------------------------------------------
                         #COACH

def CoachListView(response):
    table = CoachTable(Coach.objects.all())
    return render(response, "master/coach_list.html", {
        "table": table})

def CoachCreate(response):
    form = CoachForm()
    if response.method == "POST":
        form = CoachForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/coach_list')

    contex = {'form':form}
    return  render(response, 'master/coach_form.html', contex)


def CoachUpdate(response,pk):
    coach = Coach.objects.get(coach_id=pk)
    form = CoachForm(instance=coach)
    contex = {'form':form}

    if response.method == "POST":
         form = CoachForm(response.POST, instance=coach)
         if form.is_valid():
             form.save()
             return redirect('/coach_list')

    return  render(response, 'master/coach_form.html', contex)

def CoachDelete(response,pk):
    coach = Coach.objects.get(coach_id=pk)
    if response.method == "POST":
        coach.delete()
        return redirect("/coach_list")
    contex = {"item":coach}

    return render(response,'master/coach_delete.html', contex)

#-------------------------------------------------------------
                         #STADIUM

def StadiumListView(response):
    table = StadiumTable(Stadium.objects.all())
    return render(response, "master/stadium_list.html", {
        "table": table})

def StadiumCreate(response):
    form = StadiumForm()
    if response.method == "POST":
        form = StadiumForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/stadium_list')

    contex = {'form':form}
    return  render(response, 'master/stadium_form.html', contex)

def StadiumUpdate(response,pk):
    stadium = Stadium.objects.get(stadium_id=pk)
    form = StadiumForm(instance=stadium)
    contex = {'form':form}

    if response.method == "POST":
         form = StadiumForm(response.POST, instance=stadium)
         if form.is_valid():
             form.save()
             return redirect('/stadium_list')

    return  render(response, 'master/stadium_form.html', contex)

def StadiumDelete(response,pk):
    stadium = Stadium.objects.get(stadium_id=pk)
    if response.method == "POST":
        stadium.delete()
        return redirect("/stadium_list")
    contex = {"item": stadium}

    return render(response,'master/stadium_delete.html', contex)


#-------------------------------------------------------------
                         #PLAYERS

def PlayersListView(response):
    table = PlayersTable(Players.objects.all())
    return render(response, "master/players_list.html", {
        "table": table})

def PlayersCreate(response):
    form = PlayersForm()
    if response.method == "POST":
        form = PlayersForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/players_list')

    contex = {'form':form}
    return  render(response, 'master/players_form.html', contex)

def PlayersUpdate(response,pk):
    players = Players.objects.get(player_id=pk)
    form = PlayersForm(instance=players)
    contex = {'form':form}

    if response.method == "POST":
         form = PlayersForm(response.POST, instance=players)
         if form.is_valid():
             form.save()
             return redirect('/players_list')

    return  render(response, 'master/players_form.html', contex)

def PlayersDelete(response,pk):
    players = Players.objects.get(player_id=pk)
    if response.method == "POST":
        players.delete()
        return redirect("/players_list")
    contex = {"item": players}

    return render(response,'master/players_delete.html', contex)

#-------------------------------------------------------------
                    #EVENT_ORGANIZER

def OrganizerListView(response):
    table = OrganizerTable(Event_organizer.objects.all())
    return render(response, "master/organizer_list.html", {
        "table": table})

def OrganizerCreate(response):
    form = OrganizerForm()
    if response.method == "POST":
        form = OrganizerForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/organizer_list')

    contex = {'form':form}
    return  render(response, 'master/organizer_form.html', contex)

def OrganizerUpdate(response,pk):
    organizer = Event_organizer.objects.get(organizer_id=pk)
    form = OrganizerForm(instance=organizer)
    contex = {'form':form}

    if response.method == "POST":
         form = OrganizerForm(response.POST, instance=organizer)
         if form.is_valid():
             form.save()
             return redirect('/organizer_list')

    return  render(response, 'master/organizer_form.html', contex)

def OrganizerDelete(response,pk):
    organizer = Event_organizer.objects.get(organizer_id=pk)
    if response.method == "POST":
        organizer.delete()
        return redirect("/organizer_list")
    contex = {"item": organizer}

    return render(response,'master/organizer_delete.html', contex)


#-------------------------------------------------------------
                    #TEAM_MANAGER

def TeamManagerListView(response):
    table = TeamManagerTable(Team_manager.objects.all())
    return render(response, "master/team_manager_list.html", {
        "table": table})

def TeamManagerCreate(response):
    form = TeamManagerForm()
    if response.method == "POST":
        form = TeamManagerForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/team_manager_list')

    contex = {'form':form}
    return  render(response, 'master/team_manager_form.html', contex)

def TeamManagerUpdate(response,pk):
    manager = Team_manager.objects.get(manager_id=pk)
    form = TeamManagerForm(instance=manager)
    contex = {'form':form}

    if response.method == "POST":
         form = TeamManagerForm(response.POST, instance=manager)
         if form.is_valid():
             form.save()
             return redirect('/team_manager_list')

    return  render(response, 'master/team_manager_form.html', contex)

def TeamManagerDelete(response,pk):
    manager = Team_manager.objects.get(manager_id=pk)
    if response.method == "POST":
        manager.delete()
        return redirect("/team_manager_list")
    contex = {"item": manager}

    return render(response,'master/team_manager_delete.html', contex)



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


