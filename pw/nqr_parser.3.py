#!/usr/bin/env python3

import numpy as np
import sys

#################################
#################################
##                           ####
## working version!  tested! ####
## NEW NEW NEW NEW NEW NEW   ####
## AS OF SEPTEMBER 6, 2016   ####
##                           ####		
#################################
#################################

def f52(cq, eta=0, verbose=False):
    x2 = 1 - 11/54*eta**2
    x1 = 1 + 5/54*eta**2
    return 3 / 10 * cq * np.array( [1/2*x1, x2 ] )

def f32(cq, eta=0):
  return np.sqrt( 1 + (eta**2)/3 ) * cq/2

def f1(cq, eta=0):
  x0 = 2/3 * eta
  x1 = 1 - eta/3
  x2 = 1 + eta/3
  return (3/4) * cq * np.array( [x0, x1, x2] )

def cq32(f, eta=0):
  return np.sqrt( 4 * f**2 / (1 + eta**2 / 3) )

def cq1(freq_arr, eta=0):
  f_0, fmin, fmax = np.sort(np.array([x for x in freq_arr]))
  cq_0    = 2 * f_0/(eta )
  cq_min  = 4 * fmin/( 3 - eta )
  cq_plus = 4 * fmax/( 3 + eta )
  print( """
		
		"cq_0": {},
		"cq_minus": {},
		"cq_plus": {}
		
         """.format(cq_0, cq_min, cq_plus)) 
  return np.array([cq_0, cq_min, cq_plus])




def main(): 
  if len(sys.argv) < 2:
    infile = sys.stdin.read().split('\n') 
  elif len(sys.argv) == 2:
    infile = open(sys.argv[1],'r').readlines()
  else:
    infile = []
    for fil in sys.argv[1:]:
      infile = infile + open(fil,'r').readlines()

  relevant_lines = []  
  for line in infile:
    if "Cq=" in line:
      relevant_lines.append(line)

  sys.stdout.write('nucleus\t\tsite\t\tCq(mhz)\t\teta\t\tv0\t\tv-\t\tv+\n')
  
  for line in relevant_lines:
    line.replace("eta=-", "eta= ")
    x = line.split()
    cq = float(x[7])
    eta = float(x[10])
    v0, vminus, vplus = ' - ',' - ',' - '

    if x[0] == 'Cl':
      v0 = str(f32(cq, eta))[:7]

    elif x[0] == 'N':
      v0     = str(f1(cq, eta)[0])[:7]
      vminus = str(f1(cq, eta)[1])[:7]
      vplus  = str(f1(cq, eta)[2])[:7]

    space_size = 15
    space1 = (space_size - len(x[0 ] ))*" "
    space2 = (space_size - len(x[1 ] ))*" "
    space3 = (space_size - len(x[7 ] ))*" "
    space4 = (space_size - len(x[10] ))*" "
    space5 = (space_size - len(v0    ))*" "
    space6 = (space_size - len(vminus))*" "

    sys.stdout.write('{}{}{}{}{}{}{}{}{}{}{}{}{}\n'.format(x[0], space1, x[1], space2, x[7], space3, x[10], space4,  v0,space5,  vminus,space6 , vplus))

  sys.stdout.write("\n\n... bye\n\n")


if __name__ == '__main__':
  main()

