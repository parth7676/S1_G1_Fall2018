from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import generic
from myapp.models import User, Password, RoleCode, UserRole
import datetime
from myapp.forms.users import ActiveStatusForm, UserFormWithRelatedFields
from django.core.paginator import Paginator


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


def user_edit_view(request, user_id):
    user = User.objects.get(userID=user_id)
    form = UserFormWithRelatedFields(request.POST or None, instance=user)

    if request.POST:
        if form.is_valid():
            user = form.save(commit=False)
            new_password = request.POST['password']
            new_roles = request.POST.getlist('role')
            if new_password:
                password = Password.objects.filter(user__userID=user_id).first()
                password.password = make_password(new_password)
                password.save()

            if new_roles:
                # delete prev roles
                UserRole.objects.filter(user_id=user.userID).delete()

                # add new roles
                roles = RoleCode.objects.filter(roleName__in=new_roles)
                for role in roles:
                    user_role = UserRole(user_id=user.userID, role_id=role.id)
                    user_role.save()
                    user.roles.add(user_role)
                    user.save()

                form.save_m2m()
            user.save()
            return redirect('/users/edit/' + user_id)
    else:
        if form.is_valid():
            form.save()
            return redirect('users')

        context = {
            'form': form,
            'isEdit': True,
            'userID': user.userID
        }
        return render(request, 'account/user_form.html', context)


def user_create_view(request):
    form = UserFormWithRelatedFields(request.POST or None)

    if request.POST:
        if form.is_valid():
            user = form.save()
            new_password = request.POST['password']
            new_role = request.POST['role']

            if new_password:
                password = Password()
                password.password = make_password(new_password)
                password.userAccountExpiryDate = datetime.date.today() + datetime.timedelta(30)
                password.user = user
                password.save()

            if new_role:
                role = RoleCode.objects.filter(roleName=new_role).first()
                user_role = UserRole()
                user_role.user = user
                user_role.role = role
                user_role.save()

            return redirect('/users')
    else:
        if form.is_valid():
            form.save()
            return redirect('users')

        context = {
            'form': form,
            'isEdit': False
        }
        return render(request, 'account/user_form.html', context)


class UsersView(generic.ListView):
    template_name = 'account/users.html'
    context_object_name = 'users'

    def get_queryset(self):
        users_list = User.objects.prefetch_related('roles').all().order_by('userID')
        paginator = Paginator(users_list, 10)
        page = self.request.GET.get('page')
        return paginator.get_page(page)