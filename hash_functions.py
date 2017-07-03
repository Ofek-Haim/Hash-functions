# -*- coding: utf-8 -*-
"""
This code was written by Ofek Haim.
Python.
v = 0.0.3
Last edit: 3.7.2017
"""
import hashlib


class HaseFunctionsGenerator():
    """
    This class include hase functions,
    you can use them.
    """
    def __init__(self, text=''):
        self.text = text

    def md5_function(self):
        """
        len = 32.
        md5 function.
        """
        return hashlib.md5(self.text).hexdigest()  # len = 32

    def sha1_function(self):
        """
        len = 40.
        sha1 function.
        """
        return hashlib.sha1(self.text).hexdigest()

    def sha224_function(self):
        """
        len = 56.
        sha224 function.
        """
        return hashlib.sha224(self.text).hexdigest()

    def sha256_function(self):
        """
        len = 64.
        sha256 function.
        """
        return hashlib.sha256(self.text).hexdigest()

    def sha384_function(self):
        """
        len = 96.
        sha384 function.
        """
        return hashlib.sha384(self.text).hexdigest()

    def sha512_function(self):
        """
        len = 128.
        sha512 function.
        """
        return hashlib.sha512(self.text).hexdigest()


def main():
    f = HaseFunctionsGenerator("")
    print f.md5_function()
    print f.sha1_function()
    print f.sha224_function()
    print f.sha256_function()
    print f.sha384_function()
    print f.sha512_function()


if __name__ == '__main__':
    main()
