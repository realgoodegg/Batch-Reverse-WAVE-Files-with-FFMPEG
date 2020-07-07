# Batch-Reverse-WAVE-Files-with-FFMPEG
> Batch reverse WAVE files using [FFMPEG](https://ffmpeg.org), while retaining the input file's bit-depth and embeded metadata.  

## Purpose

To reverse WAVE files with FFMPEG is fairly straightforward; however, some of its default transcoding behaviour can result in fundamental changes to the source file. By deafult the audio filter functions `-af` transcode files to a 16 bit wordlenth, regardless of the input; the embedded ISFT tag (usually referred to as 'software' or 'encoder') in the INFO chunk is overwritten with FFMPEG's transcoder - 'Lavf57.x'.  

The former issue can be manually overidden but the latter behaviour cannot be changed.  The only way to ensure the correct ISFT information is retained, is to re-write the data using [BWF MetaEdit](https://mediaarea.net/BWFMetaEdit).

The script has been written in both [Python 3.x](https://www.python.org) and as a Windows batch file.

## Dependencies

The script requires the following external libraries:

* [FFMPEG](https://ffmpeg.org/download.html)
* [FFPROBE](https://ffmpeg.org/download.html)
* [BWF MetaEdit - CLI](https://mediaarea.net/BWFMetaEdit/Download)

*precompiled builds of FFMPEG usually include FFPROBE*

[Python 3.x](https://www.python.org/downloads/) (if running the Python script)

On a Windows system the executables should be installed to the system32 folder; on Mac OS they should be stored in your `PATH`; alternativly, they can run from the local folder with the files / script.

## Usage

To run the Python script:

`python3 batch-reverse.py`

The Windows batch file can be run by double-clicking on the batch-reverse.bat file.

The files you want to process should be placed in the same folder as the script.  When run, a new folder `_reversedFiles` will be written to the root of the directory, the file bit-depth and the ISFT metadata will be captured from the output of FFPROBE.  FFMPEG will reverse the files using it's `areverse` audio filter and output the processed files, with the correct bit-depth, into the `_reversedFiles` folder.

BWF MetaEdit will then re-write the orignal ISFT tag information that has been overwritten by FFMPEG.

The original files are left untouched in their place, these should be manually deleted by the user if no longer needed.
