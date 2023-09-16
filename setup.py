#!/usr/bin/env python

import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))
exec(open(os.path.join(here, 'version.py')).read())

setuptools.setup(
    name        = 'metocean-api',
    description = 'metocean-api - Tool to extract time series of metocean data from hindcasts/reanalysis',
    author      = 'Konstantinos Christakos MET Norway & NTNU',
    url         = 'https://github.com/MET-OM/metocean-api',
    download_url = 'https://github.com/MET-OM/metocean-api',
    version = __version__,
    license = 'GPLv2',
    install_requires = [
        'python',
        'matplotlib',
        'numpy',
        'pandas',
        'xarray',
        'dask',
        'pip',
        'nco',
        'pynco',
        'netcdf4',
        'time',
        'pytest'
    ],
    packages = setuptools.find_packages(),
    include_package_data = True,
    setup_requires = ['setuptools_scm'],
    tests_require = ['pytest'],
    scripts = []
)
