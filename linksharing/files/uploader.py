from .models import File
from token import generate_token


def upload_file(file):
    filepath = '/tmp/files/%s' % file.name
    token = generate_token()
    new_file = File(file=file, name=file.name, token=token, path=filepath,
                    url="/storage/%s" % token.key)
    store_file(filepath, file)
    new_file.save()
    return new_file


def store_file(path, file):
    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)