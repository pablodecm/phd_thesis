# Machine Learning in High-Energy Physics {#sec:machine_learning}

\epigraph{Computers are useless. \\ They can
  only give you answers.}{Pablo Picasso}

Machine learning is an interdisciplinary field that deals with the
general problem of how
computers can automatically improve at certain tasks given data. The usefulness
and range of applicability of such techniques has surged in the last
decades due to the increase on accessible computational power and
the amount of useful data available. In this section, a general overview of
machine learning methods as well as the main tasks that can addressed with them
will be provided. Subsequently, the technical basis of two specific types of
tools used in the next chapters will be explored: boosted
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

### Probabilistic Classification and Regression

One of the most unassuming, yet versatile, tasks that can be addressed with
machine learning algorithms is *classification*. A classifier or a
classification rule is a function
$f(\boldsymbol{x}) : \mathcal{X} \longrightarrow \mathcal{Y}$ that
predicts a label $y \in \{0,...,k-1\}$, denoting correspondance to
on category in a set of of $k$ categories,
for each input $\boldsymbol{x} \in \mathcal{X}$. The task of
classification, in the context of machine learning algorithms, is
to produce classification functions $f(\boldsymbol{x})$ that perform
increasingly well on a set of data.

Classification is hence often framed as a belonging to a larger
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

From an statistical standpoint, the input observations
and target values from the learning set can be viewed as
random variables sampled from an joint probability distribution
$p(\boldsymbol{x}, \boldsymbol{y})$, which is typically unknown.
The family of supervised learning tasks also includes *regression*, which amounts
construct a $f(\boldsymbol{x})$ that can to predict a numerical
target output $\boldsymbol{y}$, and *structured output* tasks where the output
vector $\boldsymbol{y}$ is a vector or a complex data structure where its
elements are tightly interrelated. As will be reviewed in [Section @sec:ml_hep],
most analysis problems amenable by machine learning  in high-energy
physics experiments are framed as classification and regression tasks,
while the use of structured of structured output task is instead
not quite extensive. The reconstruction of the set and
properties of physical objects in an event directly from
the detector readout could be framed as a structured output task, if it
was to be approached directly using machine learning algorithms
instead of the procedures described in [Section @sec:event_reco].

The goal of supervised learning is not to perform well on the learning set $S$
used for improving at the specified task, but rather to perform well
for additional unseen observations sampled from the joint distribution
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
can be casted as a supervised learning problem. The learning set $S$ would consist
on simulated observations $\boldsymbol{x}_i$ (or a summary of it
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
where $L$ is a *loss function*, that quantifies the discrepancy between
the true output and the prediction. The quantity defined in
[Equation @eq:exp_pred_err]
is often also referred to as *risk*,
*test error*,  or also as *generalisation error*.
The optimal model for a given task $T$, thus depends on the definition
of its loss function $L$, if the objective is minimising the
expected prediction error. In practice, the expected prediction
error cannot be estimated
analytically because $p(\boldsymbol{x}, \boldsymbol{y})$ is not
unknown, or not tractable in the case of a generative simulation model. The
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
problem can be then be stated as
finding the function $\hat{f}$ from a class of functions $\mathcal{F}$, which
depends on the particularities of the algorithm, that minimises the empirical
risk over the learning set $S$:
$$
\hat{f} = \textrm{arg min}_{f \in \mathcal{F}} R_S(f)
$$ {#eq:learning_erm}
which is referred to as empirical risk minimisation (ERM) [@vapnik1999overview],
and it is at core of most of the existing learning techniques, such as those
described in [Section @sec:ml_techniques]. However, the ultimate goal of an
learning algorithm is to find a function $f*$ that minimises the risk
or expected prediction error $R(f)$:
$$
f^* = \textrm{arg min}_{f \in \mathcal{F}} R(f)
$$ {#eq:learning_rm}
where $R(f)$ is the quantity defined in [Equation @eq:exp_pred_err], corresponding
to the generalisation error, or average expected performance on unseen observations
sampled from $p(\boldsymbol{x}, \boldsymbol{y})$.

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
is often referred as *over-fitting*.

To compare different prediction functions or to realistically evaluate the
generalised performance of a given prediction model $f$, it is useful to
being able to compute unbiased estimates of $R(f)$. The simplest way to
obtain such estimate is to divide the learning set $S$ in two disjoint
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

Another important concept for most machine learning techniques, is that of
*hyper-parameters*. The majority of machine learning algorithms depend on
a set of parameters that regulate the flexibility of the family
of functions $\mathcal{F}$ to consider for empirical risk minimisation as
well as the details of the optimisation followed to solve the task
presented in [Equation @eq:learning_erm]. The expected performance of a given
model depends on these parameters, however their optimal value depends on the
particularities of the data (e.g. number of input dimensions or number
of size of the data size). This motivates the notion of *hyper-parameter
optimisation*, where the performance of the various choices of
hyper-parameters on the validation set or by mean of cross-validation
techniques, in order to select the best configuration.



## Machine Learning Techniques {#sec:ml_techniques}

### Boosted Decision Trees

### Artificial Neural Networks

## Applications in High Energy Physics {#sec:ml_hep}
