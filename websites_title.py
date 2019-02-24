import urllib.request
from pyquery import PyQuery


def get_url_title(url):
    html = urllib.request.urlopen(url)
    content = html.read()
    pq = PyQuery(content)
    tag = pq("title")
    print(tag.text())


def main():
    while True:
        input_url = input("Enter url: \n")
        get_url_title(input_url.strip())


if __name__ == '__main__':
    main()