from django.shortcuts import render
from mailing.models import Mailing, Client

def home(request):
    context = {
        'mailings_count': Mailing.objects.count(),
        'active_mailings': Mailing.objects.filter(status='started').count(),
        'clients_count': Client.objects.count(),
    }
    return render(request, 'mailing/home.html', context)
