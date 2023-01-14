from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Coach,Stadium,Team,Players,Event_organizer,Team_manager,Request,Match_history,Budget,Box_office,Employee

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TeamForm, CoachForm, StadiumForm, PlayersForm, OrganizerForm, TeamManagerForm,RequestForm,MatchForm,BudgetForm,BoxOfficeForm,EmployeeForm
from .tables import TeamTable, CoachTable, StadiumTable, PlayersTable, OrganizerTable, TeamManagerTable, RequestTable, MatchTable,BudgetTable,BoxOfficeTable,EmployeeTable

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

def TeamListView(response,pk):
    if pk:
        table = TeamTable(Team.objects.filter(team_id = pk))
    else:
        table = TeamTable(Team.objects.all())
    return render(response, "master/team_list.html", {
        "table": table})

def SearchTeam(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/team_list/0')
        teams = Team.objects.filter(team_name__contains=searched)
        return render(response, 'master/search_team.html', {'searched':searched,"teams":teams})

def TeamCreate(response):
    form = TeamForm()
    if response.method == "POST":
        form = TeamForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/team_list/0')

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
             return redirect('/team_list/0')

    return  render(response, 'master/team_form.html', contex)

def TeamDelete(response,pk):
    team = Team.objects.get(team_id=pk)
    if response.method == "POST":
        team.delete()
        return redirect("/team_list/0")
    contex = {"item":team}

    return render(response,'master/team_delete.html', contex)



#-------------------------------------------------------------
                         #COACH

def CoachListView(response,pk):
    if pk:
        table = CoachTable(Coach.objects.filter(coach_id = pk))
    else:
        table = CoachTable(Coach.objects.all())

    return render(response, "master/coach_list.html", {"table": table})

def SearchCoach(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/coach_list/0')
        coachs = Coach.objects.filter(last_name__contains=searched)
        return render(response, 'master/search_coach.html', {'searched':searched,"coachs":coachs})

def CoachCreate(response):
    form = CoachForm()
    if response.method == "POST":
        form = CoachForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/coach_list/0')

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
             return redirect('/coach_list/0')

    return  render(response, 'master/coach_form.html', contex)

def CoachDelete(response,pk):
    coach = Coach.objects.get(coach_id=pk)
    if response.method == "POST":
        coach.delete()
        return redirect("/coach_list/0")
    contex = {"item":coach}

    return render(response,'master/coach_delete.html', contex)

#-------------------------------------------------------------
                         #STADIUM

def StadiumListView(response,pk):
    if pk:
        table = StadiumTable(Stadium.objects.filter(stadium_id = pk))
    else:
        table = StadiumTable(Stadium.objects.all())

    return render(response, "master/stadium_list.html", {"table": table})

def SearchStadium(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/stadium_list/0')
        stadiums = Stadium.objects.filter(adres__contains=searched)
        return render(response, 'master/search_stadium.html', {'searched':searched,"stadiums":stadiums})

def StadiumCreate(response):
    form = StadiumForm()
    if response.method == "POST":
        form = StadiumForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/stadium_list/0')

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
             return redirect('/stadium_list/0' )

    return  render(response, 'master/stadium_form.html', contex)

def StadiumDelete(response,pk):
    stadium = Stadium.objects.get(stadium_id=pk)
    if response.method == "POST":
        stadium.delete()
        return redirect("/stadium_list/0")
    contex = {"item": stadium}

    return render(response,'master/stadium_delete.html', contex)


#-------------------------------------------------------------
                         #PLAYERS
def PlayersListView(response,pk):
    if pk:
        table = PlayersTable(Players.objects.filter(player_id = pk))
    else:
        table = PlayersTable(Players.objects.all())

    return render(response, "master/players_list.html", {"table": table})

def SearchPlayers(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/players_list/0')
        players = Players.objects.filter(last_name__contains=searched)
        return render(response, 'master/search_players.html', {'searched':searched,"players":players})

def PlayersCreate(response):
    form = PlayersForm()
    if response.method == "POST":
        form = PlayersForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/players_list/0')

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
             return redirect('/players_list/0')

    return  render(response, 'master/players_form.html', contex)

def PlayersDelete(response,pk):
    players = Players.objects.get(player_id=pk)
    if response.method == "POST":
        players.delete()
        return redirect("/players_list/0")
    contex = {"item": players}

    return render(response,'master/players_delete.html', contex)

#-------------------------------------------------------------
                    #EVENT_ORGANIZER
def OrganizerListView(response,pk):
    if pk:
        table = OrganizerTable(Event_organizer.objects.filter(organizer_id = pk))
    else:
        table = OrganizerTable(Event_organizer.objects.all())

    return render(response, "master/organizer_list.html",{"table": table})

def SearchOrganizer(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/organizer_list/0')
        organizers = Event_organizer.objects.filter(last_name__contains=searched)
        return render(response, 'master/search_organizer.html', {'searched':searched,"organizers":organizers})

def OrganizerCreate(response):
    form = OrganizerForm()
    if response.method == "POST":
        form = OrganizerForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/organizer_list/0')

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
             return redirect('/organizer_list/0')

    return  render(response, 'master/organizer_form.html', contex)

def OrganizerDelete(response,pk):
    organizer = Event_organizer.objects.get(organizer_id=pk)
    if response.method == "POST":
        organizer.delete()
        return redirect("/organizer_list/0")
    contex = {"item": organizer}

    return render(response,'master/organizer_delete.html', contex)


#-------------------------------------------------------------
                    #TEAM_MANAGER

def TeamManagerListView(response,pk):
    if pk:
        table = TeamManagerTable(Team_manager.objects.filter(manager_id = pk))
    else:
        table = TeamManagerTable(Team_manager.objects.all())

    return render(response, "master/team_manager_list.html", {"table": table})

def SearchTeamManager(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/team_manager_list/0')
        managers = Team_manager.objects.filter(last_name__contains=searched)
        return render(response, 'master/search_team_manager.html', {'searched':searched,"managers": managers})

def TeamManagerCreate(response):
    form = TeamManagerForm()
    if response.method == "POST":
        form = TeamManagerForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/team_manager_list/0')

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
             return redirect('/team_manager_list/0')

    return  render(response, 'master/team_manager_form.html', contex)

def TeamManagerDelete(response,pk):
    manager = Team_manager.objects.get(manager_id=pk)
    if response.method == "POST":
        manager.delete()
        return redirect("/team_manager_list/0")
    contex = {"item": manager}

    return render(response,'master/team_manager_delete.html', contex)



#-------------------------------------------------------------
                        #REQUEST

def RequestListView(response,pk):
    if pk:
        table = RequestTable(Request.objects.filter(request_id = pk))
    else:
        table = RequestTable(Request.objects.all())

    return render(response, "master/request_list.html", {"table": table})

def SearchRequest(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/request_list/0')
        requests = Request.objects.filter(create_date__contains=searched)
        return render(response, 'master/search_request.html', {'searched':searched,"requests": requests})


def RequestCreate(response):
    form = RequestForm()
    if response.method == "POST":
        form = RequestForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/request_list/0')

    contex = {'form':form}
    return  render(response, 'master/request_form.html', contex)

def RequestUpdate(response,pk):
    request = Request.objects.get(request_id=pk)
    form = RequestForm(instance=request)
    contex = {'form':form}

    if response.method == "POST":
         form = RequestForm(response.POST, instance=request)
         if form.is_valid():
             form.save()
             return redirect('/request_list/0')

    return  render(response, 'master/request_form.html', contex)

def RequestDelete(response,pk):
    request = Request.objects.get(requsr_id=pk)
    if response.method == "POST":
        request.delete()
        return redirect("/request_list/0")
    contex = {"item": request}

    return render(response,'master/request_delete.html', contex)

#-------------------------------------------------------------
                         #MATCH_HISTORY

def MatchListView(response,pk):
    if pk:
        table = MatchTable(Match_history.objects.filter(match_id = pk))
    else:
        table = MatchTable(Match_history.objects.all())

    return render(response, "master/match_list.html", {"table": table})

def SearchMatch(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/match_list/0')
        matchs = Match_history.objects.filter(match_date__contains=searched)
        return render(response, 'master/search_match.html', {'searched':searched,"matchs": matchs})


def MatchCreate(response):
    form = MatchForm()
    if response.method == "POST":
        form = MatchForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/match_list/0')

    contex = {'form':form}
    return  render(response, 'master/match_form.html', contex)

def MatchUpdate(response,pk):
    match = Match_history.objects.get(match_id=pk)
    form = MatchForm(instance=match)
    contex = {'form':form}

    if response.method == "POST":
         form = MatchForm(response.POST, instance=match)
         if form.is_valid():
             form.save()
             return redirect('/match_list/0')

    return  render(response, 'master/match_form.html', contex)

def MatchDelete(response,pk):
    match = Match_history.objects.get(match_id=pk)
    if response.method == "POST":
        match.delete()
        return redirect("/match_list/0")
    contex = {"item": match}

    return render(response,'master/match_delete.html', contex)


#-------------------------------------------------------------
                         #BUDGET

def BudgetListView(response,pk):
    if pk:
        table = BudgetTable(Budget.objects.filter(organizer_id = pk))
    else:
        table = BudgetTable(Budget.objects.all())

    return render(response, "master/budget_list.html", {"table": table})

def SearchBudget(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/budget_list/0')
        budgets = Budget.objects.filter(prize_fund__contains=searched)
        return render(response, 'master/search_budget.html', {'searched':searched,"budgets": budgets})

def BudgetCreate(response):
    form = BudgetForm()
    if response.method == "POST":
        form = BudgetForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/budget_list/0')

    contex = {'form':form}
    return  render(response, 'master/budget_form.html', contex)

def BudgetUpdate(response,pk):
    budget = Budget.objects.get(organizer_id=pk)
    form = BudgetForm(instance=budget)
    contex = {'form':form}

    if response.method == "POST":
         form = BudgetForm(response.POST, instance=budget)
         if form.is_valid():
             form.save()
             return redirect('/budget_list/0')

    return  render(response, 'master/budget_form.html', contex)

def BudgetDelete(response,pk):
    budget = Budget.objects.get(organizer_id=pk)
    if response.method == "POST":
        budget.delete()
        return redirect("/budget_list/0")
    contex = {"item": budget}

    return render(response,'master/budget_delete.html', contex)


#-------------------------------------------------------------
                         #BOX_OFFICE
def BoxOfficeListView(response,pk):
    if pk:
        table = BoxOfficeTable(Box_office.objects.filter(window_id = pk))
    else:
        table = BoxOfficeTable(Box_office.objects.all())

    return render(response, "master/box_office_list.html", {"table": table})

def SearchBoxOffice(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/box_office_list/0')
        offices = Box_office.objects.filter(window_id__contains=searched)
        return render(response, 'master/search_box_office.html', {'searched':searched,"offices": offices})

def BoxOfficeCreate(response):
    form = BoxOfficeForm()
    if response.method == "POST":
        form = BoxOfficeForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/box_office_list/0')

    contex = {'form':form}
    return  render(response, 'master/box_office_form.html', contex)

def BoxOfficeUpdate(response,pk):
    office = Box_office.objects.get(window_id=pk)
    form = BoxOfficeForm(instance=office)
    contex = {'form':form}

    if response.method == "POST":
         form = BoxOfficeForm(response.POST, instance=office)
         if form.is_valid():
             form.save()
             return redirect('/box_office_list/0')

    return  render(response, 'master/box_office_form.html', contex)

def BoxOfficeDelete(response,pk):
    office = Box_office.objects.get(window_id=pk)
    if response.method == "POST":
        office.delete()
        return redirect("/box_office_list/0")
    contex = {"item": office}

    return render(response,'master/box_office_delete.html', contex)



#-------------------------------------------------------------
                         #EMPLOYEE

def EmployeeListView(response,pk):
    if pk:
        table = EmployeeTable(Employee.objects.filter(employee_id = pk))
    else:
        table = EmployeeTable(Employee.objects.all())

    return render(response, "master/employee_list.html", {"table": table})

def SearchEmployee(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched == "":
            return redirect('/employee_list/0')
        employees = Employee.objects.filter(last_name__contains=searched)
        return render(response, 'master/search_employee.html', {'searched':searched,"employees": employees})

def EmployeeCreate(response):
    form = EmployeeForm()
    if response.method == "POST":
        form = EmployeeForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/employee_list/0')

    contex = {'form':form}
    return  render(response, 'master/employee_form.html', contex)

def EmployeeUpdate(response,pk):
    employee = Employee.objects.get(employee_id=pk)
    form = EmployeeForm(instance=employee)
    contex = {'form':form}

    if response.method == "POST":
         form = EmployeeForm(response.POST, instance=employee)
         if form.is_valid():
             form.save()
             return redirect('/employee_list/0')

    return  render(response, 'master/employee_form.html', contex)

def EmployeeDelete(response,pk):
    employee = Employee.objects.get(employee_id=pk)
    if response.method == "POST":
        employee.delete()
        return redirect("/employee_list/0")
    contex = {"item": employee}

    return render(response,'master/employee_delete.html', contex)


