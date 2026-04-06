from pydantic import BaseModel

# This defines what data the frontend sends to us
class PatientData(BaseModel):
    Age: float
    Gender: float        # 0 = Male, 1 = Female
    ESR: float
    CRP: float
    RF: float
    Anti_CCP: float
    HLA_B27: float
    ANA: float
    Anti_Ro: float
    Anti_La: float
    Anti_dsDNA: float
    Anti_Sm: float
    C3: float
    C4: float
    ASCA: float
    Anti_CBir1: float
    Anti_OmpC: float
    pANCA: float
    EMA: float
    DGP: float
    Anti_tTG: float
    Anti_TPO: float
    Anti_SMA: float