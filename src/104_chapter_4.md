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
$L = \{(\boldsymbol{x}_0,\boldsymbol{y}_0),...,(\boldsymbol{x}_n,\boldsymbol{y}_n)\}$.
The output values $\boldsymbol{y}$ are known in the learning set, because they
were previously determined by an external method, typically a teacher
or supervisor looking at past observations, thus explaining the name of these
family of techniques. From an statistical standpoint, the input observations
and target values from the learning set can be viewed as
random variables sampled from an joint probability distribution
$p(\boldsymbol{x}, \boldsymbol{y})$, which is typically unknown.

The goal of supervised learning is not to perform well on the learning set $L$
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
can be casted as a supervised learning problem. The learning set would consist
on simulated observations $\boldsymbol{x}_i$ (or a summary of it
$\boldsymbol{s}(\boldsymbol{x}_i)$), and a matching subset of interest of the
latent variables $\boldsymbol{y}_i \in \mathcal{Y} \subseteq \mathcal{Z}$.
The supervised
learning task can then be viewed as the estimation of the conditional
expectation value
$\mathbb{E}_{p(\boldsymbol{y} | \boldsymbol{x} = \boldsymbol{x}_i)} [\boldsymbol{y}]$
for each given input observation  $\boldsymbol{x}_i$.

<!-- regression, structured output and density estimation -->


## Machine Learning Techniques {#sec:ml_tecniques}

### Boosted Decision Trees

### Artificial Neural Networks

## Applications in High Energy Physics {#sec:ml_hep}
