import datetime

from django.http import HttpResponse, StreamingHttpResponse, Http404, HttpResponseNotAllowed
from django.shortcuts import render

from .forms import UploadFileForm
from .models import Token, File
from uploader import upload_file, download_file


def upload(request):
    """
    The view which handles new files uploading
    In case of GET request it return the new form,
    in case of POST request it validates the form
    and stores file returning file download link in
    the response
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = upload_file(request.FILES['file'])
            context = {'form': form,
                       'link': new_file.url,
                       'message': u'File was uploaded. Please use this link to access it'}
            return render(request, 'success.html', context)
    else:
        form = UploadFileForm()
        context = {'form': form}
    return render(request, 'upload.html', context)


def storage(request, token_key):
    """
    The view which handles new files downloading
    In case of GET request it returns the file contents
    """
    if request.method == 'GET':
        try:
            token = Token.objects.filter(key=token_key).exclude(expires__lte=datetime.datetime.now())
            file = File.objects.get(token=token)
            with open(download_file(token_key, file), 'r') as path:
                response = HttpResponse(content=path.read())
                response['Content-Disposition'] = 'attachment; filename=%s' % file.name

                # response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                #                                  content_type="text/csv")
                # response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
                return response
        except:
            raise Http404("File does not exist")
    else:
        raise HttpResponseNotAllowed("Method is not allowed")
