import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_qiniu.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='aaron',
    author_email='arstman@foxmail.com',
    description=description,
    keywords='Lektor plugin',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-qiniu',
    packages=find_packages(),
    py_modules=['lektor_qiniu'],
    # url='[link to your repository]',
    version='0.1',
    install_requires=[
        'Lektor',
        'qiniu'
    ],
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],
    entry_points={
        'lektor.plugins': [
            'qiniu = lektor_qiniu:QiniuPlugin',
        ]
    }
)
