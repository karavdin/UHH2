# This is a small example how the crab api can easily be used to create something like multi crab.
# It has some additional features like also creating the xml files for you. 
# For it to work you need inputDatasets & requestNames apart from the classical part 
#
# Make sure to have a unique directory where your joboutput is saved, otherwise the script gets confused and you too!!
#
# Usage ./CrabConfig ConfigFile [options]
#
# Take care here to make the request names *nice*
# 
# autocomplete_Datasets(ListOfDatasets) works also for several entries with *
#
from DasQuery import autocomplete_Datasets

inputDatasets = ['/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM']
inputDatasets = autocomplete_Datasets(inputDatasets)
requestNames = []
for x in inputDatasets:
    name = x.split('/')[1]
    modified_name =name.replace('_TuneCUETP8M1_13TeV-madgraphMLM-pythia8','')
    if 'ext1' in x:
        modified_name += '_ext1'
    elif 'ext2' in x:
        modified_name += '_ext2'
    elif 'ext' in x:
        modified_name += '_ext'
    requestNames.append(modified_name)


# ===============================================================================
# Classical part of crab, after resolving the * it uses in the example below just the first entry
#

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ProxyException
import os

config = config()
config.General.workArea = 'crab_Test'
config.General.transferOutputs = True
config.General.transferLogs = True
        
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = os.path.join(os.environ['CMSSW_BASE'], 'src/UHH2/core/python/ntuplewriter_mc_2018_dijet.py')
config.JobType.psetName = os.path.join(os.environ['CMSSW_BASE'], 'src/UHH2/core/python/ntuplewriter_mc_2018.py')
config.JobType.outputFiles = ["Ntuple.root"]
config.JobType.maxMemoryMB = 3000
        
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.unitsPerJob = 7500
#config.Data.unitsPerJob = 13000
#config.Data.unitsPerJob = 9800
#config.Data.unitsPerJob = 2000
#config.Data.unitsPerJob = 4000
config.Data.unitsPerJob = 16000
#config.Data.unitsPerJob = 15000
#config.Data.lumiMask = os.path.join(os.environ['CMSSW_BASE'], 'src/UHH2/scripts/crab/JSON_QCD_HT_6.txt')
try:
    config.Data.outLFNDirBase = '/store/user/%s/RunII_102X_v1_TEST/' % (getUsernameFromSiteDB())
except ProxyException as e:
    print "Encountered ProxyException:"
    print e.message
    print "Not setting config.Data.outLFNDirBase, will use default"

config.Data.publication = False
config.JobType.sendExternalFolder = True 
#config.Data.allowNonValidInputDataset = True
#config.Data.publishDataName = 'CRAB3_tutorial_May2015_MC_analysis'

config.Site.storageSite = 'T2_DE_DESY'

if len(inputDatasets) > 0 and len(requestNames) > 0:
    config.General.requestName = requestNames[0]
    config.Data.inputDataset = inputDatasets[0]


