from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, SubjectCombination
from .forms import SubjectForm, SubjectCombinationForm
from django.urls import reverse_lazy
# Create your views here.



class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    
    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Creation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Add Subject'
        return context

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    field_list = [
        'Subject Name', 'Subject Code', 'Creation Date', 'Last Updated'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Subjects'
        context['panel_name']   =   'Subjects'
        context['panel_title']  =   'View Subjects Info'
        context['field_list']   =   self.field_list
        return context

class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Subject
    template_name_suffix = '_form'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:subject_list')

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name_suffix = '_delete'
    success_url = reverse_lazy('subjects:subject_list')

    
    def get_context_data(self, **kwargs):
        context = super(SubjectDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Delete Confirmation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Delete Subject'
        return context
    
class SubjectCombinationCreateView(LoginRequiredMixin, CreateView):
    model = SubjectCombination
    form_class = SubjectCombinationForm
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject to their various classes Creation'
        context['panel_name'] = 'Subject to Classes'
        context['panel_title'] = 'Assign Subjects to Classes'
        return context

class SubjectCombinationListView(LoginRequiredMixin, ListView):
    model = SubjectCombination
    field_list = [
        'Class', 'Subject'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Subject to Classes'
        context['panel_name']   =   'Subject to Classes'
        context['panel_title']  =   'View all Subjects to every Class Info'
        context['field_list']   =   self.field_list
        return context

class SubjectCombinationUpdateView(LoginRequiredMixin, UpdateView):
    model = SubjectCombination
    template_name_suffix = '_form'
    form_class = SubjectCombinationForm
    success_url = reverse_lazy('subjects:subject_combination_list')

class SubjectCombinationDeleteView(LoginRequiredMixin, DeleteView):
    model = SubjectCombination
    template_name_suffix = "_delete"
    success_url = reverse_lazy('subjects:subject_combination_list')

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject to Class Delete Confirmation'
        context['panel_name'] = 'Subject to Classes'
        context['panel_title'] = 'Delete Subject to Class'
        return context
