from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the README.
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

# Get the version from coorblimey/__init__.py.
with open('coorblimey/__init__.py') as init:
    for line in init:
        if line.startswith("__version__"):
            version = eval(line.split("=")[1].strip())
            break

# Get requirements from requirements.txt.
with open('requirements.txt') as reqs:
    install_requires = [line.strip() for line in reqs]


setup(name='coorblimey',
      version=version,
      description="coorblimey is an open source Python3 library to transform geocentric coordinates to geographic, and vice versa.",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author="Louise Ireland",
      author_email='louireland@gmail.com',
      url='https://github.com/lo-ise/coorblimey',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      extras_require={},
      entry_points="""
      [console_scripts]
      coorblimey=coorblimey.script:main
      """
      )
