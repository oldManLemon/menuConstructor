from menu import *



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
""" folderTitle = input('Enter the folder name: ') """

if len(menuTitles) != len(menuLinks) and len(menuSlugs):
    print('All Arrays should be equal length, please go back and check arrays')


for title, link in zip(menuTitles, menuLinks):
    Menu(title, link)
    output = open("menuCreate.html", "w+")
    output.write(menuTopHtml)
    for title, link in zip(menuTitles, menuLinks):
        output.write('<li><a href="' + link + '" class="alert-link">'+title+'</a></li>')
    output.write(menuBottomHtml)
    output.close()

""" Create the slugs and thier pages """


