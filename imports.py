#!/usr/bin/env python

# general
import json
import itertools
import pickle
#import hickle 
import gzip
import operator
import os
import sys
from time import time
import pprint as pp
import collections
import ConfigParser

# numpy
import numpy as np
import pandas as pd

# Twitter public API
#import twitter

#sklearn
from sklearn.feature_extraction import text
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cross_validation import train_test_split
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.externals import joblib


# bokeh
import bokeh.plotting as bkplt
from bokeh.charts import Histogram
from bokeh.io import output_notebook
from bokeh.charts import Histogram, show

# import requirments 
from IPython.display import Image
from IPython.display import display
import matplotlib.pyplot as plt
import json
import rpy2
from ggplot import *
