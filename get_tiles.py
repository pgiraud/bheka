# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import urllib2
import re
import json
import string

from utils import get_tiles_in_geom

from shapely.geometry import Polygon
from shapely.wkt import loads


def get_tiles(zoom=18):
    """
    Create a list of tiles for the spherical mercator grid that are in the
    given geometry.
    :arg zoom:zoom level 
    :returns: A list of tiles.
    :rtype: list
    """
    #polygon = loads('POLYGON((3159925.8581263926 -339972.7925080684, 3160728.4469232745 -341597.0793589013, 3161875.002347393 -341081.1294180469, 3161875.002347393 -340393.19616357837, 3161282.6153782653 -339800.8091944527, 3159925.8581263926 -339972.7925080684))')
    polygon = loads('POLYGON((3210966.6837567138 -279377.3383434296, 3210966.6837567138 -277542.8496648408, 3212954.046491852 -277542.8496648408, 3212954.046491852 -279377.3383434296, 3210966.6837567138 -279377.3383434296))')
    return get_tiles_in_geom(polygon, zoom)

if __name__ == '__main__':
    file = open('tasks.json', 'w')
    tiles = get_tiles()
    file.write(json.dumps(tiles))
    print "Done: %d tiles added" % len(tiles)
    file.close()
