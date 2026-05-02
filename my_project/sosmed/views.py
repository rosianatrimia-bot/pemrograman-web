from django.shortcuts import render, redirect
from .models import Instagram
from .forms import InstagramForm


def create(request):
    akun_form = InstagramForm(request.POST or None)

    if request.method == 'POST':
        if akun_form.is_valid():
            akun_form.save()
            return redirect('sosmed:list')

    context = {
        "page_title": "Tambah akun",
        "akun_form": akun_form,
    }

    return render(request, 'sosmed/create.html', context)


def list_instagram(request):
    semua_akun = Instagram.objects.all()

    context = {
        'page_title': 'Sosial Media',
        'semua_akun': semua_akun,
    }

    return render(request, 'sosmed/list.html', context)