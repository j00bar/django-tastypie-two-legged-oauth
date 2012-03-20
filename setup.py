import os
from setuptools import setup, find_packages


VERSION = "0.1"

setup(
    name="fm",
    version = VERSION,
    author="amrox",
    packages=find_packages(),
    namespace_packages = [],
    include_package_data = True,
    zip_safe=False,
    license="None",
    install_requires=["python-oauth2", "django-tastypie"]
)



