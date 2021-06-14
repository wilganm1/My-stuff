https://peterroelants.github.io/posts/neural-network-implementation-part02/

"""Make a classification neural network. Use cross entropy for loss function"""
a = read("my_voice_data.wav")
inputs = np.array(a[1], dtype = float)
weights = np.array(np.random.uniform(np.random.randn(), np.random.randn(), len(inputs)))
bias = 1

t = target
y = predicted output
x = input
i = which input currently on

def logistic(z): 
    return 1. / (1 + np.exp(-z))

# Define the neural network function y = 1 / (1 + numpy.exp(-x*w))
def nn(x, w): 
    return logistic(x.dot(w.T))

# Define the neural network prediction function that only returns
#  1 or 0 depending on the predicted class
def nn_predict(x,w): 
    return np.around(nn(x,w))
    
# Define the loss function
def loss(y, t):
    return - np.mean(
        np.multiply(t, np.log(y)) + np.multiply((1-t), np.log(1-y)))

 def gradient(w, x, t):
    """Gradient function."""
    return (nn(x, w) - t).T * x

 
def delta_w(w_k, x, t, learning_rate):
    """Update function which returns the update for each 
    weight {w_a, w_b} in a vector."""
    return learning_rate * gradient(w_k, x, t)

def CEloss(prediction):
    for i in range(len(inputs)):
        sumCE += 1*np.log(prediction) + (1-1)*np.log(1-prediction)    
        sumCE *= -1

Change in weight:
    alpha * inputs[i] * (predicted - target)

    
    
    
