# Statistical Inference and Modelling at the LHC {#sec:statinf}

\epigraph{Life is complicated, but
  not uninteresting.}{Jerzy Neyman}

In this chapter, the problem of extracting quantitative
information about the validity or properties of the different
theoretical models (see Chapter [-@sec:theory]) can be made given the
data experimental data acquired in a controlled setting (see Chapter
[-@sec:experiment]) will be tackled. We will begin by formally defining
common inference problems in experimental high-energy physics and how they
can be tackled with classical techniques.
Then some relevant particularities of the inference problems
at the LHC experiments will be discussed, mainly the
generative-only nature of the simulation models and the high dimensionality
of the data. As we will see, both issues are intimately related, the former
requiring the use of likelihood-free inference techniques such as constructing
a non-parametric sample likelihoods, which in turn demands for lower
dimensional summary statistics.


## Problem Definition

Let us suppose that we record a collection of raw detector readouts
$R = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$ for a total $n$ bunch crossings
at a particle collider experiment, such as CMS at the LHC (see Section
[-@sec:cms]). Note that vector notation is used for each individual readout,
also referred to as event, because for mathematical simplification
we will be assuming that each detector observation can be embedded
as a member of a fixed size
$d$-dimensional space, i.e. $\boldsymbol{x} \in \mathcal{X}
\subseteq \mathbb{R}^d$, even though variable-size sets or tree-like
structures might be a more compact and useful representation in practise,
as will be discussed later.
As an starting point,
let us assume that the detector readout for every bunch crossing
is recorded, i.e. no trigger filtering system as the one described in
[Section @sec:trigger] is in place, hence after each bunch crossing $i$ a
given raw detector readout $\boldsymbol{x}_i$ will be obtained. From
here onwards, each event/observation/readout will be assumed to
independent and identically distributed (i.i.d.),
a reasonable approximation if the experimental conditions
are stable during the acquisition period as discussed at the
beginning of [Section @sec:event], consequently the event ordering
or index $i$ are not relevant.
Within such framework, we could begin by posing the question of how
we expect the readout output, which can be effectively treated as a
random variable $\boldsymbol{x}$, is distributed and how such distribution
is related with the (theoretical) parameters we are interested in measuring
in the experiment. We would like then to model the probability density
distribution function generating the data conditional on the parameters
of interest, that is:
$$ 
  \boldsymbol{x} \sim p ( \boldsymbol{x}|\boldsymbol{\theta} )
$$ {#eq:cond_density}
where $\boldsymbol{\theta} \in \mathcal{\Theta} \subseteq \mathbb{R}^p$ 
denotes all the parameters we are interested in and affect
the detector outcome of each collision. As will be extensively
discussed in this chapter, an analytical or even tractable
approximation of $p ( \boldsymbol{x}|\boldsymbol{\theta})$
is not attainable, given that we are considering $\boldsymbol{x}$
to be a representation of the raw readout of all sub-detectors,
thus its dimensionality $d$, even if extremely sparse given
that most of the detectors would not sense any signal,
can easily be of the order $\mathcal{O}(10^8)$. Furthermore,
the generating processes are assumed that produce
particles outcome in the event as well as the subsequent
physical processes that produce readouts in the detectors
are overly complex, and realistic modelling can only be obtained
through simulation, as jointly reviewed in [Section @sec:pheno]
and [Section @sec:event].

### Confidence Intervals

### Hypothesis Testing

### Likelihood-Free Inference

## Summary Statistics

## Statistical Methods

