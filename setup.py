from setuptools import setup, find_packages

setup(
    name='mini_cd',
    version='0.1',
    url='',
    author='',
    author_email='',
    description='',
    packages=find_packages(),
    install_requires=[
        'Flask-API==3.0.post1',
        'Flask==2.0.2',
        'cryptography==36.0.1',
        'redis==4.1.0',
        'rq==1.10.1',
        'waitress==2.1.1',
    ],
    extras_require={
        'build': [
            'shiv',
        ],
    },
    entry_points={
        'console_scripts': [
            'webserver=mini_cd.webserver:main',
        ],
    }
)
