import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

here = lambda *args: os.path.join(os.path.dirname(__file__), *args)

import pytest

import aseg_gdf2

def test_read_ext_dfn():
    gdf = aseg_gdf2.read(here('aseg_examples', 'Example_AeroMag_MuppetTown_2009.dfn'))

def test_read_ext_des():
    gdf = aseg_gdf2.read(here('aseg_examples', 'Example_AeroMag_MuppetTown_2009.des'))

def test_read_ext_dat():
    gdf = aseg_gdf2.read(here('aseg_examples', 'Example_AeroMag_MuppetTown_2009.dat'))

def test_read_no_ext():
    gdf = aseg_gdf2.read(here('aseg_examples', 'Example_AeroMag_MuppetTown_2009'))

def test_read_incorrect():
    with pytest.raises(OSError):
        gdf = aseg_gdf2.read(here('aseg_examples', 'Example_AeroMag_MuppetTown_2009.data'))