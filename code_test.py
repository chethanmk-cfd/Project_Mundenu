from glob import glob
from typing import List, Tuple
from os.path import isdir, join
from shutil import copy
from copy import deepcopy
from time import time
from collections import defaultdict
import numpy as np
import torch as pt
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
from flowtorch.data import FOAMDataloader

for dtype in [np.float32, np.float64]:
    finfo = np.finfo(dtype)
    print(f"dtype: {finfo.dtype}")
    print(f"Number of bits: {finfo.bits}")
    print(f"Bits reserved for mantissa: {finfo.nmant}")
    print(f"Bits reserved for exponent: {finfo.iexp}")
    print("Largest representable number: {:e}".format(finfo.max))
    print("Smallest representable number: {:e}".format(finfo.min))
    print("Machine tolerance: {:e}".format(finfo.eps))
    print(f"Approximately accurate up to {finfo.precision} decimal digits")
    print("-"*46)

