from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("view/",views.AllViews,name='view'),
    path("create/", views.AllCreate, name='create'),

]

# Team
urlpatterns += [
    path("team_list/", views.TeamListView, name="team_list"),
    path("delete_team/<int:pk>",views.TeamDelete, name="delete_team"),
    path("update_team/<int:pk>",views.TeamUpdate, name="update_team"),
    path("create/create_team/",views.TeamCreate,  name="create_team"),
]

# Coach
urlpatterns += [
    path("coach_list/", views.CoachListView, name="coach_list"),
    path("delete_coach/<int:pk>",views.CoachDelete, name="delete_coach"),
    path("update_coach/<int:pk>",views.CoachUpdate, name="update_coach"),
    path("create/create_coach/",views.CoachCreate,  name="create_coach"),
]


# Stadium
urlpatterns += [
    path("stadium_list/", views.StadiumListView, name="stadium_list"),
    path("delete_stadium/<int:pk>",views.StadiumDelete, name="delete_stadium"),
    path("update_stadium/<int:pk>",views.StadiumUpdate, name="update_stadium"),
    path("create/create_stadium/",views.StadiumCreate,  name="create_stadium"),
]


# Players
urlpatterns += [
    path("players_list/", views.PlayersListView, name="players_list"),
    path("delete_players/<int:pk>",views.PlayersDelete, name="delete_players"),
    path("update_players/<int:pk>",views.PlayersUpdate, name="update_players"),
    path("create/create_players/",views.PlayersCreate,  name="create_players"),
]

# Event_organizer
urlpatterns += [
    path("organizer_list/", views.OrganizerListView, name="organizer_list"),
    path("delete_organizer/<int:pk>",views.OrganizerDelete, name="delete_organizer"),
    path("update_organizer/<int:pk>",views.OrganizerUpdate, name="update_organizer"),
    path("create/create_organizer/",views.OrganizerCreate,  name="create_organizer"),
]


# Team_manager
urlpatterns += [
    path("team_manager_list/", views.TeamManagerListView, name="team_manager_list"),
    path("delete_team_manager/<int:pk>",views.TeamManagerDelete, name="delete_team_manager"),
    path("update_team_manager/<int:pk>",views.TeamManagerUpdate, name="update_team_manager"),
    path("create/create_team_manager/",views.TeamManagerCreate,  name="create_team_manager"),
]


# Request
urlpatterns += [
     path("request_list/", views.RequestListView, name="request_list"),
     path("create_request/",views.RequestCreate.as_view(), name="create_request"),
]


# Match_history
urlpatterns += [
     path("match_history_list/", views.MatchHistoryListView, name="match_history_list"),
     path("create_match_history/",views.MatchHistoryCreate.as_view(), name="create_match_history"),
]


# Budget
urlpatterns += [
     path("budget_list/", views.BudgetListView, name="budget_list"),
     path("create_budget/",views.BudgetCreate.as_view(), name="create_budget"),

]


# Box_office
urlpatterns += [
     path("box_office_list/", views.BoxOfficeListView, name="box_office_list"),
     path("create_box_office/",views.BoxOfficeCreate.as_view(), name="create_box_office"),

]


# Employee
urlpatterns += [
     path("employee_list/", views.EmployeeListView, name="employee_list"),
     path("create_employee/",views.EmployeeCreate.as_view(), name="create_employee"),
]


