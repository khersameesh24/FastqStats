from setuptools import setup


setup(
    name='fastqstats',
    version='1.0',
    scripts=['fastqstats'],
    author='',
    description='',
    packages=['FastqStats.src', 'FastqStats.src.utils'],
    install_requires=[
        'setuptools',
    ],
    python_requires='>=3.5'
)