from setuptools import setup

setup(
    name='pylbxd',
    version='0.1.0',
    description='A wrapper for the Letterboxd API.',
    url='https://github.com/rjww/pylbxd',
    author='Robert Woods',
    author_email='pylbxd@robertwoods.me',
    license='MIT',
    packages=['pylbxd'],
    install_requires=['requests'],
    zip_safe=False)
