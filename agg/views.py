from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from agg.models import Job

from datetime import datetime

import feedparser
import requests

job_urls = [('dj', 'https://djangojobs.net/jobs/latest/feed/rss/'),
            ('dg', 'https://djangogigs.com/feeds/gigs/'),
            ('lj', 'https://landing.jobs/partner_feed?q=skill%3A%22django%22')]


def index(request):
    template = 'index.html'

    jobs = Job.objects.filter(applied=False).filter(hide=False)
        
    context = {'jobs': jobs}

    return render(request, template, context)

def import_jobs(request):
    jobs = []
    count = 0
    # RSS
    for site, url in job_urls:
        for job in feedparser.parse(url)['entries']:
            jobs_found = Job.objects.filter(title__icontains=job['title']).count()
            if jobs_found > 0:
                continue

            if 'published' in job:
                published = job['published']
                try:
                    published = datetime.strptime(published, "%a, %d %b %Y %H:%M:%S %z")
                except ValueError:
                    published = datetime.strptime(published, "%Y-%m-%dT%H:%M:%S%z")
            else:
                published = datetime.now()

            j = Job(title=job['title'], body=job['summary'], link=job['link'], published=published, site=site)
            j.save()
            count += 1

    #JSON - remoteok.io
    r = requests.get("https://remoteok.io/api")
    for job in r.json()[1:]:

        if 'date' in job:
            published = job['date']
            published = datetime.strptime(published, "%Y-%m-%dT%H:%M:%S%z")

        j = Job(title=job['position'], body=job['description'], link=job['url'], published=published, site='rok')
        j.save()
        count += 1
        

    messages.success(request, "OK - %s added"%(count))
    return redirect('/agg/')

def update(request):
    count = 0
    if request.method == 'POST':
        for field, value in request.POST.items(): 
            if '_' not in field:
                continue

            id, what = field.split('_')

            if value == 'on':
                j = Job.objects.get(pk=int(id))
                setattr(j, what, True)
                j.save()
                
                count += 1

    messages.success(request, 'OK - %s updated'%(count))
    return redirect("/agg/")
