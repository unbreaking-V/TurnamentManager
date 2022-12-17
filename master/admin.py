from django.contrib import admin
from .models import Coach,Stadium,Team,Players,Event_organizer,Team_manager,Request,Match_history,Budget,Box_office,Employee
# Register your models here.
admin.site.register(Stadium)
admin.site.register(Team)
admin.site.register(Players)
admin.site.register(Event_organizer)
admin.site.register(Team_manager)
admin.site.register(Request)
admin.site.register(Match_history)
admin.site.register(Budget)
admin.site.register(Box_office)
admin.site.register(Employee)

class CoachAdmin(admin.ModelAdmin):
    list_display = ('coach_id','last_name', 'first_name','phone_number')



admin.site.register(Coach, CoachAdmin)
