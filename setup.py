from distutils.core import setup
import py2exe

file_group_root = (".",[
	  "index.html",
	  "byebye.html",
	  "thanks.html"
	])

setup(
	console=['webserver.py'],
	data_files=[file_group_root]
)
