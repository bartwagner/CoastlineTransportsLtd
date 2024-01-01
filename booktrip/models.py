from django.db import models

class Vehicle(models.Model):
    number = models.IntegerField()
    sets = models.IntegerField()
    def __str__(self):
        return 'Vehicle: ' + str(self.number) + ' sets: ' + str(self.sets)

class TravelBoard(models.Model):
    board = models.CharField(max_length=60)
    time_board = models.TimeField()
    def __str__(self):
        return 'Board: ' + self.board + ' | Time Board: ' + str(self.time_board)

class TravelDestination(models.Model):
    destination = models.CharField(max_length=60)
    time_destination = models.TimeField()
    def __str__(self):
        return 'Destionation: ' + self.destination + ' | Time Destination: ' + str(self.time_destination)

class Travel(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    travelboard = models.ForeignKey(TravelBoard, on_delete=models.DO_NOTHING)
    traveldestination = models.ForeignKey(TravelDestination, on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.travelboard) + ' - ' + str(self.traveldestination)

class LocalDestination(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.DO_NOTHING)
    local_destination = models.CharField(max_length=60)
    time_destination = models.TimeField()
    def __str__(self):
        return str(self.local_destination) + ' | Time Dest.: ' + str(self.time_destination)
    
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