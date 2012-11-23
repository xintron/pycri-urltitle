# -*- coding: utf-8 -*-
import unittest

from pycri import Pycri
app = Pycri(__name__)

from pycri_urltitle import URLTitle

class URLTitleTestCase(unittest.TestCase):

    def test_parse(self):
        html = """<html><head><title>Täst &amp;\n foobar
        </title></head></html>"""

        title = URLTitle().parse_title(html)
        t = "Täst & foobar"
        self.assertEquals(t, title)

    def test_url(self):
        urls = ['http://xintron.se', 'http://youtu.be/aMYF1svga5Q',
                'http://www.youtube.com/watch?v=aMYF1svga5Q',
                'https://www.google.com/search?hl=en&q=f%C3%B6r']
        titles = ['Marcus Carlsson // Everyday superhero',
                "Rövbajs - munnen fullå me pess - YouTube",
                "Rövbajs - munnen fullå me pess - YouTube",
                "för - Google Search"]
        for i, v in enumerate(urls):
            title = URLTitle().fetch_title(v)
            self.assertEquals(titles[i], title)

if __name__ == '__main__':
    unittest.main()
