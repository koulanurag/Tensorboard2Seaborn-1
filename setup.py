from os import path

from setuptools import setup

setup(name='tensorboard2seaborn',
      version='0.0.1',
      description='Plot Tensorflow Summary event in a beautiful way '
                  '(using seaborn actually) instead of using Tensorboard.',
      long_description=open(path.join(path.abspath(path.dirname(__file__)), 'README.md')).read(),
      long_description_content_type="text/markdown",
      license='MIT',
      author='Anurag Koul',
      url="https://github.com/koulanurag/tensorboard2seaborn",
      install_requires=[x.strip() for x in
                        open(path.join(path.abspath(path.dirname(__file__)), 'requirements.txt')).readlines()],
      py_modules=['tensorboard2seaborn'],
      packages=['tensorboard2seaborn'],
      classifiers=(
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Science/Research",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ),
      entry_points='''
                    [console_scripts]
                    tensorboard2seaborn=tensorboard2seaborn.main:main
                    ''',
      )
