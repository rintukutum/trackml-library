import io
import os.path as op

from setuptools import setup

here = op.abspath(op.dirname(__file__))

# Get the long description from the README file
with io.open(op.join(here, 'README.md'), mode='rt', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='trackml',
    version='1.dev0',
    description='TrackML utility library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # url='TODO',
    author='Moritz Kiehn', # TODO who else
    author_email='msmk@cern.ch', # TODO or mailing list
    classifiers=[
        'Development Status :: 3 - Alpha', # TODO update for first release
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['trackml'],
    install_requires=['numpy', 'pandas'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
)
