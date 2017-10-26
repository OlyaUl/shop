from django.db import models
from datetime import datetime


class CarModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)


class Color(models.Model):
    title = models.CharField(max_length=30)
    code_color = models.CharField(max_length=20)


class Specifications(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    scope = models.IntegerField()
    power = models.IntegerField()
    FULL = '1'
    FRONT = '2'
    REAR = '3'
    CARDAN = '4'
    BELT = '5'
    CHAIN = '6'
    DRIVE_TYPE = (
        (FULL, 'Full'),
        (FRONT, 'Front'),
        (REAR, 'Rear'),
        (CARDAN, 'Cardan'),
        (BELT, 'Belt'),
        (CHAIN, 'Chain'),
    )
    drive_type = models.CharField(max_length=2,
                                  choices=DRIVE_TYPE,
                                  default=FULL)
    PETROL = 'P'
    DIESEL = 'D'
    GAS = 'G'
    GAS_PETROL = 'GP'
    OTHER = 'O'
    FUEL = (
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel'),
        (GAS, 'Gas'),
        (GAS_PETROL, 'Gas/Petrol'),
        (OTHER, 'Senior'),
    )
    petrol = models.CharField(max_length=2,
                              choices=FUEL,
                              default=PETROL)


class Image(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField()
    main_image = models.BooleanField(default=False)


class Car(models.Model):
    title = models.CharField(max_length=30)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    specifications = models.ForeignKey(Specifications, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    year = models.IntegerField()


























class Book(models.Model):
    title = models.CharField(max_length=30)
    year = models.DateField()
    description = models.CharField(max_length=1000)
    authors = models.ManyToManyField('Author')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='all_img', blank=True)
    prev = models.ImageField(upload_to='all_img', blank=True)

    def __str__(self):
        return '{0}'.format(self.title)


class Rating(models.Model):
    like = models.IntegerField()
    dislike = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return '{0}'.format(self.title)


class Author(models.Model):
    name = models.CharField(max_length=30)
    date_bir = models.DateField()
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return '{0}'.format(self.name)
        # return '{0} {1}'.format(self.authors, self.category)



