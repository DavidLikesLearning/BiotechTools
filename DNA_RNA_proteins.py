#David J Florez Rodriguez for EE225 Jan 18 2023. I wrote some code to help with the transcription and translation.


def pair(strn, table):
  out = ''
  for i in strn.upper():
    out+=table[i]
  return out

def DNApair(strn):
  #just matching bases in DNA
  table = {'A':'T','T':'A','C':'G','G':'C'}
  return pair(strn,table)

def RNApair(strn):
  #just matching bases, returning RNA from DNA input
  table = {'A':'U','T':'A','C':'G','G':'C'}
  return pair(strn,table)

AA2RNAs = {'Phe':'UUU UUC','Leu':'UUA UUG CUU CUC CUA CUG', 'Ile': 'AUU AUC AUA', 
           'Met':'AUG', 'Val':'GUU GUC GUA GUG', 'Ser' : 'UCU UCC UCA UCG AGU AGC', 
           'Pro':'CCU CCC CCA CCG','Thr':'ACU ACC ACG ACA', 'Ala' : 'GCU GCC GCA GCG', 
           'Tyr':'UAU UAC', 'Stop': 'UAA UAG UGA', 'His' : 'CAU CAC', 'Gln':'CAA CAG',
           'Asn':'AAU AAC', 'Lys':'AAA AAG', 'Asp':'GAU GAC', 'Glu':'GAA GAG',
           'Cys':'UGU UGC', 'Trp': 'UGG', 'Arg':'CGU CGC CGA CGG AGA AGG',
           'Gly':'GGU GGC GGA GGG'}
           # I just copied this table from the book

# this code turns the table above into a map of every three base codon to its
# base pair or start/stop instruction