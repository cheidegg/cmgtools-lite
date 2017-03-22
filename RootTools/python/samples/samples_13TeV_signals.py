import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

SMS_T1bbbb_mGluino1500_mLSP100 = kreator.makeMCComponent("SMS_T1bbbb_mGluino1500_mLSP100", "/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM", "CMS", ".*root", 0.0141903)
SMS_T1tttt_mGluino1500_mLSP100 = kreator.makeMCComponent("SMS_T1tttt_mGluino1500_mLSP100", "/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM", "CMS", ".*root", 0.0141903)
SMS_T2tt_mStop_150to250 = kreator.makeMCComponent("SMS_T2tt_mStop_150to250", "/SMS-T2tt_mStop-150to250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", -1)
SMS_T2tt_mStop_250to350 = kreator.makeMCComponent("SMS_T2tt_mStop_250to350", "/SMS-T2tt_mStop-250to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", -1)
SMS_T2tt_mStop_350to400 = kreator.makeMCComponent("SMS_T2tt_mStop_350to400", "/SMS-T2tt_mStop-350to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", -1)
SMS_T2tt_mStop_400to1200 = kreator.makeMCComponent("SMS_T2tt_mStop_400to1200", "/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", -1)
SMS_T2tt_mStop_425_mLSP_325 = kreator.makeMCComponent("SMS_T2tt_mStop_425_mLSP_325", "/SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 1.31169 )
SMS_T2tt_mStop_500_mLSP_325 = kreator.makeMCComponent("SMS_T2tt_mStop_500_mLSP_325", "/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM", "CMS", ".*root", 0.51848 )
SMS_T2tt_mStop_850_mLSP_100 = kreator.makeMCComponent("SMS_T2tt_mStop_850_mLSP_100", "/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 0.0189612 ) 
SMS_T1tttt=kreator.makeMCComponent("SMS_T1tttt","/SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_T5qqqqVV=kreator.makeMCComponent("SMS_T5qqqqVV","/SMS-T5qqqqVV_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_T6ttWW=kreator.makeMCComponent("SMS_T6ttWW","/SMS-T6ttWW_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_T6ttHZ=kreator.makeMCComponent("SMS_T6ttHZ","/SMS-T6ttHZ_BR-H_0p6_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root",1,True)

SMS_T6bbllslepton_mSbottom_1000To1500_mLSP_120To1450 = kreator.makeMCComponent("SMS_T6bbllslepton_mSbottom_1000To1500_mLSP_120To1450", "/SMS-T6bbllslepton_mSbottom-1000To1500_mLSP-120To1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_T6bbllslepton_mSbottom_400To950_mLSP_120To140 = kreator.makeMCComponent("SMS_T6bbllslepton_mSbottom_400To950_mLSP_120To140", "/SMS-T6bbllslepton_mSbottom-400To950_mLSP-120To140_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_T6bbllslepton_mSbottom_400To575_mLSP_150To550 = kreator.makeMCComponent("SMS_T6bbllslepton_mSbottom_400To575_mLSP_150To550", "/SMS-T6bbllslepton_mSbottom-400To575_mLSP-150To550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-pLHE_PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS",".*root",1,True)
SMS_T6bbllslepton_mSbottom_600To775_mLSP_150To725 = kreator.makeMCComponent("SMS_T6bbllslepton_mSbottom_600To775_mLSP_150To725", "/SMS-T6bbllslepton_mSbottom-600To775_mLSP-150To725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-pLHE_PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS",".*root",1,True)
SMS_T6bbllslepton_mSbottom_800To950_mLSP_150To900 = kreator.makeMCComponent("SMS_T6bbllslepton_mSbottom_800To950_mLSP_150To900", "/SMS-T6bbllslepton_mSbottom-800To950_mLSP-150To900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-pLHE_PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS",".*root",1,True)


## EWKino signals 
#SMS_TChiWZ=kreator.makeMCComponent("SMS_TChiWZ","/SMS-TChiWZ_ZToLL_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM","CMS",".*root",1,useAAA=True) ## ICHEP
SMS_TChiWZ=kreator.makeMCComponent("SMS_TChiWZ","/SMS-TChiWZ_ZToLL_mZMin-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root",1,True) ## post-ICHEP
SMS_TChiWH=kreator.makeMCComponent("SMS_TChiWH","/SMS-TChiWH_WToLNu_HToVVTauTau_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiSlepSnux0p5=kreator.makeMCComponent("SMS_TChiSlepSnux0p5","/SMS-TChiSlepSnu_x0p5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiSlepSnux0p5ext=kreator.makeMCComponent("SMS_TChiSlepSnux0p5ext","/SMS-TChiSlepSnu_x0p5_mC1-1250to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiSlepSnux0p05=kreator.makeMCComponent("SMS_TChiSlepSnux0p05","/SMS-TChiSlepSnu_x0p05_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiSlepSnux0p05ext=kreator.makeMCComponent("SMS_TChiSlepSnux0p05ext","/SMS-TChiSlepSnu_x0p05_mC1-1250to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiSlepSnux0p95=kreator.makeMCComponent("SMS_TChiSlepSnux0p95","/SMS-TChiSlepSnu_x0p95_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiSlepSnuTEx0p5=kreator.makeMCComponent("SMS_TChiSlepSnuTEx0p5","/SMS-TChiSlepSnu_tauenriched_x0p5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiSlepSnuTEx0p05=kreator.makeMCComponent("SMS_TChiSlepSnuTEx0p05","/SMS-TChiSlepSnu_tauenriched_x0p05_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiSlepSnuTEx0p95=kreator.makeMCComponent("SMS_TChiSlepSnuTEx0p95","/SMS-TChiSlepSnu_tauenriched_x0p95_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiStauStaux0p5=kreator.makeMCComponent("SMS_TChiStauStaux0p5","/SMS-TChiStauStau_x0p5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiStauStaux0p5ext=kreator.makeMCComponent("SMS_TChiStauStaux0p5ext","/SMS-TChiStauStau_x0p5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM","CMS",".*root",1,True)

SMS_TChiZZ2L=kreator.makeMCComponent("SMS_TChiZZ2L","/SMS-TChiZZ_ZToLL_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiZZ4L=kreator.makeMCComponent("SMS_TChiZZ4L","/SMS-TChiZZ_ZToLL_ZToLL_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiHZ=kreator.makeMCComponent("SMS_TChiHZ","/SMS-TChiHZ_HToWWZZTauTau_2LFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM","CMS",".*root",1,True)
SMS_TChiHH=kreator.makeMCComponent("SMS_TChiHH","/SMS-TChiHH_HToWWZZTauTau_HToWWZZTauTau_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM","CMS",".*root",1,True)

SignalSUSY = [
SMS_T1bbbb_mGluino1500_mLSP100,
SMS_T1tttt_mGluino1500_mLSP100,
SMS_T2tt_mStop_150to250,
SMS_T2tt_mStop_250to350,
SMS_T2tt_mStop_350to400,
SMS_T2tt_mStop_400to1200,
SMS_T2tt_mStop_425_mLSP_325,
SMS_T2tt_mStop_500_mLSP_325,
SMS_T2tt_mStop_850_mLSP_100,
SMS_T1tttt,
SMS_T5qqqqVV,
SMS_T6ttWW,
SMS_T6ttHZ,
SMS_T6bbllslepton_mSbottom_1000To1500_mLSP_120To1450,
SMS_T6bbllslepton_mSbottom_400To950_mLSP_120To140,
SMS_T6bbllslepton_mSbottom_400To575_mLSP_150To550,
SMS_T6bbllslepton_mSbottom_600To775_mLSP_150To725,
SMS_T6bbllslepton_mSbottom_800To950_mLSP_150To900,
SMS_TChiWZ,
SMS_TChiWH,
SMS_TChiSlepSnux0p5,
SMS_TChiSlepSnux0p5ext,
SMS_TChiSlepSnux0p05,
SMS_TChiSlepSnux0p05ext,
SMS_TChiSlepSnux0p95,
SMS_TChiSlepSnuTEx0p5,
SMS_TChiSlepSnuTEx0p05,
SMS_TChiSlepSnuTEx0p95,
SMS_TChiStauStaux0p5,
SMS_TChiStauStaux0p5ext,
SMS_TChiZZ2L, 
SMS_TChiZZ4L,
SMS_TChiHZ,
SMS_TChiHH,
]

### ----------------------------- summary ----------------------------------------


signalSamples = SignalSUSY

samples = signalSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in signalSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
