from setuptools import setup

setup(name='poker-specialist',
      version='0.1',
      description='We are the specialists',
      license='MIT',
      install_requires=[
          'pyknow',
          'lark-parser',
          'python-dotenv'
      ],
    
      zip_safe=False)