import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.coordinates import SkyCoord
from astropy import units as u

tbl = ascii.read("catalog.dat", readme="ReadMe")
mask = (tbl["d"] < 10e3) * (tbl["logt"] < 7.5)       # <20 kpc, <30 Myr
tbl = tbl[mask]
coords = SkyCoord(frame="galactic", l=tbl["GLON"], b=tbl["GLAT"], distance=tbl["d"])
galcen = SkyCoord(frame="galactic", l=0*u.deg, b=0*u.deg, distance=8500*u.pc)
earth = SkyCoord(frame="galactic", l=0*u.deg, b=0*u.deg, distance=0*u.pc)

plt.scatter(galcen.cartesian.x, galcen.cartesian.y, c="r", marker="^", s=100)
plt.scatter(earth.cartesian.x, earth.cartesian.y, c="k", marker="+", s=100)
plt.scatter(coords.cartesian.x, coords.cartesian.y, c=tbl["logt"], s=2*tbl["rt"])

plt.xlim(-10e3, 10e3)
plt.ylim(-10e3, 10e3)
plt.gca().set_aspect("equal")
plt.colorbar()
plt.show()
