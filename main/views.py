from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Django 測試成功！這是我的第一個網頁。</h1>")