from django_tables2 import tables, TemplateColumn
from .models import Team
from django_tables2.utils import A  # alias for Accessor

class TeamTable(tables.Table):
    class Meta:
         model = Team
         attrs = {'class': 'table table-sm'}
         fields = ['team_id','team_name','rating','coach_id','stadium_id','edit', 'delete']
    edit = TemplateColumn(template_name='master/team_update_column.html')
    delete = TemplateColumn(template_name='master/team_delete_column.html')

