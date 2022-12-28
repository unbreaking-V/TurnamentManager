from django.db import models
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField
from  django.utils import timezone
from django.urls import reverse


class Coach(models.Model):
    coach_id = models.PositiveIntegerField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.coach_id)


    def get_absolute_url(self):
        return reverse('create_coach')

class Stadium(models.Model):
     stadium_id = models.PositiveIntegerField(primary_key=True,unique=True)
     adres = models.CharField(max_length=100, unique = True)
     number_of_seats = models.PositiveIntegerField()

     def __str__(self):
         return str(self.stadium_id)

     def get_absolute_url(self):
        return reverse('create_stadium')


class Team(models.Model):
     team_id = models.PositiveIntegerField(primary_key=True,unique=True)
     team_name = models.CharField(max_length=50,unique = True)
     rating = models.PositiveIntegerField(unique = True)
     coach_id = models.OneToOneField(Coach,on_delete=models.SET_NULL, null=True)
     stadium_id = models.ForeignKey(Stadium,on_delete=models.SET_NULL, null=True)


     def __str__(self):
         return str(self.team_id)

     def get_absolute_url(self):
        return reverse('create_team')


class Players(models.Model):
      player_id = models.PositiveIntegerField(primary_key=True,unique=True)
      team_id = models.ForeignKey(Team,on_delete=models.SET_NULL, null=True)
      first_name = models.CharField(max_length=30)
      last_name = models.CharField(max_length=30)
      phone_number = PhoneNumberField(null=False, blank=False, unique=True)

      def __str__(self):
          return str(self.player_id)

      def get_absolute_url(self):
        return reverse('create_players')


class Event_organizer(models.Model):
       organizer_id = models.PositiveIntegerField(primary_key=True,unique=True)
       stadium_id = models.OneToOneField(Stadium,on_delete=models.SET_NULL, null=True)
       first_name = models.CharField(max_length=30)
       last_name = models.CharField(max_length=30)
       phone_number = PhoneNumberField(null=False, blank=False, unique=True)

       def __str__(self):
           return str(self.organizer_id)

       def get_absolute_url(self):
            return reverse('create_event_organizer')


class Team_manager(models.Model):
        manager_id = models.PositiveIntegerField(primary_key=True,unique=True)
        team_id = models.OneToOneField(Team,on_delete=models.SET_NULL, null=True)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        phone_number = PhoneNumberField(null=False, blank=False, unique=True)

        def __str__(self):
            return str(self.manager_id)

        def get_absolute_url(self):
            return reverse('create_team_manager')


class Request(models.Model):
         request_id = models.PositiveIntegerField(primary_key=True,unique=True)
         create_date = models.DateField()
         salary = models.PositiveIntegerField()
         manager_id = models.ForeignKey(Team_manager,on_delete=models.SET_NULL, null=True)
         organizer_id = models.ForeignKey(Event_organizer,on_delete=models.SET_NULL, null=True)


         def __str__(self):
             return str(self.create_data)

         def get_absolute_url(self):
            return reverse('create_request')


class Match_history(models.Model):
    match_id = models.PositiveIntegerField(primary_key=True,unique=True)
    team_id = models.ManyToManyField(Team)
    team_score = models.PositiveIntegerField()
    match_date = models.DateField()
    stadium_id = models.ForeignKey(Stadium,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.match_id)

    def get_absolute_url(self):
        return reverse('create_match_history')



class Budget(models.Model):
    organizer_id = models.OneToOneField(Event_organizer,on_delete=models.CASCADE,primary_key=True)
    prize_fund = models.PositiveIntegerField()
    balance = models.PositiveIntegerField()
    expenses = models.PositiveIntegerField(null=True)
    profit = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.organizer_id)

    def get_absolute_url(self):
        return reverse('create_budget')



class Box_office(models.Model):
    window_id = models.PositiveIntegerField(primary_key=True,unique=True)
    window_name = models.CharField(max_length=30,unique=True)
    stadium_id = models.ForeignKey(Stadium,on_delete=models.SET_NULL, null=True)
    number_of_tickets = models.PositiveIntegerField()
    ticket_price = models.PositiveIntegerField()

    def __str__(self):
        return str(self.window_id)

    def get_absolute_url(self):
        return reverse('create_box_office')


class Employee(models.Model):
    employee_id = models.PositiveIntegerField(primary_key=True,unique=True)
    organizer_id = models.ForeignKey(Event_organizer,on_delete=models.SET_NULL, null=True)
    window_id = models.ForeignKey(Box_office,on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
           return str(self.employee_id)

    def get_absolute_url(self):
        return reverse('create_employee')



