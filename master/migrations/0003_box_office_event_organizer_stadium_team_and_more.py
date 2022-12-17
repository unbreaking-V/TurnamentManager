# Generated by Django 4.1.3 on 2022-12-03 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_alter_coach_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box_office',
            fields=[
                ('window_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_id', models.IntegerField()),
                ('number_of_tickets', models.IntegerField()),
                ('ticket_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_organizer',
            fields=[
                ('organizer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('stadium_id', models.AutoField(primary_key=True, serialize=False)),
                ('adres', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='coach',
            name='coach_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Team_manager',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(null=True)),
                ('team_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='coach_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.coach'),
        ),
        migrations.AddField(
            model_name='team',
            name='stadium_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.stadium'),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_data', models.DateField()),
                ('salary', models.IntegerField()),
                ('manager_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.team_manager')),
                ('organizer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.event_organizer')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(null=True)),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.team')),
            ],
        ),
        migrations.CreateModel(
            name='Match_history',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_score', models.IntegerField()),
                ('match_date', models.DateField()),
                ('stadium_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.stadium')),
                ('team_id', models.ManyToManyField(to='master.team')),
            ],
        ),
        migrations.AddField(
            model_name='event_organizer',
            name='stadium_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.stadium'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(null=True)),
                ('organizer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.event_organizer')),
                ('window_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.box_office')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize_fund', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('expenses', models.IntegerField(null=True)),
                ('profit', models.IntegerField(null=True)),
                ('budget_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='master.event_organizer')),
            ],
        ),
        migrations.AddField(
            model_name='box_office',
            name='stadium_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.stadium'),
        ),
    ]
