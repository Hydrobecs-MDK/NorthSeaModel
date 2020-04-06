HydroBeCS user manual and SOP for SWAN
======================================

Introduction
^^^^^^^^^^^^

This documentation describes the stand-alone SWAN model employed during the HydroBeCS model development. For the SWAN model deployed as part of the ROMS model, see **-- INSERT LINK HERE --**

Background
^^^^^^^^^^
Formal and social activities conducted throughout the coastal zone are highly dependent on the characteristics and dynamic interaction of the natural environment, e.g. coastal protection, safe ship navigation, harbour access, seabed mining, dredging, etc. Consequently, the knowledge and determination of key parameters, such as the mean water level, wave height, water depth, shoreline evolution, water run-up, are of great importance for the quality of these activities in terms of safety, maintenance and future planning. As ships sizes increase and ship drafts deepen, new challenges are formed within the context of the limited number of waterways in the Belgian part of the North Sea. This refers to the optimization of the use of the available waterways, while maintaining safe ship navigation and minimizing the amount of expensive dredging campaigns. 
Next to safety of navigation, optimizing coastal protection also benefits from the seamless forecasting of the water levels. Furthermore, the enhanced climate change phenomena intensify the variability of sea level and coastal geomorphology, posing an additional challenge for accurate long-term and short-term morphological predictions.
The above described concept stimulated the present project 'Ondersteuning bij opzetten, validatie van: ellipsoidale en reductievlakken, modelinstrumentaria op zee en in het intergetij gebied' ('Creation and validation of: geodetic and tidal datums, acquisition tools at sea and in the intertidal zone'). In this context, the various hydrodynamic and geomorphological processes must be modelled, as accurately as possible, for the entire Belgian continental shelf.

The accurate modelling of theses physical process will aid in short- and medium-term forecasting of coastal flooding, beach erosion and sea water level evolution, which are crucial aspects for the design of coastal defence and ship navigation.

Scope of Work
^^^^^^^^^^^^^
The required scope of work is as follows:

1. A numerical model is developed that resolves all relevant dynamic 3D physical processes; 
2. A coastal morphology model, that simulates processes related to the Belgian coast, based on the results of the aforementioned models will be produced. 
3. The model forcing must be derived from readily available forcing data (wind, tides, atmospheric conditions, etc.) in order to drive the model, which makes the model independent of input measurements (boundary conditions) by measuring campaigns or acquiring data from foreign entities.
4. An equipotential gravimetric surface (geoid) for the Belgian part of the North Sea must be determined, based on satellite, airborne, shipborne and terrestrial data.

Objectives
^^^^^^^^^^
The objectives of this project are as follows:

1. Create a combined hydrodynamic, wave and morphological model for the North Sea and the Belgian coast;
2. The model is calibrated on validated hindcast data;
3. The model will be used for forecast purposes. As such, the model input must be derived from environmental forcing conditions; and
4. The model output to simulate coastal hydrodynamic process for decision making purposes.
5. Determine a marine (quasi-)geoid; and
6. Vertically reference the hydrodynamic model to the (quasi-)geoid. As such, ellipsoidal heights of chart datum can be determined.

Methodology
^^^^^^^^^^^
In order to fulfil the aim of the present project, compound numerical modelling of the various physical processes throughout the Belgian coastal zone are performed. In particular, a "chain" of coupled hydrodynamic, wave, sediment transport and morphological models are being developed and validated in order to offer a functional tool for operational reasons. In brief, the main variables and fields that must be estimated are the following:
* Efficient tidal prediction with accurate representation of the most common harmonic components for the selected coastal zone with respect to a set of reference planes;
* Computation of the general circulation throughout the North Sea, and in more detail along the Belgian coastal shelf, due to various agents, i.e. tides, meteorological factors, etc.;
* Determination of the wave climate (significant wave height and peak period) all over the North Sea and, in greater detail, throughout the Belgian coastal zone. The latter also includes the estimation of the wave-induced current field;
* Quantification of wave and tidal energy along the Belgian continental shelf that will resolve the nearshore coastal dynamic processes (e.g. wave runup, set-up, etc.); and 
* Estimation of sediment transport loads and the induced morphological evolution, e.g. beach erosion, accretion, sand bank migration, etc.

In this context, several different numerical models must be developed and, where relevant, coupled online, each of which will undertake one or more of the above tasks. These are the following:
* A hydrodynamic model for the general circulation and mean sea level 
* A spectral wave model for the wave climate through the entire North Sea
* A phase-resolving wave model for the wave characteristics and the wave-induced currents on restricted parts of the Belgian coastal zone 
* A sediment transport and morphological model for the processes related to morphodynamics

The numerical models are to be operationally robust, accurate (within the given constraints) and able to be validated for forecasting purposes. 

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
