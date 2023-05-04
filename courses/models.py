from django.db import models



class Instructor(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='instructor/',default='default.png')
    bio = models.TextField(max_length=1000,null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
      return self.name

class Courses(models.Model):
    instructor = models.ForeignKey(Instructor,related_name='inst_courses',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='courses/',default='default.png') 
    price = models.FloatField()
    duration = models.FloatField(null=True,blank=True)
    subtitle = models.CharField(max_length=200,null=True,blank=True)   
    description =models.TextField(max_length=1000,null=True,blank=True)
    category = models.ForeignKey('Category',related_name='courses_cat',on_delete=models.CASCADE)

    def __str__(self):
      return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
      return self.name