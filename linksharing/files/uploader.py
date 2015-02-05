from .models import File
from token import generate_token
from file_encryption import encrypt_file, decrypt_file
import logging

logger = logging.getLogger(__name__)


def upload_file(file):
    """
        Uploads file on server, stores encrypted version

        file
            represents an instance of file to be stored

        Returns the new File instance

    """
    try:
        token = generate_token()
        filepath = 'data/%s.enc' % token.key
        new_file = File(name=file.name, token=token, path=filepath,
                        url="/storage/%s" % token.key)
        encrypt_file(file, token.key, filepath)
        new_file.save()
        return new_file
    except Exception as e:
        logger.error("Unable to upload the file: ", e)


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
        logger.error("Unable to download the file: ", e)