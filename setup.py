from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name = 'notify',
    version = 0.1,
    description = 'A simple script to show desktop notifications',
    long_description = readme(),
    url = 'https://github.com/pk16',
    author = 'Prateek Kesarwani', 
    author_email = 'prtk.1692@gmail.com',
    packages = ['notify'],
    install_requires=[
          'pushbullet.py',
          'tweepy',
          'beautifulsoup4',
          'requests',
          'yweather'
      ],
    entry_points={
        'console_scripts':[
            'notify = notify.app:main'
            ]
        },
    zip_safe = False
        )
