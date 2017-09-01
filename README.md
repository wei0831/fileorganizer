# Files Organizer

Batch Files Organizer

## Status
Working in progress...

## Requirements
- python 3.5+
- [setuptools](https://github.com/pypa/setuptools)
- [click](https://github.com/pallets/click)

## Install
```bash
# Navigate to the folder that contains setup.py 
cd fileorganizer
```
```bash
# Install
easy_install -m .
```

# Index
- [replacename](#replacename)
- [folderin](#folderin)
- [folderout](#folderout)
- [movefilestofolder](#movefilestofolder)

# replacename

## Usage
```
Usage: replacename [OPTIONS] FIND REPLACE WORK_DIR

  Find string in File name/Folder name and replace with another string

  Args:
      find (str): Regex string to find in filename/foldername
      replace (str): Regex string to replace in filename/foldername
      work_dir (str): Working Directory
      exclude (str, optional): Regex string to exclude in mattches
      mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
      wetrun (bool, optional): Test Run or not

Options:
  -e, --exclude TEXT  Exclude regex pattern
  -m, --mode INTEGER  0: FILE_ONLY, 1: FOLDER_ONLY, 2: BOTH
  -w, --wetrun        Commit changes
  --help              Show this message and exit.
```

## Notes
* Commit changes by using ```-w``` flag

## Example

### Remove [Bad] in file name only

```bash
$ replacename "\[Bad\]" "" -d "D:\Video" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [Bad]Something_Folder[Bad] 
├── [Bad]Something_S01E01[Bad].mp4
├── [Bad]Something_S01E02[Bad].avi
            </code></pre></td>
            <td><pre><code>.
├── [Bad]Something_Folder[Bad]  
├── Something_S01E01.mp4
├── Something_S01E02.avi
            </code></pre></td>
        </tr>
    </tbody>
</table>


### Replace [Bad] in folder name obly

```bash
$ replacename "\[Bad\]" "" -d "D:\Video" -m1 -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [Bad]Something_Folder[Bad]   
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
$ replacename "\[Bad\]" "" -d "D:\Video" -m2 -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [Bad]Something_Folder[Bad]   
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

### Replace "_" in filename with "-" 

```bash
$ replacename "_" "-" -d "D:\Video" -w
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
$ replacename "(.*)(Something)(.*)(S[0-9]+E[0-9]+)(.*)(\.(mp4|avi))" "\2-\4\6" -d "D:\Something" -w
```
<table>
    <thead>
        <tr><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code>.
├── [20240202]Something_S01E01[Bad].mp4
├── [20240207]Something_S01E02[Bad].avi
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
Usage: folderin [OPTIONS] WORK_DIR

  Put files into folder with the same name

  Args:
    work_dir (str): Working Directory
    wetrun (bool, optional): Test Run or not

Options:
  -w, --wetrun  Commit changes
  --help        Show this message and exit.
```

## Example

### Move Something_SXXEXX into their individual folder

```bash
$ folderin "D:\Video" -w
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
Usage: folderout [OPTIONS] WORK_DIR

  Move files out of folders

  Args:
      work_dir (str): Working Directory
      to_dir (str, optional): Target Directory
      wetrun (bool, optional): Test Run or not

Options:
  -t, --to_dir PATH  Target Directory
  -w, --wetrun       Commit changes
  --help             Show this message and exit.
```

## Example

### Move files in the folder out

```bash
$ folderout "D:\Video" -w
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
Usage: moveintofolder [OPTIONS] FIND WORK_DIR TO_DIR

  Move matching files/folder into a folder

  Args:
      find (str): Regex string to find in filename/foldername
      work_dir (str): Working Directory
      to_dir (str): Target Directory
      exclude (str, optional): Regex string to exclude in mattches
      mode (int, optional): 0=FILE ONLY, 1=FOLDER ONLY, 2=BOTH
      wetrun (bool, optional): Test Run or not

Options:
  -e, --exclude TEXT  Exclude regex pattern
  -m, --mode INTEGER  0: FILE_ONLY, 1: FOLDER_ONLY, 2: BOTH
  -w, --wetrun        Commit changes
  --help              Show this message and exit.
```

## Example

### Move all Something_SXXEXX video files into a folder

```bash
$ movefilestofolder "(.*)(Something)(.*)(S[0-9]+E[0-9]+)(.*)" "D:\Video" ".\Somthing_Collection" -w
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