from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import os
import vikings
import vikings.settings

from .forms import PhotoForm
from .models import Photo

def index(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # Получение загруженного изображения из формы
            photo = form.cleaned_data['photo']
            
            # Создание объекта модели Photo с пользовательским именем файла
            file_name = photo.name
            photo_instance = Photo()
            photo_instance.photo_name = file_name
            file_path = os.path.join(vikings.settings.MEDIA_ROOT, 'photos', file_name)
            
            # Сохранение загруженного файла в директорию
            with open(file_path, 'wb') as file:
               for chunk in photo.chunks():
                   file.write(chunk)
                   
            # Сохранение имени файла в модель Photo
            photo_instance.model_field = 'photos/' + file_name
            photo_instance.save()
            
            return render(request, 'success.html', {'form': form})
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})
