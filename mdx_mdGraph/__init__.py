#!/usr/bin/env python
"""
Create graphs in markdown using the google graph api

>>> import markdown
>>> md = markdown.Markdown(extensions=['mdGraph'])
>>> h = md.convert('http://test.test.com')
>>> h
"""

import os
import re
import sys
import urllib
import markdown

def _is_numeric(x):
    try:
        float(x)
        return True
    except:
        return False
    
class GraphProcessor(markdown.blockprocessors.BlockProcessor):

    GCHURL = 'https://chart.googleapis.com/chart?'

    def test(self, parent, block):
        if not "\n" in block:
            return False
        if block[:2] != '!!':
            return False
        return True
    
    def run(self, parent, blocks):
        """ Parse a table block and build table. """

        rows = blocks.pop(0).split("\n")
        title = rows.pop(0)[2:].strip()

        xtra = [x for x in rows if x[:2] == '!#']        
        rows = [x.strip().split() for x in rows if x[:2] != '!#']
        
        col_headers = rows.pop(0)
        
        data = {}
        data['chs'] = '800x200'
        data['chbh'] = 'a,0,10'
        data['chds'] = 'a'
        data['chxt'] = 'x,y'
        data['chco'] = '4D89F9,C6D9FD'
        data['cht'] = 'bvg'
        data['chtt'] = title
        data['chdl'] = '|'.join(col_headers)
        data['chxl'] = '0:|' + "|".join([x[0] for x in rows])
        data['chma'] = '5,5,5,5'
        chd = []
        for col in range(1,len(rows[0])):
            d = ','.join([x[col] for x in rows])
            chd.append(d)            
        data['chd'] = 't:' + "|".join(chd)

        for x in xtra:
            for a in x[2:].strip().split():
                k,v = a.split("=", 1)
                data[k] = v
                #
        
        imgUrl = self.GCHURL + urllib.urlencode(data)
        el = markdown.etree.SubElement(parent, "img")
        el.set('src', imgUrl)
        


class mdGraphExtensions(markdown.Extension):
    """ mdGraph Extension for Python-Markdown. """
    def extendMarkdown(self, md, md_globals):
        md.parser.blockprocessors.add(
            'graph', 
            GraphProcessor(md.parser),
            '<hashheader')
    
    # """ Insert """
    #    md.inlinePatterns['autolink'] = UrlizePattern(URLIZE_RE, md)

def makeExtension(configs=None):
    return mdGraphExtensions(configs=configs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
