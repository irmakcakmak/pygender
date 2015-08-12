from setuptools import setup, Extension, find_packages

module=Extension(
    'pygender',
    sources = ['pygender.c'],
)

setup(
    name='pygender',
    version='0.0.6',
    description = 'Python wrapper for gender.c',
    author = 'Irmak Cakmak',
    author_email = 'irmak@fastmail.com',
    url = 'https://github.com/irmakcakmak/pygender',
    license = 'LGPL',
    packages = find_packages(),
    package_data={
        'pygender': ['nam_dict.txt'],
    },
    include_package_data = True,
    data_files=[
       ('/var/lib/gender', ['nam_dict.txt'])
    ],
    ext_modules=[module]
)
