import os
import re

path = 'C:\\Users\\inhenkel\\Documents\\GitHub\\DocsContent\\singlesource\\selfhelp'
sstring = "pageTitle"

for filename in os.listdir(path):
    print("******************************************")
    print(f"Filename: ", filename)
    v2 = re.search("v2", filename)
    print(v2)
    with open(os.path.join(path, filename), 'r') as f:
        data = f.read()
        title = re.findall(r'pageTitle="(.*?)"', data)
        print(f"pageTitle: ", title)
        description = re.findall(r'description="(.*?)"', data)
        print(f"description: ", description)
        msauthor = re.findall(r'ms.author="(.*?)"', data)
        print(f"ms.author: ", msauthor)
        authors = re.findall(r'authors="(.*?)"', data)
        print(f"authors: ", authors)
        h1 = re.search(r'# (.*?)\n', data)
        h1g = str(h1.group(1))
        vfile = re.search("v2",filename)
        print(f"vfile is: ", vfile)
        if(re.search("v2",filename) == None):
            print("== condition met")
            v = ""
        else:
            print("== condition NOT met")
            v = " v2"
        original_text = data.replace(h1g, h1g + v)
        f.close()
    with open(os.path.join(path, filename), 'w') as f:
        if(re.search("v2",filename) == None):
            v = ""
        else:
            v = " v2"
        f.write("---" + "\n")
        if(len(title)>0):
            f.write("title: " + title[0] + v + "\n")
        else:
            f.write("title: no title " + filename + "\n")
        if(len(description)>0):
            f.write("description: " + description[0] + "\n")
        else:
            f.write("description: none " + filename + "\n")
        if(len(msauthor)>0):
            f.write("ms.author: " + msauthor[0] + "\n")
        else:
            f.write("ms.author: inhenkel" + "\n")
        if(len(authors)>0):
            f.write("authors: " + authors[0] + "\n")
        else:
            f.write("authors: no authors " + filename + "\n")
        f.write("author: IngridAtMicrosoft" + "\n")
        f.write("ms.service: media-services" + "\n")
        f.write("ms.date: 08/5/2022" + "\n")
        f.write("---"+ "\n" + "\n")
        f.write(original_text)
        f.close
