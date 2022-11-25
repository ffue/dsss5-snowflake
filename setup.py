from distutils.core import setup

setup(name='snowflake',
      version='1.0',
      description='Drawing snowflakes with tutle',
      author='Florian Fürnohr',
      author_email='florian.fuernrohr@fau.de',
      url='https://github.com/ffue/dsss5-snowflake',
      packages=['snowflake'],
      install_requires=['numpy', 'turtle']
     )