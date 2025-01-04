from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UploadedImageForm
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = UploadedImageForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')

def image_list(request):
    images = UploadedImage.objects.all()  # Fetch all uploaded images
    return render(request, 'image_list.html', {'images': images})