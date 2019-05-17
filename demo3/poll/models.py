from django.db import models

# Create your models here.
class test(models.Model):
    title=models.CharField(max_length=30,verbose_name='投票列表')
    choseA=models.CharField(max_length=30,verbose_name="A选项")
    choseB=models.CharField(max_length=30,verbose_name="B选项")
    resualtA=models.IntegerField(null=True,verbose_name="A选项的结果")
    resualtB=models.IntegerField(null=True,verbose_name="B选项的结果")
    def __str__(self):
        return '%s,%s,%s,%d%d'%(self.title,self.choseA,self.choseB,self.resualtA,self.resualtB)
