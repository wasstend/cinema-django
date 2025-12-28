from django.db import models


class Hall(models.Model):
    name = models.CharField('Название зала', max_length=100)
    seats = models.PositiveIntegerField('Количество мест')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField('Название фильма', max_length=200)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Время начала')

    def __str__(self):
        return f'{self.movie} — {self.start_time}'


class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField('Место')
