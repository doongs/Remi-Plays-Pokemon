import urllib.request

contents = urllib.request.urlopen('https://github.com/doongs/Remi-Plays-Pokemon/blob/main/LICENSE').read()
print(contents)