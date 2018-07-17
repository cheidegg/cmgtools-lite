#!/bin/env python
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer import *  
from PhysicsTools.Heppy.analyzers.core.autovars import *  
from PhysicsTools.Heppy.analyzers.objects.autophobj import  *
from math import *

##------------------------------------------  
## LEPTON
##------------------------------------------  

leptonTypeXtracks = NTupleObjectType("leptonXtracks", baseObjectTypes = [ leptonType ], variables = [
    NTupleVariable("etaSc", lambda x : x.superCluster().eta() if abs(x.pdgId())==11 else -100, help="Electron supercluster pseudorapidity"),
    NTupleVariable("mcMatchPdgId",  lambda x : x.mcLep.pdgId() if getattr(x,'mcLep',None)!=None else -99, int, mcOnly=True, help="Match to source from hard scatter (pdgId of heaviest particle in chain, 25 for H, 6 for t, 23/24 for W/Z): pdgId of the matched gen-level lepton, zero if non-prompt or fake"),
    NTupleVariable("mcPromptGamma", lambda x : x.mcPho.isPromptFinalState() if getattr(x,"mcPho",None) else 0, int, mcOnly=True, help="Photon isPromptFinalState"),
])
leptonTypeXtracks.removeVariable("relIsoAn04")
leptonTypeXtracks.removeVariable("eleCutIdSpring15_25ns_v1")
leptonTypeXtracks.removeVariable("ICHEPsoftMuonId")
leptonTypeXtracks.removeVariable("ICHEPmediumMuonId")

##------------------------------------------  
## TAU
##------------------------------------------  

tauTypeXtracks = NTupleObjectType("tauXtracks",  baseObjectTypes = [ tauType ], variables = [
     NTupleVariable("idMVAdR03", lambda x : x.idMVAdR03, int, help="1,2,3,4,5,6 if the tau passes the very loose to very very tight WP of the IsolationMVArun2v1DBdR03oldDMwLT discriminator"),
])
tauTypeXtracks.removeVariable("idMVANewDM")
tauTypeXtracks.removeVariable("idCI3hit")


jetTypeXtracks = NTupleObjectType("jetXtracks",  baseObjectTypes = [ jetTypeExtra ], variables = [
    NTupleVariable("chHEF", lambda x : x.chargedHadronEnergyFraction(), float, mcOnly = False, help="chargedHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("neHEF", lambda x : x.neutralHadronEnergyFraction(), float, mcOnly = False,help="neutralHadronEnergyFraction (relative to uncorrected jet energy)"),
])
jetTypeXtracks.removeVariable("btagCMVA")
jetTypeXtracks.removeVariable("nLeptons")

jetTypeXtracksFwd = NTupleObjectType("jetFwd",  baseObjectTypes = [ jetType ], variables = [
    NTupleVariable("chHEF", lambda x : x.chargedHadronEnergyFraction(), float, mcOnly = False, help="chargedHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("neHEF", lambda x : x.neutralHadronEnergyFraction(), float, mcOnly = False,help="neutralHadronEnergyFraction (relative to uncorrected jet energy)"),
])
jetTypeXtracks.removeVariable("btagCMVA")
jetTypeXtracksFwd.removeVariable("nLeptons")

##------------------------------------------  
## MET
##------------------------------------------  
  
metTypeXtracks = NTupleObjectType("metXtracks", baseObjectTypes = [ metType ], variables = [
])

metTypeXtracksBasic = NTupleObjectType("metXtracksBasic", baseObjectTypes = [ fourVectorType ], variables = [
])

##------------------------------------------  
## IsoTrackDeDx
##------------------------------------------

isoTrackTypeDeDx = NTupleObjectType("isoTrackTypeDeDx", baseObjectTypes = [ particleType ], variables = [
    NTupleVariable("charge",   lambda x : x.charge(), int),
    NTupleVariable("dxy",   lambda x : x.dxy(), help="d_{xy} with respect to PV, in cm (with sign)"),
    NTupleVariable("dz",    lambda x : x.dz() , help="d_{z} with respect to PV, in cm (with sign)"),
    NTupleVariable("edxy",  lambda x : x.dxyError(), help="#sigma(d_{xy}) with respect to PV, in cm"),
    NTupleVariable("edz", lambda x : x.dzError(), help="#sigma(d_{z}) with respect to PV, in cm"),    

    NTupleVariable("trackerLayers", lambda x : x.hitPattern().trackerLayersWithMeasurement(), int, help="Tracker Layers"),
    NTupleVariable("pixelLayers", lambda x : x.hitPattern().pixelLayersWithMeasurement(), int, help="Pixel Layers"),
    NTupleVariable("trackerHits", lambda x : x.hitPattern().numberOfValidTrackerHits(), int, help="Tracker hits"),
    NTupleVariable("pixelHits", lambda x : x.hitPattern().numberOfValidPixelHits(), int, help="Pixel hits"),
    NTupleVariable("missingInnerPixelHits", lambda x : x.hitPattern().numberOfLostPixelHits(1), int, help="Missing inner pixel hits"),
    NTupleVariable("missingOuterPixelHits", lambda x : x.hitPattern().numberOfLostPixelHits(2), int, help="Missing outer pixel hits"),
    NTupleVariable("missingInnerStripHits", lambda x : x.hitPattern().numberOfLostStripHits(1), int, help="Missing inner strips hits"),
    NTupleVariable("missingOuterStripHits", lambda x : x.hitPattern().numberOfLostStripHits(2), int, help="Missing outer strips hits"),
    NTupleVariable("missingInnerTrackerHits", lambda x : x.hitPattern().numberOfLostTrackerHits(1), int, help="Missing inner tracker hits"),
    NTupleVariable("missingOuterTrackerHits", lambda x : x.hitPattern().numberOfLostTrackerHits(2), int, help="Missing outer tracker hits"),
    NTupleVariable("missingMiddleTrackerHits", lambda x : x.hitPattern().numberOfLostTrackerHits(0), int, help="Missing tracker hits in the middle of the track"),

    NTupleVariable("highPurity", lambda x : x.isHighPurityTrack(), int, help="High purity"),

    NTupleVariable("caloEmEnergy",   lambda x : x.matchedCaloJetEmEnergy(), help="Energy in the ECAL behind the track"),
    NTupleVariable("caloHadEnergy",   lambda x : x.matchedCaloJetHadEnergy(), help="Energy in the HCAL behind the track"),
    NTupleVariable("channelsGoodECAL", lambda x : x.channelsGoodECAL, int, help="Flag set to 1 when the track extrapolates to all good ECAL channels"),
    NTupleVariable("channelsGoodHCAL", lambda x : x.channelsGoodHCAL, int, help="Flag set to 1 when the track extrapolates to all good HCAL channels"),

    NTupleVariable("awayJet_idx", lambda x : x.leadAwayJet.index if x.leadAwayJet else -1, int),
    NTupleVariable("awayJet_pt", lambda x : x.leadAwayJet.pt() if x.leadAwayJet else 0),
    NTupleVariable("awayJet_dr", lambda x : deltaR(x, x.leadAwayJet) if x.leadAwayJet else 0),

    NTupleVariable("awayNJet", lambda x : x.awayJetInfo['num'], int),
    NTupleVariable("awayHTJet", lambda x : x.awayJetInfo['ht']),

    NTupleVariable("awayMu_idx", lambda x : x.leadAwayMu.index if x.leadAwayMu else -1, int),
    NTupleVariable("awayMu_dr", lambda x : deltaR(x, x.leadAwayMu) if x.leadAwayMu else 0),
    NTupleVariable("awayMu_mll", lambda x : (x.leadAwayMu.p4()+x.p4()).M() if x.leadAwayMu else 0),

    NTupleVariable("awayEle_idx", lambda x : x.leadAwayEle.index if x.leadAwayEle else -1, int),
    NTupleVariable("awayEle_dr", lambda x : deltaR(x, x.leadAwayEle) if x.leadAwayEle else 0),
    NTupleVariable("awayEle_mll", lambda x : (x.leadAwayEle.p4()+x.p4()).M() if x.leadAwayEle else 0),

    NTupleVariable("closestMu_idx", lambda x : x.closestMu.index if x.closestMu else -1, int),
    NTupleVariable("closestEle_idx", lambda x : x.closestEle.index if x.closestEle else -1, int),
    NTupleVariable("closestTau_idx", lambda x : x.closestTau.index if x.closestTau else -1, int),

    NTupleVariable("trigLepton_idx", lambda x : x.trigLepton.index if getattr(x, 'trigLepton', None) else -1, int),

    NTupleVariable("myDeDx", lambda x : x.myDeDx),
    NTupleVariable("dedxByLayer0", lambda x : x.dedxByLayer[0]),
    NTupleVariable("dedxByLayer1", lambda x : x.dedxByLayer[1]),
    NTupleVariable("dedxByLayer2", lambda x : x.dedxByLayer[2]),
    NTupleVariable("dedxByLayer3", lambda x : x.dedxByLayer[3]),
    NTupleVariable("dedxByLayer4", lambda x : x.dedxByLayer[4]),
    NTupleVariable("dedxByLayer5", lambda x : x.dedxByLayer[5]),
    NTupleVariable("dedxByLayer6", lambda x : x.dedxByLayer[6]),
    NTupleVariable("dedxByLayer7", lambda x : x.dedxByLayer[7]),
    NTupleVariable("dedxByLayer8", lambda x : x.dedxByLayer[8]),
    NTupleVariable("dedxByLayer9", lambda x : x.dedxByLayer[9]),
    NTupleVariable("dedxByLayer10", lambda x : x.dedxByLayer[10]),
    NTupleVariable("dedxByLayer11", lambda x : x.dedxByLayer[11]),
    NTupleVariable("dedxByLayer12", lambda x : x.dedxByLayer[12]),
    NTupleVariable("dedxByLayer13", lambda x : x.dedxByLayer[13]),
    
    NTupleVariable("subDetIdByLayer0", lambda x : x.subDetIdByLayer[0], int),
    NTupleVariable("subDetIdByLayer1", lambda x : x.subDetIdByLayer[1], int),
    NTupleVariable("subDetIdByLayer2", lambda x : x.subDetIdByLayer[2], int),
    NTupleVariable("subDetIdByLayer3", lambda x : x.subDetIdByLayer[3], int),
    NTupleVariable("subDetIdByLayer4", lambda x : x.subDetIdByLayer[4], int),
    NTupleVariable("subDetIdByLayer5", lambda x : x.subDetIdByLayer[5], int),
    NTupleVariable("subDetIdByLayer6", lambda x : x.subDetIdByLayer[6], int),
    NTupleVariable("subDetIdByLayer7", lambda x : x.subDetIdByLayer[7], int),
    NTupleVariable("subDetIdByLayer8", lambda x : x.subDetIdByLayer[8], int),
    NTupleVariable("subDetIdByLayer9", lambda x : x.subDetIdByLayer[9], int),
    NTupleVariable("subDetIdByLayer10", lambda x : x.subDetIdByLayer[10], int),
    NTupleVariable("subDetIdByLayer11", lambda x : x.subDetIdByLayer[11], int),
    NTupleVariable("subDetIdByLayer12", lambda x : x.subDetIdByLayer[12], int),
    NTupleVariable("subDetIdByLayer13", lambda x : x.subDetIdByLayer[13], int),

    NTupleVariable("sizeXbyLayer0", lambda x : x.sizeXbyLayer[0], int),
    NTupleVariable("sizeXbyLayer1", lambda x : x.sizeXbyLayer[1], int),
    NTupleVariable("sizeXbyLayer2", lambda x : x.sizeXbyLayer[2], int),
    NTupleVariable("sizeXbyLayer3", lambda x : x.sizeXbyLayer[3], int),
    NTupleVariable("sizeXbyLayer4", lambda x : x.sizeXbyLayer[4], int),
    NTupleVariable("sizeXbyLayer5", lambda x : x.sizeXbyLayer[5], int),
    NTupleVariable("sizeXbyLayer6", lambda x : x.sizeXbyLayer[6], int),
    NTupleVariable("sizeXbyLayer7", lambda x : x.sizeXbyLayer[7], int),
    NTupleVariable("sizeXbyLayer8", lambda x : x.sizeXbyLayer[8], int),
    NTupleVariable("sizeXbyLayer9", lambda x : x.sizeXbyLayer[9], int),
    NTupleVariable("sizeXbyLayer10", lambda x : x.sizeXbyLayer[10], int),
    NTupleVariable("sizeXbyLayer11", lambda x : x.sizeXbyLayer[11], int),
    NTupleVariable("sizeXbyLayer12", lambda x : x.sizeXbyLayer[12], int),
    NTupleVariable("sizeXbyLayer13", lambda x : x.sizeXbyLayer[13], int),
                                                                                                         
    NTupleVariable("sizeYbyLayer0", lambda x : x.sizeYbyLayer[0], int),
    NTupleVariable("sizeYbyLayer1", lambda x : x.sizeYbyLayer[1], int),
    NTupleVariable("sizeYbyLayer2", lambda x : x.sizeYbyLayer[2], int),
    NTupleVariable("sizeYbyLayer3", lambda x : x.sizeYbyLayer[3], int),
    NTupleVariable("sizeYbyLayer4", lambda x : x.sizeYbyLayer[4], int),
    NTupleVariable("sizeYbyLayer5", lambda x : x.sizeYbyLayer[5], int),
    NTupleVariable("sizeYbyLayer6", lambda x : x.sizeYbyLayer[6], int),
    NTupleVariable("sizeYbyLayer7", lambda x : x.sizeYbyLayer[7], int),
    NTupleVariable("sizeYbyLayer8", lambda x : x.sizeYbyLayer[8], int),
    NTupleVariable("sizeYbyLayer9", lambda x : x.sizeYbyLayer[9], int),
    NTupleVariable("sizeYbyLayer10", lambda x : x.sizeYbyLayer[10], int),
    NTupleVariable("sizeYbyLayer11", lambda x : x.sizeYbyLayer[11], int),
    NTupleVariable("sizeYbyLayer12", lambda x : x.sizeYbyLayer[12], int),
    NTupleVariable("sizeYbyLayer13", lambda x : x.sizeYbyLayer[13], int),
                                                                                                         
    NTupleVariable("mcMatch", lambda x : x.mcMatch.index if x.mcMatch else -1, int, mcOnly=True)
]
)

##------------------------------------------  
## genCharginoType
##------------------------------------------  
genCharginoType  = NTupleObjectType("genCharginoType", baseObjectTypes = [ genParticleWithMotherId ], variables = [
    NTupleVariable("beta", lambda x : x.p()/x.energy()),
    NTupleVariable("decayR", lambda x : x.decayPoint.R()),
    NTupleVariable("decayZ", lambda x : x.decayPoint.Z()),
])

## Tree Producer
treeProducer = cfg.Analyzer(
    AutoFillTreeProducer, name='treeProducerXtracks',
    vectorTree = True, saveTLorentzVectors = False,  defaultFloatType = 'F', PDFWeights = [],
    globalVariables = [
        NTupleVariable("rho",  lambda ev: ev.rho, float, help="kt6PFJets rho"),
        NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"),

        NTupleVariable("nJet30", lambda ev: sum([j.pt() > 30 for j in ev.cleanJets]), int, help="Number of jets with pt > 30, |eta|<2.4"),
        NTupleVariable("nJet30a", lambda ev: sum([j.pt() > 30 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 30, |eta|<4.7"),

        ## ------- lheHT, needed for merging HT binned samples
        NTupleVariable("lheHT", lambda ev : getattr(ev,"lheHT",-999), mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer"),
        NTupleVariable("lheHTIncoming", lambda ev : getattr(ev,"lheHTIncoming",-999), mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer (only LHE status<0 as mothers)"),
        ],
    globalObjects = {
        "met"             : NTupleObject("met", metTypeXtracks, help="PF E_{T}^{miss}"),
        "metNoMu"         : NTupleObject("metNoMu", metTypeXtracksBasic, help="PF E_{T}^{miss} without muons"),
        "met_jecUp"       : NTupleObject("met_jecUp", metTypeXtracks, help="PF E_{T}^{miss}, after type 1 corrections (JEC plus 1sigma)"),
        "metNoMu_jecUp"   : NTupleObject("metNoMu_jecUp", metTypeXtracksBasic, help="PF E_{T}^{miss} without muons, after type 1 corrections (JEC plus 1sigma)"),
        "met_jecDown"     : NTupleObject("met_jecDown", metTypeXtracks, help="PF E_{T}^{miss}, after type 1 corrections (JEC minus 1sigma)"),
        "metNoMu_jecDown" : NTupleObject("metNoMu_jecUp", metTypeXtracksBasic, help="PF E_{T}^{miss} without muons, after type 1 corrections (JEC minus 1sigma)"),
        },
    collections = {
        ##--------------------------------------------------
        "selectedTaus"    : NTupleCollection("TauGood",  tauTypeXtracks, 8, help="Taus after the preselection"),
        "selectedLeptons" : NTupleCollection("LepGood",  leptonTypeXtracks, 8, help="Leptons after the preselection"),
        ##------------------------------------------------
        "cleanJets"       : NTupleCollection("Jet",     jetTypeXtracks, 15, help="Cental jets after full selection and cleaning, sorted by pt"),
        "cleanJetsFwd"    : NTupleCollection("JetFwd",  jetTypeXtracksFwd,  6, help="Forward jets after full selection and cleaning, sorted by pt"),
        ##------------------------------------------------
        "isoTracks"       : NTupleCollection("IsoTrack",  isoTrackTypeDeDx, 4, help="Isolated tracks"),
        ##------------------------------------------------
        "genCharginos"    : NTupleCollection("GenChargino",  genCharginoType, 4, mcOnly=True, help="Gen chargino"),
        },
    )

