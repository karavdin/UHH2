#include "UHH2/common/include/JetIds.h"

using namespace std;
using namespace uhh2;

CSVBTag::CSVBTag(wp working_point) {
    switch(working_point){
        case WP_LOOSE:
            csv_threshold = 0.460f;
            break;
        case WP_MEDIUM:
            csv_threshold = 0.800f;
            break;
        case WP_TIGHT:
            csv_threshold = 0.935f;
            break;
        default:
            throw invalid_argument("invalid working point passed to CSVBTag");
    }
}

CSVBTag::CSVBTag(float float_point):csv_threshold(float_point) {}


bool CSVBTag::operator()(const Jet & jet, const Event &) const{
    return jet.btag_combinedSecondaryVertex() > csv_threshold;
}

MVABTag::MVABTag(wp working_point) {
    switch(working_point){
        case WP_LOOSE:
            mva_threshold = -0.715f;
            break;
        case WP_MEDIUM:
            mva_threshold = 0.185f;
            break;
        case WP_TIGHT:
            mva_threshold = 0.875f;
            break;
        default:
            throw invalid_argument("invalid working point passed to MVABTag");
    }
}

MVABTag::MVABTag(float float_point):mva_threshold(float_point) {}


bool MVABTag::operator()(const Jet & jet, const Event &) const{
    return jet.btag_combinedSecondaryVertexMVA() > mva_threshold;
}


JetPFID::JetPFID(wp working_point):m_working_point(working_point){}

bool JetPFID::operator()(const Jet & jet, const Event &) const{
  switch(m_working_point){
  case WP_LOOSE:
    return looseID(jet);
  case WP_TIGHT:
    return tightID(jet);
  case  WP_TIGHT_LEPVETO:
    return tightLepVetoID(jet);
  default:
    throw invalid_argument("invalid working point passed to JetPFID");
  }
  return false;
}

bool JetPFID::looseID(const Jet & jet) const{
  if(fabs(jet.eta())<=3 
     && jet.numberOfDaughters()>1 
     && jet.neutralHadronEnergyFraction()<0.99
     && jet.neutralEmEnergyFraction()<0.99){
    
    if(fabs(jet.eta())>=2.4)
      return true;
      
    if(jet.chargedEmEnergyFraction()<0.99
       && jet.chargedHadronEnergyFraction()>0
       && jet.chargedMultiplicity()>0)
      return true;   
  }
  else if(fabs(jet.eta())>3
	  && jet.neutralMultiplicity()>10
	  && jet.neutralEmEnergyFraction()<0.90){
    return true;
  }
  return false;
}

bool JetPFID::tightID(const Jet & jet) const{
  if(!looseID(jet)) return false;
  if(fabs(jet.eta())<=3 
     && jet.neutralEmEnergyFraction()<0.90
     && jet.neutralHadronEnergyFraction()<0.90){
    return true;
  }
  else if(fabs(jet.eta())>3){
    return true;
  }
  return false;
}

bool JetPFID::tightLepVetoID(const Jet & jet) const{
  if(!tightID(jet))return false;
  return jet.muonEnergyFraction() <0.8;
}
