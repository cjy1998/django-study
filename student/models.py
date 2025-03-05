from django.db import models

# Create your models here.
class Student(models.Model):
    STATUS_CHOICES = (
        # (数据库值，程序显示给外界看的文本)
        (0,"正常"),
        (1,"未入学"),
        (2,"已毕业")
    )
    # django模型不需要自己单独声明主键，模型会自动创建主键 ID，在代码中直接可以通过模型对象.id或者模型对象.pk就可以调用主键。
    name = models.CharField(max_length=15,db_index=True,verbose_name="姓名")
    age = models.IntegerField(default=0,verbose_name="年龄")
    sex = models.BooleanField(default=True,verbose_name="性别")
    phone = models.CharField(max_length=20,unique=True,verbose_name="手机号码")
    classmate = models.CharField(max_length=50,db_column="class",default="",verbose_name="班级编号")
    description = models.TextField(null=True,verbose_name="个性签名")
    status  = models.IntegerField(choices=STATUS_CHOICES,default=0,verbose_name="学生状态")
    created_time = models.DateTimeField(auto_now_add=True,null=True,verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True,null=True,verbose_name="更新时间")
    class Meta:
        db_table = 'student'
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name