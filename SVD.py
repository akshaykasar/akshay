# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:12:21 2020

@author: Akshay
"""

import numpy as np


A=np.array([[1,0,1,0],[0,1,0,1]])

C=(A.T).dot(A)

e,eig=np.linalg.eig(C)

u1=A.dot(eig[:,0])/1.41

u2=A.dot(eig[:,2])/1.41


U=np.hstack((u1.reshape(2,1),u2.reshape(2,1)))


Sig= np.array([[1.41,0,0,0],[0,1.41,0,0]])


p=eig[:,1]
eig[:,1]=eig[:,2]
eig[:,2]=p

X=(U.dot(Sig)).dot(eig.T)

