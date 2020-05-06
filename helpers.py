# functions.py
# BST 263, Spring 2020
# HW 3

import numpy as np
import matplotlib.pyplot as plt


def rgb2gray(X):
	return 0.2989*X[:,:,0] + 0.587*X[:,:,1] + 0.114*X[:,:,2]


def cropR(X,h,w):
	(h1,w1) = np.shape(X)
	x1 = int(np.random.choice(w1-w+1,1))
	y1 = int(np.random.choice(h1-h+1,1))
	return X[y1:(y1+h), x1:(x1+w)]


def cropC(X,h,w):
	(h1,w1) = np.shape(X)
	h_margin = np.floor((h1-h)/2)
	w_margin = np.floor((w1-w)/2)
	x1 = int(w_margin)
	y1 = int(h_margin)
	return X[y1:(y1+h), x1:(x1+w)]


def hog(xgrad,ygrad,hn,wn,an):
	(h,w) = np.shape(xgrad)
	h1 = h/hn
	w1 = w/wn
	xr = w1*np.arange(1,wn+1)
	xl = xr-w1
	yd = h1*np.arange(1,hn+1)
	yu = yd-h1
	theta = np.zeros((h,w))

	for i in range(h):
		for j in range(w):
			if (ygrad[i,j] > 0):
				theta[i,j] = np.arccos(xgrad[i,j]/np.sqrt(xgrad[i,j]**2 + ygrad[i,j]**2 + 1e-10))
			else:
				theta[i,j] = -np.arccos(xgrad[i,j]/np.sqrt(xgrad[i,j]**2 + ygrad[i,j]**2 + 1e-10))

	angle = []
	for i in range(hn):
		for j in range(wn):
			angle = angle + list(np.histogram(theta[int(yu[i]):int(yd[i]), int(xl[j]):int(xr[j])]+np.pi,
				bins=np.arange(0,2*np.pi*(1+1e-10),2*np.pi/an))[0]/(h1*w1))

	return angle


def grad(X,h,w,pic):
	X1 = cropC(X,h+2,w+2)
	xgrad = (X1[1:(h+1), 2:] - X1[1:(h+1), :w])/2
	ygrad = (X1[:h, 1:(w+1)] - X1[2:, 1:(w+1)])/2

	if (pic):
		for i in range(h):
			for j in range(w):
				plt.arrow(j,h+1-i,xgrad[i,j]*5,ygrad[i,j]*5, head_width=0.25)
		plt.axis([0,70,0,130])
		plt.xlabel('X')
		plt.ylabel('Y')
		plt.show()

	return (xgrad,ygrad)


def readPNG(filename):
	return plt.imread(filename)


def writePNG(X,filename):
	plt.imsave(filename,X,cmap='gray')

