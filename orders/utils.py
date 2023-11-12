from django.shortcuts import redirect

def _redirect(request, url):
    next = request.GET.get('next', None)
    if next is not None:
        url += '?next=' + next
    return redirect(url)