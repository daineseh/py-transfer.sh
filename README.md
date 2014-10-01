py-transfer.sh
==============
https://transfer.sh/

transfer.sh wrapper

usage: pt.py [-h] [-u FILE [FILE ...]] [-d FILE [FILE ...]] [-w DIR]

#optional arguments:
    -h, --help          show this help message and exit
    -u FILE [FILE ...]  input upload file(s)
    -d FILE [FILE ...]  input download file(s)
    -w DIR              specify download path



**example1 :**
```bash
    # Upload a file to http://transfer.sh
    $./pt.py -u /home/something/file1

    # and output a link for download:
    https://transfer.sh/19Xwp/file1
```


**example2 :**
```bash
    # Upload multiple files to http://transfer.sh
    $./pt.py -u /home/something/file1  /home/something/file2  /home/something/file3

    # and output some link for downloads:
    https://transfer.sh/19Xwp/file1
    https://transfer.sh/19Xwp/file2
    https://transfer.sh/19Xwp/file3
```

**example3 :**
```bash
    # download a file from http://transfer.sh
    ./pt.py -d https://transfer.sh/19Xwp/file1
    
    # Print download information:
    Download ./file1 done.
```

**example4 :**
```bash
    # download multiple files from http://transfer.sh
    ./pt.py -d https://transfer.sh/19Xwp/file1  https://transfer.sh/1fn4k/file2
    
    # Print downloads information:
    Download ./file1 done.
    Download ./file2 done.
```

**example5 :**
```bash
    # download multiple files and specify path from http://transfer.sh
    ./pt.py -d https://transfer.sh/19Xwp/file1  https://transfer.sh/1fn4k/file2 -w /home/user/
    
    # Print downloads information:
    Download /home/user/file1 done.
    Download /home/user/file2 done.
```
