from setuptools import setup


setup(
    name='fastqstats',
    version='1.0',
    scripts=['fastqstats'],
    author='',
    description='',
    packages=['FastqStats.src', 'FastqStats.src.utils'],
    python_requires='>=3.5',
    install_requires=['psutil']
)
