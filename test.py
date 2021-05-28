# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np

LoadIsawPeaks(
    Filename='data/Natrolite_runs_133752_133812.peaks',
    OutputWorkspace='pws',
    )
SCDCalibratePanels(
    PeakWorkspace='pws',
    a=18.29,
    b=18.64,
    c=6.56,
    alpha=90, beta=90, gamma=90,
    CalibrateBanks=True,
    SearchRadiusTransBank=0.1,
    ToleranceTransBank=1e-16,
    SearchradiusRotBank=10,
    ToleranceRotBank=1e-16,
    CalibrateT0=True,
    TuneSamplePosition=False,
    OutputWorkspace='pws_caliL1',
    DetCalFilename='SCDCalibrate2.DetCal',
    XmlFilename='SCDCalibrate2.xml',
    CSVFilename='SCDCalibrate2.csv',
    VerboseOutput=True,
    )

LoadEmptyInstrument(
    InstrumentName='CORELLI',
    OutputWorkspace='corelli',
    )

LoadIsawDetCal(
    InputWorkspace='corelli',
    Filename='SCDCalibrate2.DetCal',
    )
