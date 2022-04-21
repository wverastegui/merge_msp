import glob

def read_filenames():
    filenames = glob.glob('*.msp', recursive=True)
    return filenames