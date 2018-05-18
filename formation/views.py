from django.shortcuts import render

# from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from formation.models import Formation, Office, Infographie, English, Art_Culture, Programmation


# Create your views here.


class FormationList(ListView):
    # model = Formation
    context_object_name = 'formation'
    queryset = Formation.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['formation_list'] = Formation.objects.all()
        return context


class OfficeList(ListView):
    # model = Formation
    context_object_name = 'formation'
    queryset = Office.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['office_list'] = Office.objects.all()
        return context


class InfographieList(ListView):
    # model = Formation
    context_object_name = 'formation'
    # template_name = 'formation/infographie_list.html'
    queryset = Infographie.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['infographie_list'] = Infographie.objects.all()
        return context


class ArtList(ListView):
    # model = Formation
    context_object_name = 'formation'
    queryset = Art_Culture.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['art_culture_list'] = Art_Culture.objects.all()
        return context


class EnglishList(ListView):
    # model = Formation
    context_object_name = 'formation'
    queryset = English.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['art_culture_list'] = English.objects.all()
        return context


class ProgrammationList(ListView):
    # model = Formation
    context_object_name = 'formation'
    queryset = Programmation.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['entrepeneuriat_list'] = Programmation.objects.all()
        return context


# class FormationDetail(DetailView):
#
#     queryset = Formation.objects.all
#
#     def get_object(self, queryset=None):
#         # Call the superclass
#         object = super().get_object()
#         # Record the last accessed date
#         object.last_accessed = timezone.now()
#         object.save()
#         # Return the object
#         return object

