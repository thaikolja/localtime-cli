from setuptools import setup

setup(
    name='localtime-cli',
    version='1.0.2',
    packages=['localtime'],
    install_requires=['requests', 'dotenvfile'],
    entry_points={
        'console_scripts': [
            'localtime=localtime.cli_tool:main',
        ],
    },
)
