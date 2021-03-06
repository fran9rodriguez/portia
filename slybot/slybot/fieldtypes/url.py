from urlparse import urljoin
from scrapely.extractors import url as strip_url
from scrapy.utils.url import safe_download_url
from scrapy.utils.markup import unquote_markup
from slybot.baseurl import get_base_url

class UrlFieldTypeProcessor(object):
    """Renders URLs as links"""

    name = 'url'
    description = 'URL'
    limit = 80

    def extract(self, text):
        return strip_url(text)

    def adapt(self, text, htmlpage=None):
        if htmlpage is None:
            return text
        text = text.encode(htmlpage.encoding)
        joined = urljoin(get_base_url(htmlpage).encode(htmlpage.encoding), text)
        return safe_download_url(unquote_markup(joined, encoding=htmlpage.encoding))
