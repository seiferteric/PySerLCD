from setuptools import setup, find_packages

setup(
    name = "PySerLCD",
    version = "0.0.1",
    packages = find_packages(),
    author = "Eric Seifert",
    author_email = "seiferteric@gmail.com",
    description = "Library to drive the sparkfun SerLCD",
    install_requires = ['pySerial']
    )
