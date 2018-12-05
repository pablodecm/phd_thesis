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
fluctuations and properties in the data. The Bayes model can be expressed
as:
$$
f_B(\boldsymbol{x}) = \mathop{\textrm{arg min}}_{\boldsymbol{y} \in \mathcal{Y}}  \mathop{\mathbb{E}}_{
\boldsymbol{y} \sim p(\boldsymbol{y} | \boldsymbol{x})}
\left [ L(\boldsymbol{y}, f(\boldsymbol{x})) \right ]
$$ {#eq:bayes_optimal}
where the last term indicates the optimal choice of target $\boldsymbol{y}$ for each
value of $\boldsymbol{x}$. The previous expression
can be obtained by explicitly considering the conditional
expectation in the risk term described in [Equation @eq:learning_rm],
that is
$R(h) = \mathbb{E}_{\boldsymbol{x} \sim p(\boldsymbol{x} | \boldsymbol{y})}
\left [ \mathbb{E}_{\boldsymbol{y} \sim p(\boldsymbol{y} | \boldsymbol{x})}
\left [ L(\boldsymbol{y}, f(\boldsymbol{x})) \right ] \right ]$, that can
be obtained using Bayes theorem. The Bayes model $f_B(\boldsymbol{x})$,
and its corresponding risk $R(f_B)$, also referred as *residual error*,
can only be estimated if $p(\boldsymbol{x},\boldsymbol{y})$ is known
and the expectation can be computed analytically. Even though the
Bayes optimal model cannot be obtained for real world problems, it
can be useful nevertheless when benchmarking techniques in synthetic
datasets or for theoretical studies.

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
In those cases, an estimation of the
generalisation error as the training evolves may be useful to stop
the training procedure and avoid the degradation of generalisation
due over-fitting, in what is referred as *early stopping*.
In those cases, as well as to compare and ensemble
the results of various predictor functions and model configurations,
is useful to hold out a fraction
of $S_\textrm{train}$ which is commonly referred as validation
set $S_\textrm{valid}$. Alternative approaches to estimate
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
hyper-parameters is evaluated on the validation set or
by mean of cross-validation techniques, in order to select the best
configuration.

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
$R_{0-1}$ empirical risk with a training sample is a NP-hard
problem [@nguyen2013algorithms]. The
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
it is more generally more useful to consider the problem of *soft classification*,
which instead amounts to estimate the class probability for each input
$\boldsymbol{x}$.

Soft classification is especially useful when the classes are not separable,
which is often the case for applications in collider experiments. Luckily,
soft classification is also a consequence of most convex relaxations of the
zero-one loss of [Equation @eq:zero_one_risk]. For a two-class
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
is a common choice in machine learning. It is a generalisation
of the logistic function to
$k$ dimensions, and is defined as:
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
represent the probabilities of each of the $k$ possible outcomes. We will
make use of this function in [Chapter @sec:inferno].
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
be described in detail: boosted decision trees and artificial neural networks.
These families of learning methods are also those that are most commonly used
in machine learning within experimental particle physics, mostly to solve
supervised learning problems, as will be described in [Section @sec:ml_hep].
The overview included here is by no means comprehensive about the mentioned
approaches or alternative popular statistical learning techniques such
as random forests or support vector machines, for which the following references
provided a more extensive review [@friedman2001elements;@Goodfellow-et-al-2016;@louppe2014understanding].

### Boosted Decision Trees {#sec:boosted_decision_trees}

### Artificial Neural Networks {#sec:ann}

## Applications in High Energy Physics {#sec:ml_hep}

Machine learning techniques, in particular supervised learning, are
increasingly being used in experimental particle physics analysis
at the LHC [@Guest:2018yhq].
In this section, the main use cases are described,
linking the learning task with the statistical
problems and properties which were described in [Chapter @sec:statinf]. In
broad terms, most supervised learning at collider experiments
can be viewed as a way to approximate the latent variables of the
generative model based on simulated observations. Those latent variable
approximations are often very informative about the parameters of interest
and then can be used to construct summary statistics of the observations,
which allow to carry out likelihood-free inference efficiently.

### Signal vs Background Classification {#sec:sig_vs_bkg}

The mixture structure of the statistical model for collisions outcomes,
discussed in [Chapter @sec:statinf], facilitates its
framing as a classification problem. Intuitively, the classification
objective could be
stated as the separation of detector outcomes coming from processes that
contain information about the parameters of interest from those that do not,
which will be referred as signal and background respectively, following
the same nomenclature from [Section @sec:sig_and_bkg]. The two classes
are often non-separable - i.e. a given detector outcome $\boldsymbol{x}$
(or any function of it) could have been produced either by signal or background
processes, and only probabilistic statements of class assignment can be made.

In order to use supervised machine learning techniques to classify detector
outcomes, labelled samples are required, yet only the detector readout
$\boldsymbol{x}$
is known for collected data. Realistic simulated observations, generated
specifically to model events from a given set processes (e.g. signal
and background) can instead be used as training data, where the categorical
latent variable $z_i$ that represents a given set of processes can
effectively used as classification label. If the simulator model is
misspecified, e.g. due to the effect of known unknowns as discussed
in [Section @sec:known_unknowns], the resulting classifiers
would be trained to to optimise the classification objective for
different distributions.

To understand the role of classification in the larger goal of statistical
inference of a subset of parameters of interest in a mixture model,
let us consider the general problem of inference for a two-component
mixture problem. One of the components will be denoted as signal
$p_s(\boldsymbol{x}| \boldsymbol{\theta})$ and the other as background
$p_b(\boldsymbol{x} | \boldsymbol{\theta})$, where  $\boldsymbol{\theta}$ is
are of all parameters the distributions might depend on. As
discussed in [Section @sec:mixture_components], it is often the case that
$f_s(\boldsymbol{x}| \boldsymbol{\theta})$ and
$f_b(\boldsymbol{x} | \boldsymbol{\theta})$ are not known, observations
can only be simulated, which will not affect the validity the following
discussion. The probability
distribution function of the mixture can be expressed as:
$$
p(\boldsymbol{x}| \mu, \boldsymbol{\theta} ) = (1-\mu) p_b(\boldsymbol{x} | \boldsymbol{\theta}) 
                                                + \mu p_s(\boldsymbol{x} | \boldsymbol{\theta})
$${#eq:mixture_general}
where $\mu$ is a parameter corresponding to the signal mixture fraction,
which will be the only parameter of interest for the time being. As
discussed in [Section @sec:sig_and_bkg],
most the of the parameters of interest in analyses at the LHC, such cross
sections, are proportional to the mixture coefficient of the signal
in the statistical model.
The results presented here would also be also be valid if alternative mixture
coefficient parametrisation such as the one considered in [Section @sec:synthetic_mixture] are used, e.g. $\mu=s/(s+b)$ where $s$ and $b$
is the expected number of events for signal and background respectively, as
long as $b$ is known and fixed and $s$ is the only parameter of interest.

#### Likelihood Ratio Approximation {#sec:lr_clf}

Probabilistic classification techniques will effectively approximate
the conditional probability of each class, as discussed in
[Equation @eq:bayes_optimal_bce] for the binary classification. A way to
approximate the density ratio $r(\boldsymbol{x})$ 
between two arbitrary distribution functions $\rho(\boldsymbol{x})$ and
$q(\boldsymbol{x})$ is then to train
a classifier - e.g. a neural network optimising cross-entropy. If samples
from $\rho(\boldsymbol{x})$ are labelled as $y=1$, while $y=0$ is used
for observations from $q(\boldsymbol{x})$, the density ratio can be
approximated from the soft BCE classifier output $s(\boldsymbol{x})$ as:
$$
\frac{s(\boldsymbol{x})}{1-s(\boldsymbol{x})} \approx
\frac{p(y = 1| \boldsymbol{x})}{p(y = 0| \boldsymbol{x})} = 
\frac{p(\boldsymbol{x} | y = 1) p(y = 1)}{p(\boldsymbol{x} | y = 0) p(y = 0)}
=  r(\boldsymbol{x}) \frac{p(y = 1)}{p(y = 0)}
$$ {#eq:lr_clf}
thus the density ratio  $r(\boldsymbol{x})$ 
can be approximated by a simple function of the trained classifier output
directly from samples of observations. The factor
$p(y = 1)/p(y = 0)$ is independent on $\boldsymbol{x}$, and can
be simply estimated as the ratio between the total number of observations
from each category in the training dataset - i.e. equal to 1 if it is
balanced.

Density ratios are very useful for inference, particularly for
hypothesis testing, given that the likelihood ratio $\Lambda$
from [Equation @eq:likelihood_ratio] is the most powerful test
statistic to distinguish between two simple hypothesis
and can be expressed as a function of density ratios. Returning
to the two component mixture from [Equation @eq:mixture_general], for discovery
the null hypothesis $H_0$ corresponds to background-only
$p(\boldsymbol{x}| \mu = 0, \boldsymbol{\theta})$ while the alternate
is often a given mixture of signal and background
$p(\boldsymbol{x}| \mu = \mu_0, \boldsymbol{\theta})$, where $\mu_0$
is fixed. For the time being, the other distribution parameters  $\boldsymbol{\theta}$ will be assumed to be known and fixed to
the same values for both hypothesis.
The likelihood ratio in this case can be expressed as:
$$
\Lambda( \mathcal{D}; H_0, H_1) =
\prod_{\boldsymbol{x} \in \mathcal{D}}
\frac{p(\boldsymbol{x}| H_0)}{ p(\boldsymbol{x} |H_1)} =
\prod_{\boldsymbol{x} \in \mathcal{D}}
\frac{p(\boldsymbol{x}| \mu = 0, \boldsymbol{\theta})}{
p(\boldsymbol{x}| \mu = \mu_0, \boldsymbol{\theta})}
$$ {#eq:lr_mixture}
where the $p(\boldsymbol{x}| \mu = 0, \boldsymbol{\theta})/p(\boldsymbol{x}|
\mu_0, \boldsymbol{\theta})$ factor could be approximated from the output
of a probabilistic classifier trained to distinguish observations from
$p(\boldsymbol{x}| \mu = 0, \boldsymbol{\theta})$  and those from
$p(\boldsymbol{x}| \mu = \mu_0, \boldsymbol{\theta})$. A certain $\mu_0$ would  
have to be specified to generate $p(\boldsymbol{x}| \mu = \mu_0,
\boldsymbol{\theta})$ observations in order to train the classifier. The
same classifier output could be repurposed to model the likelihood ratio
when $H_1$ is $p(\boldsymbol{x}| \mu = \mu_1, \boldsymbol{\theta})$ with
a simple transformation, yet the mixture structure of the problem allows a
for a more direct density ratio estimation alternative, which is the
one regularly used in particle physics analyses.

Let us consider instead the inverse of the likelihood ratio
$\Lambda$ from [Equation @eq:lr_mixture], each factor term is thus
proportional to the following ratio:
$$
\Lambda^{-1} \sim
\frac{p(\boldsymbol{x} | H_1)}{ p(\boldsymbol{x} | H_0 )}  =
\frac{ (1-\mu_0) p_\textrm{b}(\boldsymbol{x}| \boldsymbol{\theta}) +
  \mu_0 p_\textrm{s}(\boldsymbol{x}|
   \boldsymbol{\theta})}{p_\textrm{b}(\boldsymbol{x}|
   \boldsymbol{\theta})}
$$ {#eq:lr_one}
which can in turn be be expressed as:
$$
\Lambda^{-1} \sim
1-\mu) \left ( \frac{p_\textrm{s}(\boldsymbol{x}| \boldsymbol{\theta})}{
                          p_\textrm{b}(\boldsymbol{x}| \boldsymbol{\theta})}-1 \right)
$$ {#eq:lr_two}
thus each factor in likelihood ratio is bijective function of
the density ratio
$p_\textrm{s}(\boldsymbol{x}| \boldsymbol{\theta})
/p_\textrm{b}(\boldsymbol{x}| \boldsymbol{\theta})$.
The previous density ratio can be approximated by training a classifier
to distinguish signal and background observations, which is computationally
more efficient and easier to interpret intuitively 
than the direct $p(\boldsymbol{x}| H_0)/p(\boldsymbol{x} |H_1)$
approximation mentioned before.

From a statistical inference point of view, supervised machine learning framed
as the classification of signal versus background can be viewed as a way to
approximate the likelihood ratio directly from simulated samples, bypassing
the need of a tractable density function (see [Section @sec:likelihood-free]).
It is worth noting that because it is only an approximation, in order to
be useful for inference it requires careful calibration. Such calibration
is usually carried out using a histogram and an holdout dataset
of simulated observations, effectively building a synthetic likelihood
of the whole classifier output range or the number of observed
events after cut in the classifier is imposed
(see [Section @sec:synthetic_likelihood]). Alternative density estimation
techniques could also be used for the calibration step, which could reduce
the loss of information due to the histogram binning.

The effect of nuisance parameters, due to known unknowns,
have also to be accounted for during the calibration step. The true
density ratio between signal and background depends on any parameter
$\boldsymbol{\theta}$ that modifies the signal $p_s(\boldsymbol{x} |
\boldsymbol{\theta})$ or
background $p_b(\boldsymbol{x} | \boldsymbol{\theta})$ probability densities,
thus its approximation using machine learning classification can become
complicated. In practice, the classifier can be trained for the most
probable likely value of the nuisance parameters and their effect can
be adequately accounted during calibration, yet the resulting
inference will be degraded. While this issue can be somehow
ameliorated using parametrised classifiers [@baldi2016parameterized],
the main motivation for using the likelihood ratio - i.e. the
Neyman-Pearson lemma - does not apply because the hypothesis considered
are not simple when nuisance parameters are present.


#### Sufficient Statistics Interpretation {#sec:sufficiency_clf}

Another interpretation of the use of signal versus background
classifiers, which more generally applies to any type
of statistical inference, is based on applying the
concept of statistical sufficiency (see [Section @sec:suff_stats]). Starting
from the mixture distribution function in [Equation @eq:mixture_general],
and both dividing and multiplying by $p_b(\boldsymbol{x} | \boldsymbol{\theta})$
we obtain:
$$
p(\boldsymbol{x}| \mu, \boldsymbol{\theta} ) = p_b(\boldsymbol{x} | \boldsymbol{\theta})   \left ( 1-\mu
                    + \mu \frac{p_s(\boldsymbol{x} | \boldsymbol{\theta})}{p_b(\boldsymbol{x} | \boldsymbol{\theta})}
                    \right )  
$${#eq:mixture_div}
from which we can already prove that the density ratio
$s_{s/ b}(\boldsymbol{x})= p_s(\boldsymbol{x} | \boldsymbol{\theta}) /
           p_b(\boldsymbol{x} | \boldsymbol{\theta})$
(or alternatively its inverse) is a sufficient summary statistic for the
mixture coefficient parameter $\mu$, according the Fisher-Neyman
factorisation criterion defined in [Equation @eq:sufficient_single]. The
density ratio can be approximated directly from signal versus background
classification as indicated in [Equation @eq:lr_clf].

In the analysis presented in [Chapter @sec:higgs_pair] and
in the synthetic problem considered in [Section @sec:synthetic_mixture],
as well as for most LHC analysis using
classifiers to construct summary statistics, the
summary statistic
$$
s_{s/(s+b)}= \frac{p_s(\boldsymbol{x} | \boldsymbol{\theta})}{
p_s(\boldsymbol{x} | \boldsymbol{\theta}) +
 p_b(\boldsymbol{x} | \boldsymbol{\theta})}$$  
instead of $s_{s/ b} (\boldsymbol{x})$ is used.
The advantage of $s_{s/(s+b)}(\boldsymbol{x})$ is that it represents
the conditional probability of one observation $\boldsymbol{x}$ coming
from the signal assuming a balanced mixture, so it can be approximated
by simply taking the classifier output. In addition, being a probability
it is bounded between
zero and one which greatly simplifies its visualisation and non-parametric
likelihood estimation. Taking [Equation @Eq:mixture_div] and manipulating
the subexpression depending on $\mu$ by adding and
subtracting $2\mu$  we have:
$$
p(\boldsymbol{x}| \mu, \boldsymbol{\theta} ) = p_b(\boldsymbol{x} | \boldsymbol{\theta})   \left ( 1-3\mu
                    + \mu \frac{p_s(\boldsymbol{x} | \boldsymbol{\theta}) + p_b(\boldsymbol{x} | \boldsymbol{\theta})}{p_b(\boldsymbol{x} | \boldsymbol{\theta})}
                    \right )  
$${#eq:mixture_sub}
which can in turn can be expressed as:
$$
p(\boldsymbol{x}| \mu, \boldsymbol{\theta} ) = p_b(\boldsymbol{x} | \boldsymbol{\theta})   \left ( 1-3\mu
                    + \mu \left ( 1- \frac{p_s(\boldsymbol{x} | \boldsymbol{\theta})}{p_s(\boldsymbol{x} | \boldsymbol{\theta})
                  +p_b(\boldsymbol{x} | \boldsymbol{\theta})} \right )^{-1}
                    \right )  
$${#eq:mixture_suff}
hence proving that $s_{s/(s+b)}(\boldsymbol{x})$
is also a sufficient statistic and theoretically
justifying its use for inference about $\mu$. The advantage of both
$s_{s/(s+b)}(\boldsymbol{x})$ 
and $s_{s/b}(\boldsymbol{x})$ is that they
are one-dimensional and do not depend on the
dimensionality of $\boldsymbol{x}$ hence allowing much more efficient
non-parametric density estimation from simulated samples. Note that
we have been only discussing sufficiency with respect to the mixture
coefficients and not the additional distribution parameters
$\boldsymbol{\theta}$. In fact, if a subset of $\boldsymbol{\theta}$ 
parameters are also relevant for inference (e.g. they are nuisance
parameters) then $s_{s/(s+b)}(\boldsymbol{x})$ and
$s_{s/b}(\boldsymbol{x})$ are not sufficient statistics
unless the $p_s(\boldsymbol{x}| \boldsymbol{\theta})$ and
$p_b(\boldsymbol{x}| \boldsymbol{\theta})$ have very specific functional
form that allows a similar factorisation.

In summary, probabilistic
signal versus background classification is an effective
proxy to construct summary statistic that asymptotically
approximate sufficient statistics directly from simulated
samples, when the distributions of signal
and background are fully defined and $\mu$ (or $s$ in the alternative
parametrisation mentioned before) is the only unknown parameter.
If the statistical model depends on additional nuisance parameters, probabilistic
classification does not provide any sufficiency guarantees, so useful
information about that can used to constrain the parameters of interest
might be lost if a low-dimensional
classification-based summary statistic is used in place
of $\boldsymbol{x}$. This theoretical observation will be observed
in practice in [Chapter @sec:inferno], where a new technique to
construct summary statistics, that is not based on classification,
but accounts for the effect of nuisance parameters is presented.


### Particle Identification and Regression {#eq:particle_id_reg}

While the categorical latent variable $z_i$, denoting the interaction
process that happened in the collision, is very useful to define an event
selection or directly as a summary statistic, some information about
other latent variables can also be recovered using supervised machine learning.
As discussed in [Section @sec:event_reco], event reconstruction techniques
are used to cluster the raw detector output so the various readouts are
associated with a list of particles produced in the the collision. It
is possible that in the near future the algorithmic reconstruction procedure
might be substituted by supervised learning techniques, training directly
on simulated data to predict the set of latent variables at parton level,
especially given the recent progress with sequences and other non-tabular
data structures. For the time being, machine learning techniques are
instead often used to augment the event reconstruction output, mainly for
particle identification and fine-tuned regression.

The set of physics objects obtained from event reconstruction, when adequately
calibrated using simulation, can estimate effectively a subset of the latent
variables $\boldsymbol{z}$ associated with the resulting parton level
particles, such as their transverse momenta and direction. Due to the
limitations of the hand-crafted algorithms, some
latent information is lost in the standard reconstruction process, particularly
for composite objects such as jets. Supervised machine learning techniques
can be used to regress some of these latent variables, using simulated
data and considering both low-level and high-level features associated
with the relevant reconstructed objects. These information could be used to
complement the reconstruction output for each object and design better
summary statistics, e.g. adding this information as an input to the
classifiers discussed in [Section @sec:sig_vs_bkg].

The details of the application of machine learning techniques
in particle identification and regression
depend on the particle type and the relevant physics case. In the remainder
of this section, the application of new deep learning techniques to jet
tagging within CMS is discussed in more detail. The integration
of deep learning jet taggers with the CMS experiment software
infrastructure was one of the secondary research goals of the project
embodied in this document. Leveraging better machine
learning techniques for jet tagging and regression
could substantially increase the
discovery reach of analyses at the LHC that are based on final states
containing jets, such as the search for Higgs boson pair production
described in [Section @sec:higgs_pair].


#### Deep Learning for Jet Tagging {#sec:deepjet}

The concept of jet tagging, introduced in [Section @sec:jet_btag], is
based on augmenting the information of reconstructed jets based on
their properties to provide additional details about latent variables
associated to the physics object which were not provided by the standard
reconstruction procedure. Heavy flavour tagging, and in particular b-tagging,
is extremely useful to distinguish and select events containing
final states from relevant physical interactions. The efficiency of
b-tagging algorithms in CMS has been gradually improving for each successive
data taking period since the first collisions in 2010. The advance in b-tagging
performance, which was already exemplified by [Figure @fig:CMS_btag_comp],
is mainly
due the combined effect of using additional or more accurate
jet associated information (e.g. secondary vertex reconstruction or lepton
information) and better statistical techniques.

Jet tagging can generally
be posed as a supervised machine learning classification problem.
Let us take for example the case of b-tagging, i.e. distinguishing jets
originating from b-quarks from those originating from lighter quarks
or gluon, which can be framed as binary classification problem: predicting
wether a jet is coming from a b-quark or not
given a set of inputs associated to each jet. The truth label is available
for simulated samples, that can be used to train the classifier. The CSVv2
b-tagging algorithm (and older variants) mentioned in
[Section @sec:jet_btag], is based on the output of
supervised classifiers trained from simulation, the combination of
three shallow neural network combination depending on vertex information
for CSVv2. The CMVAv2 tagger, which is used in the CMS analysis included
in [Section @sec:higgs_pair], is instead based on a boosted decision tree
binary classifier that uses other simpler b-tagger outputs as input. Similar
algorithms based on binary classification have been also developed for
charm quark tagging and double b-quark tagging for large radius jets.

The first attempt to use some of the recent advances in neural networks
(see [Section @sec:ann]) for jet tagging within CMS was commissioned using
2016 data, and it is referred to as DeepCSV tagger. The purpose for
the development for this tagger was to quantify the performance gain
due to the use of deep neural networks for jet tagging in CMS, which
was demonstrated effective using a simplified detector simulation
framework [@Guest:2016iqz; @deOliveira:2015xxd]. Thus, a classifier
based on a 5-layer neural network, each layer with 100 nodes using ReLu
activation functions,
was trained based on the information considered for the CSVv2
tagger. A vector of variables from up to six
charged tracks, one secondary vertex and 12 global variables was
considered as an input, amounting to 66 variables in total. Another
change with respect to previous taggers is that flavour tagging
is posed as a multi-class classification problem, which is
a principled and simple for tacking the various flavour tagging
problems simultaneously.

Five exclusive categories were defined
based different on the generator level hadron information: the
jet contains exactly one B hadron, at least two B hadrons,
exactly one C hadrons and no B hadrons, at least two C hadrons 
and at least two C hadrons and no B hadrons or none of the
defined categories. The softmax operator
(see [Equation @eq:softmax_function]) was used to normalise
the category output as probabilities and construct a loss
function based on cross entropy (see [Equation @eq:general_ce]).
As was shown in [Figure @fig:CMS_btag_comp]
for b-tagging performance, the DeepCSV tagger is considerably better
than CSVv2 for the b-jet efficiency/misidentification range - e.g.
about 25\% more efficient at light jet and gluon mistag rate of $10^{-3}$.
In fact, DeepCSV outperforms the CMVAv2 super-combined tagger,
which uses additional leptonic information.
While not shown in this document, the performance for c-tagging was
found also comparable with dedicated
c-taggers [@Sirunyan:2017ezt].

The very favourable results obtained for DeepCSV motivated the use of
newer machine learning technologies, such as convolutional and
recurrent layers, which were readily available in open-source
software libraries [@chollet2015keras; @tensorflow2015-whitepaper]
as well as advances in hardware (i.e. more powerful GPUs
for training). The large amount of jets available in
simulated data, e.g. in 2016 about $10^9$ $\textrm{t}\bar{\textrm{t}}$
events were simulated for CMS (each with two b-quarks and probably several
light quarks), conceptually justifies the use of more complex machine learning
models because over-fitting is unlikely. Thus, a new multi-class
jet tagger referred to as DeepJet (formerly know as DeepFlavour)
was developed, whose
architecture is depicted in [Figure @fig:DeepJet_schematic], that can be
characterised by a more
involved input structure and both convolutional and recurrent layers.

![Scheme of DeepJet tagger architecture. Four different sets of inputs are
considered: a sequence of charged candidates, a sequence of neutral
candidates, a sequence of secondary vertices and a 15 global variables.
Sequences go first through a series of 1x1 convolution filter that learn a more
compact feature representation and then through a recurrent layer that summarises
the information of the sequence to in a fixed size vector. All the inputs
are then feed to a 7-layer dense network. A total of six exclusive output
categories are
considered depending on the generator-level
components: b, bb, leptonic b, c, light or gluon.
Figure adapted from [@CMS-DP-2018-058].
](gfx/104_chapter_4/DeepJet-schematic.pdf){
#fig:DeepJet_schematic width=90%}

Instead of a fixed input vector, optionally padded with zeroes for the elements
that did not exist (e.g. not reconstructed secondary vertex has been
reconstructed), a complex input object is considered for DeepJet.
Variable-size sequences are directly taken as input
for charged candidates, neutral candidates and secondary vertices; each
element in the sequence characterised by 16, 8 and 12 features respectively.
Each of the three input sequences go through a 3-layers of 1x1 convolutions
in order to obtain a more compact element representation, 8-dimensional for
charged candidates and secondary vertices and 4-dimensional for neutral
candidates. The output of the convolutional layers is connected with a recurrent
layer, which transforms a variable-size input to fixed-size embedding. The
fixed-size outputs after the recurrent layer, as well as a set of 15 global jet
variables, are feed into a 6-layer dense network with 100 (200 for the
first layer) cells with ReLu activation functions per layer.

A total of six mutually exclusive output categories are considered
based on the generator-level
particle content associated to the jet: exactly one B hadron
that does not decay to a lepton,
at least two B hadrons, one hadron B decaying to a soft lepton,
at least one C hadron and no B hadrons, no heavy hadrons but was originated
from a light quark or not heavy hadrons but was originated from a gluon.
This tagger aims to provide gluon-quark discrimination in addition to
b-tagging, c-tagging and double b-tagging. The output probabilities are normalised
by using the softmax operator (see [Equation @eq:softmax_function]).
The training loss function was constructed based on cross entropy
(see [Equation @eq:general_ce]). Additional details regarding
the training procedure and performance are available at [@stoye2017deepjet].

![DeepJet performance. Figure adapted from [@CMS-DP-2018-058].
](gfx/104_chapter_4/DeepJet_SF_30GeV.pdf){
#fig:DeepJet_b_performance width=90%}

