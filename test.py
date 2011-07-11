#!/usr/bin/env python

import markdown

md = markdown.Markdown(extensions=['mdGraph'])

with open('test.md') as F:
    raw = F.read()

convert = md.convert(raw)

with open('test.html', 'w') as G:
    G.write(convert)


