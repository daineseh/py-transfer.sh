py-transfer.sh
==============
https://transfer.sh/

transfer.sh (https://transfer.sh/
) is a service that you can share your files. You can upload your files by drag and drop on that web site.
Now you can upload and download files by using **pt.py** in your shell.


transfer.sh wrapper


usage: pt.py [-h] [-u FILE [FILE ...]] [-d URL [URL ...]] [-w DIR]

#optional arguments:
    -h, --help          show this help message and exit
    -u FILE [FILE ...]  specify the path of file(s) you want to upload.
    -d URL [URL ...]    specify one or more URL you want to download.
    -w DIR              specify a directory to download. The default directory is the working directory.



**Example1 : Upload a file**
```bash
    # Upload a file to http://transfer.sh
    $./pt.py -u /home/something/file1

    # and output a link for download:
    https://transfer.sh/19Xwp/file1
```


**Example2 : Upload more files**
```bash
    # Upload multiple files to http://transfer.sh
    $./pt.py -u /home/something/file1  /home/something/file2  /home/something/file3

    # and output some link for downloads:
    https://transfer.sh/19Xwp/file1
    https://transfer.sh/19Xwp/file2
    https://transfer.sh/19Xwp/file3
```

**Example3 Download a file:**
```bash
    # download a file from http://transfer.sh
    ./pt.py -d https://transfer.sh/19Xwp/file1
    
    # Print download information:
    Download ./file1 done.
```

**Example4 : Download multiple files**
```bash
    # download multiple files from http://transfer.sh
    ./pt.py -d https://transfer.sh/19Xwp/file1  https://transfer.sh/1fn4k/file2
    
    # Print downloads information:
    Download ./file1 done.
    Download ./file2 done.
```

**Example5 : Specify the download directory**
```bash
    # download multiple files and specify path from http://transfer.sh
    ./pt.py -d https://transfer.sh/19Xwp/file1  https://transfer.sh/1fn4k/file2 -w /home/user/
    
    # Print downloads information:
    Download /home/user/file1 done.
    Download /home/user/file2 done.
```
