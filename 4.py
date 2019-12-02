import numpy as np
x = np.array(([2,9],[1,5],[3,6]),dtype=float)
y = np.array(([92],[86],[89]),dtype=float)
x = x/np.amax(x,axis=0)
y = y/100

in_layer=2
h_layer = 3
out_layer=1
epoch = 6500
lr = 0.1

wh = np.random.uniform(size =(in_layer,h_layer))
bh = np.random.uniform(size =(1,h_layer))
wout = np.random.uniform(size=(h_layer,out_layer))
bout = np.random.uniform(size=(1,out_layer))

def sigmoid(x):
 return(1/(1+np.exp(-x)))

def deriative_sigmoid(x):
 return(x*(1-x))

for i in range(epoch):
	hp = np.dot(x,wh)
	hp1 = hp + bh
	hidden = sigmoid(hp1)
	out = np.dot(hidden,wout)
	out1 = out + bout
	output = sigmoid(out1)

	Eo = y - output
	out_grad = deriative_sigmoid(output)
	d_out = Eo * out_grad

	Eh = d_out.dot(wout.T)
	out_hidden = deriative_sigmoid(hidden)
	d_hidden = Eh*out_hidden

	wout+= hidden.T.dot(d_out)*lr
	wh+= x.T.dot(d_hidden)*lr
print("expected",str(y))
print("generated",str(output))