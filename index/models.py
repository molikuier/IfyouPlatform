from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='书名')
    public = models.CharField(max_length=50, verbose_name='出版社')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='定价')

    def default_price(self):
        return '￥30'

    retail_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='零售价', default=default_price)

    def __str__(self):
        return f"title:{self.title} pub:{self.public} price:{self.price}"

class Author(models.Model): #创建作者表
    name=models.CharField(max_length=30,verbose_name='姓名')
    email=models.EmailField(verbose_name='邮箱')
    def __str__(self):
        return '作者：%s'%(self.name)

class UserInfo(models.Model): #创建用户信息表
    username=models.CharField(max_length=24,verbose_name='用户注册')
    password =models.CharField(max_length=24,verbose_name='密码')

    choices = (
            ('male', '男性'),
            ('female', '女性'),
    )
    gender = models.CharField(max_length=6, choices=choices, default='male',verbose_name="性别")

if __name__=="__main__":
    book = Book()
    print(book)