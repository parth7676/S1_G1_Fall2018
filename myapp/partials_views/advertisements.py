from myapp.forms.advertisement import CreateAdvertisementForm
from django.shortcuts import render, redirect


def create_advertisement(request):
    form = CreateAdvertisementForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('create-advertisement')
    return render(request, 'advertisement_form.html', {'form': form })
