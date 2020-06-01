import os
import glob
import subprocess

dir = os.getcwd()
os.makedirs(f'{dir}/_reversed', exist_ok=True)
rev_out = dir + r'/_reversed'

get_files = glob.glob(dir + '/*.wav')

def reverse_file():
    for i in get_files:
        file = i
        get_filename = os.path.splitext(str(i))[0]
        filename_only = os.path.basename(get_filename)

        attributes = subprocess.Popen(['ffprobe', file], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

        for x in attributes.stdout.readlines():
            x = x.decode(encoding='utf-8')
            if 'encoder' in x:
                encoder = x[22:-1]

            if 'Stream' in x:
                bit_depth = x[24:33]

        subprocess.call(['ffmpeg', '-i', file, '-af', 'areverse', '-c:a', bit_depth, rev_out + '/' + filename_only + '.wav'])

        subprocess.call(['bwfmetaedit', rev_out + '/' + filename_only + '.wav', '-a', '--ISFT=' + encoder])

reverse_file()
