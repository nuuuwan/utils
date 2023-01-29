## Version History (1.1.x)

### 1.1.19 
* fix: cache BUG


### 1.1.18 
* feat: Add Directory etc
* feat: Added get_time_id, get_date_id
* feat: Added find_element etc to Browser 
* More Time/TimeDelta operators
* Added Browser to default __init__. Added get screenshot 


### 1.1.17 
* Added TimeIDs 
* Added TimeUnits 
* #Refactor Time into new folder 

### 1.1.16 

* Refactored log to have Log(name)
* Added Time addition 
* Renamed RandomColor to Color
* Cleaned-up Browser
* Deleted Image

### 1.1.15 

* Deprecated xy, geo, latlng
* Refactored dt into String

### 1.1.14 

* Deprecated jsonx
* feat: import cache directly, instead of cache.cache
* Deprecated db
* renamed www -> WWW
* Deprecated printx
* Deprecated sysx
* Deprecated timex
* Deprecated filex, tsv
* Deprecated ds

### 1.1.13 

* Deprecated zipx
* Deprecated legacy www

### 1.1.12 

* Make WWW primary, and add PendingDeprecationWarnings to stand-alone functions

* Deprecated colorx; replaced with RandomColor

* Added (smart) Dict
* Added (smart) List
* Added Iter
* Added Table and TableRow

### 1.1.11 

* Added Time, TimeDelta and TimeFormat (i.e. made time a class)

### 1.1.8 

* Removed pandas, geopandas and shapely

### 1.1.7

* Fixed bug in Git

### 1.1.6

* Added WWW
* Added readBinary to File
* Git - lazy clone. Clone only the branch to checkout

### 1.1.5

* Added Zip
* Updated Git checkout to pull on checkout

### 1.1.4

* Added Git

### 1.1.3

* Fixed Tweepy "me" bug

### 1.1.2

* Added write_lines to file
* Added get_address_details to GoogleMaps

### 1.1.1

* Added GoogleMaps with basic mapping functions. Requires API keys

### 1.1.0

Version 1.1 will start replacing and deprecating 1.0.

* Added CSVFile, File, JSONFile, TSVFile, XSVFile which togther should replace filex, jsonx, and tsv.
