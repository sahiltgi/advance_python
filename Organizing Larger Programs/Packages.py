"""
Python is mainly based on packages and packages can be called/ used using 'import' :keyword
"""

import urllib
import urllib.request

print(type(urllib))
print(type(urllib.request))
print(urllib.__path__)
# print(urllib.request.__path__)

'''
Packages are generally directories
Modules are generally files
'''

'''
How Python Locates Modules
= Looks into the files system for the modules
'''