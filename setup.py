i# coding: utf-8

from setuptools import setup, find_packages

setup(
	name = 'thumbor_indexed_file_result_storage',
	version = "1",
	description = 'Thumbor File result storage, indexed by Redis',
	author = 'Clif Reeder',
	author_email = 'clif@voxmedia.com',
	zip_safe = False,
	include_package_data = True,
	packages=find_packages(),
	requires=['thumbor','redis']
)
