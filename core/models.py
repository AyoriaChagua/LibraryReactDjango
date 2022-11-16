from django.db import models

# Create your models here.
class User(models.Model):
    numUser = models.IntegerField()
    nif = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Autor(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    code = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    numPages = models.SmallIntegerField()
    
    def __str__(self):
        return self.title

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    loanDate = models.DateTimeField('loan date')
    returnDate = models.DateTimeField('return date')


