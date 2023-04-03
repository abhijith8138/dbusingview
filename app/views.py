from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def Insert_Topic(request):
    tn=input('enter Topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic_name is inserted')
def Insert_Webpage(request):
    tn=input('enter Topic_name')
    n=input('enter name')
    url=input('enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('Webpages data  is inserted')
def Insert_AccessRecord(request):
    tn=input('enter Topic_name')
    n=input('enter name')
    url=input('enter url')
    a=input('enter  author name')
    d=input('enter date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    AR=Accessrecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    AR.save()
    return HttpResponse('AccessRecorddata  is inserted')
