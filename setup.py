from setuptools import setup
import configparser

config = configparser.ConfigParser()
config.read('setup.cfg')

setup(
    name=config['application']['package'],
    packages=[config['application']['package']],
    version=config['application']['version'],
    description='Synthesizing Realistic Images From Facial Sketches',
    python_requires=config['application']['python'],
    author=config['application']['author'],
    author_email=config['application']['email'],
    maintainer=config['application']['author'],
    maintainer_email=config['application']['email'],
    license='Not open source',
    entry_points={
        'console_scripts': [
            'sriffs-cli={}.commands.cmd:main'.format(config['application']['package'])
        ]
    }
)
