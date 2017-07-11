# Fileorganizer

Batch File Organizer

Working in progress...


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
    -r, --regex           Treat input string as regex
```

## Example

### Remove [Bad] in file name only

```sh
$ python replacename.py "[Bad]" "" -d "D:\Something" -w
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
├── Something_S01E02.mp4
            </code></pre></td>
        </tr>
    </tbody>
</table>


### Replace [Bad] in folder name obly

```sh
$ python replacename.py "[Bad]" "" -d "D:\Something" -m1 -w
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

```sh
$ python replacename.py "[Bad]" "" -d "D:\Something" -m2 -w
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

### Keep only parts of filename using regex

```sh
$ python replacename.py "(.*)(Something_S[0-9]+E[0-9]+)(.*)(\.(mp4|avi))" "\2\4" -d "D:\Something" -rw
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

```sh
$ python replacename.py "_" "-" -d "D:\Something" -w
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

### Replace "_" in filename with "-" using regex

```sh
$ python replacename.py "(.*)(Something)(.*)(S[0-9]+E[0-9]+)(.*)(\.(mp4|avi))" "\2-\4\6" -d "D:\Something" -rw
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
