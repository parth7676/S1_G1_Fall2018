from django.shortcuts import render, redirect
from django.views import generic
from myapp.models import *
from myapp.forms.user import CreateUserForm, ActiveStatusForm
from django.core.paginator import Paginator
from django.views.generic import CreateView


def account(request):
    return render(request, 'account/accountBase.html')


def activate_user(request):
    if request.POST:
        user_id = request.POST['user_id']
        status = request.POST['status']
        if user_id and status:
            user = User.objects.filter(userID=user_id).first()
            status_form = ActiveStatusForm(request.POST)
            if status_form.is_valid():
                user.isActive = status
                user.save()
            return redirect('/users')


class UsersView(generic.ListView):
    template_name = 'account/users.html'
    context_object_name = 'users'

    def get_queryset(self):
        users_list = User.objects.all().order_by('userID')
        paginator = Paginator(users_list, 10)
        page = self.request.GET.get('page')
        return paginator.get_page(page)


class UserCreate(CreateView):
    model = User
    fields = ['firstName', 'lastName', 'email']

