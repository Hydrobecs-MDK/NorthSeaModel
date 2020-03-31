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
NorthSeaModel consists of two grids:

1. Large grid covering the North Sea Domain and a part of the North East Atlantic
2. Nested grid covering the Belgian continental shelf and parts of Brittain. The Nested grid is nested within the Large grid

CoastalModel consists of one main grid and a number of subgrids:

3. Coastal Model covering the whole of the Belgian Coast
4. Various smaller grids located at strategic locations around the Belgian coast


+--------------------------+--------------+--------------+--------------+---------------+
|                          |NorthSeaModel |NorthSeaModel |CoastalModel  |CoastalModel   |
|                          | Large Grid   | Nested Grid  |Belgium Coast |Subgrid Models |
+==========================+==============+==============+==============+===============+
|1. Grid extends           | column 2     | column 2     | column 2     | column 2      |
|1.1 Bottom left (Lon,Lat) | column 2     | column 2     | column 2     | column 2      |
|1.2 Top Right   (Lon,Lat) | column 2     | column 2     | column 2     | column 2      |
|1.3 Grid rotation (deg)   | column 2     | column 2     | column 2     |               |
+--------------------------+--------------+--------------+--------------+---------------+
|2. Spacing  (distance)    | 5km x 5km    | 1km x 1km    | 200m x 200m  | 60m x 60m     |
+--------------------------+--------------+--------------+--------------+---------------+
|3. Cells    (number)      | ...          | ...          | ...          | ...           |
+--------------------------+--------------+--------------+--------------+---------------+
