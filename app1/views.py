from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
def index(request):
    categories = Category.objects.filter(is_menu=True)
    news= New.objects.all()
    
    ctx = {
       'categories': categories,
       'big_new': news[0],
       'all_news': news[1:],
       'svejiy': New.objects.all().order_by('-id')[:8]
    }
    return render(request, 'pages/index.html',ctx)
def search(request): 
    kalit = request.GET.get('search')
    news_list = New.objects.filter(
        Q(title__icontains=kalit) |
        Q(short_desc__icontains=kalit) |
        Q(description__icontains=kalit) |
        Q(tegs__icontains=kalit)
    )

    pagination = Paginator(news_list, 2)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    ctx = {
        'kalit': kalit,
        'count': pagination.count,
        'page_obj': page_obj,
        'news': page_obj   
    }
    return render(request, 'pages/search.html', ctx)
def view(request,pk):
   #  kategory = get_list_or_404(Category,slug=slug)
    new = New.objects.get(pk=pk)
    if not new:
       return redirect('404')
    new.view += 1
    new.save()
    ctx = {
       'new':new
       
    }
    return render(request, 'pages/view.html',ctx)
def contact(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         form.save()
   ctx = {
      
   }
   return render(request, 'pages/contact.html',ctx)
def category(request,slug):
    categories = Category.objects.filter(is_menu=True)
    kategory = get_object_or_404(Category,slug=slug)
    category_new = New.objects.filter(category_id=kategory).order_by('-pk')
    pagination = Paginator(category_new, 1)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    ctx = {
       'categories': categories,
       'svejiy': New.objects.all().order_by('-id')[:8],
       'kategory': kategory,
       'category_new':category_new,
       'page_obj':page_obj,
    }
    return render(request, 'pages/category.html',ctx)
 
 
 
def login_page(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      
   ctx={
      
   }
   return render(request,'login.html',ctx)
 
def page_not_found(request):
   ctx = {
      
   }
   return render(request, 'pages/404_page.html', ctx) 
