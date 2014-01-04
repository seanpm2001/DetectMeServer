from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Category


def competition_detail(request):
    categories = Category.objects.all()
    return render_to_response('leaderboards/competition_detail.html',
                              {"categories": categories},
                              context_instance=RequestContext(request))


def show_leaderboard(request, category):
    category = Category.objects.get(name=category)
    return render_to_response('leaderboards/leaderboard.html',
                              {"category": category},
                              context_instance=RequestContext(request))