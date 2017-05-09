def orangecap(d):
  total = {}
  for k in d.keys():
    for n in d[k].keys():
      if n in total.keys():
        total[n] = total[n] + d[k][n]
      else:
        total[n] = d[k][n]

  maxtotal = -1
  for n in total.keys():
    if total[n] > maxtotal:
      maxname = n
      maxtotal = total[n]

  return(maxname,maxtotal)

# Dictionary is better than list: use exponent as key so only one term per exponent

# listtodict and dicttolist convert back and forth between representations

def listtodict(poly):
  dpoly = {}
  for term in poly:
    coeff = term[0]
    exp = term[1]
    dpoly[exp] = coeff
  return(dpoly)

def dicttolist(dpoly):
  lpoly = []
  for exp in sorted(dpoly.keys()):
    lpoly.append((dpoly[exp],exp))
  lpoly.reverse()
  return(lpoly)

# dpolyadd: initialize sum to dpoly1 and either update term or add a new term from dpoly2

def dpolyadd (dpoly1,dpoly2):
  sumpoly = {}
  for exp in dpoly1.keys():
    sumpoly[exp] = dpoly1[exp]

  for exp in dpoly2.keys():
    if exp in sumpoly.keys():
      sumpoly[exp] = sumpoly[exp] + dpoly2[exp]
    else:
      sumpoly[exp] = dpoly2[exp]

  return(sumpoly)

# dpolymult: compute each cross term and update result multpoly

def dpolymult (dpoly1,dpoly2):
  multpoly = {}
  for exp1 in dpoly1.keys():
    for exp2 in dpoly2.keys():
      newexp = exp1 + exp2
      newcoeff = dpoly1[exp1] * dpoly2[exp2]
      if newexp in multpoly.keys():
        multpoly[newexp] = multpoly[newexp] + newcoeff
      else:
        multpoly[newexp] = newcoeff
  return(multpoly)

# Remove 0 coefficient terms

def cleanup(dpoly):
  dpolyclean = {}
  for exp in dpoly.keys():
    if dpoly[exp] != 0:
      dpolyclean[exp] = dpoly[exp]
  return(dpolyclean)

# Convert to dictionary, apply operations on dictionaries, convert back

def addpoly(p1,p2):
  d1 = listtodict(p1)
  d2 = listtodict(p2)
  res = dpolyadd(d1,d2)
  return(dicttolist(cleanup(res)))

def multpoly(p1,p2):
  d1 = listtodict(p1)
  d2 = listtodict(p2)
  res = dpolymult(d1,d2)
  return(dicttolist(cleanup(res)))
