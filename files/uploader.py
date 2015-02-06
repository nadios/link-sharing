import logging
import os

from .models import File

from token import generate_token
from file_encryption import encrypt_file, decrypt_file
import settings

logger = logging.getLogger(__name__)


def upload_file(file, domain = None):
    """
        Uploads file on server, stores encrypted version

        file
            represents an instance of file to be stored

        Returns the new File instance

    """
    try:
        token = generate_token()
        directory = getattr(settings, 'DATA_FOLDER', 'data')
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = '%s/%s.enc' % (directory, token.key)
        if not domain:
            domain = getattr(settings, 'DOMAIN')
        new_file = File(name=file.name, token=token, path=filepath,
                        url="%s/storage/%s" % (domain, token.key))
        encrypt_file(file, token.key, filepath)
        new_file.save()
        return new_file
    except Exception as e:
        logger.error("Unable to upload the file: %s", e)


def download_file(key, file):
    """
    Uploads file on server, stores encrypted version

    key
        used to decrypt file contents

    file
        instance of file which should be downloaded

    Returns decrypted file object

    """
    try:
        return decrypt_file(key, file.path)
    except Exception as e:
        logger.error("Unable to download the file: %s", e)