import binascii
import os
from .models import Token


def generate_token():
    token = Token(key=binascii.hexlify(os.urandom(10)))
    token.save()
    return token





