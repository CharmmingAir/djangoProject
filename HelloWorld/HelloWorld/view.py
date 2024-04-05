from django.http import HttpResponse

from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World!")


def test_run(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'test_run.html', context)

def test_run2(request):
    views_name = '菜鸟教程'
    return render(request, 'test_run2.html', {'name':views_name})

def test_run3(request):
    views_list = ['菜鸟教程1', '菜鸟教程2', '菜鸟教程3']
    return render(request, 'test_run3.html', {'views_list':views_list})

def test_run4(request):
    views_dict = {'name':"菜鸟教程"}
    return render(request, 'test_run4.html', {'views_dict':views_dict})

def test_run5(request):
    name = '菜鸟教程'
    import datetime
    now = datetime.datetime.now()
    num = 1024

    str2 = "<a href='https://www.runoob.com/'>点击跳转</a>"

    num2 = 88

    athlete_ls = ['kate','john','mary']
    return render(request, 'test_run5.html', {'name':name, 'time':now, 'num':num, 'str2':str2, 'num2':num2, 'athlete_ls':athlete_ls})


def test_run6(request):
    return render(request, 'test_run6.html')