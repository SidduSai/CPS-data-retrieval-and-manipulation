from importlib import import_module
import os

def import_plugin(plugin):
	return import_module('plugins.%s'%plugin)

def extension_loader():
	plugins = []

	black_list = ['__init__.py', 'CPS_ALID_P6_SD3.py', 'CPS_ALID_P6_SD2.py']

	for plugin in os.listdir('plugins'):
		if plugin.endswith('.py') and plugin not in black_list:
			plugins.append(import_plugin(plugin.replace('.py','')))

	return plugins
