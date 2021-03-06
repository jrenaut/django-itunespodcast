from __future__ import unicode_literals

from django.conf import settings


PODCAST_SINGULAR = getattr(settings, 'PODCAST_SINGULAR', True)

PODCAST_ID = getattr(settings, 'PODCAST_ID', 1)

PODCAST_NO_ARTWORK = getattr(settings, 'PODCAST_NO_ARTWORK', 'podcast/img/no_artwork.png')

PODCAST_PAGINATE_BY = getattr(settings, 'PODCAST_PAGINATE_BY', 10)
