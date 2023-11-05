# Checklist for Updating

## Update Code
* Update [__init__.py](src/utils/__init__.py) with the new items
* Upddate [test_init.py](tests/test_init.py) with the new items
* Update [README.md](README.md) with the sub-package and version, and utils version 
* **If a new sub-package is added**, update [requrements.txt](requrements.txt) and [setup.py](setup.py) with the new sub-package
* Update utils version in [setup.py](setup.py)

## Test
* **Run unittests**

## Commit 
* commit code 
* **Check if unittests pass on server**
* Create and Push Tag
