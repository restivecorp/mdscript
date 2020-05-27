# mdscript
Metadata Script

## Description
Description

## Use

### Help
```
    $ python3 mds.py -h
    $ python3 mds.py --help
```

### Verbose
```
    $ python3 mds.py --verbose
```

### Version
```
    $ python3 mds.py --ver
    $ python3 mds.py --ver --verbose
```

### Rename
Rename file names:

```
    # Rename files .jpg start at 0001
    $ python3 mds.py -r /potos/album/ 

    # Rename files .avi start at 0001
    $ python3 mds.py -r /potos/album/ --ext avi

    # Rename files .avi start with prefix v0001
    $ python3 mds.py -r /potos/album/ --ext avi --pfx v

    # Rename files .avi start with prefix in counter v0005
    $ python3 mds.py -r /potos/album/ --ext avi --pfx v --idx 5
```

### Metadata
Set metadata:

```
    # Set metadata jpg files by album ID
    $ python3 mds.py -r /potos/albumes/2000/2000.json 26c44f1489c2ee3ad97a38cadc8de5a1 

    # Set metadata jpg files by album NAME
    $ python3 mds.py -r /potos/albumes/2000/2000.json 2000.01.01-newyear

    # Set metadata avi files
    $ python3 mds.py -r /potos/albumes/2000/2000.json 26c44f1489c2ee3ad97a38cadc8de5a1 --ext avi
```

### Delete
Delete metadata:

```
    # Delete metatadata jpg files
    $ python3 mds.py -d /potos/album

    # Delete metatadata avi files
    $ python3 mds.py -d /potos/album --ext avi
```

### Cover
Set cover metadata:

```
    # Set cover metatadata to YEAR.jpg file
    $ python3 mds.py --cover /potos/album/2000.jpg
```

