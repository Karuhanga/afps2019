from django.shortcuts import render
from .models import *


# Create your views here.

#View for home
def home(request):
    payload = {}
    payload = {
        'event_info': EventInformation.get_event_info(),
        'how': EventSummaryCard.objects.get_or_create(title='How'),
        'why': EventSummaryCard.objects.get_or_create(title='Why'),
        'pre': EventSummaryCard.objects.get_or_create(title='Prerequisites'),
        'organs': EventSummaryCard.objects.get_or_create(title='Organisers'),
        'abstracts': EventSummaryCard.objects.get_or_create(title='Call for Abstracts'),
        'previous': PreviousEdition.objects.order_by('-year').all(),
        'partners': Partner.objects.order_by('name').all()
    }

    return render(request, "index.html", payload)

#View for Register
def register(request):

    info = EventInformation.get_event_info()
    days_to = info.get_time_to_event()
    days_left_for_reg = info.get_time_to_reg_end()
    ads, ad = Ad.get_ads()

    payload = {
        'days_to': str(days_to),
        'reg_end': str(days_left_for_reg),
        'link_to_reg': info.link_to_reg_form,
        'ads': ads,
        'ad' : ad,
    }

    return render(request, "register.html", payload)

def abstracts(request):
    info = EventInformation.get_event_info()

    payload = {
        'link_to_abstracts_form': info.link_to_abstracts_form,
    }

    return render(request, "abstracts.html")

#View for Event Guide
def event_guide(request):

    try:
        payload = {
            'event_info': EventInformation.get_event_info(),
            'schedule': list(Schedule.objects.order_by('date')[:3]),
            'immigration_guides': ImmigrationGuide.objects.all(),
            'team': TeamMember.objects.order_by('role').all(),
        }
    except Exception as e:
        payload = {}

    return render(request, "event_guide.html", payload)

#View for Blog
def blog(request):
    posts = Post.objects.all()
    odd_posts = posts[1::2]
    even_posts = posts[::2]
    ads, ad = Ad.get_ads()

    payload = {
        "odd_posts": odd_posts,
        "even_posts": even_posts,
        "ads": ads,
        "ad" : ad,
    }

    return render(request, "blog.html", payload)

#View for Article
def article(request, slug):
    post = Post.objects.get(slug=slug)
    ads, ad = Ad.get_ads()

    payload = {
        'ads': ads,
        'article': post,
        'ad' : ad,
    }

    return render(request, "article.html", payload)
