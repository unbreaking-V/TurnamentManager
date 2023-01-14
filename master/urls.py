from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=''),
    path("view/",views.AllViews,name='view'),
   # path("view_search/<int:pk>",views.ViewSearch, name = "view_search")
]

# Team
urlpatterns += [
    path("team_list/<int:pk>", views.TeamListView, name="team_list"),
    path("delete_team/<int:pk>",views.TeamDelete, name="delete_team"),
    path("update_team/<int:pk>",views.TeamUpdate, name="update_team"),
    path("create/create_team/",views.TeamCreate,  name="create_team"),
    path("search_team/", views.SearchTeam, name = "search_team"),
]

# Coach
urlpatterns += [
    path("coach_list/<int:pk>", views.CoachListView, name="coach_list"),
    path("delete_coach/<int:pk>",views.CoachDelete, name="delete_coach"),
    path("update_coach/<int:pk>",views.CoachUpdate, name="update_coach"),
    path("create/create_coach/",views.CoachCreate,  name="create_coach"),
    path("search_coach/", views.SearchCoach, name = "search_coach"),
]


# Stadium
urlpatterns += [
    path("stadium_list/<int:pk>", views.StadiumListView, name="stadium_list"),
    path("delete_stadium/<int:pk>",views.StadiumDelete, name="delete_stadium"),
    path("update_stadium/<int:pk>",views.StadiumUpdate, name="update_stadium"),
    path("create/create_stadium/",views.StadiumCreate,  name="create_stadium"),
    path("search_stadium/", views.SearchStadium, name = "search_stadium"),
]


# Players
urlpatterns += [
    path("players_list/<int:pk>", views.PlayersListView, name="players_list"),
    path("delete_players/<int:pk>",views.PlayersDelete, name="delete_players"),
    path("update_players/<int:pk>",views.PlayersUpdate, name="update_players"),
    path("create/create_players/",views.PlayersCreate,  name="create_players"),
    path("search_players/", views.SearchPlayers, name = "search_players"),
]

# Event_organizer
urlpatterns += [
    path("organizer_list/<int:pk>", views.OrganizerListView, name="organizer_list"),
    path("delete_organizer/<int:pk>",views.OrganizerDelete, name="delete_organizer"),
    path("update_organizer/<int:pk>",views.OrganizerUpdate, name="update_organizer"),
    path("create/create_organizer/",views.OrganizerCreate,  name="create_organizer"),
    path("search_organizer/", views.SearchOrganizer, name = "search_organizer"),
]


# Team_manager
urlpatterns += [
    path("team_manager_list/<int:pk>", views.TeamManagerListView, name="team_manager_list"),
    path("delete_team_manager/<int:pk>",views.TeamManagerDelete, name="delete_team_manager"),
    path("update_team_manager/<int:pk>",views.TeamManagerUpdate, name="update_team_manager"),
    path("create/create_team_manager/",views.TeamManagerCreate,  name="create_team_manager"),
    path("search_team_manager/", views.SearchTeamManager, name = "search_team_manager"),
]


# Request
urlpatterns += [
    path("request_list/<int:pk>", views.RequestListView, name="request_list"),
    path("delete_request/<int:pk>",views.RequestDelete, name="delete_request"),
    path("update_request/<int:pk>",views.RequestUpdate, name="update_request"),
    path("create/create_request/",views.RequestCreate,  name="create_request"),
    path("search_request/", views.SearchRequest, name = "search_request"),
]


# Match_history
urlpatterns += [
    path("match_list/<int:pk>", views.MatchListView, name="match_list"),
    path("delete_match/<int:pk>",views.MatchDelete, name="delete_match"),
    path("update_match/<int:pk>",views.MatchUpdate, name="update_match"),
    path("create/create_match/",views.MatchCreate,  name="create_match"),
    path("search_match/", views.SearchMatch, name = "search_match"),
]



# Budget
urlpatterns += [
    path("budget_list/<int:pk>", views.BudgetListView, name="budget_list"),
    path("delete_budget/<int:pk>",views.BudgetDelete, name="delete_budget"),
    path("update_budget/<int:pk>",views.BudgetUpdate, name="update_budget"),
    path("create/create_budget/",views.BudgetCreate,  name="create_budget"),
    path("search_budget/", views.SearchBudget, name = "search_budget"),

]


# Box_office
urlpatterns += [
    path("box_office_list/<int:pk>", views.BoxOfficeListView, name="box_office_list"),
    path("delete_box_office/<int:pk>",views.BoxOfficeDelete, name="delete_box_office"),
    path("update_box_office/<int:pk>",views.BoxOfficeUpdate, name="update_box_office"),
    path("create/create_box_office/",views.BoxOfficeCreate,  name="create_box_office"),
    path("search_box_office/", views.SearchBoxOffice, name = "search_box_office"),
]



# Employee
urlpatterns += [
    path("employee_list/<int:pk>", views.EmployeeListView, name="employee_list"),
    path("delete_employee/<int:pk>",views.EmployeeDelete, name="delete_employee"),
    path("update_employee/<int:pk>",views.EmployeeUpdate, name="update_employee"),
    path("create/create_employee/",views.EmployeeCreate,  name="create_employee"),
    path("search_employee/", views.SearchEmployee, name = "search_employee"),

]


