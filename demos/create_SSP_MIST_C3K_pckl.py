# coding: utf-8
import glob
import itertools
import pickle

import tqdm

import numpy as np

import create_fsps_sublibrary

fns = sorted(glob.glob('00_fsps_raw/SSP_MIST_C3K_Salpeter_Z0.0*spec'))

z = np.zeros(12)
age = None
wave = None
flux = []
    
for i,f in tqdm.tqdm(enumerate(fns)):
    _z_, age, _, wave, _flux_ = create_fsps_sublibrary.load_models_fixed_z(
        f, f_lambda=False, trim_wave=(-np.inf, np.inf))

    z[i] = _z_
    flux.append(_flux_)
    
flux = np.array(flux)

modpars = list(itertools.product(10**age, z))

nmod = len(age)*len(z)
flat_flux = np.zeros((nmod, len(wave)))
for i in range(107):
    for j in range(12):
        k = np.ravel_multi_index((i, j), (107,12))
        _a_, _z_ = modpars[k]
        assert 10**age[i]==_a_, f'Wrong age at {i}, {j}, {k}'
        assert _z_ == z[j], f'Wrong z at {i}, {j}, {k}'
        flat_flux[k] = flux[j, i, :]
        
pickle.dump(
    {'wave': wave, 'modpars': modpars, 'flat_flux': flat_flux},
    open('SSP_MIST_C3K_Salpeter.pckl', 'wb'))
