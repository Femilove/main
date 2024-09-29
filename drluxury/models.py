from django.db import models

# Create your models here.

# creating a class of table in db for views to know what type of info to be stored


class Destination(models.Model):

    #    id: int
    name = models.CharField(max_length=100)
    nametype = models.CharField(max_length=100)
    discountName = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    actualPrice = models.IntegerField()
    val = models.IntegerField()


class Destination2(models.Model):

    #    id: int
    name = models.CharField(max_length=100)
    nametype = models.CharField(max_length=100)
    discountName = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    actualPrice = models.IntegerField()
    val = models.IntegerField()


class Destination3(models.Model):

    #    id: int
    name = models.CharField(max_length=100)
    nametype = models.CharField(max_length=100)
    discountName = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    actualPrice = models.IntegerField()
    val = models.IntegerField()


class Destination4(models.Model):

    #    id: int
    name = models.CharField(max_length=100)
    nametype = models.CharField(max_length=100)
    discountName = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    actualPrice = models.IntegerField()
    val = models.IntegerField()


class Destination5(models.Model):

    #    id: int
    name = models.CharField(max_length=100)
    nametype = models.CharField(max_length=100)
    discountName = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    actualPrice = models.IntegerField()
    val = models.IntegerField()


class Destination6(models.Model):

    #    id: int
    name = models.CharField(max_length=100)
    nametype = models.CharField(max_length=100)
    discountName = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    actualPrice = models.IntegerField()
    val = models.IntegerField()


class Destination7(models.Model):

    #    id: int
    name = models.CharField(max_length=100)
    nametype = models.CharField(max_length=100)
    discountName = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    actualPrice = models.IntegerField()
    val = models.IntegerField()
