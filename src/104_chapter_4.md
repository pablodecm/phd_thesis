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
be used to address some of the statistical inference and modelling issues from
[Chapter @sec:statinf].

## Problem Description {#sec:problem_description}

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
predicts a label $y \in \{0,...,k-1\}$, denoting correspondence to
one category in a set of of $k$ categories,
for each input $\boldsymbol{x} \in \mathcal{X}$. The task of
classification, in the context of machine learning algorithms, is
to produce classification functions $f(\boldsymbol{x})$ that perform
well on an unobserved set of data.

Classification is often framed as belonging to a larger
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
while the use of structured output tasks is instead
not quite extended. The reconstruction of the set and
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
samples $S'=\{(\boldsymbol{x}_0,\boldsymbol{y}_0),...,(\boldsymbol{x}_{n'},\boldsymbol{y}_{n'})\}$
as follows:
$$
R(f) \approx R_\textrm{S'} = \frac{1}{n'}
\sum_{(\boldsymbol{x}_i,\boldsymbol{y}_i) \in S'} L(\boldsymbol{y}_i,f(\boldsymbol{x}_i))
$$ {#eq:erm}
which is also commonly referred to as *empirical risk*
approximation
$R_\textrm{S'}$(f) based on the set $S'$. The supervised learning
problem can then be stated as one of
finding the function $\hat{f}$ from a class of functions $\mathcal{F}$, which
depends on the particularities of the algorithm, that minimises the empirical
risk over the learning set $S$:
$$
\hat{f} = \mathop{\textrm{arg min}}_{f \in \mathcal{F}} R_S(f)
$$ {#eq:learning_erm}
which is referred to as empirical risk minimisation (ERM) [@vapnik1999overview],
and it is at core of most of the existing learning techniques, such as those
described in [Section @sec:ml_techniques]. However, the ultimate goal of a
learning algorithm is to find a function $f^*$ that minimises the risk
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
on a new set of observations. If the family of functions $\mathcal{F}$ considered
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
of the performance of $f$ on unseen observations.

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
the amount of training data is reduced.

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
by means of cross-validation techniques, in order to select the best
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
function, which was defined in [Equation @eq:indicator].
The zero-one loss is non-differentiable when $y =f(\boldsymbol{x})$
and its gradients are zero elsewhere; in addition, it is not convex,
a property which makes the
minimisation task in [Equation @eq:learning_erm] hard to
tackle by optimisation algorithms. In fact, it can be proven
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
most problem in high-energy physics that can be cast as supervised learning
are ultimate inference problems as will be reviewed in [Section @sec:ml_hep],
it is generally more useful to consider the problem of *soft classification*,
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
prediction output is monotonic with the density ratio between
the probability density functions for each category. Similar results can
be obtained for the Bayes optimal classifier when using other soft
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
the one-dimensional target and prediction as the i=1 elements 
and that $y_0=1-y$ and $\hat{y}_0=1-f(x)$. If the prediction
output is to generally represent exclusive class probabilities, as is the goal of soft
classification, the prediction sum is expected to be one. 
A simple way to ensure the aforementioned property
is to apply a function that ensures that the prediction outputs are in
the range $[0,1]$ and normalised so $\sum_i \hat{y}_i=1$. The *softmax function*
is a common choice to achieving the mentioned
transformation within the field of machine learning. It is a generalisation
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
elsewhere in this work will
be described in detail: boosted decision trees and artificial neural networks.
These families of learning methods are also those that are most commonly used
in machine learning within experimental particle physics, mostly to solve
supervised learning problems, as will be described in [Section @sec:ml_hep].
The overview included here is by no means comprehensive about the mentioned
approaches or alternative popular statistical learning techniques such
as random forests or support vector machines, for which the following references
provided a more extensive review [@friedman2001elements;@Goodfellow-et-al-2016;@louppe2014understanding].

### Boosted Decision Trees {#sec:boosted_decision_trees}

The term *boosted decision trees* (BDT) refers to a large family of
algorithms that are based on additively constructing ensembles of
decision trees for supervised learning tasks
[@freund1997decision ; @friedman2000additive; @friedman2001greedy]
as those described in [Section @sec:supervised].
A subset of these techniques, which is often referred as *gradient boosting*,
are particularly useful for classification and
regression problems. The basis for these methods is that a strong
model can be obtained by combining the outcome of a set of weak
models, e.g. shallow binary decision trees, if they are built
to minimise the residual error at each stage. Gradient boosting
algorithms can be applied to any supervised task as long as it can
be specified by a differentiable loss function, and they
can be understood as *gradient descent* (which will be
discussed in [Section @sec:ann]) in function space [@mason2000boosting].

While it can be applied to other weak learners, gradient boosting
is often used to learn ensembles of decision trees. A decision
tree is hierarchical branched structure that associates
an outcome for each input
$\boldsymbol{x}\in\mathcal{X}$ by means of partitioning
the input space in different disjoint subsets $R = (\mathcal{X}_0,
..., \mathcal{X}_L)$, each associated
with a constant prediction $w_r$ for each leaf. A generic type
of decision trees, which is referred to as classification
and regression trees (CART) [@breiman2017classification] can be expressed
as a function of the input $t(\boldsymbol{x})$ as a sum over
the indicator function $\mathbb{1}_\mathcal{X}^r(\boldsymbol{x})$ 
of each subspace (see [Equation @eq:indicator]) as follows:
$$
t(\boldsymbol{x}) = \sum^{\mathcal{X}_r \in R} w_r \mathbb{1}_{\mathcal{X}_r}(\boldsymbol{x}) 
$$ {#eq:cart_indicator}
where $w_r$ is the outcome for each subspace, noting the summands
will be zero for all subsets $\mathcal{X}^r$ except for one because their
are disjoint. The indicator function $\mathbb{1}_{\mathcal{X}_r}(\boldsymbol{x})$
of a given subspace is specified by a series of binary decisions on a single
feature. If the leaf predictions $w_r$ are categorical, the resulting
model $t(\boldsymbol{x})$ is referred as a classification tree. If
$w_r$ are numerical, $t(\boldsymbol{x})$ is
a regression tree. In the context of gradient boosting, regression
trees are often more useful, even for classification tasks, i.e.
regression trees can be used in conjunction with soft classification
loss functions (e.g. cross entropy). For the rest of this section,
we will then focus on gradient boosting with regression trees.
A schematic representation
of a regression tree is provided in [Figure @fig:tree], which
corresponds to the first tree in the ensemble used for signal
versus background classification in the analysis
described in [Chapter @sec:higgs_pair].

![Graphical representation of a regression tree. At each node that is not
a leaf node, the tree is split in two depending on wether based on
whether a boolean condition is met,
which based on a threshold for the input variable indexed by the number
indicated. This tree corresponds to the first on the ensemble of trees used
for classification in [Chapter @sec:higgs_pair], which was trained
using binary cross entropy as loss function.
](gfx/104_chapter_4/tree.pdf){
#fig:tree width=80%}

Given its structural limitations, a single CART tree of small
maximum depth $d$ performs rather poorly a given supervised
learning task for complex non-linear problems. If $d$ is very large,
the problem of learning an optimal tree based on data is
computationally very demanding, and the resulting model would
not generalise well to unseen data. This motivates the use of tree
ensembles, where the final prediction is composed by the combined
predictions of several small trees. For an ensemble of $K$ CART trees,
the final model prediction $T(\boldsymbol{x})$ can be expressed as:
$$
T(\boldsymbol{x}) = \sum^K_{j=1} t_j(\boldsymbol{x})
$$ {#eq:reg_boosting}
where each $t_j(\boldsymbol{x})$ is a CART model, as
described in [Equation @eq:cart_indicator]. Other regression tree ensembles
based on alternative methods such as bagging [@breiman1996bagging] can
also be expressed by a similar combination of predictions. The learning
problem can be expressed as empirical risk minimisation in the space
of possible tree ensembles over the learning set of labelled observations
$S=\{(\boldsymbol{x}_0,\boldsymbol{y}_0),...,(\boldsymbol{x}_n,\boldsymbol{y}_n)\}$,
as discussed in [Equation @eq:learning_erm]. The total empirical risk
functional $R(T)$ for an ensemble of $K$ trees can usually be written as:
$$
R(T) = \sum_{(\boldsymbol{x}_i,\boldsymbol{y}_i) \in S}
 L(\boldsymbol{y}_i, T(\boldsymbol{x}_i)) + \sum_{j=1}^K \Omega(t_j)
$$ {#eq:total_risk}
where $L(\boldsymbol{y}_i, T(\boldsymbol{x}_i))$ is the preferred loss function
for the task (e.g. binary cross entropy as defined in [Equation @Eq:binary_xe]) and
$\Omega(t_j)$ is a regularisation term that depends on the properties
of each tree and controls the complexity of the model
in order to avoid overfitting.

Because learning the structure and leaf weights $w_r$
of all trees in the ensemble at the same time is intractable,
boosting is based on sequentially
learning trees. At each step, a tree $t_j$ is built to improve over
the previously ensemble of trees $T_{(j-1)}(\boldsymbol{x})$, the prediction for each
observation in the learning set a given step $j$
of the training procedure can then be expressed as:
$$
T_j(\boldsymbol{x}_i) =  T_{(j-1)}(\boldsymbol{x}_i) + t_j(\boldsymbol{x}_i)
$$ {#eq:pred_step_tree}
which can be used to redefine the equivalent risk from [Equation @eq:total_risk]
at each training step, where the tree $t_j(\boldsymbol{x})$ is being created as:
$$
R(T_j) = \sum_{(\boldsymbol{x}_i,\boldsymbol{y}_i) \in S}
 L(\boldsymbol{y}_i, T_{(j-1)}(\boldsymbol{x}_i) + t_j(\boldsymbol{x}_i)) + \sum_{j=1}^K \Omega(t_j)
$$ {#eq:seq_risk}
where the loss $L(\boldsymbol{y}_i, T_{(j-1)}(\boldsymbol{x}_i)$ can be expanded
as a Taylor series assuming that at the step $j$ the ensemble $T_{(j-1)}(\boldsymbol{x})$ is
constant. Omitting constant terms, which do not play any role in risk
minimisation, the risk at a given training step can be expressed as:
$$
\begin{aligned}
R(T_j)  \sim \sum_{(\boldsymbol{x}_i,\boldsymbol{y}_i) \in S} \bigg( &
\underbrace{\frac{ \partial L(\boldsymbol{y}_i, T_{(j-1)}(\boldsymbol{x}_i))}{
\partial T_{(j-1)}(\boldsymbol{x}_i)}}_{g_i} t_j(\boldsymbol{x}_i)  \\ &+ 
\frac{1}{2} \underbrace{\frac{\partial^2 L(\boldsymbol{y}_i, T_{(j-1)}(\boldsymbol{x}_i))}{
\partial T^{2}_{(j-1)}(\boldsymbol{x}_i)}}_{h_i} t_j^2(\boldsymbol{x}_i) \bigg)
 + \Omega(t_j)
\end{aligned}
$$ {#eq:risk_opt}
where $g_i$ and $h_i$ are so-called gradient statistics, computed
using the first and second partial derivatives of the loss
function with respect to the ensemble prediction at the previous step
$T_{(j-1)}(\boldsymbol{x}_i)$. At each step the learning problem
can then be reduced to choosing a tree structure and weights, characterised
by the function $t_j$, that minimises $R(T_j)$. This
technique can therefore be applied to any supervised learning tasks as long
the associated loss function is differentiable.

A common regularisation term, that is used by the [xgboost]{.smallcaps}
library [@chen2016xgboost]
used for training the classifier in [Chapter @sec:higgs_pair], is
a combination of the number of leaves $L$ and the squared sum of the leaf
weights $w_r$ for all the leaves:
$$
\Omega(t_j) = \gamma L + \frac{1}{2} \lambda\sum^{\mathcal{X}_r\in R} w_r^2
$$ {#eq:regulatisation}
where $\gamma$ and $\lambda$ are constants that regulate the relative importance
of each regularisation component. Using the previous regularisation term,
it is possible to redefine the risk of a given tree structure
and set of leaf weight at given training step as:
$$
 R(T_j)  \sim \sum^{\mathcal{X}_r \in R} \left (
 w_r \underbrace{\sum^{\boldsymbol{x}_i \in S} g_i \mathbb{1}_{\mathcal{X}_r}(\boldsymbol{x}_i)}_{G_r}
 + \frac{1}{2} w^2_r \underbrace{\sum^{\boldsymbol{x}_i \in S} ( h_i + \lambda ) \mathbb{1}_{\mathcal{X}_r}(\boldsymbol{x}_i)}_{H_r + \lambda}
 \right ) + \gamma L
$$ {#eq:tree_risk_redef}
where $G_r$ and $H_r$ represent the sum of $g_i$ and $h_i$ over all the
samples in the learning set that correspond to the leaf indexed by $r$.
The previous expression can in turn be used to obtain the optimal leaf weight
$w_r^{\star}$ and simplify the risk at a given step as follows:
$$
w_r^{\star} = - \frac{G_r}{H_r + \lambda} \Rightarrow  R(T_j) = - \frac{1}{2}
\sum^{\mathcal{X}_r \in R} \frac{G^2_r}{H_j + \lambda} + \gamma T
$$ {#eq:opt_weight_risk}
where $\mathcal{X}_r$ are the subsets of the input space corresponding to each leaf
of the last tree $j$. The last expression for $R(T_j)$ can be used to
compare tree structures to be added to the ensemble in a principled manner.

In practice, the number of possible tree structures is infinite so the
problem of finding the optimal tree at each step is still intractable.
A greedy heuristic is instead used, which proceeds one level of the tree
at time. For each input feature, the optimal splitting at a given
level can be found by maximising the splitting gain, which can be done
very efficiently by sorting the observations in that feature and finding
the threshold that maximises the gain $\mathcal{G}$,
that is defined as:
$$
\mathcal{G} = \frac{1}{2} \left( \frac{G_L}{H_L + \lambda}  +
  \frac{G_R}{H_R + \lambda}
  - \frac{(G_L+G_R)^2}{H_L + H_R + \lambda} \right) + \gamma
$$ {#eq:tree_gain}
where $G_L$ and $H_L$ are the sum of gradient statistics
left of the threshold and $G_R$ and $H_R$ are those
right of the threshold. If the gain is negative for the whole, no splitting
is preferred in the considered features. Once the optimal splitting
is determined for all the features, the featurs that provides the
minimal risk as defined in [Equation @eq:opt_weight_risk] is chosen. The
algorithm then proceeds to the next tree level until the maximum tree depth
is reached or any additional splitting degrades the performance.

Boosted tree ensembles are prone to overfitting to the learning set, so
additional heuristics are often used to improve generalisation. A common
approach after each step that produces a tree $t_j$
by the procedure outlined before, is to define ensemble for the next step
by weighting the constribution from the last three
 $T_j(\boldsymbol{x}_i) =  T_{(j-1)}(\boldsymbol{x}_i) + \eta\, t_j(\boldsymbol{x}_i)$,
where $\eta$ is referred as learning rate or shrinkage. The use of $\eta<1$ produces
a less efficient learning procedure, so additional trees are
required in the ensemble, however the resulting model is less prone to overfitting.
Other policies against overfitting include subsampling the set of observations
or the feature
vector dimensions. Early stopping, as defined in [Section @sec:supervised],
can also be trivially applied to boosted tree ensembles simply by leaving
out the last $n$ trees in the summation so the risk over validation set is
maximised.

\FloatBarrier

### Artificial Neural Networks {#sec:ann}

An alternative way to carry out empirical risk minimisation is
based on consider function $f(\boldsymbol{x}; \boldsymbol{\phi})$,
which depends on a vector of parameters $\boldsymbol{\phi}$, and
attempt to find the values of $\boldsymbol{\phi}$ that minimise
the risk $R_S(f)$ over the learning set
 $S=\{(\boldsymbol{x}_0,\boldsymbol{y}_0),...,
 (\boldsymbol{x}_n,\boldsymbol{y}_n)\}$. If
$f(\boldsymbol{x}; \boldsymbol{\phi})$ is differentiable with
respect to the parameter vector $\boldsymbol{\phi}$,
the minimisation from [Equation @eq:learning_rm],
can be attempted with gradient-based methods. The simplest
gradient-based optimisation technique is referred to as *gradient descent* (GD),
and can be applied to the previous problem by initialising
the parameter vector at random $\boldsymbol{\phi}^0$ and then iteratively
updating the model parameters $\boldsymbol{\phi}$ at each step $t$
according to:
$$
\boldsymbol{\phi}^{t+1} =
\eta(t) \nabla_{\boldsymbol{\phi}} R_S(\boldsymbol{\phi}^t) =
\eta(t) \nabla_{\boldsymbol{\phi}}
\frac{1}{n}
\sum_{(\boldsymbol{x}_i,\boldsymbol{y}_i) \in S}
\left ( L(\boldsymbol{y}_i,f(\boldsymbol{x}_i; \boldsymbol{\phi}^t)) +
\Omega(\boldsymbol{\phi}^t) \right )
$$ {#eq:gradient_descent}
where $\nabla_{\boldsymbol{\phi}}$ is the gradient operator with
respect the model parameters, $\eta(t)$ is the learning
rate or step size and $\Omega(\boldsymbol{\phi})$ is
a generic generalisation term added to the loss to constrain
model complexity. Many other gradient-based optimisation
methods exist [@NoceWrig06], e.g. using second-order derivative information.
The previous flavour of gradient descent is often referred
as batch gradient descent, because the whole learning set $S$ is
used to compute the parameter updates at each step. Batch gradient descent
can be very computationally demanding when the number of observations
in $S$ is large and the computation of the gradient of the loss
for each labelled observation
is costly. In addition, batch gradient descent is a deterministic
optimisation method and likely to get stuck at a local minima
if the optimisation surface is non-convex.

A variation of the previous technique, that is referred to as stochastic
gradient descent (SGD)
[@robbins1951stochastic], overcomes
the mentioned issues by using a random subset $B=\{(\boldsymbol{x}_0,\boldsymbol{y}_0),...,
(\boldsymbol{x}_m,\boldsymbol{y}_m)\}$ of $m$ observations from
the training set $S$ at each step. If $m$ is small the updates can
be computed much faster, the trade-off being more noisy estimates of
$\mathbb{E}_{(\boldsymbol{x}_i,\boldsymbol{y}_i) \in S}
\nabla_{\boldsymbol{\phi}} \left [
L(\boldsymbol{y}_i,f(\boldsymbol{x}_i; \boldsymbol{\phi}^t) \right ]$. The
parameter update rule from [Equation @eq:gradient_descent] in SGD can be instead
be expressed as:
$$
\boldsymbol{\phi}^{t+1} =
\eta(t) \nabla_{\boldsymbol{\phi}} R_S(\boldsymbol{\phi}^t) =
\eta(t) \nabla_{\boldsymbol{\phi}}
\frac{1}{m}
\sum_{(\boldsymbol{x}_i,\boldsymbol{y}_i) \in B }
\left ( L(\boldsymbol{y}_i,f(\boldsymbol{x}_i; \boldsymbol{\phi}^t)) +
\Omega(\boldsymbol{\phi}^t) \right )
$$ {#eq:sgd}
where $B$ is a random subset of size $m$ of the learning set $S$. In the
original formulation $m=1$, yet nowadays a larger value for $m$ is often used
in what is referred to as mini-batch SGD to obtain balance the estimate noise
and take advantage of vectorised computations. Several variations of SGD
exist, which in some cases can provide convergence advantages over the
previous update rule by using adaptive learning rates or momentum in
the update dynamics [@ruder2016overview]. Stochastic gradient descent methods
are a key element for training complex differentiate machine models
$f(\boldsymbol{x}; \boldsymbol{\phi})$ as
artificial neural networks, which will be discussed in the rest
of this section. SGD in combination with a non-decomposable loss
function is also used in [Chapter @sec:inferno] to learn inference-aware
summary statistics.

A particularly promising family of parametric functions
$f(\boldsymbol{x}; \boldsymbol{\phi})$ is referred
to as *artificial neural networks*. Artificial neural networks
are differentiable functions based on the composition
of simple (and possibly non-linear) operations. The simplest type
of artificial neural network is depicted in [Figure @fig:neural_network],
which is referred as *feed-forward neural network*, that maps a input
$\boldsymbol{x}$ to an output $\boldsymbol{y}$ by means of a series
of forward transformations, referred as neural network layers.
In the simplest configuration, the values at a given layer $k$ other
than the input layer can be computed as non-linear transformation
of the result of a linear combination of the
output of the previous layer after the addition of a bias term. The previous
transformation can be expressed very compactly in matrix form as:
$$
\boldsymbol{a}^k =
g( (\boldsymbol{W}^k)^T \boldsymbol{a}^{k-1} + \boldsymbol{b}^k)
$$ {#eq:layer_trans}
where $\boldsymbol{a}^k$ is the outcome in vector notation
after the layer transformation, $\boldsymbol{a}^{k-1}$ is the vector of values
from the previous transformation (or $\boldsymbol{a}^0=\boldsymbol{x}$ if
it is the first layer after the input), $\boldsymbol{W}^k$ a matrix with
all the linear combination coefficients and $\boldsymbol{b}^k$ is
the bias vector that is added after linear combination. The activation function
$g(\boldsymbol{z})$ is applied element-wise, and it is often based on a simple
non-linear function. The sigmoid function $\sigma(z)=1/(1+e^{z})$
used to be a common choice for the activation function, but nowadays
the rectified linear unit  (ReLU) function  $g(\boldsymbol{z})=\max(0,z)$ and
its variants are most frequently used instead.

![Graphical representation of a feed-forward neural network
with two hidden layers,
which is a function mapping and input $\boldsymbol{x}$ to an output
$\boldsymbol{y}$ by means simple non-linear transformations. The output
value of a node each layer (other than the input layer) is the result
of applying an activation function $g$ to a linear
combination of the previous layer outputs plus possibly a bias term.
](gfx/104_chapter_4/neural_network.pdf){
#fig:neural_network width=80%}

The full feed-forward model $f(\boldsymbol{x}; \boldsymbol{\phi})$ is
based on the composition of transformation of the type described in
[Equation @eq:layer_trans]. When a single transformation is applied,
i.e. $\boldsymbol{y} = g( (\boldsymbol{W})^T \boldsymbol{x} + \boldsymbol{b})$,
the model can be referred to as perceptron. If the model is instead based
on the composition of several transformations, it can also be called
multi-layer perceptron (MLP), and each of the intermediate
transformations (which can be composed by an arbitrary number of
computational units) is referred as hidden layers. The model in
[Figure @fig:neural_network] is a MLP. The advantage of using models
based on feed-forward neural networks with hidden layers is that
they can be used to model any arbitrary function due to the universal
approximation theorem [@cybenko1989approximation]. In fact, while
it is still the focus of theoretical research, the use of a large
number of hidden layers is found to increase the expressivity
and facilitate the training of powerful neural network models. The
experimental success of these family techniques has led to the
concept of *deep learning*,
where multiple transformations layers are used for learning
data representations in many learning tasks.
 
A good choice for depth and overall structure for a neural network
model depends on the problem at hand as well as the characteristics and size
of the learning set available, thus it frequently has to be defined
by trial-and-error, based on the performance on a validation
set as discussed in [Equation @sec:supervised]. The output size and choice
of activation function in the last transformation often
depends on the task at hand. For binary classification
classification tasks, it is practical to use the sigmoid function
$\sigma(z)=1/(1+e^{z})$ as the activation function of the last layer,
in combination with a loss function for soft classification (e.g.
binary cross entropy from [Equation @eq:binary_xe]). For
multi-class classification problems, such as the one discussed
in [Section @sec:deepjet], the size of the output vector usually matches
the number of the categories given that the softmax function (see
[Equation @eq:softmax_function])
is often used in the last layer to approximate conditional
class probabilities in combination with a cross
entropy loss (see [Equation @eq:general_ce]). For learning tasks
different from classification, different output structures
and constraints might be used, e.g. the output vector size
in the use case in [Chapter @sec:inferno] corresponds to the
number of dimensions of the resulting summary statistic, that is
based on a transformation of the input using a multi-layer neural network.

The SDG update rule from [Equation @eq:sgd] requires
the computation of the gradients of the loss function with
respect to the model parameters. For complex models, e.g.
those put together by stacking layers as those described in
[Equation @eq:layer_trans], the computation of derivatives
by numerical finite differences or symbolic differentiation
may become rather challenging.
The former requires the evaluation of the loss function after variations
for at least twice the number of parameters and are affected
by round-off and truncation errors, and a naive use of the later
could instead lead to very large expressions for the exact derivative
that cannot be easily simplified. Given that a numerical function
as implemented in a computer program is a sequence of simple operations
(e.g. addition, subtraction, exponentiation, etc.), it is possible to
efficiently obtain gradients and other derivatives by applying the chain rule
repeatedly based on the structure of the program, the derivatives of the
simple operations and a record of the intermediate values.

The previous
family of techniques, which will not be discussed in depth in this work,
are referred as *automatic differentiation* (AD) [@baydin2018automatic].
The most efficient
way of computing the gradients of a one-dimensional function
that depends on many parameters, as the gradient of the
empirical risk for a batch of observations from [Equation @eq:sgd]
is by means of reverse-mode automatic differentiation, which is also
referred to as the *backpropagation* in the context of
neural network training. The computational cost of computing the full
gradient of the loss to numerical precision
using backpropagation is of the same order than
a single forward evaluation of the loss, which provides a great advantage
relative to finite differences. In addition, when implemented in a computation
framework, it can be generally applied to any
numerical function as long as can be expressed as a computational graph,
e.g. an arbitrary program containing control flow statements, without
requiring complex expression simplification as would be the case for
symbolic differentiation. In fact, modern computational
that include automatic differenciation such as [TensorFlow]{.smallcaps}
[@tensorflow2015-whitepaper]
or [PyTorch]{.smallcaps} [@paszke2017automatic] may also be used to compute
higher-order gradients (e.g. Hessian matrix elements),
which are useful in [Chapter @sec:inferno] to build a differentiable
approximation the covariance matrix based on a summary statistic.

As mentioned before, reverse mode automatic differentiation can be
used to computed the gradients of an arbitrary function as long
as it can be represented as a computational graph containing
differentiable simple operations. Thus the neural network
model $f(\boldsymbol{x}; \boldsymbol{\phi})$ is not
restricted to the composition of layers of the
type described in [Equation @eq:layer_trans], which are often
referred as fully connected or dense layers. Alternative function
components are useful for dealing with data cannot be represented
by a fixed-length vector [@Goodfellow-et-al-2016], e.g. convolutional layers
are often useful for working with 2D images while recurrent layers extend the
application of neural networks to sequences that vary in length between
observations. Both convolutional and recurrent layers are used in the
neural network model for jet flavour-tagging described in
[Section @sec:deepjet]. Other differentiable neural network
components have also been developed to deal with permutation
invariant sets [@zaheer2017deep] or graphs [@henrion2017neural]
as input data structures, which could have promising applications
in particle collider experiments analyses.

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

The mixture structure of the statistical model for the outcome
of collisions,
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
would be trained to optimise the classification objective for
different distributions.

To understand the role of classification in the larger goal of statistical
inference of a subset of parameters of interest in a mixture model,
let us consider the general problem of inference for a two-component
mixture problem. One of the components will be denoted as signal
$p_s(\boldsymbol{x}| \boldsymbol{\theta})$ and the other as background
$p_b(\boldsymbol{x} | \boldsymbol{\theta})$, where  $\boldsymbol{\theta}$
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
most of the parameters of interest in analyses at the LHC, such as cross
sections, are proportional to the mixture coefficient of the signal
in the statistical model.
The results presented here would also be also be valid if alternative mixture
coefficient parametrisations such as the one considered in [Section @sec:synthetic_mixture] are used, e.g. $\mu=s/(s+b)$ where $s$ and $b$
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
from each category in the training dataset - i.e. equal to 1 if the latter is
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
a simple transformation, yet the mixture structure of the problem allows
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
(1-\mu) \left ( \frac{p_\textrm{s}(\boldsymbol{x}| \boldsymbol{\theta})}{
                          p_\textrm{b}(\boldsymbol{x}| \boldsymbol{\theta})}-1 \right)
$$ {#eq:lr_two}
thus each factor in the likelihood ratio is a bijective function of
the ratio
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
is used instead of $s_{s/ b} (\boldsymbol{x})$.
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
in practice in [Chapter @sec:inferno], where a new technique is proposed to
construct summary statistics, that is not based on classification,
but accounts for the effect of nuisance parameters is presented.


### Particle Identification and Regression {#eq:particle_id_reg}

While the categorical latent variable $z_i$, denoting the interaction
process that occurred in a given collision, is very useful to define an event
selection or directly as a summary statistic, information about
other latent variables can also be recovered using supervised machine learning.
As discussed in [Section @sec:event_reco], event reconstruction techniques
are used to cluster the raw detector output so the various readouts are
associated with a list of particles produced in the collision. It
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
limitations of the hand-crafted algorithms used, some
latent information is lost in the standard reconstruction process, particularly
for composite objects such as jets. Supervised machine learning techniques
can be used to regress some of these latent variables, using simulated
data and considering both low-level and high-level features associated
with the relevant reconstructed objects. This information could be used to
complement the reconstruction output for each object and design better
summary statistics, e.g. adding it as an input to the
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
for simulated samples, which are used to train the classifier. The CSVv2
b-tagging algorithm (and older variants) mentioned in
[Section @sec:jet_btag] is based on the output of
supervised classifiers trained from simulation, i.e. the combination of
three shallow neural network combination depending on vertex information
for CSVv2. The CMVAv2 tagger, which is used in the CMS analysis included
in [Section @sec:higgs_pair], is instead based on a boosted decision tree
binary classifier that uses other simpler b-tagging algorithm outputs as input.
Similar
algorithms based on binary classification have been also developed for
charm quark tagging and double b-quark tagging for large radius jets.

The first attempt to use some of the recent advances in neural networks
(see [Section @sec:ann]) for jet tagging within CMS was commissioned using
2016 data, and it is referred to as DeepCSV tagger. The purpose for
the development of this tagger was to quantify the performance gain
due to the use of deep neural networks for jet tagging in CMS, which
was demonstrated effective using a simplified detector simulation
framework [@Guest:2016iqz; @deOliveira:2015xxd]. Thus, a classifier
based on a 5-layer neural network, each layer with 100 nodes using ReLU
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
based different on the generator level hadron information[^flavour]: the
jet contains exactly one B hadron, at least two B hadrons,
exactly one C hadrons and no B hadrons, at least two C hadrons and no B hadrons,
or none of the previously
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

[^flavour]: Here by B and C hadrons we refer to hadrons containing b-quarks
  c-quarks as valence quarks respectively,
  which often have a lifetime large enough
  to fly away from the primary vertex as discussed in [Section @sec:jet_btag].

The very favourable results obtained for DeepCSV motivated the use of
newer machine learning technologies, such as convolutional and
recurrent layers, which were readily available in open-source
software libraries [@chollet2015keras; @tensorflow2015-whitepaper],
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
first layer) cells with ReLU activation functions per layer.

A total of six mutually exclusive output categories are considered
based on the generator-level
particle content associated to the jet:

- *b* - exactly one B hadron that does not decay to a lepton.
- *bb* - at least two B hadrons.
- *lepb* - one hadron B decaying to a soft lepton
- *c* - at least one C hadron and no B hadrons
- *l* - no heavy hadrons but originated from a light quark
- *g* - no heavy hadrons but was originated from a gluon.

The DeepJet tagger aims to provide gluon-quark discrimination in addition to
b-tagging, c-tagging and double b-tagging. The output probabilities are normalised
by using the softmax operator (see [Equation @eq:softmax_function]).
The training loss function was constructed based on cross entropy
(see [Equation @eq:general_ce]). Additional details regarding
the architecture and training procedure are available
at [@stoye2017deepjet].

The b-tagging performance of DeepJet, by means of the misidentification versus
efficiency curve compared with the DeepCSV tagger, is shown in
[Figure @fig:DeepJet_b_performance]. The additional model complexity and
input variables lead to a clear performance improvement, about a 20\%
additional efficiency at a mistag rate of $10^{-3}$ for light quark
and gluon originated jets. Larger relative enhancements with respect
to DeepCSV are seen for b-jet versus c-jet identification. The performance
for c-tagging and quark-gluon discrimination is slightly improved
in comparison with dedicated approaches, with the advantage of using
a single model for all the flavour tagging variations. The expected
relative performance boost, especially when compared non deep learning
based taggers (CSVv2 or CMVA) can increase significantly the discovery
potential for analyses targeting final states containing several b-tagged jets,
such as the one presented in [Chapter @sec:higgs_pair]. In addition similar
model architectures have since been successfully applied to large radius
jet tagging [@CMS-DP-2018-046]
and could be also extended to other jet related tasks, as providing
a better jet momenta estimation by means
of a regression output.

![Misidentification probability (in log scale) for jets originating
from c quarks (dashed lines) or light quarks and gluons (solid lines)
as a function of the b-tagging efficiency for both DeepCSV
and DeepJet taggers. The corrected mistag/efficiency and its uncertainty
for the loose, medium and tight working points are also included.
Figure adapted from [@CMS-DP-2018-058].
](gfx/104_chapter_4/DeepJet_SF_30GeV.pdf){
#fig:DeepJet_b_performance width=90%}

While both advances in model architecture and the addition of input features allow
notable jet tagging performance gains, they can complicate the integration
of these tools within the CMS experiment software framework [@innocente2001cms],
which is
often referred as [CMSSW]{.smallcaps}. Training and performance evaluation
of both DeepCSV and DeepJet was carried out using the
[Keras]{.smallcaps} [@chollet2015keras] and [TensorFlow]{.smallcaps}
[@tensorflow2015-whitepaper] open-source libraries. In order to
integrate jet tagging models in the standard CMS reconstruction sequence,
which has rather stringent CPU and memory requirements per event
because it is run for both acquired and simulated data in commodity hardware in
a distributed manner around the world in the LHC computing grid [@bird2005lhc].
In addition,
the [lwtnn]{.smallcaps} open-source library [@daniel_hay_guest_2018_1482645],
a low-overhead C++ based interface used for the integration of DeepCSV
did not support multi-input models with recurrent layers at the time.

An alternative path to integrate DeepJet into production was thus required. Given
than [TensorFlow]{.smallcaps} backend is based on the C++ programming
language and a basic interface to evaluating training was also provided,
the direct evaluation of machine learning model using its
native [TensorFlow]{.smallcaps} backend was chosen as the best alternative.
In addition, this way the integration effort and basic interface
developed could be re-used in future deep learning use cases in the CMS
experiment (e.g. large radius jet tagging), leading to
the development of the CMSSSW-DNN module [@marcel_cmssw]. The integration process
was made more challenging due to the difficulty recovering the same
features at reconstruction level, the strict memory requirements and
multi-threading conflicts. After resolving all the mentioned issues
[@pablodecm_deepjet], the
output of the DeepJet model at production was verified to match that of the
training framework [@markus_deepjet] to numerical precision. The successful
integration, that is currently in use, facilitated the measurement of DeepJet
b-tagging performance on data for the main discriminator working points,
as shown in [Figure @fig:DeepJet_b_performance].


