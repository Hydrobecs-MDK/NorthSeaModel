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
* NorthSeaModel_Large (5km x 5km)

+------------------------+--------------+--------------+--------------+---------------+
|                        |NorthSeaModel |NorthSeaModel |CoastalModel  |CoastalModel   |
|                        | Large Grid   | Nested Grid  |Belgium Coast |Subgrid Models |
+========================+==============+==============+==============+===============+
| Grid extends           | column 2     | column 2     | column 2     | column 2      |
|  Bottom left (Lon,Lat) | column 2     | column 2     | column 2     | column 2      |
|  Top Right   (Lon,Lat) | column 2     | column 2     | column 2     | column 2      |
+------------------------+--------------+--------------+--------------+---------------+
| body row 2             | ...          | ...          | ...          | ...           |
+------------------------+--------------+--------------+--------------+---------------+
