from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='gearbest_api',
    version='0.0.4',
    description='Retrieve info from gearbest api.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/matteobaldelli/python-gearbest-api',
    license='MIT',
    author='Matteo Baldelli',
    author_email='baldelli.matteo2@google.com',
    packages=['gearbest_api'],
    install_requires=['requests'],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
