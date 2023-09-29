# bibligator/__init__.py

import argparse
import os
import re
import zipfile
from glob import glob
from pikepdf import Pdf

DESCRIPTION = \
	"Merge PDF files as `<s> <n>.pdf` or `<s> <n>-<m>.pdf` in order of `<n>`."

m = re.compile(r"^(.+)( (\d+))(-(\d+))?\.pdf$")

def exnums(name):
	r = m.match(name)
	n0 = int(r.group(3))
	n1 = int(r.group(5) or n0)
	if n0 > n1:
		raise ValueError("Interval reversed!")
	return n0, n1

def iscoherent(intervals):
	tt = [itv[1] + 1 for itv in intervals[:-1]]
	ss = [itv[0] for itv in intervals[1:]]
	return tt == ss

def isprefixedw(stem, filename):
	r = m.match(filename)
	return r and r.group(1) == stem

def isprefixed(stem):
	return lambda filename: isprefixedw(stem, filename)

def merge(sfilenames, dfilename):
	dest = Pdf.new()
	for sfilename in sfilenames:
		src = Pdf.open(sfilename)
		dest.pages.extend(src.pages)
	dest.save(dfilename)

def zip(sfilenames, zfilename):
	zfile = zipfile.ZipFile(zfilename, "w")
	for sfilename in sfilenames:
		zfile.write(sfilename, os.path.split(sfilename)[1], zipfile.ZIP_DEFLATED)
	zfile.close()

def remove(sfilenames):
	for sfilename in sfilenames:
		os.remove(sfilename)

def main():
	parser = argparse.ArgumentParser(description=DESCRIPTION)
	parser.add_argument("filename", metavar="FILENAME", type=str,
        help = "Name of a PDF file in the sequence")
	args = parser.parse_args()
	sfilename = args.filename
	if not os.path.isfile(sfilename):
		raise FileNotFoundError("Example source file does not exist!")
	r = m.match(sfilename)
	if not r:
		raise ValueError("Example source file name not well-formatted!")
	stem = r.group(1)
	dfilename = f"{stem}.pdf"
	zfilename = f"{stem}.zip"
	if os.path.isfile(dfilename) or os.path.isfile(zfilename):
		raise FileExistsError("Destiny file already exists!")
	sfilenames = sorted(list(filter(isprefixed(stem), glob(f"{stem} *.pdf"))),
		key = lambda s: int(m.match(s).group(3)))
	if not iscoherent(list(map(exnums, sfilenames))):
		raise ValueError("Intervals not coherent!")
	merge(sfilenames, dfilename)
	zip(sfilenames, zfilename)
	remove(sfilenames)
	print(f"PDF files successfully merged to {dfilename}.")
