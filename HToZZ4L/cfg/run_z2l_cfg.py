##########################################################
##       CONFIGURATION FOR HZZ4L TREES                  ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.HToZZ4L.analyzers.hzz4lCore_modules_cff import * 
from CMGTools.HToZZ4L.analyzers.hzz4lExtra_modules_cff import * 
from CMGTools.HToZZ4L.tools.configTools import * 

#-------- SEQUENCE
sequence = cfg.Sequence(hzz4lPreSequence +  [ fastSkim2L ] + hzz4lObjSequence + [
    twoLeptonAnalyzer, 
    twoLeptonEventSkimmer, 
    twoLeptonTreeProducer 
])

run = "Both"
run = "Mu" 
#run = "El"

#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.HToZZ4L.samples.samples_13TeV_Fall15 import *
if   run == "Mu": dataSamples2L = [ d for d in dataSamples if "DoubleM" in d.name ]
elif run == "El": dataSamples2L = [ d for d in dataSamples if "DoubleE" in d.name ]
else            : dataSamples2L = [ d for d in dataSamples if "Double"  in d.name ]
for d in dataSamples2L:
    d.triggers = triggers_mumu if 'Muon' in d.name else triggers_ee
    d.vetoTriggers = []
    d.splitFactor = (len(d.files)+4)/7
if   run == "Mu": dataSamples1L = [ d for d in dataSamples if "SingleM" in d.name ]
elif run == "El": dataSamples1L = [ d for d in dataSamples if "SingleE" in d.name ]
else            : dataSamples1L = [ d for d in dataSamples if "Single"  in d.name ]
for d in dataSamples1L:
    d.triggers = triggers_1mu if 'Muon' in d.name else triggers_1e
    d.vetoTriggers = triggers_mumu if 'Muon' in d.name else triggers_ee
    d.splitFactor = (len(d.files)+4)/7

    
mcSamples = [ DYJetsToLL_LO_M50 ]
for d in mcSamples:
    d.triggers = triggers_mumu + triggers_ee + triggers_1e + triggers_1mu
    d.vetoTriggers = []
    d.splitFactor = len(d.files)/1

#selectedComponents = dataSamples2L + dataSamples1L
selectedComponents = mcSamples + dataSamples2L + dataSamples1L
#selectedComponents = [c for c in selectedComponents if c.isMC or "Run2015D" in c.name ]
configureSplittingFromTime(dataSamples2L + dataSamples1L, 5.0, 2.)
configureSplittingFromTime(mcSamples, 21, 2)
#prescaleComponents(dataSamples2L, 4)
printSummary(selectedComponents)

#redefineRunRange(selectedComponents,[258214,258214])
if True: autoAAA(selectedComponents)
if run == "Mu":
    doKalmanMuonCorrections(smear="basic")
    fastSkim2L.eleCut = lambda ele : False
    lepAna.loose_electron_isoCut = lambda ele : False
elif run == "El":
    doECalCorrections(era="25ns")
    fastSkim2L.muCut = lambda mu : False
    lepAna.loose_muon_isoCut = lambda mu : False
else:
    doECalCorrections(era="25ns")
    doKalmanMuonCorrections(smear="basic")

from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
test = getHeppyOption('test')
if test in ("1","1M","1E"):
    component = { "1":DYJetsToLL_LO_M50, "1M":DoubleMuon_Run2015D_16Dec2015_25ns, "1E":DoubleEG_Run2015D_16Dec2015_25ns }[test]
    if not component.isMC: redefineRunRange([component],[258214,258214])
    selectedComponents = doTest1( component, sequence=sequence )
elif test in ('2','3','5'):
    doTestN(test,selectedComponents)

config = autoConfig(selectedComponents, sequence)
