import os
import argparse
import shutil
import glob
res = 600
urlString = ''
fontSize = 11
latexString = ''
pid = os.getpid()
localPath = os.getcwd()
pidPath = localPath[:] + '/temporary/' + str(pid)
# URL_String = ~ s / ^'//


def argparser():
    parser = argparse.ArgumentParser(
        description='fa')
    parser.add_argument('URL', help='URL of the comic\'s cover page')
    parser.add_argument(
        '--Dont_Del', help='233')
    return parser


parser = argparser()
args = parser.parse_args()
urlString = args.URL
if args.Dont_Del:
    dontDel = True
else:
    dontDel = False

os.makedirs(pidPath)
shutil.copy(localPath + '/template.tex', pidPath)
shutil.copy(localPath + '/template.aux', pidPath)
shutil.copy(localPath + '/', pidPath)
shutil.copy(localPath + '/template.tex', pidPath)
for file in glob.glob(localPath + '/preview.*'):
    shutil.copy(file, pidPath)

Baseline_Depth = 0  # the distance from the baseline to the bottom of the image
#(in pixels)
Already_Trimmed = 0  # flag used to prevent convert's "trim" command from
# being called twice
Height  # the total height of the image (in pixels)
Numb_Points_Shift = 0  # the number of points that Word is suppossed to shift
# the image down by to compensate for the baseline
# location
Numb_Padding_Pxls = 0  # the number of pixels of padding to be added to the
# bottom of the image (see below)
temp = 0
