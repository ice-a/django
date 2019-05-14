from django.db import models
#MVT中的M模型
#ORM中的O
# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=30)
    pub_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class hero(models.Model):
    name=models.CharField(max_length=30)
    gender=models.BooleanField(True)
    skill=models.CharField(max_length=30,null=True)
    wj=models.ForeignKey(book,on_delete=models.CASCADE)
    def __str__(self):
        return self.name