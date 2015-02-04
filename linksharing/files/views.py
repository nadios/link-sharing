import datetime

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .forms import UploadFileForm
from .models import Token, File
from uploader import upload_file


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = upload_file(request.FILES['file'])
            context = {'form': form, 'link': new_file.url,
                       'message': u'File was uploaded. Please use this link to access it'}
            # return HttpResponseRedirect(reverse('upload'))
            return render(request, 'success.html', context)
    else:
        form = UploadFileForm()
        context = {'form': form}
    return render(request, 'upload.html', context)


def storage(request, token_key):
    if request.method == 'GET':
        try:
            token = Token.objects.filter(key=token_key).exclude(expires__lte=datetime.datetime.now())
            file = File.objects.get(token=token)
            abspath = open(file.path, 'r')
            response = HttpResponse(content=abspath.read())
            # response['Content-Type'] = 'application/pdf'
            response['Content-Disposition'] = 'attachment; filename=%s' % file.name
            return response
        except:
            raise Http404("File does not exist")

