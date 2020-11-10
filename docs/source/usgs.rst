Topo-bathymetry data
=====================

.. autofunction:: petrodc.usgs_eros.elevation

Example
-------

Let's select an squared area within the following coordinates:

- Latitude from 56° to 56.5°
- Longitude from 4° to 4.5°

.. code-block:: python

    >>> import petrodc.usgs_eros as elev
    >>> lat_min = 56
    >>> lat_max = 56.5
    >>> lon_min = 4
    >>> lon_max = 4.5
    >>> elev_surface = elev.elevation(lat=(lat_min, lat_max), lon=(lon_min, lon_max)).plot().show()

|elevation_surface|

.. |elevation_surface| image:: /figures/elev_surface.png
                    :scale: 30%

Web Application
---------------

There is also the web-app based on petrodc:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/1oj_e-XhirQ?start=4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
