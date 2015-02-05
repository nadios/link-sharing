import binascii
import os
import logging

from .models import Token


def generate_token():
    """
        Generates and saves new token with random key

        Returns the token
    """
    token = Token(key=binascii.hexlify(os.urandom(16)))
    token.save()
    return token





