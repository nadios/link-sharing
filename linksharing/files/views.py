from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .forms import UploadFileForm
from uploader import upload_file


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = upload_file(request.FILES['file'])
            context = {'form': form, 'link': new_file.url,
                       'message': u'File was uploaded. Please use this link to access it'}
            return HttpResponseRedirect(reverse('upload'))
    else:
        form = UploadFileForm()
        context = {'form': form}
    return render(request, 'upload.html', context)


def storage(request, token):
    if request.method == 'GET':
        pass
