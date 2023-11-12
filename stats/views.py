from django.shortcuts import render
from django.db.models import Count, Q
from .models import Problems
import json

def get_stats(request):
    stat_nos = Problems.objects.values('figure')
    stat_issue = Problems.objects.values('issue')
    
   
    issue_series = list()
    figure_series = list()
  
    for entry in stat_nos:
        figure_series.append(entry['figure'])
    for entry in stat_issue:
        issue_series.append(entry['issue'])

    context = {
        'issue_series': json.dumps(issue_series),
        'figure_series': json.dumps(figure_series)
    }

    return render(request, 'stats.html', context)
