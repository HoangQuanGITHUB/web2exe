from setuptools import setup, find_packages

setup(
    name='html2exe_python',
    version='0.6',
    license='MIT',
    author="HoangQuanGITHUB",
    author_email='caohoangquannguyen@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/HoangQuanGITHUB/web2exe',
    keywords='web to app',
    install_requires=[
          'PyQt5',
          'os',
          'sys',
          'pyinstaller'
      ],
)
