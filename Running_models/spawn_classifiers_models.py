#!/usr/bin/env python

#_________________________________________________________________________________________________
#
# Author: Leanne Nortje
# Year: 2020
# Email: nortjeleanne@gmail.com
#_________________________________________________________________________________________________
#
# This script spawns the training of final models.
#

from datetime import datetime
from os import path
import argparse
import glob
import numpy as np
import os
from os import path
from scipy.io import wavfile
import matplotlib.pyplot as plt
import logging
import tensorflow as tf
import subprocess
import sys
from tqdm import tqdm

sys.path.append("..")
from paths import model_lib_path

sys.path.append(path.join("..", model_lib_path))
import model_setup_library

import warnings
warnings.filterwarnings("ignore")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

PRINT_LENGTH = model_setup_library.PRINT_LENGTH
SEEDS = [1, 5, 10, 21, 42]
#_____________________________________________________________________________________________________________________________________
#
# Argument function
#
#_____________________________________________________________________________________________________________________________________



def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_seeds", type=str, choices=["True", "False"], default="True")
    parser.add_argument("--test_batch_size", type=str, choices=["True", "False"], default="False")
    return parser.parse_args()


#_____________________________________________________________________________________________________________________________________
#
# Main
#
#_____________________________________________________________________________________________________________________________________


def main():

    parameters = arguments()

    model_commands = [

        ## 2

        "--model_type classifier --architecture rnn --data_type buckeye  --epochs 50 " 
        + "--features_type mfcc --train_tag gt --enc 400_400_400 --latent 130 --batch_size 512",

        "--model_type classifier --architecture cnn --data_type omniglot --epochs 50 " 
        + "--enc 3.3.32.1.1.2.2_3.3.64.1.1.2.2_3.3.128.1.1 --latent 130 --batch_size 64",

    ]
    
    test_seeds = parameters.test_seeds == "True"

    for this_command in model_commands:
        if test_seeds:
            for rnd_seed in SEEDS:
                cmd = "./train_model.py " + this_command + " --rnd_seed {}".format(rnd_seed)
                print_string = cmd
                model_setup_library.command_printing(print_string)
                sys.stdout.flush()
                proc = subprocess.Popen(cmd, shell=True)
                proc.wait()
        else:
            cmd = "./train_model.py " + this_command
            print_string = cmd
            model_setup_library.command_printing(print_string)
            sys.stdout.flush()
            proc = subprocess.Popen(cmd, shell=True)
            proc.wait()
    
if __name__ == "__main__":
    main()