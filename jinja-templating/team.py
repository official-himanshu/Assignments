#!/usr/bin/python
#
# SCRIPT: Jinja template assignment
# AUTHOR: Himanshu Chaudhary
# DATE:   03/09/2020
# REV:    1.1.A 
#
#
# PLATFORM: Specific for bash
# 
# PURPOSE: A clear, even if required lenghty, use-case.
# REV LIST:
#    DATE        : Date of revision
#    BY          : AUTHOR OF MODIFICATION
#    MODIFICATION: Describe the chages made. What do they enhance.
# 
# set -n   # Uncomment to check script syntax, without execution.
#          # NOTE: Do forget comment it back as it won't allow the 
#          # the script to execute.
#
#
#
################################################################
#          Define Files and Variables here                     #
# importing Environment and FileSystemLoader  from jinja2 module
from jinja2 import Environment, FileSystemLoader

# defining a list of dictonary defining the names and gender of team mate
team = [
        {'name': 'Himanshu Chaudhary', 'gender': 'male'},
        {'name':'Himanshu Upadhayay', 'gender':'male'},
        {'name':'Kumar Pratik', 'gender':'male'},
        {'name':'Vaibav Tyagi', 'gender':'male'},
        {'name':'Vidushi Bansal', 'gender':'female'}
]

################################################################
################################################################
#          Define Functions here                               #
################################################################
################################################################
#          Beginning of Main                                   #

# We define a file_loader and environment to retrive the template from the templates directory
file_loader = FileSystemLoader('templates')
environment = Environment(loader=file_loader)

# creating template object for retriving templates from the file  using get_templete
template = environment.get_template('showteampeers.txt')

# saving the output into the output variable and passing the dict to render function
output = template.render(teams=team)
print output

################################################################
# End of script
