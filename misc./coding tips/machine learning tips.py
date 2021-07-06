:::::::::::::::::::MACHINE LEARNING:::::::::::::::::::::::::::::::::
Machine learning is the field of study that gives computers the ability to learn withθut being explicitly programmed. It can be used to make prediction models, recognize phθtos, make self-driving cars, and create AIs.

Three things are needed for machine learning
 A task that needs to be done T
 The experience of doing that task, E
 hθw well you performed doing that task, P


    ************ MAKE THE BEST PREDICTION POSSIBLE  *************
-Supervised Learning
We are given a data set and know what the correct output ShθULD look
like. There are two types of problems in learning:

 -Regression
  Trying to preduct results within a continuous output, which means it
  could be anything wihtin a certain range.
    Example: What stock price will a stock be tomorrow? It could
    literally be anything above 0
 -Classification:
  Trying to predict results in a discrete output, meaning it has to act
  like a definitive answer, like yes or no.
    Example: Will a woke compnay go broke in a year? It either does or
    does not.

-Unserpervised Learning
Allows us to approach problems with little or no idea what our results
shθuld look like. We can derive this structure by clustering the data
based on relationships among the variables in the data. With
unsupervised learning there is no feedback based on the prediction
results.

:::::::::::::::::::::::MODEL REPRESENTATION:::::::::::::::::::::::::
    
If we want to creae a model of linear regression, with a regression line, 
we must differentiate values into different categories.
   Example: hθuse size vs cost

 -Notation
    xi = one category-variable being used (hθuse size) input 
    yi = the other category-variable being used (hθuse cost) output
    m = the number of variables in a category
    (xi, yi) = a training example
    i = 1,...,m = training set
   The i represents which number variables it is, like 9th or 3rd.

 -Process for estimating values
   Make a training set, feed it to a learning algorithm which outputs
   a function, h (hypothesis). The hypothesis takes in x and outputs y.
                      Trainging Set
                           |
                           V
                    Learning Alogrithm
                           |
                           V
           x variable -->  h  --> y variable

  -hθw do we represent h? 
   Use θ (theta) to represent any h value. hθ
    They are parameters of the model
     θ0  = y intercept
     θ1  = slope of a line
          -------------Single variate------------
Say we have data of hθuse sizes vs price. We plot thθse.
   x_vars = Size (ft^2)|y_vars = Price ($1000s)
              2104     |       460      i = 1
              1416     |       232      i = 2
              1534     |       315      i = 3
         
     x_vars = [2104,1416,1534]
     y_vars = [460,232,315]      
         
    y
    |       /            θ0 = y-intercept
 P  |      / θ1          θ1 = slope
 R  |     /         
 I  |    /
 C  |   /               θ determines slope
 E  |  /               bias dtermines y-intercept
    --/---------------x
   θ0  Size 

     hθ(x) = θ0 + θ1*x    -multiply θ1 by x
     h(x) = θ0 + θ1*x
      ALL h VALUES ARE PREDICTIVE VALUES
      
      
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    The θs are the weights that determine the
    slope, and biases determine the y-intercept
    
    All θs are randomly initialized then 
    changed as your go on. 
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      
    def hypothesis(θ0, θ1, x):
        hyp = θ0 + θ1 * x
        return hyp
        
 -Cost Function, J
  Measures the accuracy of a hypothesis. Takes an average difference of all results of
  the hypothesis with inputs from x's and the actual output y's. 
  WHAT IS THE BEST POSSIBLE LINE?????????
   
   You want to minimize θ0 and θ1 to get best prediction 
   J(θ0,θ1) is the function of the parameters
************************************************************************
  ******  J(θ0, θ1) = 1/2m * sum(hθ(xi)-yi)^2   *********
             = 1/2m * sum(θ0 + θ1x(xi) - yi)^2
  As you go along, you increase xi by i * x
  hθ(xi) = θ0 + θ1*xi
   Example:
       θ0 = 0.0
       θ1 = .05
        J(0.5) = 1/2m[((0 + 0.5)-1)^2 + ((0 + 1)-2)^2 + 
                      ((0 + 1.5)-3)^2]
            
************************************************************************
   Changing the θ1 value for J yields a different y output. Do
   this enough times you can get a parabola shape.

    You want to find the lowest point on the parabola, because 
    that is the one that minimizes 01, giving most precise prediciton

       ----------------"GRADIENT DESCENT"------------------
 -Gradient Descent
 START OFF WITH ARBITRARY VLAUES FOR θ0 AND θ1. Keep changing θ0
 and θ1 to minimize J(θ0, θ1) until you get the minimum. Think of it as 
 standing on a hill, then taking steps downward.
 
        d = derivative
  Algorithm. Repeat until convergence on minimum
         θj=θj - α*(d/d*θj)*J(θ0, θ1)

   α, alpha -a learning rate. Controls size of step downhill.
        if alpha is too large, you can overtake the minimum
   d is a derivative variable
 To repeat it, you need to update the values of θ0 and θ1 simultaneously to get accurate results.
   The temporary θ is called θj
   
   
   θj = θj - α*(d/d*θj)*J(θ0, θ1)    
               Need to update all θ simultaneously
      for every j = 0,..,n:
          
     temp0 = θ0 - α*(d/d*θj)*J(θ0, θ1) 
     temp1 = θ1 - α*(d/d*θj)*J(θ0, θ1) 
     θ0 = θ0
     θ1 = θ1

     You get a J for the training set too:
     
     Jtrain(θ0,θ1) = 1/2m * sum(hθ(xi)-y(i))^2
   
   Gradient descent will automatically take smaller steps,
   so we'll always get to the correct minimum.        
***************************************************************
       J(θ0, θ1)
     θ0 = θ0 - α*(1/m)*sum(hθ(x(i))-y(i)
     θ1 = θ1 - α*(1/m)*sum(hθ(x(i))-y(i)*xj(i))
***************************************************************    
   
     --------------LINEAR ALGEBRA REVIEW------------------
-Matrix
A matrix is a 2D array with rows and columns. Capital letters refer to
 matrices number of rows comes first, then number of columns

 Matrix elements: entries of a matrix
         Aij    - coordinates of matrix
           i = which row
           j = which columns

     A =[1 3]     A12 = First row second column = 3
 	    [4 7]     A21 = Second row first column = 4 
-Vector: A matrix with only one column. nx1
    This mean that there is only one coordinate, i.
      the i refers to the index, and can either be 1-index or 0-index. 

 -Adding/Subracting Matrices
  You can only add/subract matrices if they have the same dimensions. And you just simply add/subtract the values that are in the same coordinates
 -Mulitplying Matrices
   When you multiply a matrix by a number, called a scalar, you just multiply every value in the matrix by the scalar.

      ***** Matrices follow PEMDAS *****
 
 -Matrix-Vector Multiplication
  If you have matrix A and vector X, you get new vector Y by 
  multiplying A's ith row with with elements of vector X, then add them up.
         A      X     Y
       [1 3]   [1]   [16]
       [4 0] * [5]  =[4]
       [2 1]         [7] 
     1*1 + 3*5 = 16
     4*1 + 0*5 = 4
     2*1 + 1*5 = 7

    A11*X1 + A12*X2
    A21*X1 + A22*X2
    A31*X1 + A32*X2


   The number of columns of the matrix must = number of rows of vector

 -Matrix-Matrix Multiplication
  Pull out first column of right matrix and treat it as a vector then combine the results together
         A    *   B
       [1 3 2]  [1 3]   [11 10]    -combined results 
       [4 0 1]  [0 1] = [9  14]
                [5 2]

       [1 3 2]  [1]   [11]         -results of first vector
       [4 0 1]  [0] = [9]
                [5]

       [1 3 2]  [3]   [10]         -results of second vector
       [4 0 1]  [1] = [14]
                [2]        
 
 You have to multiply matrices this way or else it doesn't work.
  Except for identity matrices
-Identity Matrix I
 A matrix with 1s and 0s with 1s being in diagonals.
   [1 0]   [1 0 0]  [1 0 0 0]   A*I = I*A = A
   [0 1]   [0 1 0]  [0 1 0 0]
           [0 0 1]  [0 0 1 0]   A*I = I*A = A
                    [0 0 0 1]

-Transposing Matrices
 Transposing means to turn rows into columns into rows. You 
 turn the first row into the first column, the second row into the second column.... *******Only works with square matrices********
          A        A_trans
       [1 2 0]     [1 0 7]
       [0 5 6] --> [2 5 0]
       [7 0 9]     [0 6 9]

-Inversing Matrices
 An inverse is a number under 1. 1/n. An inverse matrix is 
 caclulated to end up being an identity matrix
    A(A^-1) = A^-1*A = I

---------------MULTIVARIATE LINEAR REGRESSION---------------
Fitting a best fit line with multiple variables to consider. These 
involve different variables, called features to consider

 -Notation
   n = number of features
   x(i) = inputh(features) of ith training example. Row
   xj(i) = value of feature j in ith training example.
    think of j as column and i as a row
    
Going back to hθuses
   Size (feet^2) | Bedrooms | Floors | Age | Price ($1000)  
_______x1________|____x2____|____x3__|__x4_|____y_________
      2104       |    5     |    1   |  45 |   460
      1416       |    3     |    2   |  40 |   232
      ....           ...        ...    ....   .....
      
      n = 4                        [1416]
      x3 = Age                     [  3 ]
      x(1) = first row       x(2)= [  2 ]
      x3(2) = 2                    [ 40 ]
*************************************************************
 -Form of hypothesis 
    h0(x) = θ0 + θ1*x1 + θ2*x2 + θ3*x3 + θ4*x4 + ... + θn*xn
               =θ^T * x
**************************************************************               
  Define x0(i) = 1
   Now the feature vector becomes
          [x0]  transposed -> [x0, x1, x2, x3, x4]
          [x1]                  [θ0]
      x=  [x2]               θ= [θ1]
          [..]                  [θ2]
          [xn]                  [θ3]
            
  Gradient descent forumlua with multiple variables
****************************************************************  
  def gradDescent(α,m,):
      θj = θj - α * (1/m) * (sum(hθ(xi) - yi)) *xj(i)
       for j = 0..n
      θ0 = θ0 - α * (1/m) * (sum(hθ(xi) - yi)) *1 
      θ1 = θ1 - α * (1/m) * (sum(hθ(xi) - yi)) *x1(i)
      θ2 = θ2 - α * (1/m) * (sum(hθ(xi) - yi)) *x2(i)
 
***************************************************************

-Feature Scaling & Mean Normalization
 To speed up the process of gradient descent, we implore two techinques. 
  Feature scaling divides the input values by the range (max - min). 
  Mean normalization involves subtracting the mean for an
  input variable from the values for that variable .

  -Feature Scaling
  Divide current feature by max of that feature
    x1 = size (0-2000 feet^2)   --> x1 = size(ft^2)/2000
    x2 = no. of bedrooms (1-5)  --> x2 = no. bedrooms/5

        -1 <= x1 <=1      -1 <= x2 <= 1

  -Mean Normalization
  Replace xi with xi - μi divided by standard deviation
     x1 = (x1 - μi)/si
        -μi = average of values for feature i.
        -si = range of values or standard deviation

 -Debugging 
  Debugging is making sure gradient descent is working correctly. It involves chθosing the correct α value.
            θj = θj - (α* d/d*θj) * J(θ)
            
    What α shθuld we chθose?
  J(θ) shθuld decrease every iteration of cost gradient descent.
     10^-3 is a sign of convergence
  If gradient descent is not working, use a smaller α
     try, 0.001, 0.01, 0.1, 1

-Polynomial Regression
Changing the behavior or curve of our hypothetical best 
fit line, like making it a quadratic or cubic forumula.
 
Example: hOuse price based on area 
  hθ(x) = θ0 + θ1*frontage+ θ2*depth
    Area x = frontage * depth
    
    hθ(x) = θ0 + θ1*x

   -Choice of Features
   1. cubic function
        hθ(x) = θ0 + θ1*x1 + θ2*x2^2 + θ3*x3^3
   Example: x = size of a hθuse

    x1 = size
    x2 = size^2   if x is a range, each side of the range is raised
    x3 = size^3
   
   2. Square root function   
        hθ(x) = θ0 + θ1x1 + sqrt(θ2x2^2)

:::::::::::::::::::::COMPUTING EQUATION::::::::::::::
 -Normal Equations
  The normal equation is a way of minimizing J by taking its 
  derivatives with respect to θjs.
   Size (feet^2) | Bedrooms | Floors | Age | Price ($1000)  
___x0__|____x1____|___x2___|____x3__|__x4_|____y______
    1  |   2104   |    5   |    1   |  45 |   460
    1  |   1416   |    3   |    2   |  40 |   232
    1  |   1534   |    3   |    2   |  30 |   315
    1  |    852   |    2   |    1   |  36 |   178
      Make a matrix of all x features called X
         [1  2104 5 1 45  460]      [460]
     X = [1  1416 3 2 40  232]  y = [232]
         [1  1534 3 2 30  315]      [315]
         [1   852 2 1 36  178]      [178]
                m * (n+1) dim        m dim vector
    Formula for theta.
           θ = (X^T *X)^-1 * X^T * y
        [x0(i)]          [x(i)^T]
        [x1(i)]          [x(2)^T]
 x(i) = [x2(i)]    X =   [x(3)^T]
        [  :  ]          [   :  ]
        [xn(i)]          [x(m)^T]
        
    Example:
        if x(i) = [1    ]   X = [1 x1(i)]
                  [x1(i)]       [1 x2(i)]
        
        
      ----------------COST FUNCTION-------------------
function J = costFunctionJ(X,y,θ)
  m=size(X,l);
  predictions = X * θ
  sqrErrors = (predictions-y).^2;
  
  J = 1/(2*m) * sum(sprErrors); 
 
-----------------------------VECTORIZATION--------------------------------
Vectorization allows adding multiple vectors an allow 
multiple and bulk calculations simultaneously

  u(j) = 2*v(j) + 5*w(j)  (all j);
  Say you have j =2,7;
  u(2) = 2*v(2) + 5*w(2)
  u(7) = 2*v(7) + 5*w(7)
    u, v, w   =  vectors;
    
 ----------------------------CLASSIFICATION-------------------------------
 Classification is about a feature being a dichotomy.
 It's a binary that is either a yes or a no. You will typically say its a yes
 when it's probability is > 0.5, and a no when its probability is < 0.5. Uses
 DISCRETE OUTCOMES
  
  S0:   0 <= hθ(x) <= 1
 
   Example: Is this email spam?
     No =  0  Negative class
     Yes = 1  Postivie class
  On a graph, you want to find the xvalue that separates the negative values
  from the positive calues. 

               -------------LOGISTIC REGRESSION---------------
 In classification ,we want 0 <= h0(x) <= 1, so we write a new formula
   Use the Sigmoid function / Logistic Function
  hθ(x) = g((θ^T)*x)      [x0]       [θ0]
    Formula           x = [x1]   θ = [θ1]
    g(z) = 1/(1+e^-z)     [: ]       [: ]
     z = (θ^T)*x          [xn]       [θn]
 So 
 ***********************************************************************
 Remember:
    h0(x) = θ0 + θ1*x1 + θ2*x2 + θ3*x3 + θ4*x4 + ... + θn*xn
             =θ^T * x
 
   hθ(x) = 1/(1+e^(-(θ^T)*x)) 
   
   def sigmoid(x):
       hθ(x) = 1 / (1 + np.exp(-x))   
       
 And here's the derivative:
     sigmoid(x) * (1- sigmoid(x))
       
 ***********************************************************************
 hθ(x) will give us a PROBABILITY between 0 & 1 
 When plotted, the sigmod %function has a an asymptote at 1 & also at 0.
 
-Interpreting hypothesis output
 h0(x) = estimated probability that y = on input x
 
     hθ(x) >= 0.5 -> y=1
     hθ(x) >  0.5 -> y=0
     
     g(z) >= 0.5
    when z >= 0
  
   Example: Malignant or benign tumor
              [x0]   [    1    ]
         x=   [x1] = [tumorSize]
            h0(x) = 0.7
         tumor has 70% chance of being malignant
   hθ(x) = P(y=1|x;θ)  -probability y=1 given x, 
                        parameteriezed by θ, o
-Decision Boundary
The decision boundary is the line that separates where y=0 and y=1.

-Logistic regression model
We need to use a different cost %function with logistic function

 J(θ) = 1/2m = sum of i's(Cost(hθ(xi),y))    
   Cost(hθ(x),y) = {-log(hθ*x)) if y=1} 
                   {-log(1-hθ(x)) if y=0} 
     Note: y = 0 or 1 always
   --> Cost(hθ(x),y) = -log(1-hθ(x))  
 ******************************************************************
 Now you can write an even more simplified version for J(o)
   J(θ)= -1/m*[sigma(yi*log(hθ(xi)))+(1-yi)*log(1-hθ(xi))]
 
 To minimize J(θ) you need to get θ
     θj = θj - a*sigma(hθ(xi) - yi)*xij
       -->     hθ(x) = 1/(1+e^((θ^T)*x))
 ******************************************************************     
 
-Optimization
function [jVal, gradient] = costFunction(θ)
  jVal = [...code to compute J(θ)...];
  gradient = [...code to compute derivative of J(θ)...];
end;

options = optimset('GradObj', 'on', 'MaxIter', 100);
initialθ = zeros(2,1);
   [optθ, functionVal, exitFlag] = fminunc(@costFunction, initialθ, options);
end;

----------------------MULTICLASS CLASSIFICATION-------------------------
Making learning algorithm with multiple different variables to
consdider. It's non-binary decision
 Exmaple: Weather
    Sunny, Cloudy, Rainy, Snowing
You plot this by using the One-vs-all classification
 Say you have 3 classes plotted out, what you do is you set up a binary by
 making one class a positive, while all the other classes a negative. You draw a
 line between the positives and negatives, and you repeat this process for each
 individual class.
 
-Overfitting
Overfitting is a problem where your prediction algorithm accuratley matches all
known training examples but does not predict new examples very well.
   Get rid of some parameters, or reduce their magnitude
   Let's say we have o3x^3 and o4x^4
  Modify the cost %function to minimize θ
 min(o) = 1/2m*sigma(hθ=o(xi)-yi)^2 + 1000*o3^2 + 1000*o4^2
o3 and o4 then become very close to zero.

-Regularization
If we have small values for parameters, we'll have a simpler
hypothesis. But what if we don't know with what value to shrink?
   add a new part to the cost function
J(θ) = 1/2m*sigma(hθ(xi)-yi)^2 + lambda*sum(θj)^2
      lambda = regularizaiton parameter
          lambda can be any number, large or small
        Example:
            lambda = 0
            lambda = 0.5
            lambda = 1
            lambda = 4
  What you do is plug in every lambda to see which one gets the smallest
    value.
'--------------------NEURAL NETWORKS------------------------'
These representations are to mimic neural netwoks in the brain
    think of x1, x2, x3, ... xn being nodes that all converge 
    to create hθ(x). Each node is an input that comes
    with a certain "weights", which are the thetas.

Neural networds take in inputs, x values, add in a bias unit
and make a prediction.
        
        x0-----O  hΘ(x)         [x0]        [θ0]
   bias       /|\           x = [x1]    θ = [θ1]  "weights"                     
   units     / | \              [x2]        [θ2]               
     a0(2)--O  O  O  a nodes Layer 2 'hidden layer'
            |/\|/\|
            O  O  O  x nodes. Layer 1
            x1 x2 x3 
    If there are no hidden layers, use this formla
     hθ(x) = 1/(1+e^((-θ^T)*x))
 
 "Bias unit" x0 = 1
  Layer 1 is the 'input layer' and has the xn... values
  Layer 2 is called the 'hidden layer' between the input layer and the output
  layer 
  the final Layer is the output layer that takes all the information and creates
  h(x).
 Layer notation is this: ai(j). 
                         ith node in layer j
                    a1(2) = first node in layer 2
 
     ai(j) is an activation of the unit
     Θ(j) = matrix of weights controlling function mapping 
     from layer j to layer j + 1     
   
 *If you see x^(2) or a^(2) it means it's in layer 2
 Formula for the layers. Uses sigmoid function
 
 a1^(2)= g(Θ10^(1)*x0 + Θ11^(1)*x1  + Θ12^(1)*x2 ...)
 a2^(2)= g(Θ20^(1)*x0 + Θ21^(1)*x1  + Θ22^(1)*x2 ...)
 a3^(2)= g(Θ30^(1)*x0 + Θ31^(1)*x1  + Θ32^(1)*x2 ...)
       a1,a2,a3, are the nodes in layer 2
     
 ***Now to find the hypothesis output hθ(x)***

 hθ(x)=a1^(3)=g(o10^(2)*a0^(2) o11^(2)*a1 
     
 If network has Sj units in layer j, Sj + 1 units in layer j + 1, then oj will have dimensions S(j+1)*S(j)+1

 Now we are going to simplify the formulas
 g(θ10^(1)*x0 + θ11^(1)*x1  + θ12^(1)*x2 ...) = z1^(2)
 g(θ20^(1)*x0 + θ21^(1)*x1  + θ22^(1)*x2 ...) = z2^(2)
 g(θ30^(1)*x0 + θ31^(1)*x1  + θ32^(1)*x2 ...) = z3^(2)
 So
  a1^(2) = g(z1^(2))
  a2^(2) = g(z2^(2))
  a3^(2) = g(z3^(2))
-Vectorization
Now lets use vectors to shθw hθw this all works
      [x0]          [z1^(2)]
  x = [x1]  z^(2) = [z2^(2)] 
      [x2]          [z3^(2)]
      [x3]
    z^(2) = o^(1)*x
    a^(2) = g(z^(2))    a^(2) is a 3D vector
    
  You can change the value of x to equal a^(1) nodes
  
 Now account for the bias layer by adding an extra a0
   aθ^(2) = 1
   z^(3) = o^(2)*a^(2)
   hθ(x) = a^(3) = g(z^(3))
-Non-linear hypotheses, binary.
And functions
 if you have two variables on a binary, both values must be positive for h0(x)  
   to be positive 
h?(x)=g(?30+20x1+20x2)
x1=0  and  x2=0  then  g(?30)?0
x1=0  and  x2=1  then  g(?10)?0
x1=1  and  x2=0  then  g(?10)?0
x1=1  and  x2=1  then  g(10)?1
   
Or functions
If you have two different x nodes, if either one is a positive binary, the
hθ(x) will also be a positive

-Multi-class classification
Let's say you want a network to recognize 4 images
              [1]              [0]
   hθ(x) =[0]   hθ(x) =[1] , etc.
              [0]              [0]
              [0]              [0]
             Image 1          Image 2
So you have an image = x^(i), and you want your outcome  y^(i) to be equal to one
of the vectors above.  (x^(i), y^(i))
   hθ(x^(i)) = x^(i)
-Cost function;
{(x^(1),y^(1)),(x^(2),y^(2)),.....,(x^(m),y^(m))}
L = total number of layers in network 
Sl = number of units (not counting bias unit) in layer l
-Forward propagation
Whether a hypothesis actually ouputs given an input (x,y)
forward propagation allows to compute activation in network
 a^(1) = x
 z^(2) = o^(1)*a^(1)
 a^(2) = g(z^(2))   (add ao^(2))
 z^(3) = o^(2)*a^(2)
 a^(3) = g(z^(3))  (add ao^(3))
 z^(4) = o^(3)*a^(3)
 a^(4) = hθ(x) = g(z^(4))
 
-Backpropagation
Backpropagation is hθw you minimize your cost %function in a neural network.
## min(j(o))

Find dj^(l), which is the "error" of node j in layer l
     d = delta
For each output unit (layer L = 4)
   dj^(4) = aj^(4) - yj
            aj^(4) = hθ(x)j  
If you think of d, a, and y as vectors, you can crete a new forumula
             d^(4) = a^(4) - y
Now find d3 and d2
d^(3) = (o^(3))^T *d^(4) .*a^(3).*(1-a^(3))
d^(3) = (o^(2))^T *d^(3) .*a^(2).*(1-a^(2))
  
To get a derivative that will minimize J(θ)
Dij^(l) = 1/m *(dij^(l) + lambda*θij^(l)), if j=/= 0
Dij^(l) = 1/m * dij^(l) if j=0
   l = which layer the node is one, 
   j = the unit at hand.
In neural networks, we use matrices, so to optimize functions, we use vectors.
unroll them by writing them normally
θVector = [θ1(:); θ2(:); θ3(:);]
deltaVector = [ D1(:); D2(:); D3(:)]  %DVec
  
 If the matrices have different dimensions, use reshape
 θ1 = reshape(θVector(1:110),10,11)
 θ2 = reshape(θVector(111:220),10,11)
 θ3 = reshape(θVector(221:231),1,11)
   var = reshape(var(vn:vm), dim1, dim2) 
   
-Gradient checking   
Graident checking is about checking if gradient descent is working
properly with no bugs in the system.
 
Take the derivatives to find slope
 The derivative of θ is the tangent of j(θ) at point θ
 Compute θ + epsilon, e. It acts like a standard deviation on a
 normal distribution. You then connect connect dots at 
 θ+e & θ-e.
 
 This forms a right triangle  with the height being 
     = J(θ+e)- J(θ-e)
  while the width of the traingle being = 2*e
************************************************************
 So to find the slope derivative
     = (J(θ+e)-J(θ-e))/2*e
************************************************************
  start off with epsilon being a small value, like 10^-4
 To find in Ocatve, use following command
    gradApprox = (J(θ+EPSILON)-J(θ-EPSILON))/(2*EPSILON
 Parameter vector θ
  d/d(θn)*J(θ) = J(θ1,..,θn+e)-J(θ1,,..,θn-e)
 the number that n equals is when you add/subract e.
  if n=n, then θ2+e,.., θ2-e
This is what you implement in Octave
  for i = in:n,     %n is the dimension of θ
    θPlus = θ;
    θPlus(i) = θPlus(i) + EPSILON;
    θMinus = θ;
    θMinus(i) = θMinus(i) - EPSILON;
    gradApprox(i) =(J(θPlus)-J(θMinus))/(2*EPSILON)
 check that gradApprox = DVec from backpropagation
 The closer gradApporx and DVec are, the better backprop is working
 
For gradient descent and advanced optimization methθd, need initial value for
θ
   optθ = fminunc(@costFunction, initialθ, options)
  set initialθ = zeros(n,1)
  
initialize each oij^(l) to a random between -e & e
θ1 = rand(10,11) * (2*INIT_EPSILON) - INIT_EPSILON;
θ2 = rand(1,11) *(2*INIT_EPSILON) - INIT_EPSILON

-hθw to chθose a neural network model.
  Number of input units = dimension of features x^(i)
  number of output units = number of classes, i.e. vectors.
      -remember 4 different binary vector outcomes
    if output is multclass, rewrite them all as vectors
 default: 1 hidden layer, if > 1 hidden layer, have same number of units
 
 
--------------------EVALUATING LEARNING ALGORITHM-----------------------
- Model selection for Train/Validation/Test Sets
To avoid overfitting, and get least error, which model do you chθose?
You need to pick the degrees of polynomial. if d = 2, then its a
quadratic function. You want to find the function with the least error
To make sure your hypothesis is accurate, you make validation sets.
Validation sets are pieces of data that go into a third group other than
train or test sets. They try to find the best function.

 This is called cross-validation cv, or validation set.
 Validation sets are about 20% of the dataset

  Find the error using a cost function
      Jcv(θ) = 1/2mcv * sum(hθ(xicv) - yicv)^2
     
-Bias Vs Variance 
Is the cost function overfit or underfit.
   Bias (underfitting the data)
    Jtrain(θ) & Jcv(θ) will both be high
    Jcv(θ) will be relative to Jtrain(θ)
   -hθw to fix high bias:
     -Add features
     -Add polynomial features (θ^2)
     -Decrease lambda
      
   Variance (overfitting the data)
    Jtrain(θ) will be low
    Jcv(θ) >> Jtrain(θ)
   -hθw to fix high variance:
     -Get more training examples
     -Trying smaller sets of features
     -Increase lambda
     
 Regularization and Bias/Variance.
       You do the same thing as regular regularization
   Model: hθ(x) = θ0 + θ1*x + θ2*x^2 + θ3*x^3 
   J(θ) = 1/2m * sum(hθ(xi) - yi)^2 + ((lambda/2m)*sum(θj))
     Try different values of lambda to see which ones returns smallest 
     values for Jtest(θ)
  
-Learning curves
If experiencing high bias:
  -Low training set size:
    Jtrain(θ) is low and Jcv(θ) is high
  -Large training set size:
    Jtrain(θ) and Jcv(θ) is high
 If algorithm has high bias, getting more training data won't help

If experiencing high variance:
  -Low training set size:
    Jtrain(θ) is low and Jcv(θ) is high
  -Large training set size:
    Large gap between Jcv and Jtrain
    More training data will likely help.
    
    
 When you have small neural networks with fewer parameter they are more 
 prone to underfitting = high bias.
 
 Large neural networks with more parameters are more prone to
 overfitting = high variance. Use regularization (lambda) to fix it.
  

-------------------------PRIORITIZATION-----------------------------------
hθw do you chθose what to work on?

Error Analysis
Shθuld words with different endings be counted as the same word?
 discount/discounts/discounted === discount???
 
What about 'stemming': UNIverse/UNIversity

-Error metrics for skewed classes
A skewed class is usually a class that doesn't fit a model
Commonly done in classification problems

Precision/Recall precision metric
y = 1 in prescence of rare class that we want to detect.
               Actual    Class
                  1         0  
Predicted  1  True pos   False pos     %visualization of precision recall
Class      0  False neg  True neg

Precision = true positives / (true positives + false positives)
Recall = true positives / (true positives + false negatives)
             
F Score, comparing precision/recall numbers

 2* ((P*R)/(P+R))

        
-Optimization objective
Let's look at a different view of logistic regression.
      Instead of -log(1/(1+e^-z)) being a curve, it becomes 
       an obtuse angle.
       
       If y = 1: -log(1/(1+e^-z)) = Cost1(z)
       If y = 0: -log(1-(1/(1+e^-z))) = Cost0(z)

-Support Vector Machine:
Gives a cleaner way of learning complex non-linear functions.
 So you have a logistc regression term, A, and a regularization term, B.
  minθ = 1/m* [sumyi(-log(hθ(xi))+(1-yi)*((-log(1-hθ(xi))))] +
                 lambda/2m* sum(θj^2)
           A + lambda*B
      Give a new parameter C.
        Minimize C by C*A + B

  min θ C = sum(yi * cost1(θ^T * xi) + (1-yi)*cost0(θ^T *xi) +
                       (1/2) * sum(θj^2))

-Kernels
Adapting support vector machines in order to develop complex nonlinear
classifiers.  
 Let's say you have a complex non-linear decision boundary, you'll need
 many polynomial values for features.
      θ0 + θ1*x1 + θ2*x2 + θ3*x1*x2 + θ4*x1^2
  Anohter way of writing is to use features fn, to replace the x values
      θ0 + θ1*f1 + θ2*f2 + θ3*f3 + ...
 But hθw do you define these new features????
   Given x, compute new feature depending on proximity to landmarks l1,
   l2,l3.
          f1 = similarity(x,l1) = exp(-(||x - l1||^2)/2*(sigma^2))
          f2 = similarity(x,l2) = exp(-(||x - l2||^2)/2*(sigma^2))
          fn = similarity(x,ln) = exp(..........)
             the exp is a gaussian kernel
            ||x-li||^2  = -((sum(xj -lj1)^2)/2*(sigma^2))
 What do kernels do?
     if x = l1:
        f1 = exp(- (0^2/2*(sigma^2)) = 1
      
     if x is far from l1:
        f1 = exp(- (large number)^2/2*sigma^2) = 0.
 SVM parameters:          
   C( = 1/lambda)  Large C: lower bias, high variance.
                   Small C: higher bias, low variance.   
   sigma^2    Large: Features fit vary more smoothly.
                   Hihger bias, lower variance
              Small: Features fit vary less smoothly.
                   Higher variance, lower bias. Narrow shape


::::::::::::::::::::::: UNSUPERVISED LEARNING :::::::::::::::::::::::::::
Unsupervised learning is about analyzing training sets withθut any
 labels, or y values
      Training set: { x1, x2, x3,..,xm}
  The algorithm finds a structure in the dataset.      
  
  A common practice is finding clusters of datapoints in a set.
   
         --------------K-MEANS CLUSTERING----------------
-K-means clustering algorithm
Initialize random values, called cluster centroids, and assign any data
 points close to thθse centroid as being a part of that centroid.
    Algorithm
     Input:
        K(number of clusters)
        Training set {x(1), x(2),..x(m)}
     Randomly initialize K cluster centroids, mu1, mu2,..,muK
     Repeat {
        for i = 1 to m
            c(i) = index(from 1 to K) of cluster centroid closest to x(i)
        for k = 1 to K         c(i) minimizes k  k = index from 1 to K
            muK = average of points assigned to cluster K
            }
  -K-means cost function
     Let's say x(i) = 5. c(i) = 5  x(i) is in cluster 5. 
        muc(i) = mu5
        
       J(c(1),..,c(m),mu1,..,muK) = 1/m * sum(||x(i) - muc(i)||^2
        Minimizes J in respect to variables c, then to mu, then keeps
        doing it over and over.
       The cost function minimizes the distance from a K clusteroid to 
       the data points close to it.
 -hθw to initialize random K??
   Shθuld have K < m training examples
   Randomply pick K number of training examples
   set mu1,..,muK equal to these K examples
       mu1 = x(i)
       
    for i = 1 to 100 {
      Randomly initialize K-means
      Run K-means. Get c(1),..,c(m)
      Compute cost function (distortion)
       -> J(c(1),..,c(m),mu1,..,muK) }
       Pick clustering that gave lowest cost. You want K close to 0
  hθw to chθose value of K?
    Elbow methθd.
  
      -------------------DATA COMPRESSION--------------------
   Data compression is about reducing the dimensions of data. Like from
   3D data to 2D data.
      Example: You have the length of something in centimeters and inches.
         Why?? Just have one feature.
    2D to 1D  
      Represent two features, x1 and x2, as new feature z1.
       x1 --> z1
       xm --> zm
              [x1]    [z1]
              [x2] -> [z2]
              [xm]    [zm]
     3D to 2D  
       Take data in a 3D space and and convert it to a custom 2D plane.
         The z values will be the new 2D axes.      
 
-Principal Component Analysis (PCA)
  Tries to find a lower dimensional surface on which to project the data
  so that sum of squares of residuals is minimized. Also called projection
  error. Find a vector, vectoru(i) to do this. Finds a best fit line and
  makes a new graph out of that. 
   Reduce n-dimension to k-dimension. Find k vectors u(1), u(2),..,u(k)
                          | x2
                          |
                    x  x  |
                      x xx|
                       x x|
            --------------|-------------- x1
                          |x x
                          | x x
                          |   x x x
                          |
                          |
   What u(i) vector would be the best fit for this? It's like a slope
                 [-1/sqrt(2)] = x1
          u(1) = [1/sqrt(2)]  = x2
   
      There is no speical variable y that we're trying to predict
      
 -hθw to implement this
  Get training set: x(1),..x(m)
  Preprocess(mean normalization)
    muj = 1/m*sum(xj(i))
   Replace each xj(i) with xj - muj
   
  hθW TO FIND ALL THE U VECTORS
  Compute "covariance matrix";
    Sigma = 1/m * sum(x(i)*(x(i))^T
*************************************************************************
   Compute "eigenvectors" of matrix Sigma:
      [U,S,V] = svd(Sigma);    svd stands for singular value decompoistion
*************************************************************************
       U will be an n*n matrix
           [ |     |       |  ]
       U = [u(1)  u(2) .. u(n)] 
           [ |     |       |  ]
   Now get the z vector, which is a lower dimension
           [ |     |       |  ]^T       [--(u(i))^T--]
       z = [u(1)  u(2) .. u(k)]   *x =  [     :      ] 
           [ |     |       |  ]         [--(u(k))^T--]
               Ureducex
   Sigma = (1/m) * X' * X;
    

-Reconstruction from compressed representation. Going from 1D to 2D.
 hθw do we go from a lower dimensional space to a higher D space?
       z = U^Treducex
       xapprox = Ureduce * z
      
 -Chθosing k (number of principal components)
  Average squared projection error: 1/m * sum||x(i) -xapprox(i)||^2
  total variaion in data: 1/m * sum(||x(i)||^2)
    Chθose k to be smallest value so that 
    (1/m*sum||x(i) - xapprox(i)||^2) / (1/m * sum(||x(i)||^2)) <= 0.01
   start with k=1 then keep going until you get <= 0.01
   
   Gives S matrix that is a diagonal n*n matrix. from U,S,V = svd(Sigma)
       [S11     ]
       [  S22   ]
       [     S33]
   
   For given k:
      1 - ((sum(Sii)) / (sum(Sii))) <= 0.01
            or
************************************************************************* 
                     k          k
                  sum(Sii) / sum(Sii) >= 0.99
*************************************************************************
 
 
 --------------------------ANOMALY DETECTION------------------------------
 Detecting anomalies in your data and getting rid of them.
  Is there a datapoint that looks like it doesn't fit with the rest?
  
  Dataset: {x(1), x(2),..,x(3)}
    You have a model of x, called p(xtest)
       if p(xtest) < epsilon --> anomaly.     epsilon = anything
        p(xtest) >= epsilon --> ok.  
         
    *********If too many anomalies, try decreasing epsilon**********
 
 -Gaussian distribution
  x ~ (mu, sigma^2)
  
   Write as p(x; mu, sigma^2)
**************************************************************************
-Algorithm
  1. Chθose features xi that might be anomalies.
  2. Fit parameters mu1,..,mun, sigma1^2,..,sigman^2
         muj = (1/m) * sum(xj(i)
         sigmaj^2 = (1/m) * sum(xj(i) - muj)^2
         
  3. Given new example x, compute p(x):
  p(x) = sum(1/sqrt(2*pi*simgaj))*exp((xj-muj)^2/(2*simgaj^2))
      if p(x) < epsilon --> anomaly
*************************************************************************

-Make and evaluate an anomaly detection system.  
   y = 1 if p(x) < epsilon = anomaly
   y = 0 if p(x) >= epsilon = normal
   
-Chθosing features to use.  
  Chθose features that might take on unusually large or small values in
  the event of a nanomaly.
  
 
                 -----Recommender System-----
Recommender systems are systems that analyzes a person's activities and 
just recommends stuff that is similar. Like recommending music

   Example: Predicting movie ratings
______Movie__________|__Alice(1)___Bob(2)__Carol(3)___Dave(4)_|______
    Blah Blah        |    5          5       0          0     | xi)
 Niggers Cant Read   |    5          ?       ?          0     |
   Some Bullshit     |    ?          4       0          ?     |
      Title          |    0          0       5          4     |
      
             [5 5 0 0]  (θ(nu)^T*(x(1))
             [5 ? ? 0]  (θ(nu)^T*(x(2))
         Y = [? 4 0 ?]            :            These are predictions
             [0 0 5 4]  (θ(nu)^T*(x(nm))
           
     nu = number of users
     nm = number of moves
     r(i,j) = 1 if user j has rated movie i
     y^(i,j) = rating given by user j to movie i if r(i,j) = 1
   
-Optimization
     Given θ^(1),..,θ^(nu), to learn x^(i),..,x^(nm):
    min = 1/2 * sum(sum((θ^(j))^T *x^(i)-y^(i,j))^2) + lambda/2 *
                       sum(sum(xk^(i))^2)
-Collaborative Filtering  Algorithm
   1.Initialize x^(i),..x^(n,) & θ^(i),..,θ^(nu) to small randaom 
   2.Minimize J(x^(1),..,x^(nm) & θ^(1),..,θ^(nu) using grad. desc
     for every j = 1,..,nu, i = 1,..,nm:
    xk(i) =  xk(i)-α*(sum(((θ(j))^T *x(i) - y(i,j))*θk(j) +
                            lambda* xk(i)
    θk(i) =  θk(i)-α*(sum(((θ(j))^T *x(i) - y(i,j)) *
                                xk(j) + lambda* θk(i) 
                                
-Low Rank Matrix Factorization
    For user j, on movie i predict:
(θ(i))^T * (x(i)) = μi    

-----------------------------LARGE DATASETS-------------------------------
hθw do we run algorithms with extremely large datasets, like millions?
 Plot learning curve for range of m values and verify that the algorithm
 has high variance when m is small.
 
-Stochastic gradient descent.
  Intead of running every single examples, only run a few.
   cost(θ,(x(i),y(i))) = 1/2*(hθ(x(i))-y(i))^2
   Jtrain(θ) = 1/m * sum(cost(θ,(x(i),y(i))))
   
   1. Randomly shuffle dataset. Use 1 example in each iteration
   2. Repeat {
        for i = 1,..,m {
          θj = θj - α*(hθ(x(i))iy(i))*xj(i)}}
        
-Mini-batch gradient descent
   Use b examples each iteration   b = mini-batch size
     Get b = 10 examples   (x(i),y(i)),..,(x(i+9),y(i+9))
       θj = θj - d*(1/10) * sum(hθ(x(k))-y(k))*xj(k)
           (for every j = 0,..,n)
   Do this multiple times to get gradient descent faster

-Checking for convergence
     Plot cost(θ,(x(i),y(i))), averaged over a lot of examples
    Learning rate α typically held constant. Can decrease over time
    to converge. 
          α = const1/(iterationNumber + const2)
          
          
        -------------------ONLINE LEARNING------------------
Allows us to model problems where we have a continuous stream of data.
    Features x capture properties of user. We want to learn 
             p(y=1|x;θ)
         Get (x,y) corresponding to user
         update θ using (x,y)
       θj = θj - α*(hθ(x)-y)*xj
        
