import argparse
from itertools import chain

from matchms.importing import load_from_msp
from matchms.exporting import save_as_msp



def read_spectra(filenames):
    spectra = list(chain(*[load_from_msp(file) for file in filenames]))
    return spectra

def write_spectra(filenames, outfilename):    
    spectra = read_spectra(filenames)
    save_as_msp(spectra, outfilename)


def merge_spectra(filenames, outfilename):
    return write_spectra(filenames, outfilename)


listarg = argparse.ArgumentParser()
listarg.add_argument('--filenames', type=str) 
listarg.add_argument('--outfilename', type=str) 
args = listarg.parse_args()
outfilename = args.outfilename
filenames = args.filenames

if __name__ == "__main__":
    files = str(filenames).split(",")
    merge_spectra(files, outfilename)

