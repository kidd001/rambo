from setuptools import setup

setup(name='rambo',
      version='0.1',
      description='Ram your images into sprites with Rambo',
      url='https://github.com/springload/rambo.git',
      author='Springload',
      author_email='josh@springload.co.nz',
      license='MIT',
      packages=['rambo'],
      install_requires=['pil', 'argparse'],
      scripts=['bin/sprites.sh', 'bin/rambo'],
      zip_safe=False)