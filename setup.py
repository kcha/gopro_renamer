from setuptools import setup

setup(
    name = 'gopro_renamer',
    author = 'Kevin Ha',
    version = '3.2',
    py_modules = ['gopro_chapter_renamer'],
    entry_points = {
        'console_scripts': ['gopro_renamer = gopro_chapter_renamer:main']
    }
)
