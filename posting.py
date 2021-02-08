import os

def getInput():
    global post
    a = input("Enter Post Title: ")
    b = input("Enter Post Content: ")
    post = """
    \n
    <div class="main">
    <h1> Post Title <img align="right" src=static/icon.png></h1>
    <p> Content </p>
    </div>
    \n
    """
    post = post.replace("Post Title", a); post = post.replace("Content", b)
    return post

getInput()

with open('index.html', 'r') as file:
    content = file.readlines()

content[44] = post

with open("index.html", "w") as file:
    file.writelines(content)

print("Post created")

os.system("git add index.html")
os.system("git commit -m 'New Post'")
os.system("git push origin main")


