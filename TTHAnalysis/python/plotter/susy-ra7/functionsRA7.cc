#include "TMath.h"
#include <assert.h>
#include <iostream>
#include "TH2F.h"
#include "TH1F.h"
#include "TFile.h"
#include "TSystem.h"
#include "TGraphAsymmErrors.h"

int allTight(int nLep, int l1isTight, int l2isTight, int l3isTight, int l4isTight = 0){
    if(nLep == 3) return ((l1isTight+l2isTight+l3isTight)==3);
    return ((l1isTight+l2isTight+l3isTight+l4isTight)==4);
}

int isGoodFake(float pt, int isTight) {
    if(pt == 0) return 0;
    if(isTight) return 0;
    return 1;
}

int isFake(int nLep, int lep1mcUCSX, int lep2mcUCSX, int lep3mcUCSX, int lep4mcUCSX = 0) {
    if(nLep == 3) return ((lep1mcUCSX==2 || lep1mcUCSX==3) || (lep2mcUCSX==2 || lep2mcUCSX==3) || (lep3mcUCSX==2 || lep3mcUCSX==3));
    return ((lep1mcUCSX==2 || lep1mcUCSX==3) || (lep2mcUCSX==2 || lep2mcUCSX==3) || (lep3mcUCSX==2 || lep3mcUCSX==3) || (lep4mcUCSX==2 || lep4mcUCSX==3));
}



float mTcalc(float mT_3l, float mT_4l, float mT_fo_3l, float mT_fo_4l, int nLepTight, int nLepSel, int UCSX1, int UCSX2, int UCSX3){
  float mTW = 0.;
  if (nLepTight<3 || UCSX1>1 || UCSX2>1 || UCSX3>1){
      if (nLepSel==3) mTW = mT_fo_3l;
      else if (nLepSel==4) mTW = mT_fo_4l;
  } else {
      if (nLepTight==3) mTW = mT_3l;
      else if (nLepTight==4) mTW = mT_4l;
  }
  return mTW;
}


float getLeptonSF_mu_Unc(float pt, int var) {
  if (pt<20) 
    return var*TMath::Sqrt(0.03*0.03+0.01*0.01+0.01*0.01);
  else 
    return var*TMath::Sqrt(0.02*0.02+0.01*0.01);  
}




float getSF(TH2F* hist, float pt, float eta){
    int xbin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt)));
    int ybin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(eta)));
    return hist->GetBinContent(xbin,ybin);
}

float getUnc(TH2F* hist, float pt, float eta){
    int xbin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt)));
    int ybin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(eta)));
    return hist->GetBinError(xbin,ybin);
}


TFile *_file_reco_leptonSF_mu = NULL;
TFile *_file_recoToMedium_leptonSF_mu = NULL;
TFile *_file_MediumToMVA_leptonSF_mu = NULL;
TFile *_file_MediumToMultiIso_leptonSF_mu = NULL;
TFile *_file_recoToMVA_leptonSF_el = NULL;
TFile *_file_reco_leptonSF_el = NULL;

TGraphAsymmErrors *_histo_reco_leptonSF_mu = NULL;
TH2F *_histo_recoToMedium_leptonSF_mu = NULL;
TH2F *_histo_MediumToMVA_leptonSF_mu = NULL;
TH2F *_histo_MediumToMultiIso_leptonSF_mu = NULL;
TH2F *_histo_recoToMVA_leptonSF_el = NULL;
TH2F *_histo_reco_leptonSF_el = NULL;

TH2F *_histo_recoToTight_leptonSF_el = NULL;
TH2F *_histo_TightToMultiIso_leptonSF_el = NULL;



TString CMSSW_BASE_RA7 = gSystem->ExpandPathName("${CMSSW_BASE}");
TString DATA_RA7 = CMSSW_BASE_RA7+"/src/CMGTools/TTHAnalysis/data";

//// LEPTON SF FULLSIM

float leptonSF_ra7(int pdgid, float pt, float eta, int var=0){
  
  if (!_histo_reco_leptonSF_mu) {
     _file_reco_leptonSF_mu = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fullsim/muons/sf_mu_trk_susy_ICHEP.root", "data");
     _file_recoToMedium_leptonSF_mu = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fullsim/muons/TnP_MuonID_NUM_MediumID_DENOM_generalTracks_VAR_map_pt_eta.root", "read");
     _file_MediumToMultiIso_leptonSF_mu = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fullsim/muons/TnP_MuonID_NUM_MultiIsoLoose_DENOM_MediumID_VAR_map_pt_eta.root", "read");
     _histo_reco_leptonSF_mu = (TGraphAsymmErrors*)(_file_reco_leptonSF_mu->Get("ratio_eta"));
     _histo_recoToMedium_leptonSF_mu = (TH2F*)(_file_recoToMedium_leptonSF_mu->Get("pt_abseta_PLOT_pair_probeMultiplicity_bin0"));
     _histo_MediumToMultiIso_leptonSF_mu = (TH2F*)(_file_MediumToMultiIso_leptonSF_mu->Get("pt_abseta_PLOT_pair_probeMultiplicity_bin0_&_Medium2016_pass"));
   }
   if (!_histo_recoToTight_leptonSF_el) {
     _file_recoToMVA_leptonSF_el = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fullsim/electrons/sf_el_susy_ICHEP.root", "read");
     _histo_recoToTight_leptonSF_el = (TH2F*)(_file_recoToMVA_leptonSF_el->Get("GsfElectronToTightID2D3D"));
     _histo_TightToMultiIso_leptonSF_el = (TH2F*)(_file_recoToMVA_leptonSF_el->Get("MVATightElectronToMultiIsoM"));
     
     _file_reco_leptonSF_el = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fullsim/electrons/sf_el_trk_susy_ICHEP.root", "read");
     _histo_reco_leptonSF_el = (TH2F*) (_file_reco_leptonSF_el->Get("EGamma_SF2D"));
   }
   float out = 0.;
   if (abs(pdgid)==13){
     out = _histo_reco_leptonSF_mu->Eval(eta);
     TH2F *hist = _histo_recoToMedium_leptonSF_mu;
     int ptbin  = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt)));
     int etabin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(fabs(eta))));
     /*out *= hist->GetBinContent(ptbin,etabin);
     hist = _histo_MediumToMultiIso_leptonSF_mu;
     ptbin  = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt)));
     etabin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(fabs(eta))));
     out *= hist->GetBinContent(ptbin,etabin);*/
     return out + out*getLeptonSF_mu_Unc(pt,var);
   }
   float err = 0.;
   if (abs(pdgid)==11){
     TH2F *hist = _histo_recoToTight_leptonSF_el;
     int ptbin  = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt)));
     int etabin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(fabs(eta))));
     out = hist->GetBinContent(ptbin,etabin);
     err = hist->GetBinError(ptbin,etabin)*hist->GetBinError(ptbin,etabin);
     hist = _histo_TightToMultiIso_leptonSF_el;
     ptbin  = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(pt)));
     etabin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(eta)));
     out *= hist->GetBinContent(etabin,ptbin);
     err += hist->GetBinError(etabin,ptbin)*hist->GetBinError(etabin,ptbin);
     hist = _histo_reco_leptonSF_el;
     ptbin  = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(pt)));
     etabin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(eta)));
     out *= hist->GetBinContent(etabin,ptbin);
     err += hist->GetBinError(etabin,ptbin)*hist->GetBinError(etabin,ptbin);
     err = TMath::Sqrt(err);
     return out + out*err*var;
   }
   //cout << "[ERROR]!!!! SF UnKNOWN!!! PLEASE CHECK" << endl;
   return 1.;
 }



// LEPTON SCALE FACTORS FASTSIM
// -------------------------------------------------------------

// electrons
TFile* f_elSF_FS_MIM = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fastsim/electrons/sf_el_multiMedium.root", "read");
TFile* f_elSF_FS_Tid = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fastsim/electrons/sf_el_tightMVA_IDISOEmu_mutliT_tight2DIP_tight3DIP_vtxC_hitseq0_charge.root"   , "read");
TH2F* h_elSF_FS_MIM  = (TH2F*) f_elSF_FS_MIM->Get("histo2D");
TH2F* h_elSF_FS_Tid  = (TH2F*) f_elSF_FS_Tid->Get("histo2D");

// muons
TFile* f_muSF_FS_MIL = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fastsim/muons/sf_mu_mediumID_multiL.root", "read");
TFile* f_muSF_FS_Mid = new TFile(DATA_RA7+"/leptonSF/ra7_lepsf_fastsim/muons/sf_mu_medium.root"   , "read");
TH2F* h_muSF_FS_MIL  = (TH2F*) f_muSF_FS_MIL->Get("histo2D");
TH2F* h_muSF_FS_Mid  = (TH2F*) f_muSF_FS_Mid->Get("histo2D");


float getElectronSFFS(float pt, float eta){
    return getSF(h_elSF_FS_MIM, pt, abs(eta))*getSF(h_elSF_FS_Tid, pt, abs(eta));
}

float getElectronUncFS(int var = 0){
	return var*0.02;
}

float getMuonSFFS(float pt, float eta){
    return getSF(h_muSF_FS_MIL, pt, abs(eta))*getSF(h_muSF_FS_Mid, pt, abs(eta)); 
}

float getMuonUncFS(float pt, int var = 0) {
	return var*0.02;
}



float getLepSFFS(float pt, float eta, int pdgId, int isTight, int wp = 0, int var = 0){
    if(!isTight) return 1.0;
    if(abs(pdgId) == 13) return (var==0)?getMuonSFFS    (pt, eta):(1+getMuonUncFS(var));
    if(abs(pdgId) == 11) return (var==0)?getElectronSFFS(pt, eta):(1+getElectronUncFS(var));
    return 1.0;
}

float leptonSFFS(float lepSF1, float lepSF2, float lepSF3 = 1.0, float lepSF4 = 1.0){
    return lepSF1*lepSF2*lepSF3*lepSF4;
}







TFile* f_trigSF       = new TFile(DATA_RA7+"/triggerSF/triggerSF_EWKino_fullsim_ICHEP2016_9p2fb.root"       , "read");
TFile* f_trigSF_ele27 = new TFile(DATA_RA7+"/triggerSF/triggerSF_Ele27_EWKino_fullsim_ICHEP2016_12p9fb.root", "read");

TH2F* h_trigSF_3l_mu = (TH2F*) f_trigSF      ->Get("eff_3l_mu" );
TH2F* h_trigSF_3l_el = (TH2F*) f_trigSF      ->Get("eff_3l_ele");
TH2F* h_trigSF_2l_mu = (TH2F*) f_trigSF      ->Get("eff_2l_mu" );
TH2F* h_trigSF_2l_el = (TH2F*) f_trigSF      ->Get("eff_2l_ele");
TH2F* h_trigSF_ele27 = (TH2F*) f_trigSF_ele27->Get("hist2dnum_Ele27_WPLoose_Gsf__HLT_Ele27_WPLoose_Gsf");

float triggerSF(int BR, float pt1, int pdg1, 
                        float pt2, int pdg2, 
                        float pt3 = 0, int pdg3 = 0, 
                        float pt4 = 0, int pdg4 = 0){
    // Lesya's mail:
    // - split for trailing ele or trailing mu
    // - 3l: subleading vs trailing lepton pt (1l + 2l triggers)
    // - 2l: leading light lepton vs subleading light lepton ==> good for both 2l+tau and 2lSS cases (1l + 2l triggers)
    // - l+tautau: use flat 86% everywhere; pt_e > 35 GeV; pt_mu > 25 GeV (1l + l/tau triggers)

    // 3l: 2tau (flat 86% in dedicated function)
    if(BR == 6) return 1.0;

    // 3l: 3light
    if(BR <= 2) {
        TH2F* hist = (abs(pdg3) == 13)?h_trigSF_3l_mu:h_trigSF_3l_el;
        int xbin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt2)));
        int ybin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(pt3)));
        return hist->GetBinContent(xbin,ybin);
    } 

    // 3l: 2light + 1tau
    if(BR >= 3 && BR <= 5){
        vector<int> pdgs; vector<float> pts;
        if(abs(pdg1)!=15) { pdgs.push_back(abs(pdg1)); pts.push_back(pt1); }
        if(abs(pdg2)!=15) { pdgs.push_back(abs(pdg2)); pts.push_back(pt2); }
        if(abs(pdg3)!=15) { pdgs.push_back(abs(pdg3)); pts.push_back(pt3); }
        TH2F* hist = (pdgs[1] == 13)?h_trigSF_2l_mu:h_trigSF_2l_el;
        int xbin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pts[0])));
        int ybin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(pts[1])));
        return hist->GetBinContent(xbin,ybin);
    }

    // 2lss 
    if(BR == -1){
        TH2F* hist = (pdg2 == 13)?h_trigSF_2l_mu:h_trigSF_2l_el;
        int xbin = std::max(1, std::min(hist->GetNbinsX(), hist->GetXaxis()->FindBin(pt1)));
        int ybin = std::max(1, std::min(hist->GetNbinsY(), hist->GetYaxis()->FindBin(pt2)));
        return hist->GetBinContent(xbin,ybin);
    }

    // others: (4l, crwz) 
    return 1;
}







TFile* f_puw_nInt_ICHEP    = new TFile(DATA_RA7+"/pileup/puWeights_12fb_63mb.root"     , "read");;
TFile* f_puw_nInt_ICHEP_Up = new TFile(DATA_RA7+"/pileup/puWeights_12fb_63mb_Up.root"  , "read");
TFile* f_puw_nInt_ICHEP_Dn = new TFile(DATA_RA7+"/pileup/puWeights_12fb_63mb_Down.root", "read");
TH1F* h_puw_nInt_ICHEP    = (TH1F*) (f_puw_nInt_ICHEP   ->Get("puw"));
TH1F* h_puw_nInt_ICHEP_Up = (TH1F*) (f_puw_nInt_ICHEP_Up->Get("puw"));
TH1F* h_puw_nInt_ICHEP_Dn = (TH1F*) (f_puw_nInt_ICHEP_Dn->Get("puw"));

float puw_nInt_ICHEP(float nInt, int var=0) { 

  float puw = h_puw_nInt_ICHEP->GetBinContent(h_puw_nInt_ICHEP->FindBin(nInt)); 
  if(var== 0) return puw;
  if(var== 1) return h_puw_nInt_ICHEP_Up->GetBinContent(h_puw_nInt_ICHEP_Up->FindBin(nInt)) / puw;
  if(var==-1) return h_puw_nInt_ICHEP_Dn->GetBinContent(h_puw_nInt_ICHEP_Dn->FindBin(nInt)) / puw;
  cout <<"[WARNING!!!]  don't know what to do with PUweight, please check!! ";
  return -9999.;
}

TFile* f_puw_nInt_Moriond    = new TFile(DATA_RA7+"/pileup/puw_nTrueInt_Moriond2017_36p5fb_Summer16_central.root", "read");
TFile* f_puw_nInt_Moriond_Up = new TFile(DATA_RA7+"/pileup/puw_nTrueInt_Moriond2017_36p5fb_Summer16_up.root", "read");
TFile* f_puw_nInt_Moriond_Dn = new TFile(DATA_RA7+"/pileup/puw_nTrueInt_Moriond2017_36p5fb_Summer16_down.root", "read");
TH1F* h_puw_nInt_Moriond    = (TH1F*) (f_puw_nInt_Moriond   ->Get("puw"));
TH1F* h_puw_nInt_Moriond_Up = (TH1F*) (f_puw_nInt_Moriond_Up->Get("puw"));
TH1F* h_puw_nInt_Moriond_Dn = (TH1F*) (f_puw_nInt_Moriond_Dn->Get("puw"));

float puw_nInt_Moriond(float nInt, int var=0) { 
 
  float puw = h_puw_nInt_Moriond->GetBinContent(h_puw_nInt_Moriond->FindBin(nInt)); 
  if(var== 0) return puw;
  if(var== 1) return h_puw_nInt_Moriond_Up->GetBinContent(h_puw_nInt_Moriond_Up->FindBin(nInt)) / puw;
  if(var==-1) return h_puw_nInt_Moriond_Dn->GetBinContent(h_puw_nInt_Moriond_Dn->FindBin(nInt)) / puw;
  cout <<"[WARNING!!!]  don't know what to do with PUweight, please check!! ";
  return -9999.;
}





void functionsRA7() {}
