from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
from web.models import Painting, Project
import random


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {"title": "💀"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paintings = Painting.objects.all()
        if paintings:
            context['painting'] = random.choices(Painting.objects.all())[0]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
    extra_context = {"title": "About"}


class ProjectsView(ListView):
    template_name = 'projects.html'
    queryset = Project.objects.order_by('priority')
    context_object_name = 'projects'
    extra_context = {"title": "Projects"}


class ProjectView(DetailView):
    template_name = 'project.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().name
        return context

    def get(self, *args, **kwargs):
        response = super().get(*args, **kwargs)
        if self.object.redirect and self.object.link:
            return HttpResponseRedirect(self.object.link)
        return response


class ContactView(TemplateView):
    template_name = 'contact.html'
    extra_context = {"title": "Contact"}
