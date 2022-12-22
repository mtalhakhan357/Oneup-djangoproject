from django.shortcuts import render ,redirect ,HttpResponseRedirect
from django.http import HttpResponse , request
import requests ,random ,json
from app_s.models import *
from games.models import *
from .models import *
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models.functions import Lower
from math import ceil
# from django.conf import settings
# import threading
# from .utils import generate_token
# from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.contrib.auth import authenticate, login , logout

# random.shuffle(game)
# my all views  

def home(request):
    products= game.objects.all()
    allProds=[]
    catprods= game.objects.values('game_categary', 'id')
    cats= {item["game_categary"] for item in catprods}
    for cat in cats:
        prod= game.objects.filter(game_categary=cat)
        n = len(prod)
        nSlides = n 
        allProds.append([prod, range(40), nSlides])
    products2= app.objects.all()
    
    allProds2=[]
    catprods2= app.objects.values('app_categary', 'id')
    cats2= {item["app_categary"] for item in catprods2}
    for cat2 in cats2:
        prod2=app.objects.filter(app_categary=cat2)
        n2 = len(prod2)
        nSlides2 = n2 
        allProds2.append([prod2, range(40), nSlides2])
    pages = page_details.objects.get(page_name ='home')
    params={'allProds2':allProds2 ,'allProds':allProds,'page':pages}
    views = statustics.objects.get(page_name='home')  
    views.page_views = views.page_views + 1
    views.save() 
    
    return render(request,'home.html', params )
def remove(string):
    return string.replace(" ", "")
def searchMatchgame(query,item):
    if remove(query) in remove(item.game_name.lower()) or remove(query) in remove(item.game_author.lower()) or remove(query) in remove(item.game_categary.lower()) or remove(query) in remove(item.game_sub_categary.lower()) or remove(query) in remove(item.game_size.lower()) or remove(query) in remove(item.game_license.lower()) or query in remove(item.game_tags.lower()):
        return True
    elif query in item.game_name.lower() or query in item.game_author.lower() or query in item.game_categary.lower() or query in item.game_sub_categary.lower() or query in item.game_size.lower() or query in item.game_license.lower() or item.game_tags.lower() in query:
        return True
    elif query in item.game_name or query in item.game_author or query in item.game_categary or query in item.game_sub_categary or query in item.game_size or query in item.game_license or item.game_tags in query:
        return True
    else:
        return False
def searchMatchapp(query,item):
    if remove(query) in remove(item.app_name.lower()) or remove(query) in remove(item.app_author.lower()) or remove(query) in remove(item.app_categary.lower()) or remove(query) in remove(item.app_sub_categary.lower()) or remove(query) in remove(item.app_size.lower()) or remove(query) in remove(item.app_license.lower()) or query in remove(item.app_tags.lower()):
        return True
    elif query in item.app_name.lower() or query in item.app_author.lower() or query in item.app_categary.lower() or query in item.app_sub_categary.lower() or query in item.app_size.lower() or query in item.app_license.lower() or item.app_tags.lower() in query:
        return True
    elif query in item.app_name or query in item.app_author or query in item.app_categary or query in item.app_sub_categary or query in item.app_size or query in item.app_license or item.app_tags in query:
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search').lower()
    if query.strip() :
        allProds2=[]
        catprods2= app.objects.values('app_categary', 'id')    
        cats2= {item["app_categary"] for item in catprods2} 
        noresults = "Not Found"
        for cat2 in cats2:
            prodtemp2 = app.objects.filter(app_categary= cat2)
            prod2 = [item for item in prodtemp2 if searchMatchapp(query,item)]
            n2 = len(prod2)
            nSlides = n2 // 4 + ceil((n2 / 4) - (n2 // 4))

            if len(prod2) != 0 :   
                allProds2.append([prod2, range(40), nSlides])
                noresults = "Found in Apps" 

        products= game.objects.all()
        allProds=[]
        catprods= game.objects.values('game_categary', 'id')
        cats= {item["game_categary"] for item in catprods}
        pages = page_details.objects.get(page_name='search')
        for cat in cats:
            prodtemp= game.objects.filter(game_categary=cat) 
            prod = [item for item in prodtemp if searchMatchgame(query,item)]
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            if len(prod) != 0 :   
                allProds.append([prod, range(40), nSlides])
                noresults = "Found in Games" 
        params={'allProds':allProds,'allProds2':allProds2 ,'query':query,'noresults':noresults,'page':pages}
    else:
        query = '''"blank"'''
        noresults = "Not Found"
        pages = page_details.objects.get(page_name='search')
        params={'noresults':noresults,'query':query,'page':pages}
    return render(request,'search.html',params)

   
def contact_us(request):
    if request.method == 'POST':     
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        messtype = request.POST.get('type')
        site_key = request.POST['g-recaptcha-response']
        secret_key = '6LdbgZoaAAAAAH-rIard2yhIDyz4YR5ShdG5eslN'
        urls = 'https://www.google.com/recaptcha/api/siteverify'
        captchaData = {'secret':secret_key,'response':site_key}
        cap_r = requests.post(urls,data=captchaData)
        responses = json.loads(cap_r.text)
        verify = responses['success']
        if verify:
            contact = contactrequests( user_name=name , user_email=email , user_subject=subject , user_message=message , user_type=messtype )
            contact.save()
            messages.success(request,'Contact us form Successfully Submited')
            views = statustics.objects.get(page_name='contact-requests-got')  
            views.page_views = views.page_views + 1
            views.save()
        else:
            messages.error(request,'Invailid reCaptcha, Please retry.')
    else:
        pass
    pages = page_details.objects.get(page_name ='contact_us')    
    views = statustics.objects.get(page_name='contact_us')  
    views.page_views = views.page_views + 1
    views.save() 
    return render(request,'contact_us.html',{'page':pages})
# class EmailThread(threading.Thread):
    
#     def __init__(self, email_message):
#         self.email_message = email_message
#         threading.Thread.__init__(self)

#     def run(self):
#         self.email_message.send()


def singup(request):
    # get the sign up form output
    if request.method == 'POST':
        signupUsername = request.POST['signupUsername']
        signupfirst_name = request.POST['signupfirst_name']
        signuplast_name = request.POST['signuplast_name']
        signupemail = request.POST['signupemail']
        singupPassword = request.POST['singupPassword']
        signupconfirm_password = request.POST['signupconfirm_password']
        loginPath = request.POST['loginPath']
        site_key = request.POST['g-recaptcha-response']
        secret_key = '6Leq0JkaAAAAAKW1V5rRK0nQzitDra7t39QOrIcz'
        urls = 'https://www.google.com/recaptcha/api/siteverify'
        captchaData = {'secret':secret_key,'response':site_key}
        cap_r = requests.post(urls,data=captchaData)
        responses = json.loads(cap_r.text)
        verify = responses['success']
        if verify:
            if User.objects.filter(username = signupUsername).first():
                messages.error(request, ' Username is taken.')
                return redirect('home')
            # email should not repeat
            if User.objects.filter(email = signupemail).first():
                messages.error(request, ' Email has  taken.')
                return redirect('home')
            # username has to be lowercase and alphanumeric 
            if not signupUsername.isalnum() :
                messages.error(request, ' Your Username must be 8-20 characters long, contain letters and numbers , and must not contain spaces, special characters, or emoji.')
                return redirect('home') 
            # user name shoul not be smaller 
            if len(signupUsername) < 8 :          
                messages.error(request,' Your is username is too small . Please enter a username of 8 charactors.')
                return redirect('home')
            # username should not be larger 
            if len(signupUsername) > 20:
                messages.error(request,' Your is username is too large . Please enter a username of below 20 charactors.')
                return redirect('home')
            # password and confirm password should match
            if singupPassword != signupconfirm_password :
                messages.error(request,' Your Confirm password Must Match Password')
                return redirect('home')
            # password should not be smaller 
            if len(singupPassword) < 8 :
                messages.error(request,' Your Password is Too Small') 
                return redirect('home')
            # password should not be biger
            if len(singupPassword) > 20 :
                messages.error(request,' Your Password is Too Big') 
                return redirect('home')

            # making user 
            user = User.objects.create_user(username=signupUsername,email=signupemail)
            user.set_password(signupconfirm_password)
            user.first_name = signupfirst_name
            user.last_name = signuplast_name
            user.save()
            profile = Profile(user=user)
            profile.save()
            # passing succes message
            messages.success(request,' Account has been created succesfullly created succesfully')
            return redirect('home') 
        else:
            messages.error(request,'Please fill up the recaptcha')
            return HttpResponseRedirect(loginPath)
    else:
        messages.warning(request,' Invalid : Something went wrong. ERORR:404')
        return redirect('home')
def ulogin(request):
    if request.method == 'POST':
        username = request.POST['loginUsername']
        password = request.POST['loginpassword']
        loginPath = request.POST['loginPath']
        site_key = request.POST['g-recaptcha-response']
        secret_key = '6LcEzpkaAAAAAHfxpA_npaC2wBYMgBcCKVG_YPmX'
        urls = 'https://www.google.com/recaptcha/api/siteverify'
        captchaData = {'secret':secret_key,'response':site_key}
        cap_r = requests.post(urls,data=captchaData)
        responses = json.loads(cap_r.text)
        verify = responses['success']       
        if verify == True:     
            user = authenticate(request, username=username, password=password)        
            if user is not None :
                login(request,user)
                messages.success(request,' Succesfully logged in' )
                return HttpResponseRedirect(loginPath)
            else:
                messages.error(request,'Username Or Password is not correct and Make sure you have made an Account')
                return HttpResponseRedirect(loginPath)
        else:
            messages.error(request,'Please fill up the recaptcha')
            return HttpResponseRedirect(loginPath)

    else :
        messages.warning(request,' Error:404')
        return redirect('home')    
    return HttpResponseRedirect(loginPath)
def ulogout(request):
    logout(request)
    messages.success(request,' Succesfully Logged OUT')
    return redirect('home')
def about(request):    
    pages = page_details.objects.get(page_name ='about')     
    return render(request,'abouts.html',{'page':pages})
def profile(request): 
    # pages = page_details.objects.get(page_name ='terms_of_use')     ,{'page':pages}   
    
    return render(request,'profile.html')
def terms_of_use(request): 
    pages = page_details.objects.get(page_name ='terms_of_use')        
    return render(request,'terms_of_use.html',{'page':pages})
def privacy_policy(request):
    pages = page_details.objects.get(page_name ='privacy_policy')         
    return render(request,'privacy_policy.html',{'page':pages})
