# cloudyfsps

Python interface between FSPS and Cloudy. Edited to process C3K FSPS

# Basic usage instructions.
1. Create and activate some sort of environment, with either `conda` or `virtualenv`. `cloudy` should also be installed and locatable within the path. To make sure your environment is safe, run `which pip`. This should give you a path to a pip3 version *within the environment*.
2. From the environment, run
```pip3 install /path/to/cloudyfsps/.```
(note final dot. The folder should contain the `setup.py` file).
3. Get the FSPS/C3K library from somewhere. Put the file `SSP_MIST_C3K_Salpeter.pckl` somewhere.
4. Go to `/path/to/cloudyfsps/demos`, from there, edit the file `generateCloudyBinaryFile_C3KMIST.py` to specify the path to `SSP_MIST_C3K_Salpeter.pckl` in your machine. Then run
```python3 generateCloudyBinaryFile_C3KMIST.py```
This will generate the files `FSPS_MIST_C4K_SSP.ascii` and `FSPS_MIST_C4K_SSP.mod`, and save them in your `cloudy` folder, under `data`.
5. Now run
```python3 exampleCloudyGrid_C3K_selfcons.py```
This is the self-consistent grid (i.e. logU fixed by the SSP SED). It will generate a set of cloudy input files under `path/to/cloudyfsps/demos/output_mist_c3k_ssp/`
 It will generate a set of cloudy input files under `path/to/cloudyfsps/demos/output_mist_c3k_ssp/`
6. Now, from the new directory, you can run `cloudy` with e.g.
```for infile in `ls ZAU*.in`; do echo "${infile%.*}"; $CLOUDY_EXE -r "${infile%.*}"; done```
7. Common pitfall. If your environment path is too long, `cloudy` will fail to read the `cloudyLines.dat` file in the `*.in` files. In this case, you may replace the line
```save last linelist ".lin" "/long/and/involved/path/to/cloudyfsps/cloudyLines.dat" absolute column```
with
```save last linelist ".lin "../cloudyLines.dat" absolute column```
An example automated command is provided in `sed_command`. This is a bash command (remember to escape all /).



**Read the documentation:** [nell-byler.github.io/cloudyfsps](http://nell-byler.github.io/cloudyfsps/)

If you use this code, follow the citation requirements [on the FSPS homepage](https://github.com/cconroy20/fsps) and reference these Python bindings:

[![DOI](https://zenodo.org/badge/47210025.svg)](https://zenodo.org/badge/latestdoi/47210025)

**For BibTex, cite with:**
```
@MISC{nell_byler_2018_1156412,
  author       = {{Byler}, N.},
  title        = {cloudyFSPS},
  version      = {1.0.0},
  publisher    = {Zenodo},
  month        = jan,
  year         = 2018,
  doi          = {10.5281/zenodo.1156412},
  url          = {https://doi.org/10.5281/zenodo.1156412}
}
```
