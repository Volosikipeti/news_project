from django.shortcuts import render

def home_page(request):
    return render(request,"./primary/news_page.html")

def home_page(request):
      return render(request,"./primary/home_page.html")

def news_detail_page(request):
    return render(request,"./primary/news_detail_page.html")