from setuptools import setup

setup(
    name = 'gopro_renamer',
    author = 'Kevin Ha',
    version = '0.3.3',
    py_modules = ['gopro_chapter_renamer'],
    entry_points = {
        'console_scripts': ['gopro_renamer = gopro_chapter_renamer:main']
    }
)
