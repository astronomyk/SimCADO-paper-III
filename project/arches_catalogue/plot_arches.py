from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
from astropy.io import fits, ascii

import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

def query_gaia():
    # Westerlund 1
    coord = SkyCoord(ra="16 47 04.00", dec="-45 51 04.9", unit=(u.degree, u.degree), frame='icrs')
    width = 1 * u.deg
    height = 1 * u.deg
    r = Gaia.query_object_async(coordinate=coord, width=width, height=height)

    return r
print(r.colnames)
plt.plot(r["ra"], r["dec"], ".")
plt.show()