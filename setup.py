from setuptools import setup, find_packages

setup(
    name='dj_docs',
    version='0.1',
    description='Document creation library for Django',
    author='Sreeshanth Thekkedath',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/mylibrary',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)