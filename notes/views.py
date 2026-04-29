from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import NotesForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Q


from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = reverse_lazy('notes.list')
    template_name = 'notes/notes_delete.html'

    login_url = "/login/"
    
    def get_queryset(self):
        return self.request.user.notes.all()


class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    success_url = reverse_lazy('notes.list')
    form_class = NotesForm

    login_url = "/login/"
    
    def get_queryset(self):
        return self.request.user.notes.all()


class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = reverse_lazy('notes.list')
    form_class = NotesForm

    login_url = "/login/"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_tags(self.object)
        return HttpResponseRedirect(self.get_success_url())
    

class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/login/"
    
    def get_queryset(self):
        queryset = self.request.user.notes.all().prefetch_related('tags')
        query = self.request.GET.get('q', '').strip()
        tag_name = self.request.GET.get('tag', '').strip()

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(text__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()

        if tag_name:
            queryset = queryset.filter(tags__name__iexact=tag_name).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '').strip()
        context['active_tag'] = self.request.GET.get('tag', '').strip()
        context['all_tags'] = self.request.user.notes.filter(tags__isnull=False).values_list('tags__name', flat=True).distinct().order_by('tags__name')
        return context


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"

    login_url = "/login/"
    
    def get_queryset(self):
        return self.request.user.notes.all()


    
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def detail(request, pk):
#     note = Notes.objects.get(pk = pk)
#     return render(request, 'notes/notes_details.html', {'note': note})
     