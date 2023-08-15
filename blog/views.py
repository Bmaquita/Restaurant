from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator 

from contact.models import ContactDetail

from .models import Post, Category


def all_news(request):


    categories = Category.objects.all()

    published_news = Post.objects.filter(post_status = 'P')

    #number of items per page 
    paginator = Paginator(published_news, 6)

    #get the current page number or page 

    current_page_number = request.GET.get('page')

    #the actual pagination pages with content 

    news_page = paginator.get_page(current_page_number)

    contact_details = ContactDetail.objects.first()

    context = {
        'contact_details':contact_details,
        'categories':categories,
        'published_news':news_page}

    return render(request, 'news/all_news.html', context)


def single_news(request, news_slug):

    contact_details = ContactDetail.objects.first()

    single_news = get_object_or_404(Post, slug=news_slug)

    context = {
        'contact_details':contact_details,
        'single_news':single_news,
        
    }
    return render(request, 'news/single_news.html', context)


def search_by_category(request, category):

    contact_details = ContactDetail.objects.first()

    categories = Category.objects.all()

    filter_posts_by_category = Post.objects.filter(category__category=category, post_status='P')

    paginator = Paginator(filter_posts_by_category, 6)

    page_number = request.GET.get('page')

    filter_posts_by_category_page = paginator.get_page(page_number)

    context = {
        'contact_details':contact_details,
        'categories':categories,
        'published_news':filter_posts_by_category_page }

    return render(request, 'news/all_news.html', context)