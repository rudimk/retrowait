from setuptools import setup

setup(name='retrowait',    
    version='0.1',
    description="A Python adaptation of XKCD's 'Backward in Time'.",
    url='https://github.com/rudimk/retrowait',
    author='Rudraksh MK',
    author_email='rudraksh.mk@gmail.com',
    license='MIT',
    packages=['retrowait'],
    install_requires=[
        'wikipedia',
        'arrow',
    ],
    zip_safe=False)