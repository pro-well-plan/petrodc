# TUTORIAL - Using 'petrodc'

## Index ##

* [1. Wellbore data from NPD.](#1.-wellbores)
* [2. Topography/bathymetry data from USGS-EROS.](#2.-elevation)

## 1. Wellbores


```
>>> import petrodc.npd as npd

>>> df = npd.wellbore(12)   # Get exploration dataset

# Selecting name, TVD, MD, and location (N and S)
>>> df = df[['wlbWellboreName','wlbFinalVerticalDepth','wlbTotalDepth','wlbNsDecDeg','wlbEwDesDeg']]    
```


## 2. Elevation

```
>>> import petrodc.usgs_eros as elev

>>> latitude, longitude = (55, 57), (3, 6)    # Setting coordinates

>>> c = elev.elevation(latitude, londitude)     # Request data

>>> c.plot()    # Plot 3D surface
```
<img width="623" alt="Screenshot 2020-08-26 at 13 14 33" src="https://user-images.githubusercontent.com/52009346/91297223-38ae0880-e79e-11ea-948b-a8626b879fa7.png">
