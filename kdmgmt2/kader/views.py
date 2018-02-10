from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

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


class MemberListView(LoginRequiredMixin, generic.ListView):
    template_name = 'kader/member_list.html'
    context_object_name = 'members'
    login_url = reverse_lazy('login')

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
    permission_required = 'kader.add_member'
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
    permission_required = 'kader.change_member'
    model = Training
    fields = ['date', 'attended']
    success_url = reverse_lazy('training_list')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('training_list'))
        else:
            return super(TrainingUpdateView, self).post(request, *args, **kwargs)


class TrainingDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'kader.delete_member'
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
    permission_required = 'kader.add_member'
    model = Fight
    fields = ['red','white','red_point_one','red_point_two','white_point_one','white_point_two']
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect(reverse_lazy('training_list'))
        else:
            return super(FightCreateView, self).post(request, *args, **kwargs)
