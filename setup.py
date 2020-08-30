from setuptools import setup

setup(
    name='connectdots',
    version='0.1.0',
    description='A simple package to draw lines between green, red and blue dots on a black image',
    url='https://github.com/espenthaem/connectdots',
    author='Espen Tierolff',
    author_email='e.tierolff@gmail.com',
    license='MIT',
    packages=['connectdots'],
    install_requires=['opencv-python',
                      'numpy',
                      ],

    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)
