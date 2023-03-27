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
        'Jinja2==3.0.3',
        'MarkupSafe==2.0.1',
        'PyYAML==6.0',
        'Werkzeug==2.0.2',
        'ansible==2.9.18',
        'cffi==1.15.0',
        'click==8.0.3',
        'cryptography==36.0.1',
        'itsdangerous==2.0.1',
        'packaging==21.3',
        'pycparser==2.21',
        'pyparsing==3.0.6',
        'redis==4.5.3',
        'rq==1.10.1',
        'waitress==2.1.1',
        'wheel==0.38.1',
        'wrapt==1.13.3',
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
