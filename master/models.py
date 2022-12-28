from django.db import models
from django.urls import reverse

class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.coach_id)


    def get_absolute_url(self):
        return reverse('create_coach')

class Stadium(models.Model):
     stadium_id = models.AutoField(primary_key=True)
     adres = models.CharField(max_length=100)
     number_of_seats = models.IntegerField()

     def __str__(self):
         return str(self.stadium_id)

     def get_absolute_url(self):
        return reverse('create_stadium')


class Team(models.Model):
     team_id = models.AutoField(primary_key=True)
     team_name = models.CharField(max_length=50)
     rating = models.IntegerField()
     coach_id = models.OneToOneField(Coach,on_delete=models.SET_NULL, null=True)
     stadium_id = models.ForeignKey(Stadium,on_delete=models.SET_NULL, null=True)


     def __str__(self):
         return str(self.team_id)

     def get_absolute_url(self):
        return reverse('create_team')


class Players(models.Model):
      player_id = models.AutoField(primary_key=True)
      team_id = models.ForeignKey(Team,on_delete=models.SET_NULL, null=True)
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      phone_number = models.IntegerField(null=True)

      def __str__(self):
          return str(self.player_id)

      def get_absolute_url(self):
        return reverse('create_players')


class Event_organizer(models.Model):
       organizer_id = models.AutoField(primary_key=True)
       stadium_id = models.OneToOneField(Stadium,on_delete=models.SET_NULL, null=True)
       first_name = models.CharField(max_length=50)
       last_name = models.CharField(max_length=50)
       phone_number = models.IntegerField(null=True)

       def __str__(self):
           return str(self.organizer_id)

       def get_absolute_url(self):
            return reverse('create_event_organizer')


class Team_manager(models.Model):
        manager_id = models.AutoField(primary_key=True)
        team_id = models.OneToOneField(Team,on_delete=models.SET_NULL, null=True)
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        phone_number = models.IntegerField(null=True)

        def __str__(self):
            return str(self.manager_id)

        def get_absolute_url(self):
            return reverse('create_team_manager')


class Request(models.Model):
         #DatE not data
         create_data = models.DateField()
         salary = models.IntegerField()
         manager_id = models.ForeignKey(Team_manager,on_delete=models.SET_NULL, null=True)
         organizer_id = models.ForeignKey(Event_organizer,on_delete=models.SET_NULL, null=True)


         def __str__(self):
             return str(self.create_data)

         def get_absolute_url(self):
            return reverse('create_request')


class Match_history(models.Model):
    match_id = models.AutoField(primary_key=True)
    team_id = models.ManyToManyField(Team)
    team_score = models.IntegerField()
    match_date = models.DateField()
    stadium_id = models.ForeignKey(Stadium,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.match_id)

    def get_absolute_url(self):
        return reverse('create_match_history')



class Budget(models.Model):
    budget_id = models.OneToOneField(Event_organizer,on_delete=models.CASCADE)
    prize_fund = models.IntegerField()
    balance = models.IntegerField()
    expenses = models.IntegerField(null=True)
    profit = models.IntegerField(null=True)

    def __str__(self):
        return str(self.budget_id)

    def get_absolute_url(self):
        return reverse('create_budget')



class Box_office(models.Model):
    window_id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField()
    stadium_id = models.ForeignKey(Stadium,on_delete=models.SET_NULL, null=True)
    number_of_tickets = models.IntegerField()
    ticket_price = models.IntegerField()

    def __str__(self):
        return str(self.employee_id)

    def get_absolute_url(self):
        return reverse('create_box_office')


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    organizer_id = models.ForeignKey(Event_organizer,on_delete=models.SET_NULL, null=True)
    window_id = models.ForeignKey(Box_office,on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
           return str(self.employee_id)

    def get_absolute_url(self):
        return reverse('create_employee')



