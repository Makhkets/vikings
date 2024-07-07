from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import os
import vikings
import vikings.settings

from .forms import MultiplePhotoForm
from .models import Photo

def index(request):
    if request.method == 'POST':
        form = MultiplePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photos = request.FILES.getlist('photos')
            for photo in photos:
                file_name = photo.name
                photo_instance = Photo()
                photo_instance.photo_name = file_name
                file_path = os.path.join(vikings.settings.MEDIA_ROOT, 'photos', file_name)
                with open(file_path, 'wb') as file:
                    for chunk in photo.chunks():
                        file.write(chunk)
                photo_instance.model_field = 'photos/' + file_name
                photo_instance.save()

                ##############
                # paste code #
                ##############

            return render(request, 'success.html', {'form': form})
    else:
        form = MultiplePhotoForm()
    return render(request, 'upload_photo.html', {'form': form})