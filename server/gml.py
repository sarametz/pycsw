# -*- coding: ISO-8859-15 -*-
# =================================================================
#
# $Id$
#
# Authors: Tom Kralidis <tomkralidis@hotmail.com>
#
# Copyright (c) 2010 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

from lxml import etree
import gml

def get_bbox(bbox):
    tmp = bbox.find('{http://www.opengis.net/ogc}PropertyName')
    if tmp is not None:
        pname = tmp.text
        if pname not in ['ows:BoundingBox','/ows:BoundingBox']:
            return 'Invalid PropertyName: %s' % pname 
        tmp2 = bbox.find('{http://www.opengis.net/gml}Envelope/{http://www.opengis.net/gml}lowerCorner')
        if tmp2 is None:
            return 'Missing gml:lowerCorner'
        else:
           ll = tmp2.text

        tmp2 = bbox.find('{http://www.opengis.net/gml}Envelope/{http://www.opengis.net/gml}upperCorner')
        if tmp2 is None:
            return 'Missing gml:upperCorner'
        else:
           ur = tmp2.text

        min = ll.split()
        max = ur.split()

        bbox2 = '%s,%s,%s,%s' %(min[0],min[1],max[0],max[1])
        return bbox2