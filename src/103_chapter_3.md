# Statistical Modelling and Inference at the LHC {#sec:statinf}

\epigraph{Life is complicated, \\
but not uninteresting.}{Jerzy Neyman}

In this chapter we will consider the problem of extracting quantitative
information about the validity or properties of the different
theoretical models (see [Chapter @sec:theory]), which can be made given the
experimental data acquired in a controlled setting (see
[Chapter @sec:experiment]). We will begin by formally defining
the properties and structure of the statistical models
used to link the parameters of interest, followed by a description
of the inference problems in experimental high-energy physics
and how they can be tackled with classical and non-classical techniques.
Some relevant particularities of the inference problems typically of
interest of the LHC experiments will be discussed, mainly the
generative-only nature of the simulation models and the high dimensionality
of the data. As we will see, these issues are intimately related,
the former
requiring the use of likelihood-free inference techniques such as constructing
non-parametric sample likelihoods, which in turn demands for lower
dimensional summary statistics.


## Statistical Modelling {#sec:stat_model}

An essential element for carrying out statistical inference is the
availability of an adequate
a statistical model. In this section, the main characteristics of the statistical
models used in particle collider analysis will be formally developed from first
principles. This methodology allows a
mathematical approach to their structure and factorisation. This will
prove useful to establish a formal link between the techniques discussed
in the next chapters and the simulation-based
generative models that are often used to describe the data. Additionally,
the role and importance of event selection, event
reconstruction and dimensionality reduction - i.e. the compression
of the relevant information from high-dimensional data into a
lower-dimensional representation, such as the output of a multivariate
classifier - will be described in the larger statistical
framework of an LHC analysis. Lastly, the main
approaches commonly followed to construct synthetic likelihoods
that efficiently connect summaries of the detector observation
with the parameters of interest will be illustrated.


### Overview {#sec:model_overview}

Let us suppose that we record a collection of raw detector readouts
$D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$ for a total of $n$ bunch crossings
at a particle collider experiment, such as CMS at the LHC (see Section
[-@sec:cms]). Note that vector notation is used for each individual readout,
also referred to as event, because for mathematical simplification
we will be assuming that each detector observation can be embedded - in
the mathematical sense -
as a member of a fixed size
$d$-dimensional space, i.e. $\boldsymbol{x} \in \mathcal{X}
\subseteq \mathbb{R}^d$, even though variable-size sets or tree-like
structures might be a more compact and useful representation in practice,
as will be discussed later.
As an starting point,
let us assume for simplicity that the detector readout for every bunch crossing
is recorded, i.e. no trigger filtering system as the one described in
[Section @sec:trigger] is in place, hence after each bunch crossing $i$ a
given raw detector readout $\boldsymbol{x}_i$ will be obtained. From
here onwards, each event/observation/readout will be assumed to be
independent and identically distributed (i.i.d.),
a reasonable approximation if the experimental conditions
are stable during the acquisition period as discussed at the
beginning of [Section @sec:event]; consequently the event ordering
or index $i$ are not relevant.

#### Experiment Outcome

Within the above framework, we could begin by posing the question of how
we expect the readout output, which can be effectively treated as a
random variable $\boldsymbol{x}$, is distributed and how such distribution
is related with the (theoretical) parameters we are interested in measuring
in the experiment. We would like then to model the probability density
distribution function generating a given observation $\boldsymbol{x}_i$
conditional on the parameters
of interest, that is:
$$ 
  \boldsymbol{x}_i \sim p ( \boldsymbol{x}|\boldsymbol{\theta} )
$$ {#eq:cond_density}
where $\boldsymbol{\theta} \in \mathcal{\Theta} \subseteq \mathbb{R}^p$ 
denotes all the parameters we are interested in and affects
the detector outcome of collisions. As will be extensively
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
basic structure, which is fundamental for simplyfing the statistical treatment
of particle collider observations and simulations,
and was already hinted at in [Section @sec:main_obs] when discussing
the possible outcomes of fundamental proton-proton interactions. The underlying
process generating $\boldsymbol{x}$ can be treated as
a *mixture model*, which can be expressed
as the probabilistic composition of samples from multiple probabilistic
distributions corresponding to different types of interaction
processes occurring in the collision. If we knew the probabilistic
distribution function of each mixture component
$p_j(\boldsymbol{x}|\boldsymbol{\theta})$ then 
$p ( \boldsymbol{x}|\boldsymbol{\theta} )$ could be expressed as: 
$$
p ( \boldsymbol{x}|\boldsymbol{\theta} ) =
\sum^{K-1}_{j=0} \phi_j \ p_j ( \boldsymbol{x}|\boldsymbol{\theta} )
$$ {#eq:mixture_pdf}
where $K$ is the number of mixture components and $\phi_j$ is the mixture
weight/fraction, i.e. probability for a sample to be originated from
each mixture component $j$. The specifics of the mixture expansion as
well as the total
number of mixture components are not uniquely defined, yet based
on the independence of groups of physical processes, as will
be discussed later.
Practically, each
$p_j(\boldsymbol{x}|\boldsymbol{\theta})$ will be intractable due to the
exact
same reason that $p ( \boldsymbol{x}|\boldsymbol{\theta} )$
is intractable, thus a more sensible description of the mixture model
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

#### Mixture Components {#sec:mixture_components}

The mixture model structure can be directly linked to the physical processes
happening in fundamental proton-proton collisions and detectors used to
study them,
as described in previous chapters. As an additional simplification for now,
let us neglect the effect of multiple particle interactions,
described in [Section @sec:pile_up]. For each proton bunch
crossing, hard interactions (i.e. ones associated with
a large characteristic energy scale $Q^2$, whose cut-off does not have
be specified for this particular argument) between partons might or might
not occur, given the stochastic nature of the scattering processes. We
could nevertheless associate a probability for a hard interaction happening
$\phi_{\textrm{hard}}$, as well to it not happening
$\phi_{\textrm{not-hard}} = 1-\phi_{\textrm{hard}}$. Given the proton colliding
conditions at the LHC, the latter case is much more likely, i.e.
$\phi_{\textrm{not-hard}} \gg \phi_{\textrm{hard}}$, yet the relative
probabilities depend on the energy scale cut-off considered.

We can further break each previously mentioned category in
sub-components corresponding to different types of processes.
The hard interaction category can itself be expressed as a mixture
of groups of physical interactions that can produce
a hard scattering[^group], so the
probability $\phi_{\textrm{hard}}$ can be expresses as the following
sum:
$$ \phi_{\textrm{hard}} = \phi_0 + \dots + \phi_{K-2} = \sum_{k \in H} \phi_k
$$ {#eq:hard_prob}
where $H$ represents a given set of independent contributions $k$, each
characterised by a distribution $p_j(\boldsymbol{x}|\boldsymbol{\theta})$,
which depends on the group $j$
of processes that produce hard scatterings. Such a set is not
uniquely defined nor its the number of elements, given that any
two components $a$ and $b$ in $H$ can be substituted by $c$,
where $\phi_c = \phi_a + \phi_b$ and
$$p_c(\boldsymbol{x}|\boldsymbol{\theta})=
  \frac{\phi_a}{\phi_a+\phi_b} \ p_a(\boldsymbol{x}|\boldsymbol{\theta}) +
  \frac{\phi_b}{\phi_a+\phi_b} \ p_b(\boldsymbol{x}|\boldsymbol{\theta})
$$ {#eq:mixture_mixing}
which can be applied recursively to alter the number of components in
the set. Independently on the basis chosen for the mixture expansion,
in general it is not possible to infer the latent category $z_i$
(see [Equation @eq:mixture_pdf) given an observation $\boldsymbol{x}_i$, because
$\boldsymbol{x}_i$ may be in the support of several mixture components
$p_j(\boldsymbol{x}|\boldsymbol{\theta})$. Only
probabilistic statements about the generative group $j$ can be made
based on the observations. 

[^group]: The term *group/type of interactions* here generally
  refers to a set of processes that could be generatively modelled
  independently, not to quantum mechanical amplitudes or intensities
  of a process.
  For example, each group can correspond to a group of processes with
  a given final state (which is latent)
  $pp \rightarrow X$ which could
  be modelled by sampling its differential cross section from
  [Equation @eq:qcd_factorisation] followed by parton showering
  and detector simulation.

A convenient definition for the set $H$ is one that is aligned with
the way theoretical calculations are carried out, given that the
relative probability for a given process $\phi_{pp\rightarrow X}$
will be proportional to its total cross section $\sigma (pp\rightarrow X)$,
while its readout distribution will depend on its differential
cross section $d\sigma (pp\rightarrow X)$ and its support. In fact, given
that the total and differential cross section are proportional to
the matrix element squared (see [Section @sec:qft_basics])
of a given process $d\sigma (pp\rightarrow X) \propto |\mathcal{M}|^2$.
It is often possible to further divide each process into the cross product
of Feynman diagram expansions (including interference terms), 
which can be a very useful notion for some analysis use cases,
and is related with the approach that will be
used in [Chapter @sec:higgs_pair].

#### Signal and Background {#sec:sig_and_bkg}

Oftentimes, we are interested in studying a subset $S \subset H$
of all the hard  interaction processes, which will be referred to as signal
set in what follows. This can be a single type of physical process
$\sigma (pp\rightarrow X)$, e.g. the inclusive production of a pair
of Higgs bosons $\sigma (pp\rightarrow \textrm{HH} + \textrm{other})$, or
several, which in can be effectively viewed as one mixture
component using [Equation @eq:mixture_mixing]. We can accordingly define
the background subset $B = H - S$, as the result of all
other generating processes in $H$ that we are not interested in,
a definition which could also be extended to include collisions where
non-hard processes occurred if needed. Such distinction between generating
processes of interest $S$ and background $B$ is at the roots of every
analysis at the LHC and it is motivated by the fact that small
changes of the parameters of the SM or its theoretical extensions/alternatives
affect only a subset of the produced processes at leading order,
those that are governed
by the interactions linked to the parameter.

As a matter of a fact, customarily statistical inference at the LHC
is not carried out directly on the parameters of the SM or the
extension being studied, but on the relative frequency of the set
of processes of interest $\phi_S$ or the properties of its 
distribution $p_S(\boldsymbol{x}|\boldsymbol{\theta})$. As previously
mentioned, the former is proportional to the cross section of the
signal processes $\sigma_S$ while the latter can include properties
such as the mass of an intermediate particle resonance (e.g. the Higgs
mass $m_\textrm{H}$) or the general behaviour of the differential
distribution (i.e.
using unfolding methods to remove the experimental effects,
which are not discusses in this work). Those parametric proxies can
then be used by comparing them with the theoretical predictions of the SM
or the alternative considered, in order to exclude or
constrain its fundamental parameters (i.e. those that appear in
the Lagrangian).

#### Event Selection

Given the mixture model structure expected for 
$p ( \boldsymbol{x}|\boldsymbol{\theta} )$ and the fact we are only
interested in a small amount of the readout generating
processes for each collision, because in general $\phi_S \ll
\phi_B \ll \phi_{\textrm{not-hard}}$, the effect of trigger
or any other *event selection* should be considered. The role of
event selection is to reduce the fraction of events that do not
contain useful information for the inference task of interest.
Trigger selection can be thought of as a technical requirement,
reducing the total rate of detector readouts recorded to match
the available hardware for data acquisition, as discussed in [Section @sec:trigger]. The purpose of analysis selection, as will be discussed
in [Chapter @sec:higgs_pair], is instead to reduce
the expected contribution of background processes that are not well-modelled
by simulation, as well as to the increase the expected fraction of signal
events in synthetic counting likelihoods, such as those which will be detailed in
[Section @sec:synthetic_likelihood].

In general mathematical
terms, any deterministic event
selection can be thought of as an indicator function
$\mathbb{1}_\mathcal{C} : \mathcal{X} \longrightarrow \{0,1\}$,  of a given
subset of the set of possible detector readouts
$\mathcal{C} \subseteq \mathcal{X}$. The indicator function
$\mathbb{1}_\mathcal{C}(\boldsymbol{x})$can be defined as:

$$\mathbb{1}_\mathcal{C}(\boldsymbol{x}) =
  \begin{cases}
    1 \ \textrm{if} \ \mathbf{x} \in C \\
    0 \ \textrm{if} \ \mathbf{x} \notin C \\
\end{cases}
$$ {#eq:indicator}

where the specific definition of such function depends
on the definition of the subset $\mathcal{C}$, e.g. a simple cut on
a one-dimensional function
$f : \mathcal{X} \longrightarrow T \subseteq \mathcal{R}$
of the readout $f(\boldsymbol{x}) > t_{{\textrm{cut}}}$. Any
indicator function
can be also be viewed as a boolean predicate function, so the event selection
can also be expressed as a combination of selection functions, i.e. if the
set $\mathcal{C}=\mathcal{A} \cap \mathcal{B}$ is the intersection
between two subsets, the indicator
function of $C$ can be simply expressed as the product
$\mathbb{1}_\mathcal{C}=\mathbb{1}_\mathcal{A} \cdot \mathbb{1}_\mathcal{B}$.
This framework is flexible enough to represent all deterministic event
selections, and it could also be extended
by an independent non-deterministic 
term without affecting the rest of the
considerations presented in this chapter. A non-deterministic factor could
be useful to model for example trigger prescales,
which are trigger decisions based
on a randomly selecting a fraction of all the selected events to be recorded,
ensuring that the total rate are manageable.

In practice, a given selection
$\mathbb{1}_\mathcal{C}(\boldsymbol{x})$ would have been imposed on the
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
  \sum^{K-1}_{j=0} \phi_j \ p_j ( \boldsymbol{x}|\boldsymbol{\theta})}{
  \int \left (\mathbb{1}_\mathcal{C}(\boldsymbol{x}) 
  \sum^{K-1}_{j=0} \phi_j \ p_j ( \boldsymbol{x}|\boldsymbol{\theta}) \right ) 
  d \boldsymbol{x}}
  =
  \sum^{K-1}_{j=0} \left (  \frac{ \phi_j 
  \epsilon_j
  }{
  \sum^{K-1}_{j=0} \phi_j
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
on each mixture, and the integral sign in the denominator in the last
expression has been simplified by noting that
$\int g_j ( \boldsymbol{x}|\boldsymbol{\theta}) d \boldsymbol{x} = 1$.
From [Equation @eq:mixture_after_cut] it becomes clear that the
statistical model after any event selection is also a mixture model,
whose mixture components are $g_j (\boldsymbol{x}|\boldsymbol{\theta})$
and mixture fractions are $\chi_j=\phi_j\epsilon_j/\sum^{K-1}_{j=0} \phi_j\epsilon_j$.
This fact will be very relevant to build statistical models of the observed
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
before any event selection, what was referred to as
$p ( \boldsymbol{x}|\boldsymbol{\theta} )$  in the previous section.
Always taking into account that the distribution after
any arbitrary deterministic
event selection $\mathbb{1}_\mathcal{C}(\boldsymbol{x})$
is also a mixture model (see [Equation @eq:mixture_after_cut])
and samples under the corresponding probability distribution functions
and mixture fractions $g_j (\boldsymbol{x}|\boldsymbol{\theta})$ and
$\chi_j$ can easily obtained from the non-selected simulated events,
as it is actually done in practice.
 
####  Observable and Latent Variables

The first step to  build a generative statistical model is to define
what are the observed variables and what are the hidden quantities,
referred to as *latent variables*, that explain the structure in the data.
For particle collider experiments, we may consider the
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
in [Section @sec:pheno] and [Section @sec:event] can be used to build
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
but can only (at most) be inferred. Let us consider the problem
of finding out the
type of interaction $j$ that caused a single detector readout
observation $\boldsymbol{x}_i$. As long as $\boldsymbol{x}_i$
is in the support space of more than one of the mixture
components $p_j( \boldsymbol{x}|\boldsymbol{\theta})$, which
is almost always the case, only probabilistic
statements about the type of interaction originating $\boldsymbol{x}_i$
can be made, even if the $p_j( \boldsymbol{x}|\boldsymbol{\theta})$ are known.
In practice, $p_j( \boldsymbol{x}|\boldsymbol{\theta})$ are not known
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
\sum^{K-1}_{j=0} p ( z_i  = j |\boldsymbol{\theta})
p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_i  = j)
$$ {#eq:factor_joint}
where $p( z_i = j|\boldsymbol{\theta}) = \phi_j(\boldsymbol{\theta})$
is the probability of
a given type of process $j$ occurring,
$p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_i  = j)$ is
the conditional probability density of a given set of parton-level four-momenta
particles (characterised by the latent representation
$\boldsymbol{z}_\textrm{p} \in \mathcal{Z}_\textrm{p}$) of being the
outcome of a group of fundamental proton interaction processes
$pp \longrightarrow X$ indexed by the latent variable $z_i \in \mathcal{Z}_i$,
as a function of the theory parameters $\boldsymbol{\theta}$,
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
in [Equation @eq:factor_joint], the dependence on the parameters has
only be made explicit for $p( z_i|\boldsymbol{\theta})$
and $p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_i)$, that is because
the theoretical parameters of interest $\boldsymbol{\theta}$
often only affect the rate of the different fundamental processes
and their differential distributions, which correspond to the mentioned
conditional probability distributions. In the actual simulation chain,
all conditional factors typically depend on additional parameters which
might be uncertain, and whose effect and modelling will be discussed in
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

Some joint factorisations are particularly
useful for data analysis and simulation,
such as the one making explicit he dependence between
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
\sum^{g \in L} p(z_f = g| \boldsymbol{\theta}, z_\textrm{PDF})
p ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_f = g)
$$ {#eq:pdf_factorisation}
where $p(z_f = g| \boldsymbol{\theta}, z_\textrm{PDF})$ is the 
relative probability of given partonic process $g$ given
a parton configuration $\boldsymbol{z}_\textrm{PDF}$ and
$p(\boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}, z_f = g)$ is the probability
distribution function of the parton-level particles produced
as a result of the interaction for a given
partonic process $g$, which is proportional to the partonic differential cross
section $d\sigma(ij \rightarrow X)$. This factorisation is basically
a probabilistic model version of [Equation @eq:qcd_factorisation], 
dealing with the QCD factorisation of the parton distribution functions and the
hard process differential cross section.

Another relevant phenomenon that can be explicitated in the joint distribution
$p(\boldsymbol{x}, \boldsymbol{z} | \boldsymbol{\theta})$ is the effect of
multiple hadron interactions in the collision, or pileup, as discussed in
[Section @sec:pile_up]. Given that each proton-proton interaction is
independent from the others, the effect of pileup interactions can be
considered by
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
on the process being generated, the modelling assumptions, and the
latent space representation chosen. As an example,
it is often useful to factorise out the latent subspace
that depends directly
on the subset of parameters of interest from those that do not. 
The conditional observations in that latent subspace can sometimes be analytically
expressed, or their dimensionality is low enough to use 
non-parametric density estimation techniques effectively, which can greatly
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
which simply corresponds to the number of simulated observations
that pass the selection
divided by the total number of simulated observations $m$. Lastly, the
expected value of any measurable function $f(\boldsymbol{x})$ after
a given event selection $\mathbb{1}_\mathcal{C}(\boldsymbol{x})$ for events
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
events that passed the selection, noting that if all the events
passed the selection (i.e. $\mathbb{1}_\mathcal{C}(\boldsymbol{x}) = 1$), then
[Equation @eq:montecarlo_obs] would be recovered.

While we have been dealing independently with the estimation of arbitrary
expected values for a given mixture component $j$, the computation of
expected values of any measurable function $f(\boldsymbol{x})$ under the
total mixture distribution can be easily be expressed as function of
expectations of mixture components:
$$
\mathop{\mathbb{E}}_{x \sim g ( \boldsymbol{x}|\boldsymbol{\theta} )}
\left [ f(\boldsymbol{x}) \right ] = \int f(\boldsymbol{x})
\sum^{K-1}_{j=0} \chi_j g_j (\boldsymbol{x}|\boldsymbol{\theta})
 d\boldsymbol{x} \approx 
\sum^{K-1}_{j=0} \chi_j
\mathop{\mathbb{E}}_{x \sim g_j ( \boldsymbol{x}|\boldsymbol{\theta} )}
\left [ f(\boldsymbol{x}) \right ] 
$$ {#eq:montecarlo_obs_mix_sel}
where $\chi_j=\phi_j\epsilon_j/\sum^{K-1}_{j=0} \phi_j\epsilon_j$ 
is the mixture fraction after selection
(see [Equation @eq:mixture_after_cut]). While the problem of estimation
of expected values might seem unrelated to the inference problem at hand,
in [Chapter @sec:dim_reduction] it will become evident that the construction
of non-parametric likelihoods of summary statistics can be reduced
to the estimation of expectation values.


 Oftentimes, the simulated observations are generated using a somewhat
different probability distribution than that of experimental data, maybe because
some of the generating parameters are not known precisely beforehand (e.g.
the properties of pileup interactions). Alternatively, we might want to
use a single set of simulated
observations to realistically model observables corresponding to a
different value of the parameters $\boldsymbol{\theta}$ or even to
compute observables under a different process $j$. Let us suppose that
the samples were generated under $p_Q(\boldsymbol{x} | \boldsymbol{\theta}_Q)$
while we want to model samples 
under  $p_R(\boldsymbol{x} | \boldsymbol{\theta}_R)$. In that case, if both
distributions
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
$w_{\mathcal{C}}(\boldsymbol{x}_s) = \mathbb{1}_\mathcal{C} (\boldsymbol{x}) w(\boldsymbol{x}_s)$, which amounts to summing over the selected events.
In particle physics experiments, the probability distribution functions
$p_Q(\boldsymbol{x} | \boldsymbol{\theta}_R)$ and
$p_Q(\boldsymbol{x} | \boldsymbol{\theta}_R)$ are most likely
intractable, thus 
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
$w(\boldsymbol{x}_s,\boldsymbol{z}_s)$ for
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
cancel out
and we are left with a much simpler problem of density
ratio estimation in the latent space. This if often what is done
to model the effect of a different pileup distribution
or alternative parton distribution functions, further factoring
the joint distribution to include explicit dependencies
with respect to $\boldsymbol{z}_\textrm{pileup}$
or $\boldsymbol{z}_\textrm{PDF}$, as done in [Equation @eq:pileup_fact]
and [Equation @eq:pdf_factorisation] respectively. 
The case when the difference between distributions is contained
in a subset of the parton-level latent variables is one of special relevance,
because the event weight for a given event $w(\boldsymbol{z}_s)$ 
can be expressed as the ratio:
$$
w(\boldsymbol{z}_s) = \frac{p_R ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}_R)}{p_Q ( \boldsymbol{z}_\textrm{p}|\boldsymbol{\theta}_Q)}
$$ {#eq:gen_level_reweighting}
which is referred to as *generator-level re-weighting*, a procedure
that in some cases
can even be done analytically. The concept of *re-weighting* will be useful to
model different parameter points in [Chapter @sec:higgs_pair] with
a single set of simulated observations as well as to understand how
the effect of varying parameters can be modelled via differentiable
transformations in [Chapter @sec:inferno].



### Dimensionality Reduction {#sec:dim_reduction}

In the previous overview of the basic statistical modelling principles
of experimental high-energy physics, the structure and properties of the
probability distribution of the full detector
readout $\boldsymbol{x} \in \mathcal{X}$ has been considered. These
allow to consider a single observable variable in the generative
model, a fact which greatly simplifies the modelling narrative and
also allows to include the effect of any arbitrary event selection as
a deterministic function $\mathbb{1}_\mathcal{C} (\boldsymbol{x})$.
Nevertheless, the
high-dimensionality of the readout space $\boldsymbol{x} \in \mathcal{X}$
(i.e. $\mathcal{O}(10^8)$) significantly complicates its direct use
when comparing simulated and recorded observations, and carry out
any statistical inference procedure.

The high-dimensionality of the raw detector readout
space $\boldsymbol{x} \in \mathcal{X}$ also makes it very difficult
to specify an effective event selection
$\mathbb{1}_\mathcal{C} (\boldsymbol{x})$
that is able to reduce
the contributions from non-interesting or not well-modelled
background processes. This motivates the use of a dimensionality reduction
function
$\boldsymbol{f}(\boldsymbol{x}) : \mathcal{X} \longrightarrow \mathcal{Y}$,
from the raw detector readout
space $\mathcal{X} \subseteq \mathbb{R}^{d}$
to a lower dimensional space $\mathcal{Y} \subseteq \mathbb{R}^{b}$. Here
$\boldsymbol{f}(\boldsymbol{x})$ represents any deterministic function
of the detector readout, but in practice it can be implemented by a series
of consecutive transformations.

Let us denote as $\boldsymbol{y} \in \mathcal{Y}$ the resulting variable
after the transformation $\boldsymbol{f}(\boldsymbol{x})$ is applied
to the observed detector readout. If the function $\boldsymbol{f}$ is
differentiable and bijective (i.e. there is a one-to-one correspondence between
$\boldsymbol{x}$ and $\boldsymbol{y}$), the probability density 
distribution function of $\boldsymbol{y}$ could be obtained as:
$$
p(\boldsymbol{y} | \boldsymbol{\theta}) = 
p(\boldsymbol{x} | \boldsymbol{\theta})
\left | \det \frac{d\boldsymbol{x} }{d\boldsymbol{y} } \right |  
$$ {#eq:change_of_vars}
where the last term is the Jacobian determinant of the inverse
of $\boldsymbol{f}$. The transformations commonly used in particle
colliders are non-bijective and sometimes non-differentiable, plus
[Equation @eq:change_of_vars] is in any case of little use when
$p(\boldsymbol{x} | \boldsymbol{\theta})$ is intractable.
However, the expectation
value of $\boldsymbol{y}$ as well any other deterministic
transformation of the detector readout $\boldsymbol{x}$
after any arbitrary event selection $\mathbb{1}_\mathcal{C} (\boldsymbol{x})$
can be obtained using simulated samples for a given interaction
process as shown in [Equation @eq:montecarlo_obs_sel}],
independently of whether the transformation
is invertible or differentiable. In the rest of this section, the main
procedures followed to reduce the dimensionality of the observable
space and its objectives from a statistical perspective will be
discussed.

#### Event Reconstruction {#sec:event_reco_stat}

The methods of event reconstruction, 
as described in [Section @sec:event_reco],
provide a very efficient way to transform the high-dimensional
detector readout to a lower-dimensional space that can more easily
be interpreted from a physical standpoint. In fact, reconstruction
can be viewed as a complex procedural technique of inference
on a subset of the latent variables given the detector
readout $\boldsymbol{x}$ of an event. These methods attempt
to walk back the generative chain described in
[Equation @eq:factor_joint] to recover the subset of the
parton-level $\boldsymbol{z}_\textrm{p}$ (and
$\boldsymbol{z}_\textrm{s}$ or $\boldsymbol{z}_\textrm{d}$ 
in some cases) that strongly depend on the detector
readouts and provide a compressed summary of the
information in the event
about the parameters of interest $\boldsymbol{\theta}$. The dimensionality
of the output of the reconstruction procedure $\boldsymbol{y}_\textrm{reco}$
depends on the subset of variables considered
for each physical object, which typically amounts to a total
of $\mathcal{O}(100)$ dimensions, which
is a significant reduction from
$\dim(\mathcal{X}) \rightarrow \mathcal{O}(10^8)$.

Due to the detector noise and characteristics, the reconstruction
function 
$\boldsymbol{f}_\textrm{reco}(\boldsymbol{x}) :
\mathcal{X} \longrightarrow \mathcal{Y}_\textrm{reco}$ cannot
fully recover $\boldsymbol{z}_\textrm{p} \in \mathcal{Z}_\textrm{p}$.
This is the case for
neutrinos that leave
the detector undetected, when the measured four-momenta of a
given particle differs from the real value or the when the reconstructed
particle does not even exist in $\boldsymbol{z}_\textrm{p}$. Simulated events
can then be used to make calibrated probabilistic
statements of the resulting reconstructed physical objects and their relation
with the actual unobserved particles going through the detector. Particle
identification (e.g. jet b-tagging) and fine-tuned momentum regressions 
on the reconstructed objects can also be thought of as
inference of latent variables, which amounts to using the additional
the detector information around an object to measure more
precisely its properties, such as the type of particle that produced the
detector readouts clustered in the former, and a more precise determination
of the momenta in the latter.

One aspect of the generative model that complicates both
reconstruction and statistical inference which has not
been discussed yet is that efficient representations of
the latent spaces of simulated events are not easily represented
as a fixed-size real vector
$\boldsymbol{z} \in \mathcal{Z} \subseteq \mathbb{R}^o$. Let us
consider as an example the parton-level latent information
$\boldsymbol{z}_\textrm{p}$, which amounts to a short list of
produced particles. The total number of particles and the number of particles
of each type are variable, thus $\boldsymbol{z}_\textrm{p}$
is better represented by a set (or several sets, one for each
particle type):
$$
\boldsymbol{z}_\textrm{p}^\textrm{set} =
 \{ \boldsymbol{z}_\textrm{p}^\textrm{i} \ | \
  i \in \{{1,...,n_\textrm{p}} \} \}
$$ {#eq:set_parton}
where $n_\textrm{p}$ is the total number of particles produced
at parton-level and $\boldsymbol{z}_\textrm{p}^\textrm{i}$ are the
latent variables associated to each particle (i.e. type, four-momenta, charge,
colour and spin). A similar set structure can be attributed
to latent variables describing long-lived particles
after the  parton-shower $\boldsymbol{z}_\textrm{s}$, while additional
variables might be associated to each particle (e.g. production vertex)
and total number and type diversity would be considerably larger.
Because the number of particles and their type greatly
varies between different interaction processes, the mapping this
structure to observable variable space is very useful. In fact,
the result of the general event reconstruction process at CMS
can be expressed also as a set of physical objects:
$$
\boldsymbol{y}_\textrm{reco}^\textrm{set} =
 \{ \boldsymbol{y}_\textrm{reco}^\textrm{i} \ | \
  i \in \{{1,...,n_\textrm{reco}} \} \}
$$ {#eq:set_reco}
where $n_\textrm{reco}$ is the total number of particles
$\boldsymbol{y}_\textrm{reco}^\textrm{i}$ are the reconstructed variables
for each physical object (i.e. reconstructed type, reconstructed four-momenta,
reconstructed charge and any other reconstructed attributes). The calibration
between the reconstructed physical objects
$\boldsymbol{y}_\textrm{reco}^\textrm{set}$ and the actual particles produced
in the collision $\boldsymbol{z}_\textrm{p/s}^\textrm{set}$ hence
amounts to matching set elements (typically based
on a $\Delta R$ distance criterion, see [Section @sec:exp_geom]) and the
comparison of their reconstructed and generated attributes.

The fact that both reconstructed and latent spaces have a variable-size
set structure greatly complicates the application of inference and
learning techniques directly based on
$\boldsymbol{y}_\textrm{reco}^\textrm{set}$, because they often
can only deal with a fixed-size vector of real numbers $\mathbb{R}^b$.
Similarly to what is done for event selection, often the elements
in the set of reconstructed objects in an event are reduced
by imposing a given condition based on their attributes (e.g. type,
isolation or momenta). There exist naive ways to embed a set
such as $\boldsymbol{y}_\textrm{reco}^\textrm{set}$ as a fixed-size
vector $\mathbb{R}^b$, such as taking the relevant attributes of
the first $n_\textrm{sel}$ objects according to a specific
ordering convention after a given *object selection*
and possibly padding with zeros or alternative numerical values the elements
that do not exist for a given event. Some of the newer machine
learning techniques that will be presented in [Chapter @sec:machine_learning]
can deal with variable-size input, such as sequences, sets or graphs inputs,
by *embedding* them in vector representations internally,
which provides new
ways to deal with the mentioned representational issue.


#### Summary Statistics {#sec:summary_statistic}

The attributes of the subset of reconstructed objects selected in an event
for a given analysis,
often as a fixed-size vector
$\boldsymbol{y}_\textrm{sel} \in \mathcal{Z}_\textrm{sel} \subseteq \mathbb{R}^{b}$
representation of them,
are still often too high-dimensional
to be considered directly for statistical inference. The effectiveness
of the likelihood-free techniques that will be presented later in this chapter
strongly depend on the dimensionality of the observable space considered.
Hence, it is desirable to further combine the reconstructed outputs in
a lower dimensional *summary statistic*, which can be either a function
of each single observation
or a set of multiple observations, so simpler statistical models that
relate the parameters of interest with the observations can be constructed.

Until now, we have been dealing with the problem of how a single event
is distributed $p ( \boldsymbol{x}|\boldsymbol{\theta})$,
however in practice a collection
$D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$ of events
is considered for inference. Let us first consider again the set $D$,
before any trigger or event selection, similarly to what was done
at the beginning of [Section @sec:model_overview].
Because of the independence between events, the
probability density of a given set $D$ can be expressed as the product
of individual probability densities for each event $\boldsymbol{x}_i$:
$$
p(D | \boldsymbol{\theta}) = \prod^{\boldsymbol{x}_i \in D}
p ( \boldsymbol{x}_i|\boldsymbol{\theta} )
$$ {#eq:before_sel_prod}
where $p ( \boldsymbol{x}_i|\boldsymbol{\theta} )$ can only be modelled
realistically
by forward simulation, and
has the mixture model structure and latent factorisation discussed before.
After an arbitrary event selection $\mathbb{1}_\mathcal{C} (\boldsymbol{x})$,
only a subset of events 
$D_\mathcal{C} = \{\boldsymbol{x}_0,...,\boldsymbol{x}_{n_\mathcal{C}}\} \subseteq D$
remain. These events are also independent,
so their probability density can be expressed as:
$$
g(D_\mathcal{C} | \boldsymbol{\theta}) = \prod^{\boldsymbol{x}_i \in D_\mathcal{C}}
g ( \boldsymbol{x}_i|\boldsymbol{\theta} )
$$ {#eq:after_sel_prod}
where the dependence between the distribution function after the event selection
$g ( \boldsymbol{x}_i|\boldsymbol{\theta} )$ and that before 
$p ( \boldsymbol{x}_i|\boldsymbol{\theta} )$ was already described in
[Equation @eq:mixture_after_cut]. If we only focussed on the probability
distribution of the events in $D_\mathcal{C}$, we would be neglecting
an important quantity that can also provide information about the
parameters of interest: the total number of events that pass the event
selection $n_\mathcal{C}$. Because this quantity depends on the set
of recorded readouts D, where each individual readout $\boldsymbol{x}_i$
is assumed to be an independent and identically distributed variable, the total
number of selected events $n_C$ after a deterministic selection
$\mathbb{1}_\mathcal{C} (\boldsymbol{x})$ can be modelled using
a binomial distribution:
$$
p( n_\mathcal{C} | n, \boldsymbol{\theta}) = \textrm{Binomial}(n, \epsilon)
\approx \textrm{Poisson}(n\epsilon)
$$ {#eq:binomial_selection}
where the dependence on the parameters is contained in the total
efficiency 
$\epsilon = \int \mathbb{1}_\mathcal{C}(\boldsymbol{x}) p
(\boldsymbol{x}|\boldsymbol{\theta})$. The Poisson approximation is justified
because the number of trials $n$ is sufficiently large (i.e. 40 million
bunch crossings per second) and the total
selection efficiencies $\epsilon \leq 0.000025$ already at trigger level,
as discussed in [Section @sec:trigger]. This type of stochastic process is
also referred to in the literature as multi-dimensional
homogenous Poisson point process [@Gardiner:732221].
The expected value of $n_C$ coincides
with the Poisson mean $n\epsilon$, and can be more intuitively linked with
the parameters of interest $\theta$ by making explicit the contributions from
the different mixture processes:
$$
\mathop{\mathbb{E}}_{D \sim p ( D |\boldsymbol{\theta} )}
\left [ n_\mathcal{C} \right ] = n \sum^{K-1}_{j=0} \phi_j 
\mathop{\mathbb{E}}_{x \sim p_j ( \boldsymbol{x}|\boldsymbol{\theta} )}
\left [\mathbb{1}_\mathcal{C} (\boldsymbol{x}) \right ] =
n \sum^{K-1}_{j=0} \phi_j \epsilon_j
$$ {#eq:exp_selected}
where the efficiency for each process
$\epsilon= \int \mathbb{1}_\mathcal{C}(\boldsymbol{x}) p_j
(\boldsymbol{x}|\boldsymbol{\theta})$ can be estimated using simulated
observations as shown in [Equation @eq:montecarlo_eff]. In principle,
all possible processes $j$ that could occur have to be considered, i.e.
cases when no hard collision occurred
as well as the inclusive contribution of each possible hard process,
as described in [Equation @eq:hard_prob]. However, if the product of the
expected probability of a given process occurring  $\phi_j$ and the
event selection efficiency $\epsilon_j$ is low enough
relative to the total efficiency $\epsilon=\sum^{K-1}_{j=0} \phi_j \epsilon_j$,
the effect of those mixture components can be safely neglected. 

The situation discussed above is
often the case for events where no hard collision occurred after some
basic event selection, that is $\epsilon_\textrm{not-hard} \approx 0$ which
can thus
can be neglected.
For the subset of bunch crossing cases where hard interactions occur,
the probability of a given type of interaction before any event selection
might be expressed as the product of its cross section $\sigma_j$ by the total
integrated luminosity during the data taking period $\mathcal{L}_\textrm{int}$ 
divided by the total number of bunch crossings, thus
the expected value for number of observations $n_\mathcal{C}$ after
an event selection that reduces enough the contribution of non-hard
processes $\mathbb{1}_\mathcal{C} (\boldsymbol{x})$ can also be expressed as:
$$
\mathop{\mathbb{E}}_{D \sim p ( D |\boldsymbol{\theta} )}
\left [ n_\mathcal{C} \right ] =
n \sum^{K-1}_{j=0} \frac{\mathcal{L} \sigma_j}{n }\epsilon_j =
\mathcal{L} \sum^{K-1}_{j=0}  \ \sigma_j \  \epsilon_j
$$ {#eq:exp_cross_section}
where $n_j=\mathcal{L} \ \sigma_j \  \epsilon_j$ is the expected number
of events coming from a given process $j$, that can be estimated with theoretical
input regarding $\sigma_j$, simulated observations to estimate $\epsilon_j$
and an experimental measurement of the luminosity $\mathcal{L}$.

The number of observations $n_\mathcal{C}$ that pass a given event selection
$\mathbb{1}_\mathcal{C} (\boldsymbol{x})$, which normally includes trigger
and some additional analysis dependent selection, is the quantity that serves
as the basis of the simplest statistical model used in particle physics
to link theoretical parameters and observations. This type of summary statistic
is very effective when the parameter of interest is the cross section
of a single process $\sigma_S$ and rest of background processes are
well modelled
by theoretical predictions and simulated observations. In that case, if
all parameters but $\sigma_S$ are known, a *cut-and-count* sample-based
likelihood can be built based on [Equation @eq:binomial_selection], corresponding
to the following probability density function:
$$
p ( n_\mathcal{C} | \sigma_S) = \textrm{Poisson} 
\left (\sigma_s\epsilon_s + \sum^{j \in B} \sigma_j\epsilon_j \right)
$$ {#eq:poisson_simple}
which can be used to carry out statistical inference about $\sigma_S$
given an observed number of events that pass the event selection
$n_\mathcal{C}^\textrm{obs}$, using classical techniques.

The previous concept can be applied to several disjoint
subsets of $\mathcal{X}$ simultaneously
$T=\{\mathcal{C}_0,...,\mathcal{C}_b\}$, each characterised by a different
indicator function $\mathbb{1}_{\mathcal{C}_t} (\boldsymbol{x})$ defining
an arbitrary event selection, as long as their intersection is null.
The probability function for the variable
$\boldsymbol{n}_T = \{n_{\mathcal{C}_0},...,n_{\mathcal{C}_b}\}$, given
that each $n_{\mathcal{C}_i}$ is independent, can be obtained as:
$$
p ( \boldsymbol{n}_T | \boldsymbol{\theta}) = \prod^{\mathcal{C}_i \in T} 
\textrm{Poisson}
\left (\sum^{j \in H} n^{\mathcal{C}_i}_j(\boldsymbol{\theta}) \right )
$$ {#eq:poisson_multichannel}
where $n^{\mathcal{C}_i}_j(\boldsymbol{\theta})$ is the expected number of
observed events coming from process $j$ after the selection $\mathcal{C}_i$.
As long as a parametrisation of $n^{\mathcal{C}_i}_j(\boldsymbol{\theta})$
exists,
which can be often estimated as
$n^{\mathcal{C}_i}_j(\boldsymbol{\theta}) =\mathcal{L} \ \sigma_j \ 
\epsilon^{\mathcal{C}_i}_j(\boldsymbol{\theta})$,
[Equation @eq:poisson_multichannel] can be used 
to construct a likelihood to carry out inference on the
parameters $\boldsymbol{\theta}$ based on the observed value
of the sample summary statistic $\boldsymbol{n}_T^\textrm{obs}$.

#### Sufficient Statistics {#sec:suff_stats}

The selection count vector $\boldsymbol{n}_T^\textrm{obs}(D)$, which has not been
specified yet, could be also written
as a sum over a function 
$\boldsymbol{n}_T(\boldsymbol{x}) : \mathcal{X} \subseteq \mathbb{R}^{d} \longrightarrow \mathcal{Y}
\subseteq \{0,1\}^b \subset \mathbb{R}^{b}$
applied for each event
in $D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$ as follows:
$$
\boldsymbol{n}_T^\textrm{obs}(D) = \sum^{\boldsymbol{x}_i \in D} \boldsymbol{n}_T(\boldsymbol{x})
$$ {#eq:sum_count_vector}
where $\boldsymbol{n}_T^\textrm{obs}(D)$ could be described as a summary
statistic of the whole collection of observations while
$\boldsymbol{n}_T(\boldsymbol{x}_i)$ summarises a single event
$\boldsymbol{x}_i$.

There are infinite ways to choose a lower-dimensional
summary statistic of the detector readout
$\boldsymbol{s}(\boldsymbol{x}) : \mathcal{X} \subseteq \mathbb{R}^{d}
\longrightarrow \mathcal{Y}\subseteq \mathbb{R}^{b}$. Functions of the
type $\boldsymbol{n}_T(\boldsymbol{x})$ are a reduced subset, yet still
infinite, of the possible space of functions. Regardless of
the likelihood-free inference methods considered
(see [Section @sec:stat_inf]), the need of a
low-dimensional summary statistic is a direct consequence of
the *curse of dimensionality*, because the number of simulated observations
required to realistically model the probability density function
or compute useful distance measures rapidly increases with the number of
dimensions.

In general, the selection of a summary statistic
$\boldsymbol{s}(\boldsymbol{x})$ is far from trivial, and naive choices
can lead to large losses of useful information about the parameters of 
interest $\boldsymbol{\theta}$. Results form classical statistics identifies 
a *sufficient summary statistic* as the
the optimal summary statistic to be used for inference for a given
statistical model and characterises its properties [@hogg1995introduction].
Such a sufficient statistic
contains all the information
in the observed sample useful to compute any estimate on the model parameters.
Sufficient statistics can be formally characterised using the
Fisher-Neyman factorisation criterion, which states that a summary
statistic $\boldsymbol{s}(\boldsymbol{x})$ is sufficient if and only if
the probability
distribution function of $\boldsymbol{x}$ can be factorised as follows:
$$
p(\boldsymbol{x} | \boldsymbol{\theta}) = 
q(\boldsymbol{x})
r(\boldsymbol{s}(\boldsymbol{x}) | \boldsymbol{\theta})
$$ {#eq:sufficient_single}
where $q(\boldsymbol{x})$ is a non-negative function that does not depend
on the parameters and $r(\boldsymbol{x})$ is also a non-negative
function for which the dependence on the parameters $\boldsymbol{\theta}$
is a function of the summary statistic $\boldsymbol{s}(\boldsymbol{x})$. The
definition of sufficiency can also be applied to a collection of observations
$D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$. In fact if we assume
they are independent and identically distributed, and
$\boldsymbol{s}(\boldsymbol{x})$ is sufficient for each observation
$\boldsymbol{x}_i$,
we may rewrite [Equation @eq:before_sel_prod] as:
$$
p ( D |\boldsymbol{\theta}) =
\prod^{\boldsymbol{x}_i \in D} q(\boldsymbol{x}) 
\prod^{\boldsymbol{x}_i \in D}
r(\boldsymbol{s}(\boldsymbol{x}_i) | \boldsymbol{\theta}) =
q(D) r(\boldsymbol{s}(D)| \boldsymbol{\theta})
$$
where the set of sufficient summary statistics for each observation
is a sufficient summary statistic for the whole dataset
$\boldsymbol{s}(D) = \{ \ \boldsymbol{s}(\boldsymbol{x}_i) \ | \ \forall \boldsymbol{x}_i  \in D \}$
and the dependence on the summary statistic is contained as the product
of independent factors for each observation.

Because $p(\boldsymbol{x} | \boldsymbol{\theta})$ is not available in closed form
in particle collider experiments, the general task of finding a sufficient
summary statistic by analytic means cannot be tackled directly. However, for
finite mixture models where the only model parameters are a function of
the mixture coefficients $\phi_j$, probabilistic classification can
be used to obtain (approximate) sufficient summary statistics. We wiill
return to this topic in [Chapter @sec:machine_learning]. When the parameters
of interest or additional unknown parameters affect the mixture components
$p_j(\boldsymbol{x} | \boldsymbol{\theta})$, the construction of
sufficient summary statistics cannot be tackled directly, thus information
about the parameters $\boldsymbol{\theta}$  is lost in the dimensionality
reduction step. An automated way to obtain powerful summary statistics
in those cases using machine learning techniques will be presented in
[Chapter @sec:inferno].


#### Synthetic Likelihood {#sec:synthetic_likelihood}

The advantage of using lower-dimensional summary statistics
$\boldsymbol{s}(D) : \mathcal{X}_D \subseteq \mathbb{R}^{d\times n}
\longrightarrow \mathcal{Y}_D \subseteq \mathbb{R}^{b\times n}$ of the
detector readout collected by the experiment is that often the
generative model of $p(\boldsymbol{x} | \boldsymbol{\theta})$ can
be used to build synthetic likelihoods of $s(D)$ that 
link the observations with the model parameters, so classical inference
algorithms can be used. 

For summary statistics of the type $\boldsymbol{n}_T^\textrm{obs}(D) :
\mathcal{X}_D \subseteq \mathbb{R}^{d \times n } \longrightarrow \mathcal{Y}_D \subseteq \{0,1\}^{b}$
the likelihood can be expressed as a product of independent Poisson
count likelihoods as shown in [Equation @eq:poisson_multichannel]. Such
likelihood can be evaluated for the observed data $D$ and specific parameters
$\boldsymbol{\theta}_R$, even in the case that $\boldsymbol{\theta}$
modifies the distribution of the mixture components
$p_j(\boldsymbol{x} | \boldsymbol{\theta})$, by forward approximating 
$n^{\mathcal{C}_i}_j(\boldsymbol{\theta}_R)$ (or alternatively
$\epsilon^{\mathcal{C}_i}_j(\boldsymbol{\theta}_R)$) using simulated observations
for each process $j$ generated for $\boldsymbol{\theta}_R$.
This process would rapidly become computationally very demanding if it had to
be repeated for each likelihood evaluation during the whole inference process.
Re-weighting procedures such as those described in
[Equation @eq:gen_level_reweighting] can often be applied
to re-use already simulated
events using $\boldsymbol{\theta}_R$ to model events corresponding
to different values of the parameters $\boldsymbol{\theta}_Q$.

A more economical approach, commonly used in LHC analyses that use binned
Poisson likelihoods based on the formalism introduced in
[Equation @eq:poisson_multichannel], is to parametrise the effect of varying
parameters by interpolating between the values of the
$\epsilon^{\mathcal{C}_i}_j(\boldsymbol{\theta}_k)$ (or directly
$n^{\mathcal{C}_i}_j(\boldsymbol{\theta}_R)$) for different values
of $k$. Such parametrisation allows the analytical approximation
of the likelihood originated by [Equation @eq:poisson_multichannel],
and simplifies the computation of gradients with respect to
the parameters. This is particularly relevant to model the effect of
*nuisance parameters*, which are uncertain but not of direct interest,
and have
to be accounted for in the inference procedure; this issue will be discussed
in [Section @sec:known_unknowns]. Different interpolation conventions
exist [@Cranmer:2015nia], but they are normally based on the marginal
one-dimensional interpolation between the effect of a single parameter $\theta_i \in
\boldsymbol{\theta}$ at three equally spaced values (the nominal parameter values
and the up/down variations). In that case the total effect on
$\epsilon^{\mathcal{C}_i}_j(\boldsymbol{\theta}_k)$ is accounted by adding
absolute shifts or multiplying marginal effects. 

Even assuming that the marginal
description when a single parameter of interest varies
is accurate, which is not ensured by the interpolation, and the effect
of each parameter is factorised in $p_j(\boldsymbol{x} | \boldsymbol{\theta})$,
the integral definition of $\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta}_k)$
from [Equation @eq:montecarlo_eff] does not ensure that the correlated effect
of the variation of multiple $\theta_i \in \boldsymbol{\theta}$ is accurately
modelled. This issue can be easily exemplified, considering the
product of relative variations in the two parameter case
$\boldsymbol{\theta}_R = (\theta^R_0,\theta^R_1)$.  Let us consider the expected
value for the efficiency after a given selection $\mathbb{1}_{\mathcal{C}_i}(\boldsymbol{x})$:
$$
\begin{aligned}
\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta}_R) &=  \int 
\mathbb{1}_\mathcal{C}(\boldsymbol{x})
p_j ( \boldsymbol{x}|\boldsymbol{\theta}_R ) d\boldsymbol{x} \\
&=
\int \mathbb{1}_\mathcal{C}(\boldsymbol{x}) 
p_j ( \boldsymbol{x}|\boldsymbol{\theta}_Q )
\frac{p_j ( \boldsymbol{x}| (\theta^R_0,\theta^Q_1))}{p_j ( \boldsymbol{x}|\boldsymbol{\theta}_Q )}
\frac{p_j ( \boldsymbol{x}| (\theta^Q_0,\theta^R_1))}{p_j ( \boldsymbol{x}|\boldsymbol{\theta}_Q )}
 d\boldsymbol{x}
\end{aligned}
$$ {#eq:relative_var_integral}
where $\boldsymbol{\theta}_R$ is the parameter point we want to simulate
by interpolating around a nominal point $\boldsymbol{\theta}_Q$. The last
expression in [Equation @eq:relative_var_integral] is only correct when
the effect of each parameter is independent, i.e. the underlying probability
density function can be factorised as the product of independent factors.
However, it becomes evident
that the previous expression does not simplify:
$$
\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta}_R) \neq
\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta}_Q)
\frac{\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta}_R)}{
\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta}_Q)}
\frac{\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta}_R)}{
\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta}_Q)}
$$ {#eq:relative_var_eff}
because the integral of the product of functions is not product of integrals,
unless is the volume of the selected region $C$
is infinitesimally small - an irrelevant case as it would
correspond to null efficiencies. This
effect also applies if additive variations are considered and can be more
notable when more parameters are considered.

The previously mentioned modelling issue, even though to the best of
our knowledge has not been
made explicit in the literature before, affects a multitude of analyses at
the LHC, i.e. those that
use  *template interpolation*, as implemented in
the standard statistical libraries used in particle physics experiments
[@Conway:2011in;@Cranmer:2012sba].
A possible solution would include doing a multi-dimensional interpolation,
but it would naively require evaluating at least all 3-point combinatorial variations
of the parameters, amounting to a minimum of $3^p$ evaluations of
$\epsilon^{\mathcal{C}_i}_j (\boldsymbol{\theta})$, where $p$ is the number
of parameters. If the effect of the parameters can be factored out in the
joint distribution and the same simulated event set can be modified to describe
each marginal variation, as reviewed around [Equation @eq:latent_reweighting],
the non-marginal terms can be estimated from the
product of per-event marginal terms by considering the finite sum approximation
of the last expression in [Equation @eq:relative_var_integral], which would
only require $(2p+1)$ parameter variation evaluations.
Alternatively, the basis of the approach presented in
[Chapter @sec:inferno], where the variation of the parameters and
its derivatives are computed in place over the simulated observations by
specifying the full computational graph, could also be used in analyses
where the discussed assumption fails to realistically describe the data.

<!-- TODO: parametric and non-parametric likelihood -->


### Known Unknowns {#sec:known_unknowns}

So far we have assumed that the simulated observations can model the data
and the only parameters $\boldsymbol{\theta}$ that affect the
generative model are those we are interested in carrying out inference on.
However, simulated observations effectively depend on the
modelling of the physical processes occurring in the proton-proton
collisions and the detector, of which we only have an approximate
description. Those mis-modelling effects have to be accounted in the
inference procedure to obtain unbiased estimates, and are accounted
by additional *nuisance parameters* in the statistical model when the
effect is known and can be approximated. For cases where
simulation does not provide the desired level of accuracy,
the contribution from some of the mixture components can 
often be estimated from data directly, using what are referred to
as *data-driven estimation* techniques.

#### Nuisance Parameters {#sec:nuis_pars}

The general definition of nuisance parameters in a statistical model refers
to all the uncertain parameters of the statistical model that are not
of intermediate interest but have to be accounted for in the inference procedure.
These parameters can include uncertain theoretical parameters (e.g.
top quark mass or expected background rate), account for
limitation on the experimentally measured parameterisations of certain
phenomena (e.g. parton density functions uncertainties) or represent
the accuracy limits of calibration between data and simulation. Nuisance
parameters can also represent additional degrees of freedom in the model
that cover for possible wrong assumptions or quantify imprecisions
due to the limited number of simulated observations.

Because the actual generative process for the experimental data is not known
perfectly, the simulation-based model is extended with additional parameters
that portray the possible variability on the distribution of the detector
readouts. The formalism developed in the previous part of
[Section @sec:stat_model] still applies, noting that the parameter vector
$\boldsymbol{\theta}=\{\boldsymbol{\theta}_\iota,\boldsymbol{\theta}_\nu\}$ now
includes both parameters of interest $\boldsymbol{\theta}_\iota$
and nuisance parameters $\boldsymbol{\theta}_\nu$. While the effect of
(theoretical) parameters of interest typically only affects the parton-level
latent factor $p(\boldsymbol{z}_\textrm{p} | \boldsymbol{\theta})$, some
nuisance parameters account for possible mis-modelling in subsequent
steps of the simulation thus can affect the other factors in
[Equation @eq:factor_joint].

The effect of variation of nuisance parameters for any observable or
summary statistic
considered in a given analysis can be estimated by simulating again the
affected observation with the chosen parameters, which is often prohibitively
expensive, or by re-weighting already simulated observations as described
in [Equation @eq:latent_reweighting], which is much faster and reduces
the statistical fluctuations between variations associated with the
random sampling of the full latent space. Unprincipled modelling
shortcuts, such as considering the additive or multiplicative effect of
marginal efficiencies to account for combined effects,
are also frequently used for count vector observables
$n^{\mathcal{C}_i}_j(\boldsymbol{\theta})$, as discussed in
[Equation @eq:relative_var_eff] together with possible solutions
to mentioned issues.

The re-weighting approach from [Equation @eq:reweight_intractable] is
extremely
effective to model the effect of parameters in the conditional factor
that deal with low-dimensional latent variables, such as
$p(\boldsymbol{z}_\textrm{p} | \boldsymbol{\theta})$, because the rest of the factors
in the joint distribution simplify and we are left with a low-dimensionality
density estimation problem (even analytically tractable in some cases).
For conditional factors that deal with higher dimensional latent or
observable spaces, such as
$p(\boldsymbol{z}_\textrm{d} |\boldsymbol{z}_\textrm{s}, \boldsymbol{\theta})$
or
$p(\boldsymbol{x} |\boldsymbol{z}_\textrm{d}, \boldsymbol{\theta})$,
the ratio can be very hard to estimate unless additional simplifications
are possible. For those nuisance parameters, it is easier to consider the effect on
the lower-dimensional summary statistic instead of the detector readout $x$,
because the ratio:
$$
w(\boldsymbol{s}(\boldsymbol{x})) =
\frac{p_R(\boldsymbol{s}(\boldsymbol{x})|\boldsymbol{\theta}_R)}{
p_Q(\boldsymbol{s}(\boldsymbol{x})|\boldsymbol{\theta}_Q)}
$$ {#eq:reweight_summary}
can be simpler to estimate through density estimation or approximately
factorise if the summary statistic is chosen carefully. This fact
motivates an alternative way to model the effect of some of the nuisance
parameters,
especially those related with the differences in the reconstructed
objects observables between simulation and data after calibration. Let us
consider the case where summary statistics
$\boldsymbol{s}(\boldsymbol{x}) : \mathcal{X} \subseteq \mathbb{R}^{d}
\longrightarrow \mathcal{Y}_\textrm{sum} \subseteq \mathbb{R}^{b}$
are effectively function of the
reconstructed objects
and its properties $\boldsymbol{y}_\textrm{reco} \in \mathcal{Y}_\textrm{reco}$,
which can be schematically
represented by the following function composition chain:
$$
\mathcal{X} \overset{g}{\longrightarrow} \mathcal{Y}_\textrm{reco} \overset{h}{\longrightarrow} \mathcal{Y}_\textrm{sum}
$$ {#eq:composition_summary}
where $\boldsymbol{y}_\textrm{reco} = g(\boldsymbol{x})$ and
$\boldsymbol{y}_\textrm{sum} = h(\boldsymbol{y}_\textrm{reco})$. This
compositional approach can be extended to include also event selection
at trigger or analysis level, or other intermediate
summaries of $\boldsymbol{x}$ complementary to reconstruction, as part
of the definition of the summary statistic $\boldsymbol{s}(\boldsymbol{x})$.
In all cases where $s(\boldsymbol{x})$ is a deterministic function,
all differences between simulated
observations and data in any expected observables
originate from the differences between the
simulation-based generative 
definition of $p(\boldsymbol{x} | \boldsymbol{\theta})$ and the true
unknown generative process $p_\textrm{true}(\boldsymbol{x})$. While
the task of evaluating and parametrising these differences directly by studying
the raw detector output is quite convoluted, the differences can
be corrected and their uncertainty assessed for the
lower-dimensional intermediate states of the composition chain depicted
in [Equation @eq:composition_summary]. 

For example, if the momenta of a
certain subset of the reconstructed objects $\boldsymbol{y}_\textrm{reco}$
statistically differ between experimental data and
the simulated observations, based on a subset of the data that
is assumed to be well-modelled, the momenta of simulated observations
can be corrected to better model the data. The statistical
accuracy of such procedure due to the different factors leads
to a set of nuisance parameters that describe the limit of
the mentioned calibration as a function of the value of
$\boldsymbol{y}_\textrm{reco}$. The effect of these type of nuisance
parameters often be modelled in the simulation by using
a function of the simulated intermediate outputs, e.g.
in the case of reconstructed objects:
$$
\mathop{\mathbb{E}}_{\boldsymbol{x} \sim  p( \boldsymbol{x}| \boldsymbol{\theta} )}
\left [ \boldsymbol{s}(\boldsymbol{x}) \right ] = 
\mathop{\mathbb{E}}_{\boldsymbol{y}_\textrm{reco} \sim  p( \boldsymbol{y}_\textrm{reco}| \boldsymbol{\theta}_o )}
\left [ h(r(\boldsymbol{y}_\textrm{reco}, \boldsymbol{\theta}_\rho))\right ]
$$ {#eq:exp_rep}
so $p( \boldsymbol{x}| \boldsymbol{\theta} )$ can be approximated
by computing observables after
applying the re-parametrisation
$r(\boldsymbol{y}_\textrm{reco}, \boldsymbol{\theta}_\rho)$ to the
simulated observations,
where $\boldsymbol{\theta}_\rho$ is the vector of parameters
representing the different uncertainty factors.

In general, the effects of all relevant 
nuisance parameters can be modelled
by a combination of simulated observation re-weighting by
$w(\boldsymbol{x}_i,\boldsymbol{z}_i | \boldsymbol{\theta}_w )$
and transformations of intermediate simulated observations
$\boldsymbol{y}_\textrm{new} = r(\boldsymbol{y}_\textrm{sim},\boldsymbol{z}_i | \boldsymbol{\theta}_\rho)$. The former is based on
importance sampling [@mcbook] to estimate the properties of a different
distribution than the one sampled originally from, while the latter
assumes that the mis-modelling can be accounted by a parametrisation
of the simulated intermediate observables. If the functions
$w(\boldsymbol{x}_i,\boldsymbol{z}_i | \boldsymbol{\theta}_w )$
and $r(\boldsymbol{y}_\textrm{sim},\boldsymbol{z}_i | \boldsymbol{\theta}_\rho)$
are differentiable or can approximated by differentiable functions,
the gradient (and higher order derivatives) with
respect to the parameters $\boldsymbol{\theta}$ of any expectation
value can be very efficiently approximated. This can be very useful
for statistical inference (e.g. likelihood minimisation),
while it has not been
used so far in LHC analysis to our knowledge. This is
one of the core concepts of the technique to construct summary statistics
presented in [Chapter @sec:inferno].

The inference results of a given analysis depend strongly on the
assumptions implicit in the statistical model. The determination,
assessment and practical definition of the effect of nuisance parameters
that are relevant for a given analysis is one the most challenging
yet important aspects in experimental particle physics at the LHC. When
nuisance parameters are quantitatively taken into account in the statistical
model, they lead to an increase of the uncertainty on the parameters of interest
and larger interval width estimates (or exclusion limits)
on the parameters of interest.
The choice of summary statistics may also affect
significantly subsequent inference,
and while nuisance parameters are usually qualitatively considered when
building simple summary statistics by physics-inspired combinations
of reconstructed variables, they are not regarded at all when the automatic
multi-variate techniques described in [Chapter @sec:machine_learning]
are applied to construct complex non-linear observables. This issue is
address by the method proposed in [Chapter @sec:inferno].

#### Data-Driven Estimation {#sec:data_driven}

For some fundamental processes, the generative
modelling provided by simulated observations
might not be accurate enough for the purposes of a given LHC analysis. 
In a subset of those cases, the simulated observations can be calibrated
to better describe the observations in well-modelled data regions, as
mentioned in the previous section. However, if the description of
the summary statistics considered in the analysis provided
by the simulated observations from process $j$ is substandard,
e.g. the number of simulated observations that could be 
realistically simulated is not sufficient, then
the contribution from the mentioned mixture component might have
to be estimated from experimental observations directly.

The actual procedure used for modelling the contribution for a given
mixture component $j$ from data depend on the specifics of the
process as well the details
analysis considered, but often includes some re-weighting
factor obtained from simulated observations or additional experimental
observations with an orthogonal selection criterion. Such data-driven
estimation techniques are often used for the background processes,
but are hard to combine with the non-linear summary statistics reconstructed
by machine learning techniques such as those described in
[Chapter @sec:machine_learning]. In the CMS analysis presented in
[Chapter @sec:higgs_pair], we describe and utilise a fully data-driven
background estimation technique fine-tuned for the modelling of
the QCD-based multiple jet background for the search of Higgs
pair production decaying to four b-quarks.

## Statistical Inference {#sec:stat_inf}

In the previous section, the main characteristics of the generative
statistical model $p(D | \boldsymbol{\theta})$ used
to relate the parameters $\boldsymbol{\theta}$ with the set
of observations $D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$
have been reviewed.
In addition, we discussed the role of summary statistics
as lower dimensional functional transformations of each detector readout
$\boldsymbol{s}(\boldsymbol{x}_i)$  or even the whole dataset
$\boldsymbol{s}(D)$, as well as how the effect of additional uncertain
parameters can be included in the simulation-based generative
model of the data. In this section, we deal with the actual problem
of inference about the subset of parameters of interest
$\boldsymbol{\theta}_\iota$ once a summary statistic has already been
chosen and the final statistical model
$p(\boldsymbol{s}(D) | \boldsymbol{\theta})$ has been fully specified. 

### Likelihood-Free Inference {#sec:likelihood-free}

One of the main properties of the statistical models at particle colliders
we focussed on in the last section was their generative-only nature,
whereby their probability density $p(\boldsymbol{x} | \boldsymbol{\theta})$
cannot be expressed analytically, but only
by means of forward simulated observation. This fact greatly complicates the
application of standard inference techniques which require the
explicit definition of a likelihood
$$L(\boldsymbol{\theta} | D) =\prod^{\boldsymbol{x}_i \in D}
 p(\boldsymbol{x}_i | \boldsymbol{\theta})
$$ {#eq:likelihood_definition}
in order to make quantitative statements about the parameters of interest,
because it expresses the extent to which a set of values for
the model parameters are consistent with the observed data .
Problems where the likelihood cannot be expressed directly are common
in many scientific disciplines, because a link between
observations and the underlying parameters can often only be provided by
a probabilistic computer program when the system under study
is sufficiently complex, e.g. can only be described by
a hierarchy or a sequence
of stochastic processes.

While the evaluation of the likelihood for complex generative models
rapidly becomes impractical, especially when the space of observations
or parameters is very high-dimensional, various statistical techniques
for dealing with these cases exist, generally referred to as
*likelihood-free* or *simulation-based* inference techniques. A well
established group of techniques for inference when the likelihood
function is unknown is referred to as Approximate Bayesian Computation (ABC)
[@rubin1984bayesianly; @beaumont2002approximate]. The fundamental concept
behind ABC is the generation of a simulated sample
$S_0 = \{\boldsymbol{x}_0,...,\boldsymbol{x}_m\}$
using a given vector of parameters $\boldsymbol{\theta}_0$, which is then
compared using a distance criterion to the actual observed dataset $D$. If
the data and the simulation are close enough, then
$\boldsymbol{\theta}_0$ is retained as sample from the 
posterior. The
process is repeated until the posterior is estimated with the
desired accuracy. The quality of the posterior approximation
produced by ABC techniques, as well as the number of
sampling steps required to reach a given accuracy, strongly
depend on the distance definition. When the dimensionality
of the output is high, a summary statistic vector
$\boldsymbol{s}(\boldsymbol{x})$ must be used has in practice to increase
the computational efficiency of the previous procedure.

The approach commonly used when carrying our inference at
particle physics experiments at the LHC is somehow related from the
mentioned family of techniques. The observations are also reduced
to a lower-dimensional summary
statistic space, but then a synthetic likelihood is constructed
so that standard inference techniques can be applied. The likelihood
is often based on the product of Poisson count terms, as
depicted in [Equation @eq:poisson_simple] and [Equation @eq:poisson_multichannel],
where the dependence on the expectations
on the parameters is based on the simulation and the mixture
structure. Alternative approaches include the use of a simple one-dimensional
parametrisation for a continuous background and a bump-like signal,
which is common when the reconstructed mass of
an intermediate object is used as summary statistic and its response is
well-controlled, e.g. a Higgs bosons decaying to two photons.
An additional alternative approach, which has not been
used in LHC analyses to date, could be to use non-parametric density
estimation techniques to obtain a synthetic likelihood directly
from simulated data. This approach has been recently referred as Approximate
Frequentist Computation (AFC) [@Brehmer:2018eca], and can be also combined
with the technique presented in [Chapter @sec:inferno].


### Hypothesis Testing {#sec:hypo_test}

Statistical inference experimental particle physics is often
framed as a hypothesis testing problem. The goal of statistical
testing is to make a quantitative statement about how well observed
data agrees with an underlying model or prediction, which is often referred
to as a *hypothesis*. The statistical model under consideration
is often referred to as *null hypothesis* $H_0$.  Classical
statistical testing techniques often require the definition of an
*alternative hypothesis* $H_1$, whose agreement with the data
is compared with that of the null. A hypothesis is said to be
*simple*, when all the distribution (or generative model)
parameters are fully specified, i.e.
$p(\boldsymbol{x} | H_s) =f(\boldsymbol{x})$ does
not depend on any non-fixed parameter. A *composite* hypothesis
instead depends on one or more parameters $\boldsymbol{\theta}$,
i.e. the distribution under the hypothesis can be expressed as 
$p(\boldsymbol{x} | H_c) =f(\boldsymbol{x},\boldsymbol{\theta})$.

In order to carry out hypothesis testing based on a set of
observations $D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$,
a *test statistic* $t(D)$ that is a function
of the observations is constructed. The choice of
test statistic is especially critical when $\boldsymbol{x}$
is high-dimensional. The concepts of test statistic and summary
statistic, the latter discussed in [Section @sec:summary_statistic],
are very related. A test statistic is in fact a sample summary
statistic $s(D)$, that is used within statistical test to accept
or reject hypothesis, so all the concerns regarding
sufficiency from [Section @sec:suff_stats] also apply. Regarding
the dimensionality of $t(D) :
\mathcal{X}_D \subseteq \mathbb{R}^{d \times n } \longrightarrow \mathcal{T}$,
while it can be a multi-dimensional
vector (e.g. could even use $t(D)=(\boldsymbol{x}_0,...,\boldsymbol{x}_n)$),
a one dimensional variable is only considered in order to simplify
the process of making calibrated statistical statements.

Let us refer to the test statistic for the observed set of
observations as $t_\textrm{obs}$ from here onwards. The result of
the statistical test is whether the hypothesis $H_0$ can be
rejected in favour of $H_1$ if the null is unlikely enough. In
practice, in order to make a principled decision,
a critical region $\mathcal{T}_C \subseteq \mathcal{T}$ in the space of the test
statistic has to be defined before looking at the set of
observations. One the critical region has been
chosen, a test can be then characterised by its *significance*
level $\alpha$ and *power* $1-\beta$. The significance, which is also
referred to as the *Type I error rate*, is directly
related with the probability of rejecting $H_0$ when it is actually
true. For a given test based on the summary statistic $t(D)$ and its
critical region $\mathcal{T}_C$,
the significance level can be defined as:
$$
\alpha = P ( t \in \mathcal{T}_C | H_0) =
\int_{\mathcal{T}_C} g( t| H_0) dt 
\stackrel{\textrm{1D}}{=} \int_{t_\bold{cut}}^\infty  g( t| H_0) dt
$$ {#eq:significance_test}
where $g( t| H_0)$ is the distribution of the test statistic under the null
hypothesis $H_0$, and the latter simplification applies for one-dimensional
summary statistics where the critical region is defined based
on a given threshold $t_\textrm{cut}$. The power of a test $1-\beta$ is
instead defined by the probability of not rejecting the null hypothesis
when the alternative is actually true, which often referred as
*type II error rate* $\beta$. The type II error rate $\beta$ can
be defined as the probability of not being in the critical region
under the alternative hypothesis:
$$
\beta = P ( t \not\in \mathcal{T}_C | H_1) = 
1 - \int_{\mathcal{T}_C} g( t| H_1) dt 
\stackrel{\textrm{1D}}{=} 1 - \int_{-\infty}^{t_\bold{cut}}  g( t| H_1) dt
$$ {#eq:type2_test}
where $g( t| H_0)$ is the distribution of the test statistic under the
alternative hypothesis $H_1$, and the last terms corresponds to the
one dimensional case based on a threshold. Both significance level and
power of a test depend on the definition of its test statistic and
critical region.
The significance level
of a test $\alpha$ is often fixed at a given value in order to reject
the null in favour of an alternate, while is beneficial to design
the test so its power is as high as possible (equivalent to having a
Type II error rate as low as possible).

From the definition of Type I and Type II error rates
in [Equation @eq:significance_test] and [Equation @eq:type2_test],
it is evident that either the probability
distribution function of the test statistic under both the null
and alternate hypothesis or a way to estimate the integrals from
simulated observation are required. The main advantage of
one-dimensional statistics, similarly to low-dimensional summary
statistics, allows for an efficient estimation of the probability
distribution function using non-parametric techniques.
When both the null $H_0$ and alternate hypothesis $H_1$ are simple,
the Neyman-Pearson lemma [@NeymanPearson1933] states that the
*likelihood ratio*, which is a one-dimensional test statistic
defined as:
$$
\Lambda( \mathcal{D}; H_0, H_1) = \frac{p(D| H_0)}{p(D| H_1)} = 
\prod_{\boldsymbol{x} \in \mathcal{D}}
\frac{p(\boldsymbol{x}| H_0)}{ p(\boldsymbol{x} |H_1)}
$$ {#eq:likelihood_ratio}
is the most powerful test statistic at any threshold $t_\textrm{cut}$, which
is associated with a significance
$\alpha=P(\Lambda(\mathcal{D}; H_0, H_1) \leq t_\textrm{cut})$. The last
expansion requires independence between the different observations. While the
likelihood ratio can be proven to be the most powerful test statistic,
it cannot be evaluated exactly if the likelihood is not known, which
often the case for LHC inference problems as discussed in
[Section @sec:likelihood-free]. The alternate
hypothesis is usually composite in particle colliders
because the signal mixture
fraction $\mu$ (or its cross section equivalently) is one of the parameters
of interest. The likelihood ratio test can nevertheless be expressed
in this case a function $\mu$, which will be the most powerful
test for a given $\mu$.

It is worth noting that while the
likelihood ratio defined in [Equation @eq:likelihood_ratio] defines the
most powerful test, the likelihood ratio based on a
summary statistic $\boldsymbol{s}(D)$ can also be defined, but it is not the most
powerful test for
inference based on $D$ unless $\boldsymbol{s}(D)$ is a sufficient summary
statistic with respect to the parameters $\boldsymbol{\theta}$ which fully
define the null
$p(\boldsymbol{x} | H_0) = p(\boldsymbol{x} | \boldsymbol{\theta}_0)$
and alternate
$p(\boldsymbol{x} | H_1) = p(\boldsymbol{x} | \boldsymbol{\theta}_1)$
hypotheses.
This fact motivates the
use of machine learning techniques
to approximate the likelihood ratio directly based on simulated observations
as discussed in [Section @sec:lr_clf]. The likelihood-ratio can then be
calibrated by
means of non-parametric probability density estimation techniques or
count-based likelihoods.

Another relevant issue when defining test statistics is that hypothesis
are rarely simple (or with a composite alternate in the way previously
described). The statistical model often depends on additional
nuisance parameters $\boldsymbol{\theta}$,
as discussed in [Section @sec:known_unknowns].
The likelihood ratio
from [Equation @eq:likelihood_ratio] is not guaranteed to be the most
powerful test statistic when the hypotheses are composite. In this
case, often summary statistics based on the *profile likelihood ratio* are
used, that can be defined for LHC searches as:
$$
\lambda(\mu) =
 \frac{L(\mu, \hat{\hat{\boldsymbol{\theta}}})}{
 L(\hat{\mu}, \hat{\boldsymbol{\theta}})}
$$ {#eq:profile_lr}
where $\hat{\hat{\boldsymbol{\theta}}}$ at the numerator refers to the value
of the nuisance
parameter that maximises the likelihood for a given $\mu$, and $\hat{\mu}$
and $\hat{\boldsymbol{\theta}}$ at the denominator
are the standard maximum likelihood estimators. The property that motivates
the use of the profile likelihood ratio, other than its convergence to
the likelihood ratio when the hypothesis are simple, is that the
distribution for large numbers of observations can be effectively
approximated, as demonstrated by Wilks and Wald [@wilks1938large; @wald1943tests].

For a discussion of the different test statistics based on the profiled
likelihood ratio as well as their asymptotic approximations,
the following reference is recommended [@Cowan:2010js]. In
particular, the use of the *Asimov dataset*, where the observed sample
summary statistic of the type outlined [Equation @eq:sum_count_vector]
is assumed to be equal to the expectation, is instrumental
for the technique described in [Chapter @sec:inferno]. The statistical
framework of hypothesis testing can also be used to decide wether to reject
or not reject the null hypothesis in favour of the alternate, which
is equivalent to the probability of the observed data (or test statistic) under
the null hypothesis, which is simply referred to as the p-value or
alternatively as Z-value when standard deviation units are used. When
the null hypothesis is not rejected $H_0$, the statistical test
can be recasted to obtain *exclusion upper limits* at a given confidence
level (usually 95\% is used), as is done in the non-resonant
Higgs production search included in [Chapter @sec:higgs_pair].

For obtaining exclusion upper limits, it is useful to define
a modified test statistic $\widetilde{q}(\mu)$:
$$
\widetilde{q}(\mu) =
\begin{cases}
-2\ln \frac{L(\mu, \hat{\hat{\boldsymbol{\theta}}}(\mu))}{
 L(0, \hat{\boldsymbol{\theta}}(\mu))} \quad
  &\textrm{if}\ \hat{\mu} < 0 \\
-2\ln \frac{L(\mu, \hat{\hat{\boldsymbol{\theta}}}(\mu))}{
  L(\hat{\mu}, \hat{\boldsymbol{\theta}}(\mu))}  \quad
  &\textrm{if}\ 0 \leq \hat{\mu} \leq \mu \\
  0 \quad
  &\textrm{if}\ \hat{\mu} > \mu \\
\end{cases}
$$
which does not regard negative background fluctuations
or cases where $\hat{\mu} > \mu$ as evidence against $\mu$. When
using $\widetilde{q}(\mu)$ or similar profile-likelihood-based
one-dimensional test statistics, the observed exclusion upper upper
limit can be defined as the larger value of $\mu$ for which the probability
of obtaining a test statistic is equal or larger than
a given confidence level (e.g. $\alpha=0.05$ for 95\% confidence
intervals), which can be expressed as the following integral:
$$
P(\widetilde{q}(\mu) \geq \alpha | \mu) =
\int^{\infty}_{\widetilde{q}_\textrm{obs}(\mu)}
g(\widetilde{q}(\mu) | \mu) dq
$$ {#eq:observed_limit}
where $\widetilde{q}_\textrm{obs}(\mu)$ is the observed test statistic and
$g(\widetilde{q}(\mu) | \mu)$ is the distribution under the alternate
when the signal fraction is $\mu$. This integral can be approximated
using Monte Carlo simulations or by the asymptotic approximations
described in [@Cowan:2010js]. An different upper limit definition is
often used to avoid excluding an alternative hypothesis with
a fixed probably $\alpha$ even when the analysis has no sensitivity,
referred to as CLs procedure
[@Read:2002hq; @Junk:1999kv],
in which the exclusion limit is defined as the value of $\mu$
for which
$P(\widetilde{q}(\mu) \geq \alpha | \mu)/P(\widetilde{q}(\mu) \geq \alpha | 0) \geq\alpha)$, which solves the mentioned issue
at the cost of over-coverage.

Most data analyses at the LHC, and particularly searches such
the one discussed in [Chapter @sec:higgs_pair],
are carried out in blinded manner to reduce the experimenter's bias,
i.e. the subset of observations or results 
relevant for statistical inference are not considered
or concealed until all the analysis procedures have defined. In order to
optimise the various analysis component (e.g. selection or summary statistic),
it is useful to compute a figure of merit that is representative of the
prospective sensitivity of the analysis. The *expected significance*,
is the expectation value for the probability value from [Equation
@eq:significance_test] under the alternative hypothesis. Instead, the median
of the expectation is often considered to preserve
monotonicity with Z-values, and several approximations exist
for simple cut-and-count likelihoods. Both the expected and median significance
depend on the signal fraction $\mu$ assumed, so they are particularly useful
to optimise analysis where the order of magnitude expected for $\mu$ is known,
e.g. cross section measurements of SM processes.

Alternatively, the expected median upper limit can be defined as the
exclusion upper limit using the median test statistic
$\widetilde{q}_\textrm{med}(\mu)$ under
the null hypothesis instead of the observed statistic. In addition to
the median expected limit, it is common practice in LHC searches
to also compute the so-called 1-sigma and 2-sigma bands, that correspond
to the $50.0\pm34.1$ and $50.0\pm47.7$ percentiles instead of the median. The
upper limit bands provide a quantitive estimation
of the possible limit variation if no signal is present in the data.
Both the expected significance and the expected upper limit can be estimated
asymptotically for summary statistics like the one described
in [Equation @eq:sum_count_vector]. The effect of nuisance parameters
can be also included in both in the asymptotic approximations or
the Monte Carlo based estimation. The asymptotic approximation are found to 
be good empirically, within 10\% to 30\% (for situations where the
number of events is small) of the Monte Carlo based estimation,
and thus are frequently used for obtaining limits and significances
in New Physics searches.


### Parameter Estimation {#sec:param_est}

Another inference problem that can be defined based on the observed
data, is parameter estimation, whose goal can be generally be defined as
the determination of the possible or optimal values that the 
parameters of a statistical model in relation to a set of observations.
Two types of parameter estimation problems
are often considered: point estimation and interval estimation. If the
aim is to obtain the best estimate (i.e. a single value) of a 
vector of parameter based on a set of observations, it is referred to
as a *point estimation* problem. When we are instead interested
on using a set of observations to make statistical statements about
a range or region for the values that the statistical model
parameters, we are dealing with an *interval estimation* problem.

Parameter estimation can be addressed either
from a classical (i.e. also known as frequentist) standpoint 
where the true values of the parameter are assumed to be fixed but unknown,
and intervals represent the region of parameters for which the
set of observed data could be obtained upon repeated sampling;
or from a Bayesian perspective, where probabilistic statements representing
the degree of belief on the values for the parameters are updated based on
the set of observations. A classical inference approach is predominantly
adopted in this document, where the definition of
probability is based on the relative frequency of the outcome when
repeated trials are carried out. Classical interval estimation, often referred
to as *confidence interval* estimation is
strongly related with hypothesis testing, as reviewed in
[Section @sec:hypo_test]. The $100(1-\alpha)\%$ confidence interval (CI)
for a one-dimensional parameter $\theta$ can be defined as the interval
$[\hat{\theta}^{-},\hat{\theta}^{+}]$:, such that:

$$
P(\hat{\theta}^{-} \leq \theta \leq \hat{\theta}^{+}) = 1 - \alpha
$$ {#eq:confidence_interval}

where $\hat{\theta}^-$ and $\hat{\theta}^+$ are referred as the lower and
upper limits. The definition of confidence interval in the context
of classical parameter estimation is the range of values for a given parameter
which, upon repeated trials,
would contain the true value $100(1-\alpha)\%$ of the times.
The concept of confidence interval can also be extended a
confidence region when a multi-dimensional parameter vector is considered.
While the definition of confidence interval  based on
its coverage properties is rather simple, its construction 
based on a set of observations $D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$
can be quite challenging. It is worth noting that both upper
and lower limit are estimators, quantities calculated by applying
a given produce to the set of observations, and thus
$\hat{\theta}^- (D)$ and $\hat{\theta}^+ (D)$ explicitly depend on
the set of data.

The Neyman construction [@10.2307/91337] provides a principled procedure
to define $100(1-\alpha)\%$  confidence intervals which guarantee
the property defined in [Equation @eq:confidence_interval], by inverting
an ensemble of hypothesis test (as defined in [Section @sec:hypo_test]),
by using simulated datasets for the different values
that parameter $\theta$ can take. Confidence intervals can
be one-sided, e.g. such as the exclusion upper limits
defined in [Equation @eq:observed_limit], or two-sided as
the definition provided in [Equation @eq:confidence_interval]. In particle
collider analyses, there is often a dichotomy between one-sided intervals
for null results and two-sided intervals for non-null results, which
can be solved by extending the Neyman construction with a
likelihood-ratio ordering criterion [@Feldman:1997qc].

Confidence interval procedures based on the Neyman construction works
very well for simple statistical models with one or two parameters, however
it rapidly becomes computationally intractable for larger
the number of parameters. Even though
the number of parameters of interest in LHC analyses is usually small,
nuisance parameters play an important role in inference as reviewed in
[Section @sec:nuis_pars], and cannot be accounted in a straightforward
manner in the previous procedure. Thus when the total number of
parameters is high, confidence interval are usually computed
based on alternative approximations, often based of some of the
properties of the profiled likelihood ratio discussed in
[Section @sec:hypo_test].

Before discussing the fundamentals of the confidence interval
approximations, it is useful to formally define the *maximum likelihood
estimator* of a parameter $\boldsymbol{\theta}_{\textrm{ML}}$ based on
a set of observations $D = \{\boldsymbol{x}_0,...,\boldsymbol{x}_n\}$
as:

$$
\boldsymbol{\theta}_\textrm{ML} =
\mathop{\textrm{arg max}}_{\theta \in \Theta} L(D; \boldsymbol{\theta})
$$ {#eq:max_ll}

where $L(D; \boldsymbol{\theta})$ is the likelihood function given the
set of observations $D$ which is a function of the model parameters
$\boldsymbol{\theta}$. The maximum likelihood estimator of model
parameters was already
used to define the profile likelihood ratio test statistic in
[Equation @eq:profile_lr], an is a very common point estimator
because it is asymptotically consistent and efficient. In addition,
the maximum likelihood estimator coincides with the *maximum
a posteriori* (MAP) point estimator in Bayesian inference when the
parameter priors are uniform.

The shape of the likelihood function around the maximum likelihood
estimator $\boldsymbol{\theta}_{\textrm{ML}}$ can be used to approximate
confidence intervals. Using asymptotic theory developed by
Wilks [@wilks1938large], the $100(1-\alpha)\%$ confidence region
for the parameter vector $\boldsymbol{\theta}$ can be determined
using the following relation:

$$
- \ln L(D; \boldsymbol{\theta}) \leq
- \ln L(D; \boldsymbol{\theta}_{\textrm{ML}}) + \Delta \ln L
$$ {#eq:delta_log}

where $\ln L(D; \boldsymbol{\theta}_{\textrm{ML}})$ is the natural logarithm
of the likelihood for the maximum likelihood estimator and $\Delta \ln L$
depends on the number of parameter dimensions and the desired coverage
$1-\alpha$. For example, the values of  $\boldsymbol{\theta}$
inside the $68.27\%$ (i.e. 1-sigma) confidence region and for one dimensional
parameter are those for which the previous relation is verified using
$\Delta \ln L = 0.5$. If  $\boldsymbol{\theta}$ is one-dimensional and
the function $L(D; \boldsymbol{\theta})$ is convex, the confidence
interval limits $\hat{\theta}^- (D)$ and $\hat{\theta}^+ (D)$
can be obtained by finding the most extreme values of $\theta$
that verify [Equation @eq:delta_log] at each side of the
maximum likelihood estimator $\boldsymbol{\theta}_{\textrm{ML}}$.

As discussed in [Section @sec:nuis_pars], we are often interested on
confidence intervals for a subset of interest of the statistical
model $\boldsymbol{\theta}_\iota$, while regarding the others
as nuisance parameters $\boldsymbol{\theta}_\nu$. The previous
procedure can be extended for computing approximate confidence interval
for the parameters of interest, by considering the profiled likelihood
$\hat{L}(D; \boldsymbol{\theta}_\iota)$
instead of the full likelihood in [Equation @eq:delta_log],
which is defined as:

$$
\hat{L}(D; \boldsymbol{\theta}_\iota) =
\mathop{\textrm{arg max}}_{\theta_\nu \in \Theta_\nu}
L(D; \boldsymbol{\theta}_\iota, \boldsymbol{\theta}_\nu)
$$ {#eq:profiled_ll}

so the nuisance parameters $\boldsymbol{\theta}_\nu$ are profiled by
considering their values that would maximise the likelihood conditional to
each value of the parameters of interest $\boldsymbol{\theta}_\iota$.
Noting that a constant denominator in the likelihood would cancel out at each
side of [Equation @eq:delta_log], and its equivalent when
using the profiled likelihood, they can be linked with the profile-likelihood
ratio test statistic defined in [Equation @eq:profile_lr]. Algorithms
for likelihood maximisation and computation of intervals based
on the profiled likelihood are implemented in the [minuit]{.smallcaps}
library [@james1975minuit], which can also account for bounded parameters.
Confidence intervals based on the profiled likelihood will be used
for benchmarking different ways for constructing summary statistics
in [Chapter @sec:inferno].

Another subtlety relevant when dealing with nuisance parameters (which
also applies to a lesser degree to the combination of measurements),
is that oftentimes nuisance parameters are constrained by theory
or external measurement. This can be included in the previous
likelihood-based techniques by considering the likelihood
as a product of the likelihood derived from the statistical
model for the set of observations $L_D(D; \boldsymbol{\theta})$
with the available constraints $L_C^i(\boldsymbol{\theta})$,
as follows:
$$
L_(D; \boldsymbol{\theta}) = L_D(D; \boldsymbol{\theta})
\prod_{i=0}^{c} L_C^i(\boldsymbol{\theta})
$$ {#eq:augmented_likelihood}
where simplified likelihoods (e.g. a normal approximation) are often
used in the constrain terms $L_C^i(\boldsymbol{\theta})$ but they
could in principle also depend on an independent set of
observations. The constrain terms could be also understood as
prior probability distributions in a Bayesian setting, obtained
from previous evidence.

In order to obtain approximate confidence intervals from the shape
of the likelihood or profile likelihood function around the maximum
likelihood, several likelihood evaluations (together with a constrained
optimisation problem if $\hat{L}(D; \boldsymbol{\theta}_\iota)$ is
used) are often required to estimate accurately a confidence interval.
A cruder but often useful approximation can be obtained from the curvature of
the negative log-likelihood function at $\boldsymbol{\theta}_{\textrm{ML}}$. In
more than one dimension, the local curvature can be expressed by the
Hessian matrix $\boldsymbol{H}$. The Hessian of the
$- \ln L(D; \boldsymbol{\theta})$  is is also referred as the
Fisher information matrix ${\boldsymbol{I}(\boldsymbol{\theta})}$ [@fisher_1925]
and it is defined as:
$$
{\boldsymbol{I}(\boldsymbol{\theta})}_{ij}
=
{\boldsymbol{H}(\boldsymbol{\theta})}_{ij}
= \frac{\partial^2}{\partial {\theta_i} \partial {\theta_j}}
 \left ( - \ln L(D; \boldsymbol{\theta}) \right )
$$ {#eq:hessian_log}
which can be evaluated at any given $\boldsymbol{\theta}$, e.g. by using
numerical differentiation. The Cramér-Rao lower bound
[@cramer2016mathematical; @rao1992information] provides a link between
the inverse of the Fisher information matrix and the covariance
of an unbiased estimator $\hat{\boldsymbol{\theta}}$:
$$
\textrm{cov}_{\boldsymbol{\theta}}(\hat{\boldsymbol{\theta}}) \geq
I(\boldsymbol{\theta})^{-1}
$${#eq:CRB_ch3}
which becomes an equality in the large-sample
limit for an efficient parameter estimator
such as the maximum likelihood estimator $\boldsymbol{\theta}_\textrm{ML}$.
The diagonal elements of the inverse of the information
matrix $\sigma_i^2=\left( I(\boldsymbol{\theta})^{-1} \right)_{ii}$ may be
to construct a $68.3\%$ confidence interval for $\theta_i$ parameter
where the effect of the rest of parameters has been profiled as
$[\boldsymbol{\theta}_\textrm{ML}-\sigma_i, \boldsymbol{\theta}_\textrm{ML}+\sigma_i]$.
This approximation is equivalent to
profiling assuming that the $- \ln L(D; \boldsymbol{\theta})$ can be described
by a multi-dimensional parabola centered at $\boldsymbol{\theta}_\textrm{ML}$,
and thus leads to symmetric intervals.
In Bayesian literature, an analogous approach is used to extend MAP estimation
in order obtain a multi-dimensional normal approximation for the posterior,
which is often referred to as Laplace approximation [@laplace1986memoir].
An advantage of this approximation, that will be used in
[Chapter @sec:inferno] to construct an inference-aware machine learning
loss function, is then that can be interpreted both in the context of
classical and Bayesian inference.


