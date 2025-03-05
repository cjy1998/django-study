import json

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
        object_list = models.Student.objects.all()
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
        student = object_list[0]
        #获取模型对象的字段属性
        print(student.id,student.pk) #获取主键
        print(student.name,student.description) #获取其他属性
        print(student.created_time.strftime("%Y-%m-%d %H:%M:%S")) #获取日期格式化内容
       # 当字段声明中，使用 choices 可选值选项以后，在模型对象里边就可以通过get_<字段名>_display() 来获取当前选项的文本提示
        print(student.status,student.get_status_display())
        """
        第二种
        """
        # student_list = models.Student.objects.all().values()
        # return JsonResponse(list(student_list), safe=False)
        return JsonResponse({}, safe=False)


    def post(self, request):
        # print(request.body.decode())
        # data = request.body.decode()
        # models.Student.objects.create(data=data)
        #
        # return JsonResponse(data, status=201)
        try:
            # 解析 JSON 数据
            raw_data = request.body.decode()
            data = json.loads(raw_data)

            # 创建学生对象（注意字段对应）
            student = models.Student.objects.create(
                name=data.get('name'),
                age=data.get('age', 0),  # 默认值处理
                sex=data.get('sex', True),
                phone=data.get('phone'),
                classmate=data.get('classmate', ''),  # 注意模型中的 db_column="class"
                description=data.get('description', None),
                status=data.get('status', 0)
            )

            # 返回创建的对象数据
            return JsonResponse({
                'id': student.id,
                'name': student.name,
                'age': student.age,
                'phone': student.phone,
                'status': student.get_status_display(),  # 显示 choice 的文本
                'created_time': student.created_time.isoformat()
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request):
        data = {}
        return JsonResponse(data, status=201)

    def delete(self, request):
        data = {}
        return JsonResponse(data, status=204)