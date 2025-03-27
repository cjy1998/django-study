from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20,db_index=True)
    age = models.IntegerField()
    sex = models.BooleanField(null=True,blank=True,default=None)

    class Meta:
        db_table = 'orm_student'
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"id":self.id, "name":self.name, "age":self.age,"sex":self.sex})

class StudentProfile(models.Model):
    # 一对一 CASCADE 级联删除 DO_NOTHING 互不影响
    # models.CASCADE
    # models.DO_NOTHING
    # models.DEFERRED
    # models.SET_NULL
    # models.SET_DEFAULT
    student = models.OneToOneField('Student',on_delete=models.CASCADE,related_name='profile')
    description = models.TextField(default='',verbose_name="描述信息")
    address = models.CharField(max_length=500,verbose_name="家庭住址")
    mobile = models.CharField(max_length=15,verbose_name="紧急联系电话")

    class Meta:
        db_table = 'orm_student_profile'
        verbose_name = "学生详细信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"address":self.address, "mobile":self.mobile})

class Author(models.Model):
    name = models.CharField(max_length=20,db_index=True,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.BooleanField(null=True,blank=True,default=None,verbose_name="性别")

    class Meta:
        db_table = 'orm_author'
        verbose_name = "作者信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"id":self.pk ,"name":self.name, "age":self.age})

class Article(models.Model):
    author = models.ForeignKey(Author,on_delete= models.DO_NOTHING,related_name="article_list", verbose_name="作者")
    title = models.CharField(max_length=20,verbose_name="文章标题")
    createdTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orm_article'
        verbose_name = "文章信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"id":self.pk ,"title":self.title})

#多对多关联以后，在数据迁移时，在数据库中实际上会创建三张表，分别是：2个模型对象实体表，1张关联 2个模型的关系表
class Teacher(models.Model):
    name = models.CharField(max_length=20,db_index=True,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.BooleanField(null=True,blank=True,default=None,verbose_name="性别")
    class Meta:
        db_table = 'orm_teacher'
        verbose_name = "老师信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str({"id":self.pk ,"name":self.name})

class Course(models.Model):
    name = models.CharField(max_length=20,verbose_name="课程名称")
    teacher = models.ManyToManyField(Teacher,related_name="course")
    class Meta:
        db_table = 'orm_course'
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str({"id":self.pk ,"name":self.name})

class Area(models.Model):
    #一对多的自关联
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self",on_delete=models.SET_NULL,related_name="son_list",null=True,blank=True)
    class Meta:
        db_table = 'orm_area'
        verbose_name = '行政区划表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str({"id":self.pk ,"name":self.name})

class User(models.Model):
    name = models.CharField(max_length=20,unique=True)
    age = models.IntegerField(default=0)
    friends = models.ManyToManyField("self",symmetrical=True)
    class Meta:
        db_table = 'orm_user'
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str({"id":self.pk ,"name":self.name})