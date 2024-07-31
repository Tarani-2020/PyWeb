from setuptools import setup, find_packages

setup(
    name='PyWeb',
    version='0.1.0',
    author='Nathan Langen',
    author_email='natlanyea@gmail.com',
    description='Are you looking for a simple and easy way to program websites in Python? Then this package is the solution.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
