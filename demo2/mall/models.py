from django.db import models
col=(('1',"绿色"),('2',"蓝色"),('3',"黄色"))
# Create your models here.
class brand(models.Model):
    brandname=models.CharField(max_length=30,verbose_name="品牌名字")
    pub_data=models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
class subbrand(models.Model):
    subbrandname=models.CharField(max_length=30,verbose_name="子品牌")
    color=models.CharField(max_length=10,choices=col,verbose_name="颜色")
    memory=models.CharField(max_length=10,choices=(('2',"2GB"),('4',"4GB"),('8',"8GB"),('16',"16GB")),verbose_name="内存")
    wj=models.ForeignKey(brand,on_delete=models.CASCADE,verbose_name="父品牌")


