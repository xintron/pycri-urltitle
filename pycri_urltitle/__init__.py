# -*- coding: utf-8 -*-
import re
import urllib2

import lxml.html

from pycri.plugins import IRCObject
from pycri.globals import g

class URLTitle(IRCObject):

    logger = g.getLogger(__name__)
    http = re.compile('(https?://[^\s$]+)')

    def on_privmsg(self, irc, prefix, params):
        msg = params[-1]

        m = self.http.search(msg)
        if not m:
            return

        resp = self.fetch_title(m.group(0))
        if resp:
            channel = params[0]
            irc.msg(channel, '» Title: {}'.format(resp))

    def fetch_title(self, url):
        self.logger.debug('Fetching title for URL: {}'.format(url))
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) \
                Gecko/17.0 Firefox/17.0'}
        req = urllib2.Request(url, None, headers)
        fp = urllib2.urlopen(req)
        if not fp:
            return
        info = fp.info()

        if info.getmaintype() == 'text':
            title = self.parse_title(fp.read())
            if title is None:
                return

        return title

    def parse_title(self, htmlstring):
        html = lxml.html.document_fromstring(htmlstring)
        title = html.find('*/title')
        if title is None:
            return

        return title.text.encode('iso-8859-1').replace('\n', '').strip()
