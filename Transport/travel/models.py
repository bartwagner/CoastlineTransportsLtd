from django.db import models

class Vehicle(models.Model):
    number = models.IntegerField()
    sets = models.IntegerField()
    def __str__(self):
        return self.number

class Travel(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    board = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.number
    
class LocalBoard(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.DO_NOTHING)
    local_board = models.CharField(max_length=60)
    time_board = models.TimeField()
    def __str__(self):
        return self.local_board
    
class LocalDestination(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.DO_NOTHING)
    local_destination = models.CharField(max_length=60)
    time_destination = models.TimeField()
    def __str__(self):
        return self.local_destination