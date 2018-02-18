from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm


def detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    context = dict()
    context['photo'] = photo

    return render(request, 'photos/detail.html', context)


def create(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)

    if request.method == 'GET':
        form = PhotoForm()
    elif request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        # ToDo 1. 가져온 데이터를 검증 후, 맞다면 Photo 모델을 생성한다. 생성 후에 detail page로 리다이렉트 시킨다.

    context = {
        'photo_form': form
    }
    return render(request, 'photos/edit.html', context)


def index(request):
    photos = Photo.objects.all().order_by('-pk')
    context = dict()
    context['photos'] = photos

    return render(request, 'photos/list.html', context)


def delete(request):
    # ToDo 2. POST 요청으로 온 PK값을 받아서 Photo 모델이 맞는지 찾는다.
    # ToDo 3. try/except 구문으로 데이터를 찾으면 삭제 후 list page를 찾지 못하면, detail page를 리다이렉트 시킨다.
    pass
