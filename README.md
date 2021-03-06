<img src=".github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

# ckanext-sketchfab

[![Travis](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-sketchfab/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-sketchfab)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-sketchfab/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-sketchfab)
[![CKAN](https://img.shields.io/badge/ckan-2.9.0a-orange.svg?style=flat-square)](https://github.com/ckan/ckan)

_A CKAN extension for embedding Sketchfab models as views._


# Overview

A [Sketchfab](https://sketchfab.com) view can be added to _any_ resource, regardless of whether the original data are related to the model. The view can use either the resource's URL (if the resource links directly to a sketchfab model) or one can be specified when creating the view.

You can see some of the Natural History Museum's 3D scans [on Sketchfab](https://sketchfab.com/NHM_Imaging), and several examples of the plugin in use in [this dataset](https://data.nhm.ac.uk/dataset/3d-cetacean-scanning) on the Museum's Data Portal.


# Installation

Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1. Clone the repository into the `src` folder:

  ```bash
  cd $INSTALL_FOLDER/src
  git clone https://github.com/NaturalHistoryMuseum/ckanext-sketchfab.git
  ```

2. Activate the virtual env:

  ```bash
  . $INSTALL_FOLDER/bin/activate
  ```

3. Install the requirements from requirements.txt:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-sketchfab
  pip install -r requirements.txt
  ```

4. Run setup.py:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-sketchfab
  python setup.py develop
  ```

5. Add 'sketchfab' to the list of plugins in your `$CONFIG_FILE`:

  ```ini
  ckan.plugins = ... sketchfab
  ```

# Configuration

There are currently no configuration options for this extension.


# Usage

After installing, the "Sketchfab" view type will become available for resource maintainers. Add the new view and provide the URL to a Sketchfab model where prompted.


# Testing

_Test coverage is currently extremely limited._

To run the tests, use nosetests inside your virtualenv.
```bash
nosetests --ckan --with-pylons=$TEST_CONFIG_FILE --where=$INSTALL_FOLDER/src/ckanext-sketchfab
```
