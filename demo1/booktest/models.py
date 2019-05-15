from django.db import models
#MVT中的M模型
#ORM中的O
# Create your models here.
xb=(('1','男'),('2','女'))
class book(models.Model):
    title=models.CharField(max_length=30,verbose_name='书籍名称')
    pub_date=models.DateTimeField(verbose_name='出版时间')
    def __str__(self):
        return self.title
class hero(models.Model):
    name=models.CharField(max_length=30,verbose_name='英雄名字')
    gender=models.CharField(max_length=10,choices=xb,verbose_name='性别')
    skill=models.CharField(max_length=30,null=True,verbose_name='技能')
    wj=models.ForeignKey(book,on_delete=models.CASCADE,verbose_name='书')
    def __str__(self):
        return self.name