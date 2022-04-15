import requests
from bs4 import BeautifulSoup


def first_version(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    print(a, b, c)

first_version(1, 2, 3)