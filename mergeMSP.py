import argparse
import glob
from itertools import chain


from matchms.importing import load_from_msp
from matchms.exporting import save_as_msp   

def read_filenames(filename_extension):
    filenames = glob.glob('*.' + filename_extension, recursive=True)
    return filenames

def read_spectra(filenames):
    spectra = list(chain(*[load_from_msp(file) for file in filenames]))
    return spectra

def write_spectra(filenames, outfile):    
    spectra = read_spectra(filenames)
    outfilename = outfile + ".msp"
    save_as_msp(spectra, outfilename)


def merge_spectra(filename_extension, outfilename):
    filenames = read_filenames(filename_extension)
    return write_spectra(filenames, outfilename)



listarg = argparse.ArgumentParser()
listarg.add_argument('--filename_extension', type=str) 
listarg.add_argument('--outfilename', type=str) 
args=listarg.parse_args()
outfilename = args.outfilename
filename_extension = args.filename_extension

if __name__ == "__main__":
    merge_spectra(filename_extension, outfilename)
