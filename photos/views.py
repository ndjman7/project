from django.shortcuts import render, get_object_or_404
from .models import Photo


def detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    context = dict()
    context['photo'] = photo

    # context = {
    #     'photo': photo
    # }
    return render(request, 'photos/detail.html', context)
