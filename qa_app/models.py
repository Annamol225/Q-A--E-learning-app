from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class subject(models.Model):
    sub_name=models.CharField(max_length=250)
    slug=models.SlugField()
    img=models.ImageField(upload_to="images",blank=True,null=True)
    img1=models.ImageField(upload_to="images",blank=True,null=True) 
    indo=models.TextField()

    def __str__(self): 
        return self.sub_name
    

class syllabus(models.Model):
    sub_name = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='sy_list')
    sy_list=models.CharField(max_length=300)

    def __str__(self): 
        return self.sy_list
    

class Qa(models.Model):
    sub_name=models.ForeignKey(subject, on_delete=models.CASCADE)
    sy_list=models.ForeignKey(syllabus,on_delete=models.CASCADE, related_name='qa_set')  
    qust=models.TextField()
    ans=models.TextField()

    
    



 