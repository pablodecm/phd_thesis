# Machine Learning in High-Energy Physics {#sec:machine_learning}

\epigraph{Computers are useless. \\ They can
  only give you answers.}{Pablo Picasso}

Machine learning is an interdisciplinary field that deals with the
general problem of how
computers can automatically improve at certain tasks given data. The usefulness
and range of applicability of such techniques has surged in the last
decades due to the increase on accessible computational power and
the amount of useful data available. In this section, a general overview of
machine learning methods as well as the main tasks that can be addressed
with them will be provided. Subsequently, the technical basis of two specific
types of machine learning methods
used in the next chapters will be explored: boosted
decision trees and neural networks. Last but not least, we will go through
a brief review of the common past use cases of these techniques at high energy
physics experiments, especially focussing on those cases where they can
be used to address some of the statistical issues from
Chapter [-@sec:statinf].

## Problem Description

Machine learning is the field that deals with
algorithms, as described by computer programs,
that are able to *learn* from data. A more formal definition of learning,
yet general and useful in the context of this work, can be found
in the literature [@Mitchell:1997:ML:541177]: "A computer program is said
to learn from experience $E$ with respect to some class of tasks $T$
and performance measure $P$, if its performance at task in $T$, as
measured by $P$, improves with experience $E$". The previous sentence
clearly denotes the three key elements for learning in the context
of computer algorithms: the task (or class of task) that to be accomplished
$T$, a quantitative and robust way to measure the performance on those
tasks $P$ and a set of data that the algorithm can experience in order
to improve $E$.

The first step in order to tackle a problem with machine learning
techniques is the formal definition of the task $T$, together with
a quantifiable metric that scores the accuracy on such
task $P$. In this section, the most common machine learning
tasks that are of relevance for their possible use in particle
collider experiments and similar scientific contexts are introduced.
Simultaneously with the description of the tasks, performance
measures and data, the main general machine learning concepts
are reviewed.

### Probabilistic Classification and Regression {#sec:supervised}

One of the conceptually simple, yet versatile, tasks that can be addressed with
machine learning algorithms is *classification*. A classifier or a
classification rule is a function
$f(\boldsymbol{x}) : \mathcal{X} \longrightarrow \mathcal{Y}$ that
predicts a label $y \in \{0,...,k-1\}$, denoting correspondence to a
on category in a set of of $k$ categories,
for each input $\boldsymbol{x} \in \mathcal{X}$. The task of
classification, in the context of machine learning algorithms, is
to produce classification functions $f(\boldsymbol{x})$ that perform
well on an unobserved set of data.

Classification is often framed as a belonging to a larger
category of tasks referred to as  *supervised learning*,
where the goal is predicting the value of an output variable
$\boldsymbol{y}$ (here a multi-dimensional vector for generality)
based on the observed values of the input
variables $\boldsymbol{x}$, based on a *learning set* of $n$ input vectors
with known output values 
$S = \{(\boldsymbol{x}_0,\boldsymbol{y}_0),...,(\boldsymbol{x}_n,\boldsymbol{y}_n)\}$.
The output values $\boldsymbol{y}$ are known in the learning set, because they
were previously determined by an external method, typically a teacher
or supervisor looking at past observations, thus explaining the name of these
family of techniques.

From a statistical standpoint, the input observations
and target values from the learning set can be viewed as
random variables sampled from a joint probability distribution
$p(\boldsymbol{x}, \boldsymbol{y})$, which is typically unknown.
The family of supervised learning tasks also includes *regression*, which amounts
to construct a $f(\boldsymbol{x})$ that can to predict a numerical
target output $\boldsymbol{y}$, and *structured output* tasks where the output
vector $\boldsymbol{y}$ is a vector or a complex data structure where its
elements are tightly interrelated. As will be reviewed in [Section @sec:ml_hep],
most analysis problems amenable by machine learning  in high-energy
physics experiments are framed as classification and regression tasks,
while the use of structured output task is instead
not quite extensive. The reconstruction of the set and
properties of physical objects in an event directly from
the detector readout could be framed as a structured output task, if it
was to be approached directly using machine learning algorithms
instead of the procedures described in [Section @sec:event_reco].

The goal of supervised learning is not to perform well on the learning set $S$
used for improving at the specified task, but rather to perform well
on additional unseen observations sampled from the joint distribution
$p(\boldsymbol{x}, \boldsymbol{y})$. Supervised
learning algorithms exploit the conditional relations between the input
and the output variables, in order to classify new observations 
better than a random classification rule that does not depend on
the value of $\boldsymbol{x}$. When using machine learning
techniques in data analysis at the LHC, as will be reviewed in [Section @sec:ml_hep],
simulated observations are used instead of expert-labelled past observations.
Simulated observations correspond to random samples of the joint distribution
over the latent variables for the generative model
$p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta})$, as described in
[Section @sec:stat_model].

In fact, the problem of inferring a subset of latent variables $\boldsymbol{z}$
of the statistical model for the raw detector readouts of
a collider experiment $\boldsymbol{x}$,
or from any deterministic function of it $\boldsymbol{s}(\boldsymbol{x})$,
can be cast as a supervised learning problem. The learning set $S$ would consist
of simulated observations $\boldsymbol{x}_i$ (or a summary of it
$\boldsymbol{s}(\boldsymbol{x}_i)$), and a matching subset of interest of the
latent variables $\boldsymbol{y}_i \in \mathcal{Y} \subseteq \mathcal{Z}$.
The supervised
learning task can then be viewed as the estimation of the conditional
expectation value
$\mathbb{E}_{p(\boldsymbol{y} | \boldsymbol{x} = \boldsymbol{x}_i)} [\boldsymbol{y}]$
for each given input observation $\boldsymbol{x}_i$, thus characterising
the probability distribution $p(\boldsymbol{y} | \boldsymbol{x})$.

While several performance measures $P$ are possible for a given task $T$,
for supervised learning is common to use performance measures that estimate
the expected prediction error, or risk $R$, of a given predictor
function $f(\boldsymbol{x})$,
which can normally be expressed as:
$$
R(f) = \mathop{\mathbb{E}}_{
(\boldsymbol{x},\boldsymbol{y}) \sim p(\boldsymbol{x},\boldsymbol{y})}
\left [ L(\boldsymbol{y}, f(\boldsymbol{x})) \right ]
$$ {#eq:exp_pred_err}
where $L$ is a *loss function* that quantifies the discrepancy between
the true output and the prediction. The quantity defined in
[Equation @eq:exp_pred_err]
is often also referred to as *risk*,
*test error*,  or also as *generalisation error*.

The optimal model for a given task $T$ thus depends on the definition
of its loss function $L$, if the objective is minimising the
expected prediction error. In practice, the expected prediction
error cannot be estimated
analytically because $p(\boldsymbol{x}, \boldsymbol{y})$ is not
known, or not tractable in the case of a generative simulation model. The
generalisation error has thus to be estimated from a subset of labelled
samples $S'=\{(\boldsymbol{x}_0,\boldsymbol{y}_0),...,(\boldsymbol{x}_n',\boldsymbol{y}_n')\}$
as follows:
$$
R(f) \approx R_\textrm{S'} = \frac{1}{n'}
\sum_{(\boldsymbol{x}_i,\boldsymbol{y}_i) \in S'} L(\boldsymbol{y}_i,f(\boldsymbol{x}_i))
$$ {#eq:erm}
which is also commonly referred to as *empirical risk*
approximation
$R_\textrm{S'}$(f) based on the set $S'$. The supervised learning
problem can then be stated as
finding the function $\hat{f}$ from a class of functions $\mathcal{F}$, which
depends on the particularities of the algorithm, that minimises the empirical
risk over the learning set $S$:
$$
\hat{f} = \mathop{\textrm{arg min}}_{f \in \mathcal{F}} R_S(f)
$$ {#eq:learning_erm}
which is referred to as empirical risk minimisation (ERM) [@vapnik1999overview],
and it is at core of most of the existing learning techniques, such as those
described in [Section @sec:ml_techniques]. However, the ultimate goal of a
learning algorithm is to find a function $f*$ that minimises the risk
or expected prediction error $R(f)$:
$$
f^* = \mathop{\textrm{arg min}}_{f \in \mathcal{F}} R(f)
$$ {#eq:learning_rm}
where $R(f)$ is the quantity defined in [Equation @eq:exp_pred_err], corresponding
to the generalisation error, or average expected performance on unseen observations
sampled from $p(\boldsymbol{x}, \boldsymbol{y})$. The previous equation
can be used to define the optimal prediction function $f_B(\boldsymbol{x})$,
also referred as *Bayes model*, which represents the minimal error that any
supervised learning algorithm can achieve due to the intrinsic statistical
fluctuations and properties in the data.
$$
f_B(\boldsymbol{x}) = \mathop{\textrm{arg min}}_{\boldsymbol{y} \in \mathcal{Y}}  \mathop{\mathbb{E}}_{
\boldsymbol{y} \sim p(\boldsymbol{y} | \boldsymbol{x})}
\left [ L(\boldsymbol{y}, f(\boldsymbol{x})) \right ]
$$ {#eq:bayes_optimal}
where the last term indicates the optimal choice of target and
can be obtained by explicitly considering the conditional
expectation in the risk term described in [Equation @eq:learning_rm],
that is
$R(h) = \mathbb{E}_{\boldsymbol{x} \sim p(\boldsymbol{x} | \boldsymbol{y})}
\left [ \mathbb{E}_{\boldsymbol{y} \sim p(\boldsymbol{y} | \boldsymbol{x})}
\left [ L(\boldsymbol{y}, f(\boldsymbol{x})) \right ] \right ]$, that can
be obtained using Bayes theorem. The Bayes model $f_B(\boldsymbol{x})$,
and its corresponding risk $R(f_B)$, also referred as *residual error*,
can only be estimated if $p(\boldsymbol{x},\boldsymbol{y})$ is known
and the expectation can be computed analytically,
which is very rarely the case in real world problems, but can be useful
nevertheless when benchmarking techniques in synthetic datasets.

Because most learning algorithms optimise $f$, or its parameters,
using the learning set $S$, the empirical risk $R_\textrm{S}(f)$ is not a good
estimator of the expected generalisation error $R(f)$. In general, 
$R_\textrm{S}(f)$ underestimates $R_\textrm{S}(f)$ because the statistical
fluctuations of the finite number of observations in $S$ can be learnt to
increase the performance on $S$, while they are not useful for prediction
on a new set of observations. If the family of functions $\mathcal{F}$ conisdered
in the learning algorithm is flexible enough, which is often the case,
it is possible to achieve $R_\textrm{S}(f)=0$ for the learning set $S$ while
the generalisation error $R(f)$ is well away from zero. This effect can
actually lead to a degradation of the generalisation error while the empirical
risk in the learning set is decreasing during the learning procedure, which
is often referred to as *over-fitting*.

To compare different prediction functions or to realistically evaluate the
generalised performance of a given prediction model $f$, it is useful to
be able to compute unbiased estimates of $R(f)$. The simplest way to
obtain such estimate is to divide the learning set $S$ into two disjoint
random subsets $S_\textrm{train}$ and $S_\textrm{test}$. The train subset
$S_\textrm{train}$ will be used by the learning algorithm to optimise
the prediction function $f$ by means of empirical risk minimisation, as
described in [Equation @eq:learning_erm]. The hold-out or test
subset $S_\textrm{test}$ can then be used to obtain an unbiased estimation
of the performance of $f$ on unseen observation.

For many learning algorithms,
the learning process, or *training*, is iterative: the function $f$
is optimised incrementally based on the training data.
In this cases, an estimation
 generalisation error as the training evolves is useful to stop
the training procedure and avoid the degradation of generalisation
due over-fitting, in what is referred as *early stopping*.
In those cases, as well as to compare and ensemble
the results of various predictor functions and model configurations,
is useful to hold out a fraction
of $S_\textrm{train}$ which is commonly referred as validation
set $S_\textrm{valid}$. Alternative approaches exist to estimate
the generalisation error exist, including *cross-validation*
and its variations [@friedman2001elements], which are usually preferred when
the the amount of training data is reduced.

Another important concept for most machine learning techniques is that of
*hyper-parameters*. The majority of machine learning algorithms depend on
a set of parameters that regulate the flexibility of the family
of functions $\mathcal{F}$ to consider for empirical risk minimisation as
well as the details of the optimisation procedure followed to solve the task
presented in [Equation @eq:learning_erm]. The expected performance of a given
model depends on these parameters, however their optimal value depends on the
particularities of the data (e.g. number of input dimensions or number
of size of the data size). This motivates the notion of *hyper-parameter
optimisation*, where the performance of the various choices of
hyper-parameters on the validation set or by mean of cross-validation
techniques, in order to select the best configuration.

The loss function $L$ of a supervised learning algorithm,
which quantifies the discrepancies between the prediction and the true
output target, depends on the task $T$ and formally defines it. A principled
loss function for classification is the *zero-one loss*, which is defined
as zero when the prediction $f(\boldsymbol{x})$ matches the
target $y$ and one otherwise. The zero-one risk can then be expressed  as:
$$
R_{0-1}(f) = \mathop{\mathbb{E}}_{
(\boldsymbol{x},y) \sim p(\boldsymbol{x},y)}
\left [ \mathbb{1}(y \neq f(\boldsymbol{x})) \right ]
$$ {#eq:zero_one_risk}
where $\mathbb{1}(y \neq f(\boldsymbol{x}))$ is an indicator
function. The zero-one loss is non-differentiable when $y =f(\boldsymbol{x})$
and its gradients are zero elsewhere; in addition, it is not convex,
a property which makes the
minimisation task in [Equation @eq:learning_erm] hard to
tackled by optimisation algorithms. In fact, it can be proven
that finding the function $f$ in $F$ that minimises directly the 
$R_{0-1}$ empirical risk for a training sample is a NP-hard problem. The
Bayes optimal classifier for the 0-1 loss can nevertheless be easily
obtained from [Equation @eq:bayes_optimal] as a function
of the conditional expectation:
$$
f_B(\boldsymbol{x}) = \mathop{\textrm{arg min}}_{y \in \mathcal{Y}}  \mathop{\mathbb{E}}_{
y \sim p(\boldsymbol{y} | \boldsymbol{x})}
\left [ \mathbb{1}(y \neq f(\boldsymbol{x})) \right ] = 
\mathop{\textrm{arg max}}_{y \in \mathcal{Y}} p(y | \boldsymbol{x})
$$ {#eq:bayes_optimal}
thus the optimal classifier amounts to the prediction of the most likely
output category $y$ for a given input $\boldsymbol{x}$. The previous
problem is normally referred to as *hard classification*, where the
objective is to assign a category for each input observation. Because
most problem in high-energy physics that can be cast as supervised learning,
are ultimate inference problems as will be reviewed in [Section @sec:ml_hep],
it more generally more useful to consider the problem of *soft classification*,
which instead amounts to estimate the class probability for each input
$\boldsymbol{x}$.

Soft classification is specially useful when the classes are not separable,
which is often the case for applications in collider experiments. Luckily,
soft classification is also a consequence of the convex relaxation of the
zero-one loss of [Equation @eq:zero_one_risk], which is used . For a two-class
classification problem, e.g signal versus background,
a useful approximation of the zero-one loss is the binary
cross entropy, defined as:
$$
L_\textrm{BCE} ( y , f(\boldsymbol{x})) = -y \log (f(\boldsymbol{x})) - (1-y) \log (1 - f(\boldsymbol{x}))
$$ {#eq:binary_xe}
where now the one-dimensional output prediction $f(\boldsymbol{x})$,
when bounded between 0 and 1 (e.g. using a sigmoid/logistic function),
will effectively approximate the conditional
probability $p(\boldsymbol{y} = 1 | \boldsymbol{x})$. In fact, the Bayes
optimal model for a binary cross-entropy classifier is:
$$ \begin{aligned}
f_B(\boldsymbol{x}) &= \mathop{\mathbb{E}}_{
(\boldsymbol{x},y) \sim p(\boldsymbol{x},y)}
\left [ L_\textrm{BCE} ( y , f(\boldsymbol{x}))  \right ] =
p(y = 1| \boldsymbol{x}) \\
&= \frac{p(\boldsymbol{x} | y = 1) p(y = 1)}{
\sum_{\forall y_i \in \{0,1\}}p(\boldsymbol{x} | y = y_i) p(y = y_i)} =
\left ( 1 +
\frac{p(\boldsymbol{x} | y = 0) p(y = 0)}{
p(\boldsymbol{x} | y = 1) p(y = 1)} \right )^{-1}
\end{aligned}  
$$ {#eq:bayes_optimal_bce}
where the second line in the equation is a direct consequence of Bayes
theorem and from the last term it can be clearly seen that the
prediction output is monotonous with the density ratio between
the probability density functions for each category. Simlar results can
be obtained for the Bayes optimal classifier for other soft
relaxations of the zero-one function. Machine
learning binary classifiers will effectively approximate this quantity
directly from empirical samples, where the prior probabilities of each
class represent the relative presence of observations from each category.

Binary cross entropy is a subclass of the more general *cross entropy* loss
function, that can be used for $k$-categories classification, commonly referred
to as multi-class classification. In these cases, a k-dimensional
vector target $\boldsymbol{y}$
is often constructed, where each component $y_i$ is one if the
observation belongs to the class $i$ or zero otherwise, and the output of
the prediction function $\boldsymbol{\hat{y}} = f(\boldsymbol{x})$ is also
a vector of $k$ components. Within this framework, the cross entropy loss
can then be defined as:
$$
L_\textrm{CE} ( \boldsymbol{y} , f(\boldsymbol{x})) = - \sum_i y_i \log \hat{y}_i
$$ {#eq:general_ce}
which can be used to recover [Equation @eq:binary_xe] when $k=2$, considering
the one-dimensional target and prediction as the the i=1 elements 
and that $y_0=1-y$ and $\hat{y}_0=1-f(x)$. If the prediction
output is to generally represent exclusive class probabilities, as is the goal of soft
classification, the prediction sum is expected to be one. 
A simple way to ensure the aforementioned property
is to apply a function that ensures that the prediction outputs are in
the range $[0,1]$ and normalised so $\sum_i \hat{y}_i=1$. The *softmax function*
is a common choice in machine learning, which is a generalisation
of the logistic function to
$k$ dimensions, an is defined as:
$$
\hat{y}_i = \frac{e^{f_i(\boldsymbol{x})/\tau}}
                  {\sum_{j=0}^{k} e^{f_j(\boldsymbol{x})/\tau}}
$${#eq:softmax_function}
where $f_i$ and $f_j$ refer to the $i$ and $j$ elements of the vector
function $f(\boldsymbol{x})$ and $\tau$ is the temperature,
a parameter that regulates the softness of the operator which is often
omitted (i.e. $\tau=1$). In the limit of $\tau \rightarrow 0^{+}$,
the probability of the largest component will tend to 1 while others to 0.
The softmax output can be used to represent the probability distribution
of a categorical distribution in a differentiable way, where the outcome
represent the probabilities of each of the $k$ possible outcomes, which
will be useful in [Chapter @sec:inferno].
When the softmax function and the cross entropy loss are used together
for multiclass classification, the optimal Bayes model is:
$$
\begin{aligned}
{f_{B,i}} (\boldsymbol{x}) &= \mathop{\mathbb{E}}_{
(\boldsymbol{x},y) \sim p(\boldsymbol{x},y)}
\left [ L_\textrm{CE} ( y , f(\boldsymbol{x}))  \right ] =
p(y = y_i| \boldsymbol{x}) \\
&= \frac{p(\boldsymbol{x} | y = y_i) p(y = y_i)}{
\sum_{\forall y_i \in \{0,..., k-1\}}p(\boldsymbol{x} | y = y_i) p(y = y_i)}
\end{aligned}  
$$ {#eq:bayes_optimal_bce}
which can also be expressed as a function of a sum of density ratios
of the categories.

<!-- TODO: basic loss for regression -->


## Machine Learning Techniques {#sec:ml_techniques}

While the focus of the previous section was defining the main problems
and properties that can be addressed with machine learning techniques,
details about the actual computational and statistical
procedures used for learning were not provided. In
this chapter, the basis of the two classes of algorithms that are used
in this work will
be described in detailed: boosted decision trees and artificial neural networks.
These families of learning methods are also those that are most commonly used for
doing machine learning in experimental particle physics, mostly to solve
supervised learning problems, as will be described in [Section @sec:ml_hep].
The overview included here is by no means comprehensive about the mentioned
approaches or alternative popular statistical learning techniques such
as random forests or support vector machines, for which the following references
provided a more extensive review [@friedman2001elements;@Goodfellow-et-al-2016;@louppe2014understanding].

### Boosted Decision Trees {#sec:boosted_decision_trees}

### Artificial Neural Networks

## Applications in High Energy Physics {#sec:ml_hep}

Machine learning techniques, in particular supervised learning, are
increasingly being used in experimental particle physics analysis
at the LHC. In this section, the main use cases are described,
linking the learning task with the statistical
problems and properties which were described in [Chapter @sec:statinf]. In
broad terms, most supervised learning at collider experiments
can be viewed as a way to approximate the latent variables of the
generative model based on simulated observations. Those latent variable
approximations are often very informative about the parameters of interest
and then can be used to construct summary statistics of the observations,
which allow to carry out likelihood-free inference efficiently.

### Signal vs Background Classification {#sec:sig_vs_bkg}

#### Sufficient Statistics for Mixture Models  {#sec:sufficiency_clf}

Let us consider the general problem of inference for a two-component
mixture problem, which is very common in scientific disciplines such
as High Energy Physics.
While their functional form will not be explicitly specified to keep
the formulation general, one of the components will be denoted as signal
$f_s(\boldsymbol{x}| \boldsymbol{\theta})$ and the other as background
$f_b(\boldsymbol{x} | \boldsymbol{\theta})$, where  $\boldsymbol{\theta}$ is
are of all parameters the distributions might depend on. The probability
distribution function of the mixture can then be expressed as:
$$
p(\boldsymbol{x}| \mu, \boldsymbol{\theta} ) = (1-\mu) f_b(\boldsymbol{x} | \boldsymbol{\theta}) 
                                                + \mu f_s(\boldsymbol{x} | \boldsymbol{\theta})
$${#eq:mixture_general}
where $\mu$ is a parameter corresponding to the signal mixture fraction.
Dividing and multiplying by $f_b(\boldsymbol{x} | \boldsymbol{\theta})$ we
have:
$$
p(\boldsymbol{x}| \mu, \boldsymbol{\theta} ) = f_b(\boldsymbol{x} | \boldsymbol{\theta})   \left ( 1-\mu
                    + \mu \frac{f_s(\boldsymbol{x} | \boldsymbol{\theta})}{f_b(\boldsymbol{x} | \boldsymbol{\theta})}
                    \right )  
$${#eq:mixture_div}
from which we can already prove that the density ratio
$s_{s/ b}= f_s(\boldsymbol{x} | \boldsymbol{\theta}) / f_b(\boldsymbol{x} | \boldsymbol{\theta})$
(or alternatively its inverse) is a sufficient summary statistic for the
mixture coefficient parameter $\mu$. This would also be the case for
the parametrization using $s$ and $b$ if the alternative $\mu=s/(s+b)$
formulation presented for the synthetic problem in Sec. \ref{d-synthetic-mixture}.

However, previously in this work (as well as for most studies using
classifiers to construct summary statistics) we have been using the
summary statistic $s_{s/(s+b)}= f_s(\boldsymbol{x} | \boldsymbol{\theta}) /(
  f_s(\boldsymbol{x} | \boldsymbol{\theta}) + f_b(\boldsymbol{x} | \boldsymbol{\theta}))$
instead of $s_{s/ b}$. The advantage of $s_{s/(s+b)}$ is that it represents
the conditional probability of one observation $\boldsymbol{x}$ coming
from the signal assuming a balanced mixture, and hence is bounded between
zero and one. This greatly simplifies its visualisation and non-parametetric
likelihood estimation. Taking [@Eq:mixture_div] and manipulating the
subexpression depending on $\mu$ by adding and subtracting $2\mu$  we have:
$$
p(\boldsymbol{x}| \mu, \boldsymbol{\theta} ) = f_b(\boldsymbol{x} | \boldsymbol{\theta})   \left ( 1-3\mu
                    + \mu \frac{f_s(\boldsymbol{x} | \boldsymbol{\theta}) + f_b(\boldsymbol{x} | \boldsymbol{\theta})}{f_b(\boldsymbol{x} | \boldsymbol{\theta})}
                    \right )  
$${#eq:mixture_sub}
which can in turn can be expressed as:

$$
p(\boldsymbol{x}| \mu, \boldsymbol{\theta} ) = f_b(\boldsymbol{x} | \boldsymbol{\theta})   \left ( 1-3\mu
                    + \mu \left ( 1- \frac{f_s(\boldsymbol{x} | \boldsymbol{\theta})}{f_s(\boldsymbol{x} | \boldsymbol{\theta})
                  +f_b(\boldsymbol{x} | \boldsymbol{\theta})} \right )^{-1}
                    \right )  
$${#eq:mixture_suff}
hence proving that $s_{s/(s+b)}$ is also a sufficient statistic and theoretically
justifying its use for inference about $\mu$. The advantage of both $s_{s/(s+b)}$ 
and $s_{s/b}$ is they are one-dimensional and do not depend on the
dimensionality of $\boldsymbol{x}$ hence allowing much more efficient
non-parametric density estimation from simulated samples. Note that
we have been only discussing sufficiency with respect to the mixture
coefficients and not the additional distribution parameters
$\boldsymbol{\theta}$. In fact, if a subset of $\boldsymbol{\theta}$ 
parameters are also relevant for inference (e.g. they are nuisance
parameters) then $s_{s/(s+b)}$ and $s_{s/b}$ are not sufficient statistics
unless the $f_s(\boldsymbol{x}| \boldsymbol{\theta})$ and
$f_b(\boldsymbol{x}| \boldsymbol{\theta})$ have very specific functional
form that allows a similar factorisation. 

### Particle Identification and Regression



