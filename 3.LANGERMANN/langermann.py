##########################################################################
  #
  # LANGERMANN FUNCTION
  #
  # Authors: Sonja Surjanovic, Simon Fraser University
  #          Derek Bingham, Simon Fraser University
  # Questions/Comments: Please email Derek Bingham at dbingham@stat.sfu.ca.
  #
  # Copyright 2013. Derek Bingham, Simon Fraser University.
  #
  # THERE IS NO WARRANTY, EXPRESS OR IMPLIED. WE DO NOT ASSUME ANY LIABILITY
  # FOR THE USE OF THIS SOFTWARE.  If software is modified to produce
  # derivative works, such modified software should be clearly marked.
  # Additionally, this program is free software; you can redistribute it 
  # and/or modify it under the terms of the GNU General Public License as 
  # published by the Free Software Foundation; version 2.0 of the License. 
  # Accordingly, this program is distributed in the hope that it will be 
  # useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
  # of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
  # General Public License for more details.
  #
  # For function details and reference information, see:
  # http://www.sfu.ca/~ssurjano/
  #
  ##########################################################################
  #
  # INPUTS:
  #
  # xx   = c(x1, x2, ..., xd)
  # m    = constant (optional), with default value 5
  # cvec = m-dimensional vector (optional), with default value c(1, 2, 5, 2, 3)
  #        (when m=5)
  # A    = (mxd)-dimensional matrix (optional), with default value:
  #        [3  5]
  #        [5  2]
  #        [2  1]
  #        [1  4]
  #        [7  9]
  #        (when m=5 and d=2)
  #
  ##########################################################################

import numpy as np

    
def f(x):
    
    a = [3,5,2,1,7]
    b = [5,2,1,4,9]
    c = [1,2,5,2,3]
    
    y = 0.0
    for i in range(5):
        y += -(c[i]*np.exp(-(1/np.pi)*((x[0]-a[i])**2 + (x[1]-b[i])**2))*np.cos(np.pi*((x[0]-a[i])**2 + (x[1]-b[i])**2)))
    #end
    
    return y
      
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  