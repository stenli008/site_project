from django.shortcuts import render


def store_view(request):
    return render(request, 'core/store.html')