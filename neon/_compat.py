# -*- coding: utf-8 -*-


from __future__ import unicode_literals

import sys

PY3 = sys.version_info >= (3, 0)


if PY3:
    unicode = str
else:
    unicode = unicode
