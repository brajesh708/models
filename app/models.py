from django.db import models

# Create your models here.
class Student(models.Model):
    Name =models.CharField(max_length=50)
    Email =models.EmailField()
    Contect=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    Re_Password=models.CharField(max_length=10)
    
    def __str__(self):
        return self.Name+' '+self.Email
    class Meta:
        db_table = 'Student'
        # managed = True
        # verbose_name = 'Student'
        verbose_name_plural = 'Student'
        #  yaha oder ke liye kam karta he asending ke liye 
        #  disanding oder ke liye - lagana he
        ordering=['Name']
        
    
    
class Adhar(models.Model):
    Adhar_no=models.IntegerField(unique=True)
    Create_date=models.DateTimeField()
    Create_by=models.CharField(max_length=50)
    def __str__(self):
        return str(self.Adhar_no)
    
    
class Brajesh(models.Model):
    Name =models.CharField(max_length=50)
    Email =models.EmailField()
    city= models.CharField(max_length=20)
    Adhar_no=models.OneToOneField(Adhar,on_delete=models.CASCADE)
    