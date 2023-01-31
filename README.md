<!--header-start-->
<img src="https://github.com/NaturalHistoryMuseum/ckanext-sketchfab/raw/main/.github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

# ckanext-sketchfab

[![Tests](https://img.shields.io/github/actions/workflow/status/NaturalHistoryMuseum/ckanext-sketchfab/main.yml?style=flat-square)](https://github.com/NaturalHistoryMuseum/ckanext-sketchfab/actions/workflows/main.yml)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-sketchfab/main?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-sketchfab)
[![CKAN](https://img.shields.io/badge/ckan-2.9.7-orange.svg?style=flat-square)](https://github.com/ckan/ckan)
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/)
[![Docs](https://img.shields.io/readthedocs/ckanext-sketchfab?style=flat-square)](https://ckanext-sketchfab.readthedocs.io)

_A CKAN extension for embedding Sketchfab models as views._

<!--header-end-->

# Overview

<!--overview-start-->
A [Sketchfab](https://sketchfab.com) view can be added to _any_ resource, regardless of whether the original data are related to the model. The view can use either the resource's URL (if the resource links directly to a sketchfab model) or one can be specified when creating the view.

You can see some of the Natural History Museum's 3D scans [on Sketchfab](https://sketchfab.com/NHM_Imaging), and several examples of the plugin in use in [this dataset](https://data.nhm.ac.uk/dataset/3d-cetacean-scanning) on the Museum's Data Portal.

<!--overview-end-->

# Installation

<!--installation-start-->
Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

## Installing from PyPI

```shell
pip install ckanext-sketchfab
```

## Installing from source

1. Clone the repository into the `src` folder:
   ```shell
   cd $INSTALL_FOLDER/src
   git clone https://github.com/NaturalHistoryMuseum/ckanext-sketchfab.git
   ```

2. Activate the virtual env:
   ```shell
   . $INSTALL_FOLDER/bin/activate
   ```

3. Install via pip:
   ```shell
   pip install $INSTALL_FOLDER/src/ckanext-sketchfab
   ```

### Installing in editable mode

Installing from a `pyproject.toml` in editable mode (i.e. `pip install -e`) requires `setuptools>=64`; however, CKAN 2.9 requires `setuptools==44.1.0`. See [our CKAN fork](https://github.com/NaturalHistoryMuseum/ckan) for a version of v2.9 that uses an updated setuptools if this functionality is something you need.

## Post-install setup

1. Add 'sketchfab' to the list of plugins in your `$CONFIG_FILE`:
   ```ini
   ckan.plugins = ... sketchfab
   ```

<!--installation-end-->

# Configuration

<!--configuration-start-->
There are currently no configuration options for this extension.

<!--configuration-end-->

# Usage

<!--usage-start-->
After installing, the "Sketchfab" view type will become available for resource maintainers. Add the new view and provide the URL to a Sketchfab model where prompted.

<!--usage-end-->

# Testing

<!--testing-start-->
There is a Docker compose configuration available in this repository to make it easier to run tests. The ckan image uses the Dockerfile in the `docker/` folder.

To run the tests against ckan 2.9.x on Python3:

1. Build the required images:
   ```shell
   docker-compose build
   ```

2. Then run the tests.
   The root of the repository is mounted into the ckan container as a volume by the Docker compose
   configuration, so you should only need to rebuild the ckan image if you change the extension's
   dependencies.
   ```shell
   docker-compose run ckan
   ```

<!--testing-end-->
