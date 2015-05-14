from distutils.core import setup

author = 'daineseh'
author_email = 'daineseh@gmail.com'

maintainer = [author, 'ming']
maintainer_email = [author_email, 'archaicdust@gmail.com']

long_description = open('README.md').read() + "\n\n"

setup(name='pytranfer',
      version='1.0',
      description='a tranfer.sh wrapper',
      long_description=long_description,
      author=', '.join(author),
      author_email=', '.join(maintainer_email),
      url='https://github.com/daineseh/py-transfer.sh',
      py_modules=['transfer_option'],
      scripts=['scripts/pt.py'],
      classifiers=[
          'Enviroment :: Console',
          'Intended Audience :: End User/Desktop',
          'Operating System :: OS Independent'
          ]
     )
