
# New Technique: Inference-Aware Neural Optimisation {#sec:inferno}

\epigraph{An approximate answer to the right question
is worth a great deal more than a precise answer
to the wrong question.}{John Tukey}

By this point, it should have been made evident that powerful
statistical inference is the ultimate objective of all
experimental high-energy analyses. Supervised learning
based on simulated observation or acquired data control
regions, and in particular probabilistic classification,
provides a way to approximate latent variables of
the generative model,
that in turn are very useful to construct
powerful summaries for inference. While this approach is very
often encountered in experimental high energy physics,
complex computer simulations are also required for many
other scientific disciplines, making inference very
challenging due to the intractability of the likelihood
evaluation for the observed data. While summary
statistics based on a powerful supervised learning
algorithm can be asymptotically optimal in cases the generative
model is well-defined, such as the output of soft classification
for mixture models where we are interested in the mixture
coefficients, as demonstrated in [Section @sec:sig_vs_bkg]; their
usefulness can rapidly decrease when additional uncertain parameters
affect the generative model. As a practical example, 
in the analysis presented in [Chapter @sec:higgs_pair], the limiting
factor for experimental sensitivity was not in the choice of summary
statistics but rather on the lack of detailed knowledge about
the expected contribution from background processes, which had to
be address by the inclusion of nuisance parameters. The technique
presented in this chapter, referred to as INFERNO
and published at [@deCastro:2018mgh],
is an attempt to tackle directly the the problem of constructing
non-linear summary statistics from an statistical perspective
that considers the final inference question.
The key contribution required for achieving such goal,
is to leverage the technology that has been
develop for recent machine learning techniques, to build inference-aware
loss functions that approximate the
expected uncertainty on the parameters of interest, accounting
for the effect of nuisance parameters.

## Introduction

Simulator-based inference is currently at the core of many scientific
fields, such as population genetics, epidemiology, and experimental
particle physics.
In many cases the implicit generative procedure defined in the simulation is
stochastic and/or lacks a tractable probability density
$p(\boldsymbol{x}| \boldsymbol{\theta})$, where
$\boldsymbol{\theta} \in \mathcal{\Theta}$
is the vector of model parameters. Given some experimental
observations $D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$,
a problem of special relevance for these
disciplines is statistical inference on a subset of model parameters
$\boldsymbol{\omega} \in \mathcal{\Omega} \subseteq \mathcal{\Theta}$.
This can be approached via likelihood-free inference
algorithms such as Approximate Bayesian Computation (ABC) [@beaumont2002approximate],
simplified synthetic likelihoods [@wood2010statistical]
or density estimation-by-comparison approaches
[@cranmer2015approximating].

## Problem Statement


## Method


## Related Work

## Experiments
