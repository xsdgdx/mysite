import datetime
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.urls import reverse
from blog.models import Blog
from read_statistics.utils import get_seven_days_read_date


def home(request):
    blg_content_type=ContentType.objects.get_for_model(Blog)
    dates,read_nums=get_seven_days_read_date(blg_content_type)
    context={}
    context['read_nums']=read_nums
    context['dates']=dates
    return render(request,'home.html',context)
