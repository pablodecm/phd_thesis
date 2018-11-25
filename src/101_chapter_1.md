# Theory of Fundamental Interactions {#sec:theory}

\epigraph{Nothing in life is to be feared. \\
  It is only to be understood.}{Marie Skłodowska Curie }

Scientific theories are frameworks describing natural phenomena that are
capable of making experimentally testable predictions. Oftentimes, they are
specified using mathematical language and built on previous observational
knowledge and basic properties of the system under study. 
At the most fundamental scales known to date,
the Standard Model (SM) of particle physics is a scientific theory that
provides a very accurate description of most of the observed properties
and dynamics of the universe around us. It is constructed upon an innovative
theoretical framework, generally referred as quantum field theory (QFT),
and principles regarding fundamental symmetries of the laws of nature.
In this chapter, a non-exhaustive introduction to this theory and its
descriptive reach will be provided together with a summary of the known
limitations and possible extensions or alternatives.
Given the experimental character of the research discussed in the following
chapters, the aim of this chapter is not solely the discussion of the
basic structure and properties of the theory, but also
the methodology followed to compute predictions for observables
that can be contrasted with empirical data.

## The Standard Model {#sec:standard_model}

The Standard Model (SM) of particle physics is a mathematically
self-consistent gauge field
theory that classifies all known types of elementary particles and 
describes their electromagnetic, weak and strong interactions.
Within this fundamental theory, all known matter and energy phenomena
can be explained in terms of the kinematics and interactions
of elementary particles, which can in turn be understood as
local excitations of different fields that permeate our universe.


![Schematic overview of the particle content within the SM. Fundamental
particles include fermions, further subdivided in quarks
and leptons, and fundamental bosons, including the force mediators
and the Higgs boson. Diagram adapted from
[MissMJ](https://commons.wikimedia.org/wiki/File:Standard_Model_of_Elementary_Particles.svg).
](gfx/101_chapter_1/Standard_Model_of_Elementary_Particles.pdf){
#fig:standard_model_particles width=70%}

From a historical perspective, this theory is the product of
a succession of important theoretical developments and experimental
discoveries over the last century [@weinberg2004making],
culminating
with the discovery of the Higgs boson in 2012 [@higgs2012cms;@higgs2012atlas].
If a more principled viewpoint is taken, the SM can be thought of
as the most general but mathematically consistent
theory that respects a set of symmetries, namely
a global Poincaré group symmetry (translational, rotational
and relativistic
boost invariance) and a local
$$G_\textrm{SM} = SU(3)_{C}\otimes SU(2)_{L} \otimes U(1)_{Y}$$ {#eq:sm_gauge_symmetry}
gauge group symmetry. The
$G_\textrm{SM}$ symmetry group is essential to describe three of the four
fundamental interactions observed in nature: strong interaction,
weak interaction and electromagnetic interaction. In fact, the
$SU(3)_{C}$ is associated the strong force and the conservation of
its charge, called colour, while the $SU(2)_{L} \otimes U(1)_{Y}$ symmetry instead is
related with electroweak interactions (i.e. unification of weak and
electromagnetic) and the conservation of isospin and
weak hypercharge.
The SM is typically specified using the Lagrangian formalism and depends
on a total of 19 parameters (not accounting for neutrino masses
and mixing angles), which are not predicted by the theory
from first principles but determined through experimental measurements.

In the context of the SM, excitations of the fundamental fields
give rise to two types of elementary particles: fermions (characterised
by having half-integer spin) and bosons (characterised by having
integer spin). Fermions are the fundamental constituents of matter,
and they
are further subdivided into leptons and quarks depending on their 
interactions. A schematic overview of the fundamental particles
of the SM and their properties is provided in
[Figure @Fig:standard_model_particles]. Three particle generations
are known for both quarks and leptons, each containing a pair of particles
with different masses. For quarks, the heavier is referred to as up-type and
the lighter as down-type. Instead, for leptons we distinguish the heavier
charged particles (electron, muon and tau) from their corresponding light
and uncharged neutrinos. Regular matter is largely made of the
first generation of quarks and electrons, given that  higher generations
rapidly decay quickly to lower generations characterised by
smaller masses. All fermions interact via the weak force but
only quarks carry colour charge and are subjected to the strong
force. For each fermion in the SM, there is a another particle with
identical properties but opposite quantum numbers, globally referred to
as antimatter, and denoted for each particle with the anti prefix
and a bar over the symbol (e.g. up antiquark $\bar{u}$) 
or by explicitly denoting the charge sign (e.g. positron 
$e^+$). Neutrinos are the only fermions that do not carry electrical
charge and might be their own antiparticle.

The mediators of the strong, weak and electromagnetic fundamental interactions
are referred to as gauge bosons, and
are characterised by having spin 1. To model the strong interaction
colour charge exchanges, a total of eight independent
strong massless force mediators, or *gluons*, are needed. Gluons
carry colour charge themselves and thus participate in colour
interactions with other gluons, which leads to a phenomenon known
as *colour confinement*, which will be discussed in
Section [-@sec:qcd_detail] in more detail. The massless
and neutral *photon* is
the mediator of the electromagnetic force, while instead
the massive $Z$, $W^+$ and $W^-$ bosons mediate
weak interactions. The last piece in the SM is the *Higgs
boson*, the only fundamental known particle with spin 0. The Higgs boson
is the quantum excitation of the *Higgs field*, which  also couples with other
fundamental particles such as the gauge bosons of the weak force,
effectively generating their mass through their interaction. The Higgs boson
and Higgs field play an essential role in the
electroweak symmetry breaking (EWSB) mechanism, which will be discussed
in more detail in Section [-@sec:ewsb_higgs].

The rest of this section will be devoted a more mathematically exhaustive
review of the different components of the Standard Model, starting
by reviewing the basic formalism of quantum field theories and incrementally
building on it do describe the characteristics of both the strong and
electroweak interactions that give rise to the diverse interactions
dynamics of relevance in particle physics experiments.


### Essentials of Quantum Field Theory {#sec:qft_basics}

As hinted in the previous section, in quantum field theory (QFT), observed
particles are understood as excitations of fields that extend through whole
universe. Quantum field theory unifies the physical foundations
of quantum mechanics and special relativity, and can be used to
accurately describe phenomena in systems where relativistic and
quantum effects are relevant, such as interaction between highly
relativistic particles. In QFT, all the known physical processes
in the universe are explained in terms of the state and dynamics
of set of fundamental tensor fields. A tensor field can be defined as a
continuous and differentiable set of values, such a scalar or a vector,
that exist for any given location and time. For simplicity, the fields 
in QFT are usually defined in a relativistic
coordinate system $x = (t, \boldsymbol{x})$ in
order treat space $\boldsymbol{x}$
and time $t$ jointly.

To exemplify the fundamentals of the QFT framework, let us consider the
simplest case, e.g. a
single field that does not interact with any other field, which
will be denoted as $\phi(x)$. The dynamics of a field (or several fields)
in QFT are specified by using the *Lagrangian formalism*, similarly
to what can be done for system in classical mechanics. However,
instead of considering the Lagrangian $L$
which depends the generalised coordinate vector $\boldsymbol{q}(t)$
and its time derivatives $\dot{\boldsymbol{q}(t)}$, in QFT the Lagrangian
density $\mathcal{L}$ is commonly used, which depends only on the field
$\phi (x)$ and its first derivative $\partial_{\mu} \phi (x)$. In fact,
in an analogous manner to what is done in classical mechanics to
define the action functional $S_{\textrm{classical}}$, we can define
the action of the quantum field $S_{\textrm{classical}}$ as a function
of the Lagrangian density $\mathcal{L}$ as follows:
$$ S_{\textrm{classical}} = \int L (\boldsymbol{q}(t) ,\dot{\boldsymbol{q}} (t)) dt 
   \quad \Rightarrow \quad
   S_{\textrm{QFT}}  =  \int \mathcal{L}(\phi, \partial_{\mu} \phi)\ d^4 x
$$ {#eq:langrangian_density}
noting that the previous definition would also be valid when
the Lagrangian depends on multiple fields and their derivatives instead of
a single free field. Identically to what is done in classical systems,
we can attempt to solve for the field that minimises the action,
i.e. $\delta S=0$. With the help of some functional calculus [@Goldberg:2244785],
it is possible obtain the relativistic field theory version of
the Euler-Langrange equation:
$$\partial_\mu \left ( \frac{\partial \mathcal{L}}
                             {\partial (\partial_\mu\phi)}
               \right ) 
  - \frac{\partial\mathcal{L}}{\partial\phi} = 0
$$  {#eq:euler_lagrange}
where $\partial_\mu=\partial/\partial x_\mu$  and the repetition
of the coordinate index $\mu \in \{0,1,2,3\}$ means summation over
the product. The previous relation would still apply to each field
in the case that a Lagrangian including several fields were
considered; therefore,
given a Lagrangian, we can use Equation [-@eq:euler_lagrange]
to obtain their equations of motion. As an example, let us consider
the following Lagrangian $\mathcal{L}_\textrm{Dirac}$, which  is a function of
a bispinor field $\psi$, a 4-dimensional complex vector field that
can represent a field whose excitations behave like fermions of mass
$m$:
$$\mathcal{L}_\textrm{Dirac}
  =\bar{\psi} (i\gamma^\mu \partial_{\mu} - m)\psi
$$ {#eq:dirac_lagrangian}
where $\gamma^\mu$ are the gamma matrices and 
$\bar{\psi}=\psi^\dag \gamma^0$ is the spinor adjoint. As the chosen naming
for the previous Lagrangian $\mathcal{L}_\textrm{Dirac}$ gave away,
the Euler-Lagrange relation obtained by
minimising the action $\delta S=0$, can be used to obtain field equations
of motion that correspond to the Dirac equation [@Peskin:257493] for the
spinor field and its adjoint:
$$ i\gamma^\mu \partial_{\mu} \psi - m \psi=0 \quad \textrm{and} \quad
   i\gamma^\mu \bar{\psi} \partial_{\mu} + m\bar{\psi}=0
$$ {#eq:dirac_equation}
as well as the well-known Klein-Gordon equation component-wise
$(\partial^\mu \partial_\mu + m^2)\psi=0$,
where $\partial^\mu=\partial/\partial x^\mu$. Both Dirac and
Klein-Gordon equations were proposed in the context fo relativistic
formulation of quantum mechanics.

To shed some light on how a field like $\psi$ can represent actual fermions
in the universe, such as electrons or positrons, it can be quantised
by considering a plane wave expansion and defining creation and
annihilation operators.


### Quantum Chromodynamics {#sec:qcd_detail}


### Electroweak Interactions  {#sec:ew_detail}


### Symmetry Breaking and the Higgs Boson {#sec:ewsb_higgs}

### Standard Model Lagrangian



## Beyond the Standard Model {#sec:sm_alternatives}

The experimental success of the Standard Model and its main 
subcomponents QED, QCD and EW unification and
symmetry breaking is clearly incontestable, ranging from the confirmation
of theoretical prognostiscation of the existence and some the properties
of new particles
(e.g. $Z$, $W^{\pm}$ and Higgs bosons or top quark) to
the agreement of precise predictions with meticulous experimental
observations. The fine structure constant $\alpha$ at zero energy scale
is an example of the latter, with its experimentally determined value being
compatible with the Standard Model based theoretical prediction up
to 12 orders of magnitude [@hanneke2008new; @parker2018measurement]. In addition to describing natural phenomena
with unprecedented accuracy, the SM it is a self-consistent theory that 
provide non-divergent predictions at the highest energy scales probed to date.

### Known Limitations


In spite of the successes mentioned above,
several shortcomings of the Standard Model are known
and hence is not considered as a complete theory of natural phenomena
at the most fundamental scales. Those concerns include unexplained empirically
observed phenomena such as gravitational interactions, neutrino masses or
dark matter particle candidates,
theoretical considerations regarding the stability of vacuum or
aesthetic principles such as naturalness.
Hence, it is presumed that the Standard Model is an effective theory, able to
successfully describe fundamental processes within a range of energies as
an approximation fo more complete unified theory. For completeness, the
main empirical and theoretical concerns are summarised:


* **Omission of gravitational interactions**: the current formulation of
 the SM completely disregards the effect of gravity in
 fundamental interactions, because no consistent quantum descriptions for
 gravity matching the experimental predictions of the well-established
 theory of general relativity [@misner2017gravitation] have been developed to date. While several
 theoretical efforts are ongoing, such as loop quantum
 gravity [@rovelli2008loop]
 or string theory [@Polchinski:363850],
 the coupling for gravitational interactions at the current experimental
 high-energy reach is expected to be more than 30 times weaker than for
 weak interaction, and hence can be safely ignored when computing theoretical
 predictions.
 
* **Lack of a viable Dark Matter candidate**: through a variety of
  astrophysical observations, including the observed galaxy rotation
  curves [@corbelli2000extended], gravitational
  lensing [@trimble1987existence]
  and the Cosmic Microwave Background (CMB) [@Ade:2015xua], there is clear
  evidence indicating the presence of more gravitational interacting matter
  in the universe than what is expected by contrasting with the
  electromagnetic spectra. It has been thus estimated that about $85\%$ of
  massive existing matter in the universe does not notably interact
  with ordinary matter and radiation, and therefore is referred
  as *Dark Matter*. While its particular nature is still unknown, scientific
  consensus seem to favour long-lived cold non-baryonic matter as an explanation,
  predominantly weakly-interacting massive particles (WIMPs). The three
  neutrino types are the
  only WIMP within the Standard Model, but considering
  the known upper limits on their masses, they can account for a very
  small fraction of the total mass of dark matter in the universe. 
  
  
* **Unexplained matter-antimatter asymmetry**: as discussed in
  [Section @sec:standard_model], each matter particle in the Standard
  Model has an identical anti-matter possessing opposite quantum
  numbers. Because pair creation and annihilation processes are symmetric, but
  our universe is manifestly dominated by what we refer as matter, some
  asymmetric interaction processes ought to exist. Within the SM, some
  electroweak processes are known to violate CP-symmetry and potentially
  explain a small part of the observed matter-antimatter asymmetry. New
  unknown CP-symmetry processes, potentially through interactions not
  included in the SM, are needed to resolve the mentioned disparity.

* **Origin of neutrino masses**: the Standard Model was developed assuming
  that neutrinos were massless, yet is currently well-stablished
  that neutrinos oscillate between different flavour states
  [@fukuda1998evidence; @sno2001measurement], implying 
  that flavour states are mixing and hence that neutrino masses are
  very small but different from zero.
  The SM Lagrangian can be extended to account for the masses of neutrinos
  in a similar fashion to what is done for leptons and quarks, but their 
  Yukawa coupling has to be much smaller than of any of the other particles,
  and it requires the existence of very weakly interacting
  right-handed neutrinos. An alternative mechanism for including
  neutrino masses exists, and it is based on assuming that these
  particles are Majorana fermions
  and hence they are their own anti-particle. This hypothesis is currently being
  experimentally tested. It also worth noting that in order to explain the
  smallness of neutrino masses in a principled way, the Seesaw mechanism [@Akhmedov:1999tm]
  has been proposed, which implicitly assumes that the SM is only a
  low-energy scale effective theory of a more complete unified theory.

  
* **Mismatch between vacuum energy and Dark Energy**: in addition of providing
  evidence for dark matter, astrophysical observations such as studies of the
  properties of the Cosmic Microwave Background [@Ade:2015xua] or the redshift of
  type Ia supernovae [@riess2004type],
  consistently point to the hypothesis of
  an accelerating expansion of the current universe. The simplest way to account
  for this in cosmological models is to include a cosmological constant,
  which should be understood as an intrinsic energy density of the vacuum,
  exerting
  a negative pressure and therefore driving the observed expansion of the
  universe. In fact, in order to reconcile the theoretical models with
  experimental observations, about $68\%$ of the total energy in the
  present universe would correspond to this type of unknown energy
  density, generally referred to as *dark energy*. In most quantum field theories,
  such as the Standard Model, some non-zero zero-point
  energy originating from quantum fluctuations is expected. However,
  modern attempts to predict energy densities from QFT are at variance
  with the observed energy vacuum energy density, some of them differing in
  120 orders of magnitude [@adler1995vacuum].
  
  
* **Naturalness, hierarchy and fine-tunning concerns**: as discussed at the
  beginning of [Section @sec:standard_model], the SM can be thought of
  the most general theory based on  a set symmetries, and its
  19 parameters (or 26 accounting for neutrino masses
  and mixing angles)
  are not obtained from first principles but measured experimentally.
  Having such a large number of free
  parameters and observing large differences among their
  relative magnitude, has been viewed as a theoretical concern from
  an aesthetic perspective. A related issue is why the electroweak
  energy scale (epitomised by the Higgs mass) is much smaller than
  the assumed cut-off scale of the SM, where gravitational
  interactions become relevant at
  $M_{\textrm{Planck}} \approx 10^{19} \textrm{GeV}$, which is
  generally referred as the *hierarchy problem*. In the absence of
  New Physics or additional interaction mechanisms, the only
  way to obtain the observed Higgs mass from a the bare Higgs
  mass (at zero energies) is through a very precise cancellation
  of divergences, which is regarded as an *unnatural* or *fine-tuned*
  property of the SM theory.

Other possible issues, in some cases related with those discussed,
have also been raised 
such as the apparent vacuum meta-stability [@degrassi2012higgs] or
the strong CP problem [@cheng1988strong]. Some of these issues can be clarified
once the higher precision measurements of the SM become available, which
are mainly obtained in particle collider experiments.

### Possible Extensions {#sec:possible_ext}

The known limitations stated in the previous section have motivated
the development of alternative theories for describing fundamental
interactions. Given the quantitative success of the Standard Model,
most of the known proposed theoretical models are either extensions of
the SM or its associated predictions can be effectively
reduced to those of the SM at the energy range current being
explored in particle physics experiments. The set of alternative
that have been proposed is too substantial to be exhaustively listed
here, especially given that many of the alternatives include
additional free parameters that greatly modify the expected
theoretical observables.

<!-- maybe mention SUSY and extra-dimensions as canonical BSM -->

#### Precision Measurements of the SM

Due the existing large space of alternatives to the SM from a theoretical
standpoint, the exploration of all possibilities through dedicated searches
becomes unattainable. An alternative way to possibly obtain quantitative
information pointing to extension of the SM is to measure its most relevant
observables with high precision. If significant discrepancies are found
between the experimental measurement and the theoretical prediction of
those observables, it could be evidence pointing to New Physics outside
the SM. 

#### Effective Field Theories

## Phenomenology of proton collisions {#sec:pheno}

Once the properties and limitations of the theoretical model that best
describes the current understanding of the fundamental structure and
dynamics of nature have been described,
we can delve into how to model proton-proton collisions from a 
quantitative perspective, so theoretical predictions
can be contrasted with experimental results at the LHC. The focus
of section then is to make sense of the various outcomes of high-energy
proton-proton collisions and how we can predict their relative
rates of occurring given some initial state
conditions of the interaction.

### Main Observables {#sec:main_obs}

A related consideration that is useful as an introduction to the
aforementioned topic is the question of what outcomes can
originate as a result of proton-proton collisions.
An answer somehow circular but compatible with our
current interpretation of the universe
is that everything that could be produced would be produced,
meaning that any outcome that can happen
in a way that is consistent with the underlying properties
of nature is possible. Even though the true description
the properties of nature is not known, as discussed in Section
[-@sec:standard_model], the Standard Model
provides an effective model and restricts considerably the space
of possible outcomes, in a way that can be compared with experimental
observations. It is worth noting that alternative descriptions of
nature, such as those motivated by the known limitations of the SM
and reviewed in Section [-@sec:sm_alternatives], may provide alternative
mechanisms for the production of outcomes that are not allowed by the SM,
and hence often drive the experimental searches for evidence of New Physics.

For those physical processes that could happen as a product of a proton-proton
collision, under the assumption of validity of a particular theoretical model,
their total expected rate of occurrence is one the most relevant
quantities to predict and compare with observation.
To ease its experimental interpretation,
the rate of occurrence of certain process is commonly
expressed as as a cross section $\sigma$,
which has dimensions of area and is typically expressed in submultiples
of barn ($1 \textrm{barn} = 10^{-28} \textrm{m}^2$). The advantage of cross
sections over rates is that their value is independent from the density
of the incident particle fluxes. The rate, or probability per unit of time,
of a process occurring can be computed simply by multiplying its cross
section by the instantaneous luminosity $\mathcal{L}_\textrm{inst}$, which
corresponds to the number of particles per unit of area per unit of time
crossing in opposite directions in the collision volume.

Another related concept, which is especially important for simulating
interactions,
is the differential cross section $d\sigma$. While the initial state
conditions are fixed, the rate of
occurrence of a physical process can be expressed as as a function of
some final-state
variables, such as the angle and energy of outgoing particles. While these
variables can be integrated over to compute total cross sections $\sigma$,
the integrand is proportional to the probability density of each
outcome happening as a function of final-state variables so is
crucial for modelling their multi-dimensional distributions
via random sampling. In fact, we will be dealing
with differential cross sections instead of total process cross section
in this section for generality.

### Parton Distribution Functions

A complication that has not been addressed yet is that protons are
composite particles, formed by two up-type quarks
and one down-type quarks bound together via the strong force.
The dynamics of proton-proton scattering are therefore dictated by quantum
chromodynamics (QCD), which cannot be addressed using perturbation
theory for low
energies, limiting the first principles computation of relevant
observables for the most common interactions. Luckily for us,
the most promising territory being explored in energy colliders correspond
to higher energies, where relevant interaction outcomes come from the
hard scattering of proton constituents (referred to as partons),
and predictions can
be perturbatively approximated under the assumption of asymptotic
freedom.


::: {#fig:subfigs_pdfs .subfigures}
![Low Energy Scale $\mu^2 = 10 \textrm{GeV}^2$
](gfx/101_chapter_1/nnpdf31nnlo-10.pdf){#fig:pdf_low width=49%}
![High Energy Scale $\mu^2 = 10^4 \textrm{GeV}^2$
](gfx/101_chapter_1/nnpdf31nnlo-1e4.pdf){#fig:pdf_high width=49%}

Distribution functions for the different
partons at low and high energies. The contribution from gluons
shown is 1/10 of the actual contribution. Image adapted from the NNPDF
collaboration [@Ball:2017nwa].
:::

Even for modelling hard scattering processes, a non-perturbative input is
required, mainly the probability of finding a particular proton constituent
with a certain momentum fraction inside each of the colliding protons,
referred to as the parton distribution function (PDF).
The model of the proton as three quarks coupled by strong force 
is too simplistic for modelling proton-proton scattering realistically,
specially at high energies. The continuous exchange of gluons between the three 
constituent quarks effectively generates
a sea of virtual quark-antiquark pairs from which other partons can
scatter off. Consequently, in the interaction of two protons, not only
the constituent quarks, referred as to valence quarks, can take part in the
hard scattering process but also gluons and sea quarks.

At the time of writing,
PDFs are not computable from first principles so they
have to be parametrised and extrapolated from various experimental sources
including fixed-target proton deep inelastic scattering (DIS) and previous
collider studies. It is worth noting that the distribution functions depend
strongly in the energy scale of the process, yet the evolution for parton
densities can be modelled theoretically
[@Altarelli:1977zs;@Dokshitzer:1977sg;@Gribov:1972ri]. Given their relevance
for computing observables in high-energy colliders,
several research collaborations such as NNPDF [@Ball:2017nwa] provide accurate
estimations that can be readily used for simulation and prediction. In
[Figure @fig:subfigs_pdfs], the parton distribution functions at two different
energy scales estimated by one of those collaborations are shown, at lower
energy scales the valence quarks (up and down) dominate while when we
extrapolate at higher energies, gluon scattering become the most likely
outcome for the interaction.


### Factorisation and Generation of Hard Processes {#sec:factorisation}


Let us consider the computation the differential cross section for a hard
scattering process $pp \rightarrow X$, which will be denoted as
$d\sigma(pp \rightarrow X)$, for two protons colliding head on
at center of mass energy $s$. Here
$X$ denotes a possible outcome for the interaction, not necessarily a single
particle and the proton remnants (e.g. a Higgs boson $X=H + \textrm{other}$),
but a set of particles (e.g. a bottom
quark-antiquark pair $X=b\hat{b} + \textrm{other}$). According to the QCD factorisation
theorem [@Collins:1989gx], the differential cross section for
$d\sigma(pp \rightarrow X)$
can be expressed as a sum of functions of the partonic cross section 
$d\hat{\sigma}_{ij \rightarrow X}$:  

$$d\sigma(pp \rightarrow X) = \sum_{i,j} \int
f_i(x_1, \mu_F^2) f_j(x_2, \mu_F^2)
d\hat{\sigma}_{ij\rightarrow X} (s x_1 x_2,\mu_R^2,\mu_F^2)
  d x_1 d x_2$$ {#eq:qcd_factorisation} 


where $i$ and $j$ indicate the partons involved (e.g. a certain type of quark or
a gluon), $f_i(x_1, \mu_F^2)$ and  $f_j(x_2, \mu_F^2)$ are their parton distribution
functions for given momentum fractions $x_1$ and $x_2$ respectively, $\mu_F$ is
the factorisation scale and $\mu_R$ is the renormalisation scale. The
differential partonic cross section $d\hat{\sigma}_{ij\rightarrow X}$ for
at center of mass energy of the interacting partons $\hat{s}=s x_1 x_2$,
can be calculated perturbatively at different expansion orders from
the Lagrangian density as hinted in Section [-@sec:standard_model]. The
total cross section  $\sigma(pp \rightarrow X)$ can
then be attained by integrating out all final state quantities, commonly
referred as phase space variables, in the differential total
cross section element $d\sigma(pp \rightarrow X)$. It is worth pointing out
that is simple cases (small number of particles in the final
state) is often possible to integrate out the final state phase space
variables directly in the partonic differential cross section
$d\sigma(ij \rightarrow X)$, and thus directly
compute the total cross section by a similar parton distribution
function integration as the one used in Equation [-@eq:qcd_factorisation].

As more more complex final states or higher perturbative
orders are considered, the final state phase space integration over
many particles can rapidly become intractable. This motivates the use
of *Monte Carlo integration* techniques, especially those based
on importance sampling such as [vegas]{.smallcaps} [@Lepage:1977sw],
which provide convergence rates that scale well with the integral
dimensionality by randomly sampling the multi-dimensional space.
In fact, the initial state integration
over parton types and momenta fractions can also be carried out
jointly with these methods, greatly simplifying the computation procedure.
The resulting weighted random samples can be used to estimate not only
the total cross section, but also any other observable or
distribution that is a function of the differential
cross section $d\sigma(pp \rightarrow X)$. A common observable that is often
used in experimental high energy physics is the efficiency $\epsilon$,
or fraction of observations from a specific process  $pp \rightarrow X$ that
are expected to satisfy a given condition that is a function of the final state
details.

<!-- weighted efficiency formula -->

In collider experiments typically we cannot measure
directly the properties of final states produced in
the hard scattering, either because of the characteristics of the detector,
the decay/hadronisation of particles producing other secondary particles, or
due to additional physical effects occurring in a bunch crossing not accounted
in Equation [-@eq:qcd_factorisation], such as additional collision products
due to multiple interactions or processes comprising the proton
remnants. Thus it is very useful in the construction of the complete
mode to consider the problem
of generation of realistic collision products. Taking into consideration
that some of the computational techniques for including
subsequent physical processes and the detailed simulation of the detectors
are considerably resource intensive, as will be detailed in
Section [-@sec:parton_showers] and Section [-@sec:detector_simulation]
respectively, the use of weighted samples is not a
very efficient approach. Hence,
for the generation of simulated products of high-energy collisions, also
referred to as *event generation*, an acceptance-rejection sampling step
is carried out to obtain an unweighted sample, where the relative
frequency of each simulated outcome is expected to match its
theoretical prediction. After such procedure, the
calculation of all observables is also simplified, because the weight of all
samples can be taken as a constant, e.g. a unitary weight $w=1$, so
the computation of quantities of interest such as efficiencies becomes trivial.

<!-- unweighted efficiency formula -->
<!-- NLO matrix elements and other details -->

### Hadronization and Parton Showers {#sec:parton_showers}

In order to link the hard scattering process outcome
with the actual observable quantities that can be detected in an
experiment, it is necessary to account for the radiation of
soft gluons or quarks form the initial or final state partons in
the collision
as well as the conversion of formation of hadrons from any
free parton due to colour confinement (see Section [-@sec:qcd_detail]).
Additional processes that affect the collision outcome include
secondary interactions between the protons, as well as the
decays for all unstable particles generated. 
An example of the typical complexity of the physical
processes occurring as a result of a single high-energy proton-proton
scattering is provided in [Figure @fig:event_shower].
These and additional minor effects
(e.g. colour reconnection) are accounted by *parton showering* (PS) programs,
that take as the input the the generated particle outcome of the
hard scattering and 
return a set of the resulting stable particles that would propagate
through the detector. 

![Diagram of a proton-proton collision and the underlying physical
processes occurring therein, adapted from [@Hoche:2014rga].
The dark green ellipses following the tree parallel arrows represent the
incoming hadrons. The main interaction between partons is shown in
red colour, producing a tree-like structure of decays, in turn
producing partons that rapidly transition to hadrons (light green ellipses)
and decay (dark green circles) as well as soft photon radiation (yellow lines).
The blue lines represent the  interaction between partons and the path of the
the initial hadron remnants followed by light blue ellipses. For completion,
an additional hard interaction within the same hadron-hadron process is
shown in purple,
which often has to be accounted for to obtain realistic simulations.
](gfx/101_chapter_1/event_shower.pdf){
#fig:event_shower width=70%}



