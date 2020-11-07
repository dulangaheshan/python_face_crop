from distutils.core import setup
setup(
  name= 'face_crop',
  packages= ['face_crop'],
  version= '0.1',
  license='MIT',
  description= 'This will automatically identify faces from image and crop faces region in image',
  author= 'dulanga jayarathne',
  author_email= 'dulangah2@gmail.com',
  url= 'https://github.com/user/reponame',
  download_url= 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords= ['face detection', 'python', 'machine learning', 'face crop', 'auto_crop'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)