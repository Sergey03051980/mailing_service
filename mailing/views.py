from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Count
from .models import Mailing, Client


class HomeView(TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Статистика для главной страницы
        context['total_mailings'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(status=Mailing.STATUS_STARTED).count()
        context['unique_clients'] = Client.objects.values('email').distinct().count()

        return context


from django.shortcuts import render


# Create your views here.
