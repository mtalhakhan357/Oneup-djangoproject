from django.shortcuts import render , redirect ,HttpResponseRedirect
from .models import  *
from main.models import *
from math import ceil
import time
from django.contrib import messages

# Create your views here.
def games_categary(request,mycat):
    prod = game.objects.filter(game_categary=mycat)
    params = {'prod':prod}
    views = statustics.objects.get(page_name='games')  
    views.page_views = views.page_views + 1
    views.save() 
    return render(request,'game_categary.html',params)

def games_home(request):
    products= game.objects.all()
    allProds=[]
    catprods= game.objects.values('game_categary', 'id')
    cats= {item["game_categary"] for item in catprods}
    for cat in cats:
        prod=game.objects.filter(game_categary=cat)
        n = 50
        nSlides = n 
        allProds.append([prod, range(40), nSlides])
    pages = page_details.objects.get(page_name ='game')
    params={'allProds':allProds,'page':pages}
    views = statustics.objects.get(page_name='games')  
    views.page_views = views.page_views + 1
    views.save() 
    return render(request,'game_home.html',params,)  

def games_download(request,myid,mynam):
    # this is download urls -------------------------------------------------
    details = game.objects.get(id=myid)
    coments = gamecomments.objects.filter(game=details)
    lof1 = len(gamecomments.objects.filter(ratting=1))
    lof2 = len(gamecomments.objects.filter(ratting=2))
    lof3 = len(gamecomments.objects.filter(ratting=3))
    lof4 = len(gamecomments.objects.filter(ratting=4))
    lof5 = len(gamecomments.objects.filter(ratting=5))
    total_rating = (5*lof5 + 4*lof4 + 3*lof3 + 2*lof2 + 1*lof1) / (lof5+lof4+lof3+lof2+lof1)
    print(lof4)
    views = statustics.objects.get(page_name='games')  
    views.page_views = views.page_views + 1
    views.save()
    allprod = {'details':details,'coments':coments,'total_rating':total_rating}
    return render(request,'game_downloads.html',allprod)
def games_d_download(request,myid,mynam):
    # this is download urls -------------------------------------------------
    details = game.objects.get(id=myid)
    coments = gamecomments.objects.filter(game=details)
    views1 = game.objects.get(id=myid)  
    views1.views = views1.views + 1
    views1.save() 
    views = statustics.objects.get(page_name='games')  
    views.page_views = views.page_views + 1
    views.save() 
    
    return render(request,'game_download2.html',{'details':details,'coments':coments})    
def postGcomment(request):
    if request.method == 'POST':
        user = request.user#
        gameide = request.POST.get('gameid')#
        games = game.objects.get(id=gameide)#
        comment = request.POST.get('comment')#
        rating = request.POST.get('rating')#
        gamepath = request.POST.get('gamepath')
        comments = gamecomments(user=user,game=games,comment=comment,ratting=rating)
        comments.save()
        messages.success(request,"Comment posted Succesfully")
        return HttpResponseRedirect(gamepath) 
    else:
        return HttpResponseRedirect(gamepath) 


