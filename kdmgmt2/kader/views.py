from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Member


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


@login_required(login_url=reverse_lazy('login'))
def home(request):
    return render(request, 'home.html')


class MemberListView(LoginRequiredMixin, generic.ListView):
    template_name = 'home.html'
    context_object_name = 'members'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Member.objects.order_by('name')


class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = Member
    template_name = 'detail.html'
    login_url = reverse_lazy('home')


class MemberCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'kader.add_member'
    model = Member
    fields = ['name', 'first_name', 'birth_date', 'gender', 'grade', 'email', 'zekken', 'jacket', 'active']
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

class MemberUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'kader.change_member'
    model = Member
    fields = ['name', 'first_name', 'birth_date', 'gender', 'grade', 'email', 'zekken', 'jacket', 'active']
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

class MemberDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'kader.delete_member'
    model = Member
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')