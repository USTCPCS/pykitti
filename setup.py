from setuptools import setup

setup(
    name='pykitti',
    version='0.1.1',
    description='A minimal set of tools for working with the KITTI dataset in Python',
    author='Lee Clement',
    author_email='lee.clement@robotics.utias.utoronto.ca',
    url='https://github.com/utiasSTARS/pykitti',
    download_url='https://github.com/utiasSTARS/pykitti/tarball/0.1.1',
    packages=['pykitti'],
    install_requires=['numpy', 'matplotlib']
)
