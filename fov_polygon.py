'''

    Developed by Mikolaj Czerkawski at ESA Phi Lab

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

'''

from pyproj import Geod

_g = Geod(ellps='clrk66')

def fov_points(lon,
               lat,
               radius=100,
               azimuth_angle=0,
               fov_angle=45):
    '''
        lat (float) : latitude value
        lon (float) : longitude value
        radius (float) : (metres) line of sight
        azimuth_angle (float or string) : (degrees) azimuth angle of the view
        fov_angle (float) : (degrees) field of view angle
    '''

    if isinstance(azimuth_angle, str):
        azimuth_angle = {
            'N' : 0,
            'E': 90,
            'S' : 180,
            'W': 270
        }[azimuth_angle]
        
    los = _g.fwd(lon, lat, azimuth_angle, radius)[:-1]
    # sides
    left =  _g.fwd(lon, lat, azimuth_angle - fov_angle/2, radius)[:-1]
    right =  _g.fwd(lon, lat, azimuth_angle + fov_angle/2, radius)[:-1]

    return left, los, right

def fov_polygon(lon,
                lat,
                radius=100,
                azimuth_angle=0,
                fov_angle=45):
    '''fov_points - but it returns an entire closed polygon (lat-lon order)'''
    
    left, los, right = fov_points(lon,lat,radius,azimuth_angle,fov_angle)

    return [(lon,lat), left, los, right, (lon,lat)]
