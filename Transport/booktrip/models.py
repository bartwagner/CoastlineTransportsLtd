from django.db import models

class Vehicle(models.Model):
    number = models.IntegerField()
    sets = models.IntegerField()
    def __str__(self):
        return 'Vehicle: ' + str(self.number) + ' sets: ' + str(self.sets)

class Travel(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    board = models.CharField(max_length=60)
    time_board = models.TimeField()
    destination = models.CharField(max_length=60)
    time_destination = models.TimeField()
    def __str__(self):
        return self.board + ' - ' + str(self.time_board) + ' | ' + self.destination + ' - ' + str(self.time_destination)

class LocalDestination(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.DO_NOTHING)
    local_destination = models.CharField(max_length=60)
    time_destination = models.TimeField()
    def __str__(self):
        return self.local_destination + ' | Time Dest.: ' + str(self.time_destination)
    
class LocalBoard(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.DO_NOTHING)
    local_board = models.CharField(max_length=60)
    time_board = models.TimeField()
    def __str__(self):
        return self.local_board + ' | Time Board: ' + str(self.time_board)
    
class DateTimeTravel(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.DO_NOTHING)
    sets_available = models.IntegerField()
    date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.travel) + ' | Date: ' +str(self.date) + ' | Price: ' + str(self.price) + ' | Sets Available: ' + str(self.sets_available)