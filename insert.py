from menu import *
from slug import *
import re
import os


class Menu(object):
    titles: []
    links: []

    def __init__(self, titles, links):
        self.titles = titles
        self.links = links


""" OK Read the files for some variables """

details = open("details.txt", "r")
lines = details.readlines()
print(lines[0])
print(lines[1])
print(lines[2])
menuTitles = lines[0].split(',')
menuLinks = lines[1].split(',')
menuSlugs = lines[2].split(',')
details.close()
folderTitle = input('Enter the folder name for your set: ')
dirc = os.mkdir(folderTitle)
os.chdir("%s" % folderTitle)

if len(menuTitles) != len(menuLinks) and len(menuSlugs):
    print('All Arrays should be equal length, please go back and check arrays')


for title, link in zip(menuTitles, menuLinks):
    Menu(title, link)
    output = open("menuCreate.html", "w+")
    output.write(menuTopHtml)
    for title, link in zip(menuTitles, menuLinks):
        output.write('<li><a href="' + link +
                     '" class="alert-link">'+title+'</a></li>')
    output.write(menuBottomHtml)
    output.close()

""" Create the slugs and thier pages """


for title, slug in zip(menuTitles, menuSlugs):
    title = re.sub("[^a-zA-Z]+", "", "%s" % title)
    output = open("%s.html" % title, "w+")
    getMenu = open("menuCreate.html", "r")
    readMenu = getMenu.read()
    output.write(slugTop + readMenu + slugMiddle + slug + slugBottom)
    getMenu.close()
    output.close()

os.remove("menuCreate.html")
