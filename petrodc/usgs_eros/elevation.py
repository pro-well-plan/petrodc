import requests
import pandas as pd
import io


def elevation(lat=(40, 41), lon=(-65, -60)):
    """
    Function to request data from SRTM30.
    Bathymetry / Topography (SRTM30) is a global bathymetry/topography data product distributed by the USGS EROS data
    center. The data product has a resolution of 30 seconds (roughly 1 km).

    Keyword Arguments:
        lat (tuple): with min and max latitude
        lon (tuple): with min and max longitude

    Returns:
        ElevationSurface object.

        - Attributes:
            df (pandas dataframe): lat, lon and elev columns

        - Methods:
            plot: generate a 3D surface plot
    """

    return ElevationSurface(lat, lon)


def point_elev(lat, lon):
    minlat = lat - 0.001
    maxlat = lat + 0.001
    minlon = lon - 0.001
    maxlon = lon + 0.001
    c = elevation(lat=(minlat, maxlat), lon=(minlon, maxlon))
    znew = round(c.df.elev.mean())

    return znew


class ElevationSurface(object):
    """
    3D surface object.

    Attributes:
        df (pandas dataframe): lat, lon and elev columns

    Methods:
        plot: generate a 3D surface plot
    """
    def __init__(self, lat, lon):

        # Define the domain of interest
        minlat = lat[0]
        maxlat = lat[1]
        minlon = lon[0]
        maxlon = lon[1]

        url = 'http://coastwatch.pfeg.noaa.gov/erddap/griddap/usgsCeSrtm30v6.csv?topo[(' + str(maxlat) + '):1:(' + \
              str(minlat) + ')][(' + str(minlon) + '):1:(' + str(maxlon) + ')]'
        s = requests.get(url).content
        df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=0)
        df.reset_index(drop=True)
        df.drop(0, inplace=True)
        df = df[['latitude', 'longitude', 'topo']].astype(float)
        df.rename(columns={'latitude': 'lat', 'longitude': 'lon', 'topo': 'elev'}, inplace=True)

        self.df = df

    def plot(self):

        import plotly.graph_objects as go
        from numpy import array, unique

        lon_u = unique(self.df.lon)
        lat_u = unique(self.df.lat)

        elev = array([self.df.elev[i: i + len(lon_u)] for i in range(0, len(self.df.elev), len(lon_u))])

        fig = go.Figure(data=[go.Surface(z=elev, x=lon_u, y=lat_u)])
        fig.update_layout(scene=dict(
            xaxis_title='Lon, °',
            yaxis_title='Lat, °',
            zaxis_title='Elevation, m'))

        return fig
