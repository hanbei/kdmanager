from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView
from django_tables2.export import ExportMixin

from kader.tables import MemberTable
from .models import Member, Training, Fight


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse('home'))
        else:
            return redirect(reverse('login'))
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))

@login_required
def export_members_to_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="kader.csv"'

    csv_data = Member.objects.all().order_by('name')

    t = loader.get_template('kader/kader.csv')
    c = {
        'data': csv_data,
    }
    response.write(t.render(c))
    return response

@login_required
def export_training_to_csv(request, pk):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="training.csv"'

    training = get_object_or_404(Training, pk=pk)

    t = loader.get_template('kader/training.csv')
    c = {
        'training': training,
    }
    response.write(t.render(c))
    return response


class MemberListView(LoginRequiredMixin, ExportMixin, SingleTableView):
    template_name = 'kader/member_list.html'
    context_object_name = 'members'
    login_url = reverse_lazy('login')
    table_class = MemberTable

    def get_queryset(self):
        return Member.objects.order_by('name')


class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = Member
    template_name = 'kader/member_detail.html'
    login_url = reverse_lazy('home')


class MemberCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'kader.add_member'
    model = Member
    fields = ['name', 'first_name', 'birth_date', 'gender', 'grade', 'email', 'zekken', 'jacket', 'active']
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('home'))
        else:
            return super(MemberCreate, self).post(request, *args, **kwargs)


class MemberUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'kader.change_member'
    model = Member
    fields = ['name', 'first_name', 'birth_date', 'gender', 'grade', 'email', 'zekken', 'jacket', 'active']
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('home'))
        else:
            return super(MemberUpdate, self).post(request, *args, **kwargs)


class MemberDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'kader.delete_member'
    model = Member
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('home'))
        else:
            return super(MemberDelete, self).post(request, *args, **kwargs)


class TrainingListView(LoginRequiredMixin, generic.ListView):
    template_name = 'kader/training_list.html'
    context_object_name = 'trainings'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Training.objects.order_by('-date')


class TrainingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Training
    template_name = 'kader/training_detail.html'
    login_url = reverse_lazy('home')


class TrainingCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'kader.add_training'
    model = Training
    fields = ['date', 'attended']
    success_url = reverse_lazy('training_list')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('training_list'))
        else:
            return super(TrainingCreateView, self).post(request, *args, **kwargs)


class TrainingUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'kader.change_training'
    model = Training
    fields = ['date', 'attended']
    # success_url = reverse_lazy('training_list')
    login_url = reverse_lazy('login')

    def get_success_url(self):
        # reverse('training_detail', args=(self.kwargs['pk'],))
        return reverse_lazy('training_detail', args=(self.kwargs['pk'],))

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('training_detail', args=(self.kwargs['pk'],)))
        else:
            return super(TrainingUpdateView, self).post(request, *args, **kwargs)


class TrainingDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'kader.delete_training'
    model = Training
    success_url = reverse_lazy('training_list')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('training_list'))
        else:
            return super(TrainingDeleteView, self).post(request, *args, **kwargs)


class FightDetailView(LoginRequiredMixin, generic.DetailView):
    model = Fight
    template_name = 'kader/fight_detail.html'
    login_url = reverse_lazy('fight_detail')


class FightCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'kader.add_fight'
    model = Fight
    fields = ['red', 'white', 'red_point_one', 'red_point_two', 'white_point_one', 'white_point_two']
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(self.get_success_url())
        else:
            return super(FightCreateView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('training_detail', args=(self.kwargs['training_pk'],))

    def dispatch(self, request, *args, **kwargs):
        self.training = get_object_or_404(Training, pk=kwargs['training_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Overridden to add the ipsum relation to the `Lorem` instance.
        """
        form.instance.training = self.training
        return super().form_valid(form)


class FightUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'kader.change_fight'
    model = Fight
    fields = ['red', 'white', 'red_point_one', 'red_point_two', 'white_point_one', 'white_point_two']
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(self.get_success_url())
        else:
            return super(FightUpdateView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('training_detail', args=(self.kwargs['training_pk'],))

class FightDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'kader.delete_fight'
    model = Fight
    success_url = reverse_lazy('training_list')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(self.get_success_url())
        else:
            return super(FightDeleteView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('training_detail', args=(self.kwargs['training_pk'],))
