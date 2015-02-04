from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import File


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            instance = File(file=f)
            handle_uploaded_file(instance)
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def handle_uploaded_file(f):
    with open('/tmp/%s' % f.file.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        f.save()