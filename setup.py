from setuptools import setup, find_packages

setup(
    name='crumbly',
    version='0.1',
    author='NoodleDX',
    packages=find_packages(),
    description='A Python library for versatile and user-friendly data storage and management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/noodledx/crumbly',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)

# dang it gh actions look see the setup.py is RIGHT HERE