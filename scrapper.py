
from pyquery import PyQuery
import urllib.request
import pprint


url = 'https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D'
pp = pprint.PrettyPrinter(indent=4)

def main():
    url = "https://developer.mozilla.org/en-US/docs/Web/API"
    with urllib.request.urlopen(url) as response:
       html = response.read()

    f = open('all.html', 'wb')
    f.write(html)
    f.close

    pq= PyQuery(html)
    objects = [i.attr('href') for i in pq('div div.index ul li a').items()]
    pp.pprint(objects)


def parse_url(url):
    with urllib.request.urlopen(url) as response:
       html = response.read()

    f = open('file.html', 'wb')
    f.write(html)
    f.close

    pq= PyQuery(html)
    object = pq('code')
    tag= pq('li.toggle')
    print(object.text())

    properties = tag.text().split('textBaseline Methods')[0].replace('Properties','').split('\n');
    methods= tag.text().split('textBaseline Methods')[1].split('\n');
    #print('Properties')
    #print(properties)
    #print('\n Methods')
    #print(methods)

if __name__ == '__main__':
    main()
