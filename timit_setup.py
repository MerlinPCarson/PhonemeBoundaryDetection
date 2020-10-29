import os
import sys
import time
from shutil import move 
import argparse
from glob import glob
from tqdm import tqdm


def setup_timit(timit_path):

    for dataset in ['train', 'test']:
        #outdir = os.path.join(timit_path, dataset.lower())
        #os.makedirs(outdir, exist_ok=True)
        print(os.path.join(timit_path, dataset, '**/*.wav'))
        for wav in tqdm(glob(os.path.join(timit_path, dataset, '**/*.wav'), recursive=True)):
            #print(wav)
            new_wav = wav.replace('.WAV.wav', '.wav')
            # copy wav file to new location
            print(f'moving {wav} --> {new_wav}')
            move(wav, new_wav)
            # copy corresponding phoneme files
            print(f'moving {new_wav.replace(".wav",".PHN")} --> {new_wav.replace(".wav",".phn")}')
            move(new_wav.replace('.wav', '.PHN'), new_wav.replace('.wav', '.phn'))
            

def main():
    start = time.time()

    parser = argparse.ArgumentParser(description='Sets up TIMIT dataset for segmentation train/test')
    parser.add_argument('--timit_path', type=str)
    args = parser.parse_args()

    # put files from TIMIT dataset in correct file structure for training and testing 
    setup_timit(args.timit_path)

    print(f'Script completed in {time.time()-start:.2f} secs')

    return 0

if __name__ == '__main__':
    sys.exit(main())
