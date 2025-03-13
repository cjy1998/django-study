import json
from itertools import count

from django.db.models import F, Q, Avg, Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# 1.先导入模型
from . import models

# Create your views here.

class StudentView(View):
    def get(self, request):
        """
        第一种方式
        """
        # object_list = models.Student.objects.all()
        # student_list = []
        # for student in object_list:
        #     student_list.append({
        #         "id": student.id,
        #         "name": student.name,
        #         "age": student.age,
        #         "sex": student.sex,
        #         "classmate": student.classmate,
        #         "description": student.description,
        #         "created_time": student.created_time,
        #         "updated_time": student.updated_time,
        #     })
        # print(student_list)

        # student = object_list[0]
        #获取模型对象的字段属性
        # print(student.id,student.pk) #获取主键
        # print(student.name,student.description) #获取其他属性
        # print(student.created_time.strftime("%Y-%m-%d %H:%M:%S")) #获取日期格式化内容
       # 当字段声明中，使用 choices 可选值选项以后，在模型对象里边就可以通过get_<字段名>_display() 来获取当前选项的文本提示
       #  print(student.status,student.get_status_display())

        """
        第二种
        """
        # student_list = models.Student.objects.all().values()
        # return JsonResponse(list(student_list), safe=False)

        name = request.GET.get('name')
        #如果获取不到则抛出DoesNotExist异常
        # try:
        #     student =  models.Student.objects.get(name=name)
        # except models.Student.DoesNotExist:
        #     return JsonResponse({'msg':'失败','code':500,'data':None})
        # return JsonResponse({'msg':'成功','code':200,'data':{'name': student.name,'age': student.age})

        #如果获取到符合条件的数据有多条也会报错
        # try:
        #     student = models.Student.objects.get(name=name)
        # except models.Student.MultipleObjectsReturned:
        #     return JsonResponse({'msg': '失败', 'code': 500, 'data': None})
        # return JsonResponse({'msg': '成功', 'code': 200, 'data': {'name': student.name,'age': student.age}})

        '''
        first
        '''
        # student = models.Student.objects.first()
        num = models.Student.objects.filter(name='p1').count()
        return JsonResponse({'msg': '成功', 'code': 200, 'data': num})

    def post(self, request):
        # print(request.body.decode())
        # data = request.body.decode()
        # models.Student.objects.create(data=data)
        #
        # return JsonResponse(data, status=201)
        try:
            # 解析 JSON 数据
            raw_data = request.body
            data = json.loads(raw_data)

            #1. create
            # #创建学生对象
            # student = models.Student.objects.create(
            #     name=data.get('name'),
            #     age=data.get('age', 0),  # 默认值处理
            #     sex=data.get('sex', True),
            #     phone=data.get('phone'),
            #     classmate=data.get('classmate', ''),  # 注意模型中的 db_column="class"
            #     description=data.get('description', None),
            #     status=data.get('status', 0)
            # )
            #2. save
            student = models.Student(
                    name=data.get('name'),
                    age=data.get('age', 0),  # 默认值处理
                    sex=data.get('sex', True),
                    phone=data.get('phone'),
                    classmate=data.get('classmate', ''),  # 注意模型中的 db_column="class"
                    description=data.get('description', None),
                    status=data.get('status', 0)
            )
            student.save()

            #3.批量添加数据
            stu1 = models.Student(
                name='p1',
                age=15,
                sex=True,
                phone= "15970076941",
                classmate= "9",
                description= "最好的安排",
                status="1"
            )
            stu2 = models.Student(
                name='p2',
                age=15,
                sex=True,
                phone="15970076942",
                classmate="9",
                description="最好的安排",
                status="1"
            )
            stu3 = models.Student(
                name='p3',
                age=15,
                sex=True,
                phone="15970076943",
                classmate="9",
                description="最好的安排",
                status="1"
            )
            models.Student.objects.bulk_create([stu1, stu2, stu3])
            # 返回创建的对象数据
            return JsonResponse({
               'msg':"成功",
                'code':200
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request):
        # raw_data = request.body
        # json_data = json.loads(raw_data)
        # print(json_data)
        # student = models.Student.objects.get(id=json_data['id'])
        # if student:
        #     student.name = json_data['name']
        #     student.age = json_data['age']
        #     student.sex = json_data['sex']
        #     student.phone = json_data['phone']
        #     student.classmate = json_data['classmate']
        #     student.description = json_data['description']
        #     student.status = json_data['status']
        #     student.save()
        student = models.Student.objects.filter(id__in=[1,2]).update(classmate='c101')
        data = {

        }
        return JsonResponse(data, status=201)

    def delete(self, request):
        id = request.GET.get('id')
        student = models.Student.objects.filter(id=id)
        if student:
            student.delete()
        # student.objects.filter(id=id).delete()
        data = {'msg':'删除成功'}
        return JsonResponse(data, status=204)

class StusView(View):
    def get(self, request):
        name = request.GET.get('name')
        # 模糊查询  是否包含
        # obj_list = models.Student.objects.filter(name__contains=name)
        # 模糊查询 以什么开头
        # obj_list = models.Student.objects.filter(name__startswith=name)
        # 以什么结尾
        #obj_list = models.Student.objects.filter(name__endswith=name)
        #空值查询
        # obj_list = models.Student.objects.filter(description__isnull=True)
        #取值范围查询
        # obj_list = models.Student.objects.filter(created_time__range=('2025-03-05','2025-03-08'))
        #范围查询
        obj_list = models.Student.objects.filter(classmate__in=['c101','c102','c103'])
        stu_list = []
        for obj in obj_list:
            stu_list.append({
                "id": obj.id,
                "name": obj.name,
                "age": obj.age,
                "classmate": obj.classmate,
                "description": obj.description,
                "status": obj.status,
                "phone": obj.phone,
                'created_time': obj.created_time,
            })

        print(stu_list)
        return JsonResponse({'code': 200, 'mes': '成功','data':stu_list}, status=200)
    def post(self, request):
        data = json.loads(request.body)
        student = models.Student.objects.filter(created_time=F('updated_time')).values("name","created_time","updated_time")

        return JsonResponse({'code': 200,'data':  list(student)}, status=200)
    def get(self, request):
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        # obj_list = models.Student.objects.filter(name=name).filter(phone=phone).values()
        obj_list = models.Student.objects.filter(Q(name='p1')|Q(name='p2')).values()
        return JsonResponse({'code': 200,'data':list(obj_list)}, status=200)
    #排序
    def get(self, request):
        obj_list = models.Student.objects.filter(Q(classmate='c101') | Q(classmate='c102') | Q(classmate='c103')).order_by('-age').values()
        return JsonResponse({'code': 200,'data':list(obj_list)}, status=200)
    #多字段排序
    def get(self, request):
        obj_list = models.Student.objects.all().order_by('-classmate','-age').values('name','classmate','age')
        return JsonResponse({'code': 200, 'data': list(obj_list)}, status=200)
    def get(self,request):
        obj_list = models.Student.objects.all().aggregate(age=Avg('age'))
        return JsonResponse({'code': 200, 'data': obj_list}, status=200)
    #统计每个班的人数
    def get(self, request):
        obj_list = models.Student.objects.values('classmate').annotate(stunumber=Count('id'))
        return JsonResponse({'code': 200, 'data': list(obj_list)}, status=200)
