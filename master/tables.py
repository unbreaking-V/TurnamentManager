from django_tables2 import tables, TemplateColumn
from .models import Team

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

