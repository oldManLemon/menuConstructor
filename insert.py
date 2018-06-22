class Menu(object):
    titles:[]
    links:[]
    slugs:[]
    def __init__(self,titles,links,slugs):
     self.titles = titles
     self.links = links
     self.slugs = slugs
    


""" OK Read the files for some variables """

details = open("details.txt","r")
lines = details.readlines()
print(lines[0])
print(lines[1])
print(lines[2])
menuTitles = lines[0].split(',')
menuLinks = lines[1].split(',')
menuSlugs = lines[2].split(',')
""" folderTitle = input('Enter the folder name: ') """

test = Menu(menuTitles[0],'.../009','[fusion builder]')
print(test.titles)

details.close()


