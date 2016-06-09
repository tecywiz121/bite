from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    with open('README.md') as f:
        long_description = f.read()

setup(  name='bite',
        version='0.0.1',
        description='Bidirectional iterators',

        author='Sam Wilson',
        author_email='tecywiz121@hotmail.com',

        url='https://github.com/tecywiz121/bite',

        license='LGPL',

        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
        ],

        packages=['bite'])
