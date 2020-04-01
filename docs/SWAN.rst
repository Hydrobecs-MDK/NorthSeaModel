HydroBeCS user manual and SOP for SWAN
======================================

Introduction
^^^^^^^^^^^^

The swan intro here

Background
^^^^^^^^^^

background of project here


Grid Setup
^^^^^^^^^^
A nested grid system is used:
The NorthSeaModel consists of two main grids:

1. Large grid covering the North Sea Domain and a part of the North East Atlantic
2. Nested grid covering the Belgian continental shelf and parts of Brittain. The Nested grid is nested within the Large grid

The CoastalModel consists of one main grid (nested within the North Sea Domain) and a number of subgrids:

3. Coastal Model covering the whole of the Belgian Coast
4. Various smaller grids located at strategic locations around the Belgian coast:

4.1 Zeebrugge Harbour Area Grid
4.2 Oostende Harbour Area Grid

North Sea Model Grids
---------------------

+---------------------------+---------------+---------------+---------------+
|                           | NorthSeaModel | NorthSeaModel | CoastalModel  |
|                           | Large Grid    | Nested Grid   | Belgium Coast |
+===========================+===============+===============+===============+
| 1.  Grid extends          |               |               |               |
| 1.1 Bottom left (Lon,Lat) | -11.98, 47.97 | 0.72 , 50.87  | 1.98 , 50.92  |
| 1.2 Top Right   (Lon,Lat) |  9.98 , 61.87 | 4.36 , 52.00  | 3.50 , 51.67  |
| 1.3 Grid rotation (deg)   |     0.0       |     0.0       |   * CALC *    |
+---------------------------+---------------+---------------+---------------+
| 2. Spacing  (distance)    |   5km x 5km   |   1km x 1km   |  200m x 200m  |
+---------------------------+---------------+---------------+---------------+
| 3. Cells    (x, y)        |   310 x 280   |   127 x 232   |   191 x 646   |
+---------------------------+-------------- +---------------+---------------+

Coastal Model Subgrid Models
----------------------------

+---------------------------+---------------+---------------+
|                           | Zeebrugge     | Oostende      |
|                           | Harbour Grid  | Harbour Grid  |
+===========================+===============+===============+
| 1.  Grid extends          |               |               |
| 1.1 Bottom left (Lon,Lat) |  3.14 , 51.29 | 2.88 , 51.20  |
| 1.2 Top Right   (Lon,Lat) |  3.26 , 51.43 | 2.95 , 51.31  |
| 1.3 Grid rotation (deg)   |   * CALC *    |   * CALC *    |
+---------------------------+---------------+---------------+
| 2. Spacing  (distance)    |   60m x 60m   |   60m x 60m   |
+---------------------------+---------------+---------------+
| 3. Cells    (number)      |   205 x 172   |   157 x 140   |
+---------------------------+-------------- +---------------+
