from setuptools import setup, find_packages

with open('README.md', 'rb') as f:
    long_description = f.read()

setup(
    name='rjob',
    version='1.0',
    author='Baryshnikov Aleksandr (reddec)',
    author_email='owner@reddec.net',
    description='Dummy simple remote task executor',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/reddec/rjob',
    packages=find_packages(),
    install_requires=[],
    setup_requires=['wheel'],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: System :: Distributed Computing'
    ]
)
