from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='qgtools',
      version='0.1dev1',
      description='A pythonian package for QG related\
              analysis',
      url='http://github.com/crocha700/qgtools',
      author='Cesar B Rocha',
      author_email='crocha@ucsd.edu',
      license='MIT',
      packages=['qgtools'],
      install_requires=[
          'numpy',
      ],
      test_suite = 'nose.collector',
      zip_safe=False)
