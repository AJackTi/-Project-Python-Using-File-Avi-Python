import urllib
from lxml import html

def getHTML(urllink):
    page = html.fromstring(urllib.urlopen(urllink).read())

    arrLinkFileAvi = []
    for link in page.xpath("//a"):
        if link.get("href").endswith('.avi'):
            arrLinkFileAvi.append( urllink + link.get("href") )

    return arrLinkFileAvi