from django.db import models
from django.utils import timezone


# Create your models here.

class Play(models.Model):
    name = models.CharField(max_length=200)
    brief_info = models.CharField(max_length=200)
    play_length = models.IntegerField()
    price = models.FloatField(max_length=10)
    # photo = models.ImageField
    image = models.ImageField(upload_to='logo/', default='/media/logo/gou.jpg')  # 这里login是目录路径 完整的路径是 /media/logo/图片
    director = models.CharField(max_length=20, default='张艺谋')
    actor = models.CharField(max_length=200, default='jfh')
    play_type = models.CharField(max_length=40, default='3D')
    # 导演
    # 主演
    # 类型
    shangyin = models.IntegerField(default=1)

# 一场演出只能对应一个演出厅
# 一个演出厅能对应多场演出
class Studio(models.Model):
    sum_row = models.IntegerField()  # 列
    sum_col = models.IntegerField()  # 行


class Scheme(models.Model):
    start_time = models.DateTimeField(default=timezone.now, null=False)
    play = models.ForeignKey(Play, on_delete=models.CASCADE, )
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, )

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(default='1@q.com')

class Ticket(models.Model):
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE, )
    col = models.IntegerField(default=0)
    row = models.IntegerField(default=0)
    state = models.IntegerField(default=0)
    sale_time = models.DateTimeField(default=timezone.now, null=False)
    # 加用户_id
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
