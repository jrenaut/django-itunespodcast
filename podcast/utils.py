from __future__ import unicode_literals

import re
from xml.sax.saxutils import escape as _escape

from django.utils.xmlutils import SimplerXMLGenerator

try:
    from django.utils.xmlutils import UnserializableContentError
except ImportError:  # < Django 1.9
    class UnserializableContentError(ValueError):
        pass


class EscapeFriendlyXMLGenerator(SimplerXMLGenerator):
    """Subclass of Django's SimplerXMLGenerator.

    Django's addQuickElement() calls XMLGenerator.characters(), which in turn
    calls xml.sax.saxutils.escape(), which escapes characters too soon.
    This class allows unescaped characters to exist in XML elements.
    https://github.com/django/django/blob/1.10/django/utils/xmlutils.py
    https://docs.python.org/3/library/xml.sax.utils.html
    https://code.djangoproject.com/ticket/15936
    """
    def addQuickElement(self, name, contents=None, attrs=None, escape=True, cdata=False):
        """Convenience method for adding an element with no children."""
        if attrs is None:
            attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            self.characters(contents, escape=escape, cdata=cdata)
        self.endElement(name)

    def characters(self, content, **kwargs):
        if content and re.search(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]', content):
            # Fail loudly when content has control chars (unsupported in XML 1.0)
            # See http://www.w3.org/International/questions/qa-controls
            raise UnserializableContentError('Control characters are not supported in XML 1.0')
        # XMLGenerator.characters(self, content)
        try:
            if content:
                self._finish_pending_start_element()
                if not isinstance(content, str):
                    content = str(content, self._encoding)
        except AttributeError:  # Python 2
            if not isinstance(content, unicode):
                content = unicode(content, self._encoding)
        # Custom kwarg
        if kwargs['escape']:
            content = _escape(content)
        # Custom kwarg
        if kwargs['cdata']:
            content = '<![CDATA[%s]]>' % content
        self._write(content)
