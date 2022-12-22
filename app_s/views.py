from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
from django.contrib import messages
from main.models import *
from math import ceil
import time



# Create your views here.
def apps_categary(request,mycat):
    details = app.objects.filter(app_categary=mycat)
    views = statustics.objects.get(page_name='apps')  
    views.page_views = views.page_views + 1
    views.save() 
    return render(request,'apps_categary.html',{'details':details})
def apps_home(request):
    products= app.objects.all()
    allProds=[]
    catprods= app.objects.values('app_categary', 'id')
    cats= {item["app_categary"] for item in catprods}
    for cat in cats:
        products=app.objects.filter(app_categary=cat)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([products, range(40), nSlides])
    pages = page_details.objects.get(page_name ='app')
    params={'allProds':allProds,'page':pages }
    views = statustics.objects.get(page_name='apps')  
    views.page_views = views.page_views + 1
    views.save() 
    return render(request,'app_home.html',params)  

def apps_download(request,myid,mynam):
    details = app.objects.get(id=myid)
    coments = appcomments.objects.filter(app=details)
    views = statustics.objects.get(page_name='apps')  
    views.page_views = views.page_views + 1
    views.save() 
    params = {'details':details,'coments':coments}
    return render(request,'download_apps.html',params)

def apps_d_download(request,myid,mynam):
    details = app.objects.get(id=myid)
    coments = appcomments.objects.filter(app=details)
    dapp = app.objects.get(id=myid)  
    dapp.views = dapp.views + 1
    dapp.save()    
    views = statustics.objects.get(page_name='apps')  
    views.page_views = views.page_views + 1
    views.save()
    params = {'details':details,'coments':coments} 
    return render(request,'download_apps2.html',params)

def postAcomment(request):
    if request.method == 'POST':
        user = request.user#
        appide = request.POST.get('appid')#
        apps = app.objects.get(id=appide)#
        comment = request.POST.get('comment')#
        rating = request.POST.get('rating')#
        apppath = request.POST.get('apppath')
        comments = appcomments(user=user,app=apps,comment=comment,ratting=rating)
        comments.save()
        messages.success(request,"Comment posted Succesfully")
        return HttpResponseRedirect(apppath) 
    else:
        return HttpResponseRedirect(apppath) 