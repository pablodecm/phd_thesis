# Statistical Modelling and Inference at the LHC {#sec:statinf}

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


## Statistical Modelling

### Overview

Let us suppose that we record a collection of raw detector readouts
$D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$ for a total $n$ bunch crossings
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

#### Experiment Outcome

Within such framework, we could begin by posing the question of how
we expect the readout output, which can be effectively treated as a
random variable $\boldsymbol{x}$, is distributed and how such distribution
is related with the (theoretical) parameters we are interested in measuring
in the experiment. We would like then to model the probability density
distribution function generating the a given observation $\boldsymbol{x}_i$
conditional on the parameters
of interest, that is:
$$ 
  \boldsymbol{x}_i \sim p ( \boldsymbol{x}|\boldsymbol{\theta} )
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
the known interactions that produce the set of
particles of the event as well as the subsequent
physical processes that generate the readouts in the detectors
are overly complex, and realistic modelling can only be obtained
through simulation, as jointly reviewed
in [Section @sec:pheno] and [Section @sec:event]. 

#### Mixture Structure

While a detailed
closed-form description of $p(\boldsymbol{x}|\boldsymbol{\theta})$
cannot be obtained, we can safely make a very useful remark about its
basic structure, which is fundamental for simplying the statisical treatment
of particle collider observations and simulations,
and was already hinted in [Section @sec:main_obs] when discussing
the possible outcomes of fundamental proton-proton interactions. The
aforementioned reflection is that the underlying
process generating $\boldsymbol{x}$ is a *mixture model*, it can be expressed
as the probabilistic composition of samples from multiple probabilistic
distributions corresponding to different types of interaction
processes occurring in the collision. If we knew the probabilistic
distribution function of each mixture component
$p_i(\boldsymbol{x}|\boldsymbol{\theta})$ then 
$p ( \boldsymbol{x}|\boldsymbol{\theta} )$ could be expressed as: 
$$
p ( \boldsymbol{x}|\boldsymbol{\theta} ) =
\sum^K \phi_j \ p_j ( \boldsymbol{x}|\boldsymbol{\theta} )
$$ {#eq:mixture_pdf}
where $K$ is the number of mixture components and $\phi_j$ is the mixture
weight/fraction, i.e. probability for a sample to be originated from
each mixture component $j$. Practically, each
$p_j(\boldsymbol{x}|\boldsymbol{\theta})$ will be intractable due to the
same reason making  $p ( \boldsymbol{x}|\boldsymbol{\theta} )$
intractable, thus a more sensible description of the mixture model
is the generative definition, described by the following
two-step sampling procedure:
$$ z_i \sim \textrm{Categorical}(\boldsymbol{\phi}) 
\quad \longrightarrow  \quad
\boldsymbol{x}_i \sim p_{z_i}( \boldsymbol{x} | \boldsymbol{\theta})
$$ {#eq:mixture_gen}
describing sampling and random integer $z_i \in \{0, \dots, K -1 \}$ from a random
categorical distribution and subsequently sampling the corresponding
mixture component indexed by  $z_i$, where
$\boldsymbol{\phi} = \{\phi_0, \dots, \phi_{K-1} \}$
is the vector of probabilities for each of the mixture components.
<!-- to include a graphical model or not to include a graphical model -->
For here onwards, mixture models might in some cases be portrayed by
using the analytical depiction as in [Equation @eq:mixture_pdf], always
noting that the generative approach might be more convenient for
the actual estimation of expectation values when the mixture
component distributions $p_j(\boldsymbol{x}|\boldsymbol{\theta})$
are not tractable.

#### Mixture Components

The mixture model structure can be directly link to the physical processes
happening in fundamental proton-proton collisions and detectors,
as described in previous chapters. As an additional simplification for now,
let us neglect the effect of multiple particle interactions,
as were described in [Section @sec:pile_up]. For each proton bunch
crossing, hard interactions (i.e. associated with
a large characteristic energy scale $Q^2$, whose cut-off does not have
be specified for this particular argument) between partons might or might
not occur, given the stochastic nature of the scattering processes. We
could nevertheless associate a probability for a hard interaction happening
$\phi_{\textrm{hard}}$, as well to it not happening
$\phi_{\textrm{not-hard}} = 1-\phi_{\textrm{hard}}$. Given the proton colliding
conditions at the LHC, the latter case is much more likely, i.e.
$\phi_{\textrm{not-hard}} \gg \phi_{\textrm{hard}}$.

However, we can further break each previously mentioned category in
sub-components corresponding to different types of processes. 
The hard interaction category can itself be expressed as a mixture
of all physical interactions, that can produce a hard scattering, so the
probability $\phi_{\textrm{hard}}$ can be expresses as the following
sum:
$$ \phi_{\textrm{hard}} = \phi_0 + \dots + \phi_n = \sum_{k \in H} \phi_k $$
where the $H$ represents a given set of independent contributions $k$, each
characterised by a distribution $p_j(\boldsymbol{x}|\boldsymbol{\theta})$,
from all different processes that produce hard scatterings. Such set is not
uniquely defined, given that any
two components $a$ and $b$ in $H$ can be substituted by $c$,
where $\phi_c = \phi_a + \phi_b$ and
$$p_c(\boldsymbol{x}|\boldsymbol{\theta})=
  \frac{\phi_a}{\phi_a+\phi_b} \ p_a(\boldsymbol{x}|\boldsymbol{\theta}) +
  \frac{\phi_b}{\phi_a+\phi_b} \ p_b(\boldsymbol{x}|\boldsymbol{\theta})
$$ {#eq:mixture_mixing}
which can be applied recursively to reduce the number of components in
the set.

A convenient definition for the set $H$ is one that is aligned with
the way theoretical calculations are carried out, given that the
relative probability for a given process $\phi_{pp\rightarrow X}$
will be proportional to its total cross section $\sigma (pp\rightarrow X)$,
while its readout distribution will depend on its differential
cross section $d\sigma (pp\rightarrow X)$ and its support. In fact, given
that the total and differential cross section are proportional to
the matrix element squared (see [Section @sec:qft_basics])
of a given process $d\sigma (pp\rightarrow X) \propto |\mathcal{M}|^2$,
it is often possible to further divide each process in the cross product
of Feynman diagram expansions (including interference terms), 
which can be very useful notion for a some analysis use cases,
and is related with the approach that will be
used in [Chapter @sec:higgs_pair].

#### Signal and Background

Oftentimes, we are interested in studying a subset $S \subset H$
of all the hard  interaction processes, that will referred to as signal
set. This can be a single type of physical process
$\sigma (pp\rightarrow X)$, e.g. the inclusive production of a pair
of Higgs bosons $\sigma (pp\rightarrow HH + \textrm{other})$, or
several, which in can be effectively viewed as one mixture
component using [Equation @eq:mixture_mixing]. We can accordingly define
the background subset $B = H - S$, as all the result of all
other generating processes in $H$ that we are not interested in,
definition which could also be extended to include collisions where
not-hard processes occurred if needed. Such distinction between generating
processes of interest $S$ and background $B$ is at the roots of every
analysis at the LHC, and it is motivated by the fact that small
changes of the parameters of the SM or its theoretical extensions/alternatives
affect a only a subset of the produced processes, those that are governed
by the interactions linked to the parameter.

As a matter of a fact, customarily statistical inference at the LHC
is not carried out directly on the parameters of the SM or the
extension being studied, but on the relative frequency of the set
of processes of interest $\phi_S$ or the properties of its 
distribution $p_S(\boldsymbol{x}|\boldsymbol{\theta})$. As previously
mentioned, the former is proportional to the cross section of the
signal processes $\sigma_S$ while the latter can include properties
such the mass of a intermediate particle resonance (e.g. the Higgs
mass $m_H$) or the general behaviour of the differential
distribution (i.e.
using unfolding methods to remove the experimental effects,
which are not discusses in this work). Those parametric proxies can
then be used compared with the theoretical predictions of the SM
or the alternative considered, in order to exclude or
constrain its fundamental parameters.

#### Event Selection

Given the mixture model structure expected for 
$p ( \boldsymbol{x}|\boldsymbol{\theta} )$ and the fact we are only
interested in a small amount of the readout generating
processes for each collision, because in general $\phi_S \ll
\phi_B \ll \phi_{\textrm{not-hard}}$, the effect of trigger
or any other *event selection* can be considered. The role of
event selection is reduce the fraction of events that do not
contain useful information for the inference task of interest. In the case
of trigger selection, it is a technical requirement in order reduce
the rate of detector readouts recorded to current technological
capabilities, as discussed in [Section @sec:trigger]. For analysis selection
instead, as will be discussed in [Chapter @sec:higgs_pair], it is used to reduce
the expected contribution of background processes that are not well-modelled
by simulation, as well as to the increase the expected fraction of signal
events in synthetic counting likelihoods those that will be detailed in
[Section @sec:synthetic_likelihood].

In general mathematical
terms, any deterministic event
selection can be thought as indicator function
$\mathbb{1}_\mathcal{C} : \mathcal{X} \longrightarrow \{0,1\}$,  of a given
subset of the set of possible detector readouts
$\mathcal{C} \subseteq \mathcal{X}$, that can be defined as:

$$\mathbb{1}_\mathcal{C}(\boldsymbol{x}) =
  \begin{cases}
    1 \ \textrm{if} \ \mathbf{x} \in C \\
    0 \ \textrm{if} \ \mathbf{x} \notin C \\
  \end{cases}$$ {#eq:indicator}

where the specific definition of of such function depends
on the definition of the subset $\mathcal{C}$, e.g. a simple cut on
a one-dimensional function
$f : \mathcal{X} \longrightarrow T \subseteq \mathcal{R}$
of the readout $f(\boldsymbol{x}) > t_{{\textrm{cut}}}$. Any
indicator function
can be also be viewed as a boolean predicate function, so the event selection
can also be a combination of operations selection, i.e. if the
set $\mathcal{C}=\mathcal{A} \cap \mathcal{B}$ is the intersection
between two subsets, the indicator
function of $C$ can be simply expressed as the product
$\mathbb{1}_\mathcal{C}=\mathbb{1}_\mathcal{A} \cdot \mathbb{1}_\mathcal{B}$.
This framework is flexible enough to represent all deterministic event
selections, and it could also be extended
by an independent non-deterministic
term to represent *trigger prescales* without affecting the succeeding
treatment.

In practise, in particle physics colliders, a given selection
$\mathbb{1}_\mathcal{C}(\boldsymbol{x})$ would be have been imposed on the
recorded detector
readouts before any statistical analysis is carried out. The structure
of the statistical model $g(\boldsymbol{x} | \boldsymbol{\theta} )$
resulting after applying an arbitrary selection 
$\mathbb{1}_\mathcal{C}(\boldsymbol{x})$ on a mixture model as the one
described in [Equation @eq:cond_density] can be obtained by multiplying
the probability density by $\mathbb{1}_\mathcal{C}(\boldsymbol{x})$ and
including the relevant normalisation term:
$$ 
g(\boldsymbol{x} | \boldsymbol{\theta} ) = \frac{
 \mathbb{1}_\mathcal{C}(\boldsymbol{x})
  \sum^K \phi_j \ p_j ( \boldsymbol{x}|\boldsymbol{\theta})}{
  \int \left (\mathbb{1}_\mathcal{C}(\boldsymbol{x}) 
  \sum^K \phi_j \ p_j ( \boldsymbol{x}|\boldsymbol{\theta}) \right ) 
  d \boldsymbol{x}}
  =
  \sum^K \left (  \frac{ \phi_j 
  \epsilon_j
  }{
  \sum^K \phi_j
  \epsilon_j
  } \right ) g_j (\boldsymbol{x}|\boldsymbol{\theta})
$$ {#eq:mixture_after_cut}
where 
$g_j (\boldsymbol{x}|\boldsymbol{\theta}) =
\mathbb{1}_\mathcal{C}(\boldsymbol{x}) p_j (\boldsymbol{x}|\boldsymbol{\theta})
 / \epsilon_j$ is the probability density function of each mixture component after
the selection,
$\epsilon_j=\int \mathbb{1}_\mathcal{C}(\boldsymbol{x}) p_j
(\boldsymbol{x}|\boldsymbol{\theta})$ is the *efficiency* on the selection
on each mixture and the integral sign in the denominator in the last
expression has been simplified by noting that
$\int g_j ( \boldsymbol{x}|\boldsymbol{\theta}) d \boldsymbol{x} = 1$.
From [Equation @eq:mixture_after_cut] it becomes clear that the
statistical model after any event selection is also a mixture model,
whose mixture components are $g_j (\boldsymbol{x}|\boldsymbol{\theta})$
and mixture fractions are $\chi_j=\phi_j\epsilon_j/\sum^K \phi_j\epsilon_j$,
which will be very relevant to build statistical models of the observed
data after an event event selection is in place.

So far, no explicit assumptions on the probability distribution functions
of each mixture component $j$ or the details of the event
selection function $\mathbb{1}_\mathcal{C}(\boldsymbol{x})$ have
been considered, in order to keep the previously developed modelling
framework as general as possible. In the next sections, it will become
increasingly clear how $p_j (\boldsymbol{x}|\boldsymbol{\theta})$,
and in turn $g_j (\boldsymbol{x}|\boldsymbol{\theta})$ and the efficiency
$\epsilon_j$, can be modelled by generating simulated detector readouts
produced by a given process $j$.

### Simulation as Generative Modelling

The physical principles underlying the simulation of detector readouts,
or events, for a given hard proton-proton interaction process were reviewed
in [Section @sec:pheno] and [Section @sec:event]. Instead of focussing
on the procedural details of event generation, the focus of this section
is the study of the simulation chain as a generative statistical model,
together with its basic structure and properties, that will be
useful later to understand many analysis techniques that are commonly
used in experimental particle physics.

For simplicity, we will be considering the statistical model describing
a dataset of detector readouts $D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$
before any event selection, what was referred as
$p ( \boldsymbol{x}|\boldsymbol{\theta} )$  in the previous section.
Always noting that the distribution after
any arbitrary deterministic
event selection $\mathbb{1}_\mathcal{C}(\boldsymbol{x})$
is also a mixture model (see [Equation @eq:mixture_after_cut])
and samples under the corresponding probability distribution functions
and mixture fractions $g_j (\boldsymbol{x}|\boldsymbol{\theta})$ and
$\chi_j$ can be easily obtained from the non-selected simulated events,
as it is actually done in practise.
 
####  Observable and Latent Variables

The first step to define a generative statistical model is to define
what are the observed variables and what are the hidden quantities,
referred to as *latent variables*, that explain the structure in the data.
For particle collider experiments, such as CMS, we can often consider the
full detector readout
$\boldsymbol{x} \in \mathcal{X} \subseteq \mathbb{R}^d$
as the only observable variable, given that any other observable
can be expressed as a function of the raw readout, as will be discussed
in [Section @sec:dim_reduction]. The probability density
function of the data $p ( \boldsymbol{x}|\boldsymbol{\theta} )$ from
a generative standpoint can be written as an integration of the
joint distribution $p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta})$
over all latent variables $\boldsymbol{z}$ of an event:
$$p ( \boldsymbol{x}|\boldsymbol{\theta} ) =
\int p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta})d\boldsymbol{z}
$$ {#eq:as_integration}
where  $\boldsymbol{\theta}$ is a vector with all model parameters, which
normally are global (same for all the observations) and include
the theory parameters of interest as well as any other parameter that
affect the detector readouts. While the true generative model of the data
$p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta})$ is unknown,
the knowledge about the underlying physical processes described in
in [Section @sec:pheno] and [Section @sec:event], can be used to build
a generative approximation of
$p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta})$ which can
describe the observed data realistically and be used to carry out
inference on the parameters of interest.

In fact, one of the most relevant latent variables at
particle colliders has been already introduced with the generative
definition of a mixture model in [Equation @eq:mixture_gen], the
mixture assignment integer $z_i \in \{0, \dots, K -1 \}$. This
latent variable represents which type of fundamental
interaction occurred in the event, and is useful to exemplify the
main property of latent variables: that they are not observed
but only can inferred. Let us consider the problem finding out the
type of interaction $j$ that caused a single detector readout
observation $\boldsymbol{x}_i$. As long as $\boldsymbol{x}_i$
is in the support space of more than one of the mixture
components $p_j( \boldsymbol{x}|\boldsymbol{\theta})$, which
is almost always the case, only probabilistic
statements about the type of interaction originating $\boldsymbol{x}_i$
can be made, even if $p_j( \boldsymbol{x}|\boldsymbol{\theta})$ are known.
In practise, $p_j( \boldsymbol{x}|\boldsymbol{\theta})$ are not known thus
analytically so probabilistic classification techniques
can be used to estimate the conditional probabilities based
on simulated samples, as discussed in [Chapter @sec:machine_learning].

####  Structure of Generative Model

Other than the basic mixture model structure, our understanding of the
underlying physical process occurring in proton-proton collisions
can be used to recognise additional structure in the generative
model by means of factorising the joint distribution
$p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta})$ in conditional
factors matching the various simulation steps and their dependencies:
$$p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta}) =
p ( \boldsymbol{x} | \boldsymbol{z}_\textrm{d})
p ( \boldsymbol{z}_\textrm{d} | \boldsymbol{z}_\textrm{s})
p ( \boldsymbol{z}_\textrm{s} | \boldsymbol{z}_\textrm{p})
\sum^K_j p ( z_i  = j |\boldsymbol{\theta})
\ p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_i  = j)
$$ {#eq:factor_joint}
where $p( z_i = j|\boldsymbol{\theta}) = \phi_j(\boldsymbol{\theta})$
is the probability of
a given type of process occurring,
$p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_i  = j)$ is
the conditional probability density of a given set of parton-level four-momenta
particles outcome for a group of fundamental proton interaction processes
$pp \longrightarrow X$ indexed by the latent
variable $z_i \in \mathcal{Z}_i$,
characterised by the latent representation
$\boldsymbol{z}_\textrm{p} \in \mathcal{Z}_\textrm{p}$,
as a function of the theory parameters,
$p( \boldsymbol{z}_\textrm{s} | \boldsymbol{z}_\textrm{p})$ is the conditional
density of a given parton-shower outcome
$\boldsymbol{z}_\textrm{s} \in \mathcal{Z}_\textrm{d}$ 
as a function of the parton-level outcome,
$p ( \boldsymbol{z}_\textrm{d} | \boldsymbol{z}_\textrm{s})$ is the conditional
density of a
set of detector interactions and readout noise
$\boldsymbol{z}_\textrm{d} \in \mathcal{Z}_\textrm{d}$
as a function of the parton-shower output, and
$p ( \boldsymbol{x} | \boldsymbol{z}_\textrm{d})$ is the conditional
density of a given detector readout
$\boldsymbol{x} \in \mathcal{X}$
as a function of the interactions
and detector noise.

The dimensionality of the latent space greatly
increases with each simulation step, from a single integer for $\mathcal{Z}_i$,
$\mathcal{O}(10)$ parton four-momenta variables within $\mathcal{Z}_p$,
$\mathcal{O}(100)$ after the parton-shower $\mathcal{Z}_s$,
to $\mathcal{O}(10^8)$ in
the detector interaction latent space $\mathcal{Z}_d$ and also
the observable readout space $\mathcal{X}$. In the factorisation presented
in [Equation @eq:factor_joint], the dependency on the parameters has
only be made explicit for $p( z_i|\boldsymbol{\theta})$
and $p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_i)$, that is because
the theoretical parameters of interest $\boldsymbol{\theta}$
often only affect the rate of the different fundamental processes
and their differential distributions, which correspond to the mentioned
conditional probability distributions. In the actual simulation chain,
all conditional factors typically depend on additional parameters which
might be uncertain, whose effect and modelling will be discussed in
[Section @sec:known_unknowns].

As previously mentioned, computer programs can be used to realistically
simulate detector observations. For simulated observations, not only
the final readout is observed, but all latent variables can be obtained
from the intermediate steps of the generative chain. These variables,
in particular $z_p$ and $z_s$, are commonly
referred as *generator level observables*, and are extremely useful to
construct techniques that approximate the latent variables from the
detector readouts. In fact, the whole simulation chain can be even viewed
as a probabilistic program [@Casado:2017cif;@Baydin:2018npr],
thus each of the factors in
[Equation @eq:factor_joint] can be further broken down as a sequence
of random samples, which can be used to speed up latent variable
inference based on the execution traces.

Some joint factorisations are specially useful for data analysis and simulation,
such as making explicit the dependency between
the differential partonic cross sections and the parton configuration
in the collision, which allows to factor out the density of
parton distribution latent variables $\boldsymbol{z}_\textrm{PDF}$
(i.e. flavour and momenta
of each interacting parton and factorisation scale $\mu_F^2$, as
depicted in [Section @sec:factorisation]). Each mixture
component $j$ in [Equation @eq:factor_joint], which represents a group
of fundamental interactions between protons $pp \longrightarrow X$, can be
expressed as the product of the probability of a given parton configuration
$p(\boldsymbol{z}_\textrm{PDF}|\boldsymbol{\theta}_\textrm{PDF})$ 
and a mixture over all parton configurations that can
that produce $pp \longrightarrow X$, referred as $L$ in the following
expression:
$$
p(z_i|\boldsymbol{\theta})
\ p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_i) = 
p(\boldsymbol{z}_\textrm{PDF}|\boldsymbol{\theta}_\textrm{PDF})
\sum^L_g p(z_f = g| \boldsymbol{\theta}, z_\textrm{PDF})
p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_f = g)
$$ {#eq:pdf_factorisation}
where $p(z_f = g| \boldsymbol{\theta}, z_\textrm{PDF})$ is the 
relative probability of given partonic process $g$ given
a parton configuration $\boldsymbol{z}_\textrm{PDF}$ and
$p(\boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_f = g)$ is the probability
distribution function of the parton-level outcome particles for a given
partonic process $g$, which is proportional to the partonic differential cross
section $d\sigma(ij \rightarrow X)$. This factorisation is basically
a probabilistic model version of [Equation @eq:qcd_factorisation], 
dealing with the QCD factorisation of the parton distribution functions and the
hard process differential cross section.

Another relevant phenomena that can be explicitated in the joint distribution
$p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta})$ is the effect of
multiple hadron interactions in the collision, or pileup, as discussed in
[Section @sec:pile_up]. Given that each proton-proton interaction is
independent from each other and the possible hard interaction in the
bunch crossing, the effect of pileup interactions can be considered by
augmenting
the factor representing the conditional probability
density of the detector interaction and noise as a function of the
hard interaction parton shower output 
$p ( \boldsymbol{z}_\textrm{d} | \boldsymbol{z}_\textrm{s})$ as follows:
$$
p ( \boldsymbol{z}_\textrm{d} | \boldsymbol{z}_\textrm{s}) =
p(\boldsymbol{z}_\textrm{d} | \boldsymbol{z}_\textrm{s},\boldsymbol{z}_\textrm{pileup})
p(\boldsymbol{z}_\textrm{pileup} | \boldsymbol{\theta}_\textrm{pileup})
$$ {#eq:pileup_fact}
where $\boldsymbol{z}_\textrm{pileup}$ is a latent variable representing
the details about the pileup interactions that happened in a given collision
(i.e. number of interactions and their corresponding particle outcome),
and $\boldsymbol{\theta}_\textrm{pileup}$ are the bunch crossing and
luminosity parameters that affect the pileup distribution.

Further structure in the generative model can be often found, depending
on the process being generated, the modelling assumptions and the
latent space representation chosen. As an example,
it is often useful to factorise out
$p(z_f = g| \boldsymbol{\theta}, z_\textrm{PDF})
p(z_f = g| \boldsymbol{\theta}, z_\textrm{PDF})$ the latents subspace
that depend directly
on the subset of parameters of interest from those that do not. Sometimes
the conditional observations in that latent subspace can be analytically
expressed, or their dimensionality is low enough to use 
non-parametric density estimation techniques efficiency, which can greatly
simplify the modelling of changes in the parameters of interest.


#### Simulated Observations {#sec:re-weighting}

The mentioned mixing structure of the probability distribution function
$p(\boldsymbol{x} | \boldsymbol{\theta})$
greatly simplifies the simulation of realistic observations, because
large datasets $S_j = \{\boldsymbol{x}_0,...,\boldsymbol{x}_m\}$ of
simulated observations for each type of interaction $j$ can
be simulated before any event selection. The expected value of any
measurable function
of the detector readout $f(\boldsymbol{x})$ for events coming from
a given process $j$ can be expressed as:
$$
\mathop{\mathbb{E}}_{x \sim p_j ( \boldsymbol{x}|\boldsymbol{\theta} )}
\left [ f(\boldsymbol{x}) \right ] =  \int f(\boldsymbol{x})     
p_j ( \boldsymbol{x}|\boldsymbol{\theta} ) d\boldsymbol{x} \approx   
\frac{1}{m} \sum^{\boldsymbol{x}_s \in S_j } f(\boldsymbol{x}_s)
$$ {#eq:montecarlo_obs}
where the last terms approximates the integral as the sum over all
stochastic simulations for a given process. The previous Monte Carlo
approximation can be used to estimate the selection efficiency $\epsilon_j$,
as defined
in [Equation @eq:mixture_after_cut], after
any deterministic event selection $\mathbb{1}_\mathcal{C}(\boldsymbol{x})$:
$$
\epsilon_j = \mathop{\mathbb{E}}_{x \sim p_j ( \boldsymbol{x}|\boldsymbol{\theta} )}
\left [ \mathbb{1}_\mathcal{C}(\boldsymbol{x}) \right ] =  \int 
\mathbb{1}_\mathcal{C}(\boldsymbol{x})
p_j ( \boldsymbol{x}|\boldsymbol{\theta} ) d\boldsymbol{x} \approx   
\frac{1}{m} \sum^{\boldsymbol{x}_s \in S_j } \mathbb{1}_\mathcal{C}(\boldsymbol{x})
$$ {#eq:montecarlo_eff}
which amounts to simply the number simulated observations that pass the selection
divided by the total of number of simulated observations $m$. Lastly, the
expected value of any measurable function $f(\boldsymbol{x})$ after
a given event selection $\mathbb{1}_\mathcal{C}(\boldsymbol{x})$ for event
generated by a given process $j$ can be approximated by:
$$
\mathop{\mathbb{E}}_{x \sim g_j ( \boldsymbol{x}|\boldsymbol{\theta} )}
\left [ f(\boldsymbol{x}) \right ] = \frac{1}{\epsilon_j }  \int f(\boldsymbol{x})
\mathbb{1}_\mathcal{C}(\boldsymbol{x})   
p_j ( \boldsymbol{x}|\boldsymbol{\theta} ) d\boldsymbol{x} \approx   
\frac{1}{\epsilon_j m} \sum^{\boldsymbol{x}_s \in S_j } f(\boldsymbol{x}_s)
\mathbb{1}_\mathcal{C}(\boldsymbol{x})
$$ {#eq:montecarlo_obs_sel}
which corresponds to the mean of $f(\boldsymbol{x})$ for all the
events that passed the selection, noting that if all the events would
pass the selection (i.e. $\mathbb{1}_\mathcal{C}(\boldsymbol{x}) = 1$), then
[Equation @eq:montecarlo_obs] is recovered.

While we have been dealing independently with the estimation of arbitrary
expected values for a given mixture component $j$, the computation of
expected values of any measurable function $f(\boldsymbol{x})$ under the
total mixture distribution can be easily be expressed as function of
expectations of mixture components:
$$
\mathop{\mathbb{E}}_{x \sim g ( \boldsymbol{x}|\boldsymbol{\theta} )}
\left [ f(\boldsymbol{x}) \right ] = \int f(\boldsymbol{x})
\sum^K_j \chi_j g_j (\boldsymbol{x}|\boldsymbol{\theta})
 d\boldsymbol{x} \approx 
\sum^{K}_j \chi_j
\mathop{\mathbb{E}}_{x \sim g_j ( \boldsymbol{x}|\boldsymbol{\theta} )}
\left [ f(\boldsymbol{x}) \right ] 
$$ {#eq:montecarlo_obs_mix_sel}
where $\chi_j=\phi_j\epsilon_j/\sum^K \phi_j\epsilon_j$ 
is the mixture fraction after selection
(see [Equation @eq:mixture_after_cut]). While the problem of estimation
of expected values might seem unrelated to the inference problem at hand,
in [Chapter @sec:dim_reduction] it will become evident that the construction
of non-parametric likelihoods of summary statistics can be reduced
to the estimation of expectation values.


 Oftentimes, the simulated observations are generated using somehow a
different probability distribution than the one inferred data, maybe because
some of the generating parameters are not known precisely before hand such
the properties of pileup distributions. Alternatively, we might want to
use a single set of simulated
observations to realistically model observables corresponding to a
different value of the parameters $\boldsymbol{\theta}$ or even to
compute observables under a different process $j$. Let us suppose that
the samples were generated under $p_Q(\boldsymbol{x} | \boldsymbol{\theta}_Q)$
while we want to model samples 
under  $p_R(\boldsymbol{x} | \boldsymbol{\theta}_R)$, if both distributions
have the same support, we can express the expectation value under the desired
distribution as:
$$
\mathop{\mathbb{E}}_{x \sim p_R ( \boldsymbol{x}|\boldsymbol{\theta}_Q )}
\left [ f(\boldsymbol{x}) \right ] = 
\frac {\int f(\boldsymbol{x}) 
\frac{p_R ( \boldsymbol{x}|\boldsymbol{\theta}_R )}{
p_Q ( \boldsymbol{x}|\boldsymbol{\theta}_Q )}  
p_Q ( \boldsymbol{x}|\boldsymbol{\theta}_Q )  d \boldsymbol{x}}{ 
\int
\frac{p_R ( \boldsymbol{x}|\boldsymbol{\theta}_R )}{
p_Q ( \boldsymbol{x}|\boldsymbol{\theta}_Q )}  
p_Q ( \boldsymbol{x}|\boldsymbol{\theta}_Q )  d \boldsymbol{x}}  
\approx   \frac{\sum^{\boldsymbol{x}_s \in S_j }
w(\boldsymbol{x}_s) f(\boldsymbol{x}_s)}{
\sum^{\boldsymbol{x}_s \in S_j }
w(\boldsymbol{x}_s)
}
$$ {#eq:reweight_intractable}
which is analogous to what was done in [Equation @eq:montecarlo_obs],
but accounting for a weight 
$w(\boldsymbol{x}_s) = p_R ( \boldsymbol{x}_s|\boldsymbol{\theta}_R )/
p_Q ( \boldsymbol{x}_s|\boldsymbol{\theta}_Q )$ for each simulated observation.
This technique can be also used together with an arbitrary event selection 
$\mathbb{1}_\mathcal{C}(\boldsymbol{x})$ simply
by considering as event weight the product
$w_{\mathcal{C}}(\boldsymbol{x}_s) = \mathbb{1}_\mathcal{C} (\boldsymbol{x}) w_(\boldsymbol{x}_s)$, which amounts to summing over the selected events.
In particle physics experiments, the probability distribution functions
$p_Q(\boldsymbol{x} | \boldsymbol{\theta}_R)$ and
$p_Q(\boldsymbol{x} | \boldsymbol{\theta}_R)$ are most likely
are intractable, thus 
estimation of $w_{\mathcal{C}}(\boldsymbol{x}_s)$ has either to be carried
out by non-parametric density estimation in a lower dimensional-space 
of the detector readouts (discussed in [Section @sec:dim_reduction]) or by
directly estimating the density ratio via probabilistic classification
as will be discussed in [Chapter @sec:machine_learning].

As previously mentioned, an advantage of using simulated observations is
that the latent variables
$\mathcal{H}_j= \{\boldsymbol{z}_0,...,\boldsymbol{z}_m\}$ for a given simulated
set of observations $S_j = \{\boldsymbol{x}_0,...,\boldsymbol{x}_m\}$ 
are known. This allows to rewrite the weight 
$w(\boldsymbol{x}_s,\boldsymbol{z}_s))$ for
a given event as the ratio of joint distributions:
$$
w(\boldsymbol{x}_s, \boldsymbol{z}_s) =
\frac{p_R(\boldsymbol{x}_s,\boldsymbol{z}_s | \boldsymbol{\theta}_R)}{
p_Q(\boldsymbol{x}_s,\boldsymbol{z}_s | \boldsymbol{\theta}_Q)
} = \frac { p_R ( \boldsymbol{x} | \boldsymbol{z}_\textrm{d})
p_R ( \boldsymbol{z}_\textrm{d} | \boldsymbol{z}_\textrm{s})
p_R ( \boldsymbol{z}_\textrm{s} | \boldsymbol{z}_\textrm{p})
p_R ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}_R) }{
p_Q ( \boldsymbol{x} | \boldsymbol{z}_\textrm{d})
p_Q ( \boldsymbol{z}_\textrm{d} | \boldsymbol{z}_\textrm{s})
p_Q ( \boldsymbol{z}_\textrm{s} | \boldsymbol{z}_\textrm{p})
p_Q ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}_Q)
}
$$ {#eq:latent_reweighting}
where the last term is an expansion of each joint distribution
as a product of the conditional distributions discussed in
[Equation @eq:factor_joint]. If the difference between
$p_R(\boldsymbol{x} | \boldsymbol{\theta}_R)$ and 
$p_Q(\boldsymbol{x} | \boldsymbol{\theta}_Q)$ is contained
in one of the factors of the joint distribution, which is
often the case, most of the factors in [Equation @eq:latent_reweighting]
and we are left with a much simpler problem of density
ratio estimation in the latent space. This if often what is done
to model the effect of a different pileup distribution
or alternative parton distribution functions, further factoring
the joint distribution to include explicit dependencies
with respect to $\boldsymbol{z}_\textrm{pileup}$
or $\boldsymbol{z}_\textrm{PDF}$, as done in [Equation @eq:pileup_fact]
and [Equation @eq:pdf_factorisation] respectively. 
The case when the difference between distributions is contained
in a subset of the parton-level latent variables is of special relevance,
because the event weight for a given event $w(\boldsymbol{z}_s)$ 
can be expressed as the ratio:
$$
w(\boldsymbol{z}_s) = \frac{p_R ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}_R)}{p_Q ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}_Q)}
$$ {#eq:gen_level_reweighting}
which is referred as *generator-level re-weighting*, and in some casessometimes
it can even be done analytically. The concept of *re-weighting* will be useful to
model different parameter points in [Chapter @sec:higgs_pair] with
single set of simulated observations as well as to understand how
the effect of varying parameters can be modelled via differentiable
transformations in [Chapter @sec:inferno].



### Dimensionality Reduction {#sec:dim_reduction}

In the previous overview of the basic statistical modelling principles
of experimental high-energy physics, the structure and properties
probability distribution of the full detector
readout $\boldsymbol{x} \in \mathcal{X}$ has been considered. These
allows to consider a single observable variable in the generative
model that has greatly simplified the modelling narrative and
including the effect of any arbitrary event selection
$\mathbb{1}_\mathcal{C} (\boldsymbol{x})$. Nevertheless, the
high-dimensionality of the readout space $\mathcal{X}$ 
(i.e. $\mathcal{O}(10^8)$) greatly complicates its direct use
for comparing simulated and recorded observations.



#### Event Reconstruction

#### Summary Statistics

#### Synthetic Likelihood {#sec:synthetic_likelihood}

### Known Unknowns {#sec:known_unknowns}

#### Nuisance Parameters

#### Background Estimation


## Statistical Inference

### Parameter Estimation

### Hypothesis Testing

### Likelihood-Free Inference


