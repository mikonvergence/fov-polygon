# Geobuffers

This repository contains code that allows simple definitions of polygons defined around a coordinate of interest using geodesic distances. Some of the functionality can be reproduced with [geopandas buffer](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.buffer.html) functionality.

Instead, all methods here rely on [pyproj.Geod](https://pyproj4.github.io/pyproj/stable/api/geod.html) geodetic computations using Clarke 1866 Ellipsoid.

## Available shapes

|          | Name    | Parameters | Description |
| -------- | ------- | :--------  | :---------- |
| ()       |  square | `r`        | Square with a distance center-to-corner `r`                                                                    |
| ()       | hexagon | `r`,`a`    | Hexagon with a distance center-to-vertex `r`, with first vertex at azimuth of `a` degrees                      |
| ()       | regpol  | `n`,`r`,`a`| Regular polygon with `n` vertices `r` metres away from the center, with first vertex at azimuth of `a` degrees |
| ()       | fov     | `r`,`a`,`f`| Field of view traingle at distance `r`, pointing towards angle `a` with angular width of `f` degrees           |

## Example Usage
```python
  import geobuffers as gbf
```
