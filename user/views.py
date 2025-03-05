from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.

@require_http_methods(["GET"])
def getlist(request):
    params = request.GET.dict()
    print(request.GET.getlist('name'))
    print(request.GET.get('name'))
    # 业务代码，调用数据，for循环之类的
    data = '<h1>我是get请求<h1>'
    return HttpResponse(data, content_type='text/html')
@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    data = '我是post请求'
    # postdata = request.POST.dict()
    # print(request.POST)
    print(request.body)
    print(request.META)
    return HttpResponse(data)
@csrf_exempt
@require_http_methods(["POST"])
def upload(request):
    import os
    # __file__ 魔术变量，写在哪里，就代表哪个文件
    for file in request.FILES.getlist('avatar'):
        # 保存在当前文件下
        # with open(f"{os.path.dirname(__file__)}/{file.name}","wb") as f:
        #   保存在根目录
          with open(f"./{file.name}", 'wb') as f:
            f.write(file.read())
    return HttpResponse("上传成功！！！")
def returnhtml(request):
    return HttpResponse("<h1>文本<h1/>", content_type='text/html',status=200,headers={'token':'bear 125465464'})

def returnjson(request):
    data = {
        'name': '1234',
        'age': 15
    }
    arr = [
        {
            'name': '张三',
            'age': 15
        },
        {
            'name': '李四',
            'age': 19
        }
    ]
    return JsonResponse(arr,safe=False)

def retunfile(request):
    with open("./logo.svg", 'rb') as f:
        img = f.read()
    return HttpResponse(content=img,content_type='image/svg+xml')

def setresponseheaders(request):
    response = HttpResponse("ok!!!")
    response['company'] = 'test'
    return response

@require_http_methods(["GET"])
def redirecturl(request):
    url = "http://www.baidu.com/"
    # 原理
    # response = HttpResponse(status=301)
    # response['location'] = url
    # return response
    return HttpResponseRedirect(url)

def redirectin(request):
    return  redirect("user:returnhtml")