"""This is the installation toolset for this project."""
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='cotizacion_mep_bot',
      version='0.5.0',
      author='dantebarba',
      description='Bot para las cotizaciones del dolar MEP',
      long_description=long_description,
      install_requires=["python-telegram-bot==11.1.0", "requests"],
      packages=find_packages(exclude=('tests',)),
      entry_points={
          'console_scripts': [
              'cotizacion_mep_bot = cotizacion_mep_bot.__main__:main'
          ]
      })
