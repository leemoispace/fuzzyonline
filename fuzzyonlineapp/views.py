from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


from fuzzyonlineapp.fuzzycompare import compare2list


def index(request):
	#这里返回主页看到的网页
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('fuzzyonlineapp/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    #return HttpResponse(template.render(context, request))
    return HttpResponse(template.render())



# @csrf_exempt
def submit(request):
    #info=request.POST['info']

    #string to list
    leftl=request.POST['from'].split("\r\n")
    rightl=request.POST['standard'].split("\r\n")
    print(type(leftl))
    #print(leftl)
    #print(rightl)
    #这里可以处理数据了
    resultdic={}
    compare2list(leftl,rightl,resultdic)
    print(resultdic)
    #resultdic怎么呈现到模板，从服务器到客户端


    #返回渲染处理后的结果
    template = loader.get_template('fuzzyonlineapp/index.html')
    return HttpResponse(template.render())
