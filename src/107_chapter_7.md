
# Conclusions and Prospects {#sec:conclusions}

\epigraph{So Long,\\ and Thanks for All the Fish.}{Douglas Adams}

A large part of this thesis has dealt with the role of statistical
learning techniques in the context of particle collider analyses,
and their usefulness from a statistical inference perspective. After a broad
introduction to the theoretical models of fundamental interactions and a summary of
the main characteristics and working principles of the Compact Muon Solenoid (CMS)
detector at the Large Hadron Collider (LHC), the fundamentals for statistical
modelling at the LHC has been discussed. The relation between the
theoretical parameters of interest and the experimental observations
can only be modelled accurately by means of a complex simulation chain
of the underlying physical processes and expected detector response. The
generative-only nature of the simulation-based model combined with its
high dimensionality make the definition of the probability density
or likelihood function intractable, thus classical inference techniques
cannot be applied to carry out statistical inference based on the
acquired observations.

The statistical model for particle colliders can be described
by a mixture model, each mixture component originating
from a group of fundamental physical interactions.
The latent variable structure of
the generative model can be mapped to the different simulation
steps in the simulation: process type, parton-level four-momenta,
parton-shower outcome and detector readout. While the dimensionality
of the latent space greatly increases for each
subsequent step, the joint distribution can be factorised as
a product of conditionals, the information about the parameters
of interest being compactly expressed by the lowest dimensional latent
variables. An efficient way to reduce the dimensionality of the data
is thus to approximate the latent variables using the observations. This
can be done by a well-calibrated combination of the different detector
readouts, as is the case when using event reconstruction is
performed, or
by directly estimating the latent variables using supervised learning
techniques trained on simulated observations.

Recent advances in supervised learning techniques have led to more accurate
latent variable estimation that can scale to more data and use advanced non-linear
transformations to obtain better performance in complex tasks,
both in the context of classification and regression. Signal versus background
probabilistic classification, a common conceptual framework
for simplifying the event selection
problem and constructing low-dimensional summaries in high-energy physics,
has been formally proven
to produce sufficient summary statistics for the mixture coefficients
when the generative model is fully defined. The usefulness of probabilistic
classification for such tasks, even in the optimal classifier case, cannot
be guaranteed when nuisance parameters affect significantly the distribution
of observed samples. In addition, particle identification and regression
problems that augment the reconstruction output and can be tackled with machine
learning techniques are also discussed. The use of deep learning
techniques for advanced jet flavour tagging in CMS are used to exemplify
the previous use case, which demonstrates the possible performance improvements
due to the combined use of deep neural networks and non-standard input
transformations that can deal with sequences. Newer machine learning
methodologies that can
deal with sets, graphs and other types of non-vector input coupled
with powerful parallel hardware could be a promising path to substitute
a larger part of the event reconstruction chain by latent variable
approximations based on simulated observations, providing higher
accuracy and throughput than hand-tuned algorithms.

An analysis using $35.9\ \textrm{fb}^{-1}$ of data
collected in 2016 by the CMS detector at the LHC was also included in this
work. Proton-proton collisions at a centre-of-mass energy of 13 TeV were
used to study the $\textrm{pp} \rightarrow \textrm{HH} \rightarrow
\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$
process in the context of the Standard Model (SM) and anomalous
couplings effective field theory (EFT) extensions.
The main challenge for this LHC analysis was the large background
contribution from multi-jet QCD processes, so numerous that
could not be modelled accurately by simulated observations. Hence,
a data-driven estimation method, referred to as hemisphere mixing, was
developed and validated on control regions to model the background
contribution. The final summary statistic used in the analysis
is based on the output of a probabilistic classifier, an
ensemble of gradient boosted decision trees, trained using
simulated signal observations and artificial events produced by
the background estimation method. After assessing the different
sources of systematic uncertainties and including their effect
in the statistical model, a median expected limit obtained for
SM HH production of $419\ \textrm{fb}$ was obtained,
which corresponds to approximately 37 times the SM expectation.
The observed limit obtained is $847\ \textrm{fb}$, which
is about two standard deviations above the expected limit. Limits were
also obtained for a set of EFT benchmarks, which summarise the kinematical
properties of a large space of EFT models. The results of the
combination of this analysis with other HH decay channels were also included.
The estimation of QCD multijet backgrounds will likely remain an
important issue for
future jet-based analysis at the LHC, given that the biases of the
data-driven estimation methods would become increasingly relevant as more
data is available.

The ultimate goal of LHC analyses is statistical inference, in the form
of hypothesis testing or parameter estimation. Machine learning techniques
are useful to approximate latent variables which can then be used to
construct powerful summary statistics for inference. In the presence
of a generative model that depends on additional uncertain parameters,
often referred to as nuisance parameters, the merits of classification
or regression based summary statistics are greatly diminished.
These concerns have motivated the development of a new family of
techniques to construct powerful summary statistics that account
directly for the final inference objective. By building and minimising
loss functions
that approximate the expected uncertainty on the parameters of interest,
also accounting for the effect of nuisance parameters, the
[INFERNO]{.smallcaps} approach
can leverage recent machine learning technologies to construct better summary
statistics for the inference problem at hand. These techniques were applied
to a series of synthetic problems and were found to significantly outperform
classification-based summary statistics (e.g. a deep neural network
and the optimal classifier) when nuisance parameters
are included in the problem. More experiments are needed to evaluate
the value of this technique for real-word inference problems, such as those
found in particle physics analyses.

As machine learning algorithms become increasingly popular in scientific
contexts, it will be more important to formally describe
the particularities of the problems we are trying to solve, in
order to understand whether the tools at hand are answering the right questions.
Otherwise we
risk falling for the anti-pattern
"if all you have is a hammer, everything looks like a nail", which could
significantly slow down the pace of scientific progress. This issue
is particularly pressing for particle collider experiments, where the
acquired familiarity with a given set of data analysis techniques might
hinder the rigour in their application relative to the final objective. Some
effort is then required to make sure of the role of a given tool is aligned
with the task at hand instead on the subtleties of the tool itself. When
using advanced statistical techniques or machine learning, the final analysis
goal is of the upmost relevance and cannot be neglected in favour of
procedural conventions. If those measures are coupled with
open research practices and a careful use
of domain-specific language and constructs in order to promote
collaboration with other disciplines, better tools
are likely to be developed which could in turn lead to major
advancements in this research field.

