# FFMPEG-batch-reverse
Python script utilising FFMPEG to batch reverse files.  The script first runs FFPROBE to caputure the input bit depth ('Stream') and encoder ('Encoder') to use as variables.  FFMPEG currently writes 'Lavf57.71.100' to the encoder tag overwriting any exisiting metadata - this behaviour cannot be changed, even with the various metadata options.  The only way to retain the original encoder (ISFT value) is to write it to the file after processing using BWF MetaEdit.

In order to run the script you need FFPROBE, FFMPEG & BWF MetaEdit binaries installed.
