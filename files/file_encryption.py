import random
import struct

from Crypto.Cipher import AES


def encrypt_file(source, key, destination=None, chunksize=64 * 1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        source:
            Name of the input file

        destination:
            If None, '<in_filename>.enc' will be used

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file, must be
            divisible by 16.
    """
    if not destination:
        destination = "%s.enc" % source.name
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    with open(destination, 'wb') as outfile:
        outfile.write(struct.pack('<Q', source.size))
        outfile.write(iv)
        while True:
            chunk = source.read(chunksize)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += ' ' * (16 - len(chunk) % 16)
            outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, source, chunksize=24 * 1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        source:
            Name of the input file

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file, must be
            divisible by 16

        Returns the descrypted file.
    """
    with open(source, 'rb') as infile:
        struct.unpack('<Q', infile.read(struct.calcsize('Q')))
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        while True:
            chunk = infile.read(chunksize)
            if len(chunk) == 0:
                break
            yield decryptor.decrypt(chunk)