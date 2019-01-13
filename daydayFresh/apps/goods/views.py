from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

# git修改URL情况下，本地修改view
# 继续上次测试
