from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("view/",views.AllViews,name='view'),
    path("create/", views.AllCreate, name='create'),
    path("team_list/", views.TeamListView, name="team_list"),

]

# Team
urlpatterns += [
    path("delete_team/<int:pk>",views.TeamDelete, name="delete_team"),
    path("update_team/<int:pk>",views.TeamUpdate, name="update_team"),
    path("create/create_team/",views.TeamCreate,  name="create_team"),
]

# Coach
urlpatterns += [
     path("create/create_coach/",views.CoachCreate.as_view(), name="create_coach"),
     path("view/coach_list/", views.CoachListView, name="coach_list"),
]


# Stadium
urlpatterns += [
     path("stadium_list/", views.StadiumListView, name="stadium_list"),
     path("create_stadium/",views.StadiumCreate.as_view(), name="create_stadium"),
]


# Players
urlpatterns += [
     path("players_list/", views.PlayersListView, name="players_list"),
     path("create/create_players/",views.PlayersCreate.as_view(), name="create_players"),
]

# Event_organizer
urlpatterns += [
     path("event_organizer_list/", views.EventOrganizerListView, name="event_organizer_list"),
     path("create_event_organizer/",views.EventOrganizerCreate.as_view(), name="create_event_organizer"),
]


# Team_manager
urlpatterns += [
     path("team_manager_list/", views.TeamManagerListView, name="team_manager_list"),
     path("create_team_manager/",views.TeamManagerCreate.as_view(), name="create_team_manager"),
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


