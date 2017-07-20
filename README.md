# Files Organizer

Batch Files Organizer

## Status
Working in progress...

## Requirements
- Python 3.5+

# Index
- [replacename](#replacename)
- [folderin](#folderin)
- [folderout](#folderout)
- [movefilestofolder](#movefilestofolder)

# replacename

## Usage
```
usage: replacename.py [-h] [-d DIR] [-m MODE] [-w] [-r] find replace

Find string in File name/Folder name and replace with another string

positional arguments:
    find                  String to Replace in filename/foldername
    replace               To Replace With in filename/foldername

optional arguments:
    -h, --help            show this help message and exit
    -d DIR, --dir DIR     Working Directory
    -m MODE, --mode MODE  0: FILE_ONLY, 1: FOLDER_ONLY, 2: BOTH
    -w, --wetrun          Disable dryrun and Commit changes
```

## Notes
* You can test run to see the results by NOT using ```-w``` flag

## Example

### Remove [Bad] in file name only

```bash
$ python replacename.py "\[Bad\]" "" -d "D:\Video" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [Bad]Something_Folder 
├── [Bad]Something_S01E01[Bad].mp4
├── [Bad]Something_S01E02[Bad].avi
            </code></pre></td>
            <td><pre><code>.
├── [Bad]Something_Folder  
├── Something_S01E01.mp4
├── Something_S01E02.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>


### Replace [Bad] in folder name obly

```bash
$ python replacename.py "\[Bad\]" "" -d "D:\Video" -m1 -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [Bad]Something_Folder   
├── [Bad]Something_S01E01[Bad].mp4
├── [Bad]Something_S01E02[Bad].avi
            </code></pre></td>
            <td><pre><code>.
├── Something_Folder
├── [Bad]Something_S01E01[Bad].mp4
├── [Bad]Something_S01E02[Bad].avi
            </code></pre></td>
        </tr>
    </tbody>
</table>

### Remove [Bad] in both folder name and file name

```bash
$ python replacename.py "\[Bad\]" "" -d "D:\Video" -m2 -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [Bad]Something_Folder   
├── [Bad]Something_S01E01[Bad].mp4
├── [Bad]Something_S01E02[Bad].avi
            </code></pre></td>
            <td><pre><code>.
├── Something_Folder
├── Something_S01E01.mp4
├── Something_S01E02.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>

### Keep only parts of filename

```bash
$ python replacename.py "(.*)(Something_S[0-9]+E[0-9]+)(.*)(\.(mp4|avi))" "\2\4" -d "D:\Something" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [Bad]Something_S01E01[Bad].mp4
├── [Bad]Something_S01E02[Bad].avi
            </code></pre></td>
            <td><pre><code>.
├── Something_S01E01.mp4
├── Something_S01E02.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>

### Replace "_" in filename with "-" 

```bash
$ python replacename.py "_" "-" -d "D:\Video" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── Something_S01E01.mp4
├── Something_S01E02.avi
            </code></pre></td>
            <td><pre><code>.
├── Something-S01E01.mp4
├── Something-S01E02.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>

### Change the name using regex group

```bash
$ python replacename.py "(.*)(Something)(.*)(S[0-9]+E[0-9]+)(.*)(\.(mp4|avi))" "\2-\4\6" -d "D:\Something" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [Bad]Something_S01E01[Bad].mp4
├── [Bad]Something_S01E02[Bad].avi
            </code></pre></td>
            <td><pre><code>.
├── Something-S01E01.mp4
├── Something-S01E02.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>

# folderin

## Usage
```
usage: folderin.py [-h] [-w] workDir

Put files into folder with the same name

positional arguments:
  workDir       Working Directory

optional arguments:
  -h, --help    show this help message and exit
  -w, --wetrun  Disable dryrun and Commit changes
```

## Example

### Move Something_SXXEXX into their individual folder

```bash
$ python folderin.py "D:\Video" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── Something_S01E01.mp4
├── Something_S01E01.jpg 
├── Something_S01E02.avi
            </code></pre></td>
            <td><pre><code>.
├── Something_S01E01
    ├── Something_S01E01.mp4
    ├── Something_S01E01.jpg 
├── Something_S01E02
    ├── Something_S01E02.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>


# folderout

## Usage
```
usage: folderout.py [-h] [-t TO] [-w] workDir

Move files out of folders

positional arguments:
  workDir         Working Directory

optional arguments:
  -h, --help      show this help message and exit
  -t TO, --to TO  Target Directory
  -w, --wetrun    Disable dryrun and Commit changes
```

## Example

### Move files in the folder out

```bash
$ python folderout.py "D:\Video" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── Something_S01E01
    ├── Something_S01E01.mp4
    ├── Something_S01E01.jpg 
├── Something_S01E02
    ├── Something_S01E02.avi
            </code></pre></td>
            <td><pre><code>.
├── Something_S01E01.mp4
├── Something_S01E01.jpg 
├── Something_S01E02.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>

# movefilestofolder

## Usage
```
usage: movefilestofolder.py [-h] [-w] find workDir toDir

Move matching files into a folder

positional arguments:
  find          Regex string to find matching files
  workDir       Working Directory
  toDir         Target Directory

optional arguments:
  -h, --help    show this help message and exit
  -w, --wetrun  Disable dryrun and Commit changes
```

## Example

### Move all Something_SXXEXX video files into a folder

```bash
$ python movefilestofolder.py "(.*)(Something)(.*)(S[0-9]+E[0-9]+)(.*)" "D:\Video" ".\Somthing_Collection" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── Something_S01E01.720p.mp4
├── Something_S01E02.1080p.avi
├── Something_HD_S01E03.mkv
├── Something-S01E04.avi
├── Holy_S01E01.avi
            </code></pre></td>
            <td><pre><code>.
├── Something
    ├── Something_S01E01.720p.mp4
    ├── Something_S01E02.1080p.avi
    ├── Something_HD_S01E03.mkv
    ├── Something-S01E04.avi
├── Holy_S01E01.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>