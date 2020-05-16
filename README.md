# mdscript
Metadata Script
## Description

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
```
    # Rename files .jpg start at 0001
    $ python3 mds.py --rename /potos/album/ 

    # Rename files .avi start at 0001
    $ python3 mds.py --rename /potos/album/ --ext avi

    # Rename files .avi start with prefix v0001
    $ python3 mds.py --rename /potos/album/ --ext avi --pfx v

    # Rename files .avi start with prefix in counter v0005
    $ python3 mds.py --rename /potos/album/ --ext avi --pfx v --idx 5
```