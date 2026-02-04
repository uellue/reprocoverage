# reprocoverage

Reproducer for an issue with `coverage==7.13.3` on Windows

## How to reproduce

* On Windows (tested with Windows Server 2025 Standard) create and activate a Python 3.13 environment, e.g.
  * `conda create -n reprocoverage313 python=3.13`
  * `conda activate reprocoverage313`
* Install tox: `pip install tox`
* Run tox: `tox -e py313`

## What happens

`pytest` hangs on the second test.

## What should happen

`pytest` runs through.

## How to make it not hang

a) Pin the `coverage` version in `pyproject.toml` to `coverage<7.13.3`
b) Remove the `--cov=libertem` in `tox.ini`
