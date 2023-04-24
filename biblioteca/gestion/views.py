from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'gestion/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class AcercaDe(TemplateView):
    template_name = 'gestion/acercade.html'

    def get_context_data(self, **kwargs):
        context = super(AcercaDe, self).get_context_data(**kwargs)
        return context


