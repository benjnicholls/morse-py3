from setuptools import setup

setup(
    name='morse-py3',
    version='1.1.0',
    scripts=['morse.py'],
    entry_points={
        'console_scripts': [
            'morse-py3=morse:output'
        ]
    },
    install_requires=[
        # List any dependencies here
        'argparse',
    ],
    author='Ben Nicholls',
    author_email='benn.andrews2022@gmail.com',
    description='Morse code translator and generator',
    license='MIT',
    keywords='morse code translator text',
    url='https://github.com/benjnicholls/morse-py3',
)
