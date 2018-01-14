from setuptools import setup

setup(
	name='fb',
	version=1.0,
	py_modules=[
		'fb',
	],
	install_requires=[
		'bs4',
		'BeautifulSoup',
		'mechanize',
		'click',
	],
	entry_points={
		'console_scripts':[
		'fb=fb:cli',
		]
	},
)
