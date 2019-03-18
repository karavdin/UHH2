import FWCore.ParameterSet.Config as cms
from UHH2.core.ntuple_generator import generate_process  # use CMSSW type path for CRAB
from UHH2.core.optionsParse import setup_opts, parse_apply_opts


"""NTuple config for 2018 MC datasets.

You should try and put any centralised changes in generate_process(), not here.
"""


process = generate_process(year="2017v3", useData=False)

# Please do not commit changes to source filenames - used for consistency testing
process.source.fileNames = cms.untracked.vstring([
      '/store/relval/CMSSW_10_5_0_pre1/RelValQCD_FlatPt_15_3000HS_13/MINIAODSIM/PU25ns_105X_mc2017_realistic_Hcal_v1_HS-v1/10000/672F16A2-5BE5-8647-A1B4-3A4B4DBE2E3C.root',
    #'/store/mc/RunIIAutumn18MiniAOD/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/2A6B8F74-04C7-1B46-A56E-8C786D0C2E84.root'
#    '/store/relval/CMSSW_10_5_0_pre2/RelValQCD_FlatPt_15_3000HS_13/MINIAODSIM/PU25ns_105X_mc2017_realistic_v4_HS_old-v1/10000/42351B6F-77DD-6F4D-807D-2746873B38F1.root'
    # '/store/mc/RunIIAutumn18MiniAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/D774DA06-04F6-5E45-B02E-70ECD0DD697F.root'
    # '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v1/110000/5A494E5A-1A3B-B947-9F85-AF4588ACBBBA.root'
])

process.MyNtuple.doTrigger=False
process.MyNtuple.doPFJetConstituentsNjets=3
process.MyNtuple.doPFTopJetConstituentsNjets=3
process.MyNtuple.doGenJetConstituentsNjets=3
process.MyNtuple.doGenTopJetConstituentsNjets=3

# Do this after setting process.source.fileNames, since we want the ability to override it on the commandline
options = setup_opts()
parse_apply_opts(process, options)

with open('pydump_mc_2017v4.py', 'w') as f:
    f.write(process.dumpPython())

