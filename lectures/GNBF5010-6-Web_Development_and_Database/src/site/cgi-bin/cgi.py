#! /usr/local/bin/python3
# -*- coding: UTF-8 -*-

import datetime

name = 'Gang Chen'

print( "Content-type:text/html")
print()
print()
print( '<html>')
print( '<head>')
print( '<meta charset="utf-8">')
print( '<title>Hello Python</title>')
print( '</head>')
print( '<body>')
print( '<h2>A new website is coming soon.</h2>')
print( name+'<br />')
print( str(datetime.datetime.now()))
print( '</body>')
print( '</html>')
