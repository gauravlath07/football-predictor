# noinspection PyPep8
import urllib
import json
import ConfigParser import SafeConfigParser
import io

url = "http://jokecamp.github.io/epl-fantasy-geek/js/static-data.json
response = urllib.urlopen(url)
data = json.loads(response.read())
# lol = str(data)
# text_file = open("Output.txt", "w")
# text_file.write(lol)
# text_file.close()
i = 0
for obj in data['elements']:
    print obj['first_name'] + " " + obj['web_name']
    i = i + 1
    print i
