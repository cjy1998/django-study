from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from . import models
# from django. import view
# Create your views here.

class Student1(View):
    def get1(self, request):
    # 添加数据操作
    # 先添加主模型 再添加外键模型
        student = models.Student.objects.create(
            name = "小小",
            age=10,
            sex=True
        )
        models.StudentProfile.objects.create(
            student = student,
            description="44585",
            address="686454",
            mobile="5454455555"
        )
        return JsonResponse({'msg':'添加成功！'})

    def get2(self,request):
        # 从主模型查询到外键模型
        student = models.Student.objects.get(id = 1)
        if student:
            print(student.profile.address)
        # 从外键模型查询到主模型
        profile = models.StudentProfile.objects.get(id = 1)
        if profile:
            print(profile.student.name)
        return JsonResponse({'msg':'查询成功'})

    def get3(self,request):
        student = models.Student.objects.get(name = "小小")
        if student:
            student.profile.address = "新地址"
            student.profile.mobile = "5454455555"
            student.profile.save()
        return JsonResponse({'msg':'1'})

    def get(self, request):
        student = models.Student.objects.get(id = 1)
        if student:
            student.delete()
        return JsonResponse({'msg':'2'})

# 一对多
class ArticleView(View):
    def get1(self, request):
        # 先添加主模型
        # author = models.Author.objects.create(
        #     name="李白",
        #     age=10,
        #     sex=True
        # )
        #
        # article_list = [
        #     models.Article(title="赠汪伦",author=author),
        #     models.Article(title="将进酒",author_id=author.id)
        # ]
        #
        # models.Article.objects.bulk_create(article_list)

        #作者已存在，添加多篇文章

        # author = models.Author.objects.get(id = 1)
        # if author:
        #     article_list = [
        #         models.Article(title="天生我材必有用",author=author),
        #         models.Article(title="杯莫停",author_id=author.id)
        #     ]
        #     models.Article.objects.bulk_create(article_list)

        models.Article.objects.create(
            title="春蚕到死丝方尽",
            author= models.Author.objects.create(
                name="李商隐",
                age=10,
                sex=True
            )
        )
        return JsonResponse({'msg':'3'})
    # 查询数据
    def get2(self,request):
        #通过主模型  拿到外键模型
        # query_id = request.GET.get('id')
        # author = models.Author.objects.get(id = query_id)
        # article = author.article_list.all().values()

        #通过主键模型作为条件，直接查询外键模型的数据
        # article_list = models.Article.objects.filter(author_id= query_id).values()

        #通过外键模型 拿到主模型
        # article = models.Article.objects.get(title="赠汪伦")
        # if article:
        #    name = article.author.name
        #    print(name)

        #通过外键模型作为条件  直接查询主键模型的数据
        name = models.Author.objects.get(article_list__title="春蚕到死丝方尽").name
        print(name)
        return  JsonResponse({'msg':'4'})
    # 更新操作
    def get(self,request):
        # 把李白所有的文章创建时间改为 2025-05-01 13:00:00
        # author = models.Author.objects.get(name = '李白')
        # for article in author.article_list.all():
        #     article.createdTime = "2025-05-01 13:00:00"
        #     article.save()

        #吧赠汪伦的作者改为汪伦
        author = models.Author.objects.filter(name = '杜甫').first()
        article = models.Article.objects.get(title = "赠汪伦")
        if author and article:
           article.author = author
           article.save()
        else:
            author = models.Author.objects.create(
                name="杜甫",
                age=10,
                sex=True
            )
            article.author = author
            article.save()
        return JsonResponse({'msg':'5'})