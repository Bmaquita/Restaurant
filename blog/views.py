from django.shortcuts import render

from django.core.paginator import Paginator 

from .models import Post
def all_news(request):

    published_news = Post.objects.filter(post_status = 'P')

    #number of items per page 
    paginator = Paginator(published_news, 6)

    #get the current page number or page 

    current_page_number = request.GET.get('page')

    #the actual pagination pages with content 

    news_page = paginator.get_page(current_page_number)


    context = {
        'published_news':news_page}

    return render(request, 'news/all_news.html', context)