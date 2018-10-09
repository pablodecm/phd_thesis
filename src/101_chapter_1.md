# Theory of Fundamental Interactions {#sec:theory}

\epigraph{Nothing in life is to be feared.
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
and principles regarding basic symmetries.
In this chapter, a non-exhaustive introduction to this theory and its
descriptive reach will be provided together with a summary of the known
limitations and possible extensions or alternatives.
Given the experimental character of the research discussed in the following
chapters, the aim of this chapter is not solely the discussion of the
fundamental structure and properties of the theory, but also
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

From a historical perspective, this theory is the product of
a succession of important theoretical developments and experimental
discoveries over the last century [@weinberg2004making],
culminating
with the discovery of the Higgs boson in 2012 [@higgs2012cms;@higgs2012atlas].
If a more principled viewpoint is taken, the SM can be thought
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
color while the $SU(2)_{L} \otimes U(1)_{Y}$ is
retated with electroweak interactions (unification of weak and
electromagnetic) and the conservation of isospin and
hypercharge.
<!--- Check and unify notation L (mean only coupling to left-handed
fermions) while the other subindex come from the generators --->

 
The SM is typically specified using the Lagrangian formalism and depends
on a total of 19 parameters, which are not predicted by the theory
but determined through experimental measurements.

![Standard Model Particles
](gfx/101_chapter_1/Standard_Model_of_Elementary_Particles.pdf){
#fig:standard_model_particles width=70%}

In the context of the SM, excitations of the fundamental fields
give rise to two types of elementary particles: fermions (characterised
by having half-integer spin) and bosons (characterised by having
integer spin). Fermions are the fundamental constituents of matter
are further subdivided into leptons and quarks depending on their 
interactions. A schematic overview of the fundamental particles
of the SM and their properties is provided in
[@Fig:standard_model_particles].


## Beyond the Standard Model {#sec:sm_alternatives}

The experimental success of the Standard Model and its main 
subcomponents QED, QCD and EW unification and
symmetry breaking is clearly incontestable, ranging from the confirmation
of theoretical prognotiscation of the existence and some the properties
of new particles
(e.g. $Z$, $W^{\pm}$ and Higgs bosons or top quark) to
the agreement of precise predictions with meticulous experimental
observations. The fine structure constant $\alpha$ at zero energy scale
is an example of the latter, the experimentaly determined value being
compatible with the Standard Model based theoretical prediction up
to 12 orders of magntitude [cite]. In addition to describing natural phenomena
with unprecedented accuracy, the SM it is a self-consistent theory that 
provide non-divergent predictions at the highest energy scales probed to date.

### Known Limitations


Nevertheless, several shortcomings of the Standard Model are known
and hence is not considered as a complete theory of natural phenomena
at the most fundamental scales. Those concerns include unexplained empirically
observed phenomena such as gravitational interactions, neutrino masses or
dark matter particle candidates,
theoretical considerations regarding the stability of vacuum or
aesthetic principles such as naturalness.
Hence, it is presumed that the Standad Model is an effective theory, able to
succesfully describe fundamental processes within a range of energies as
an approximation fo more complete unified theory. For completeness, the
main empirical and theoretical concerns are summarised:


* **omission of gravitational interactions**: the current formulation of
 the SM completely disregards the effect of gravity in
 fundamental interactions, because no consistent quantum descriptions for
 gravity matching the experimental predictions of the well-established
 theory of general relativity [cite] have been developed to date. While several
 theoretical efforts are ongoing, such as loop quantum gravity [cite]
 or string theory [cite],
 the coupling for gravitational interactions at the current experimental
 high-energy reach is expected to be more than 30 times weaker than for
 weak interaction, and hence can be safely ignored when computing theoretical
 predictions.
 
* **lack of a viable Dark Matter candidate**: through a variety of
  astrophysical observations, including the observed galaxy rotation
  curves [cite], gravitational lensing [cite]
  and the Cosmic Microwave Background (CMB) [cite], there is clear
  evidence indicating the presence of more gravitational interacting matter
  in the universe than what is expected by contrasting with the
  electromagnetic sprectra. It has been estimated that about $85\%$ of
  massive existing matter in the universe does not notably interact
  with ordinary matter and radiation [cite], and therefore is referred
  as *Dark Matter*. While its particular nature is still unknown, scientific
  consensus seem to favour long-lived cold non-baryonic matter as an explanation,
  predominatly weakly-interacting massive particles (WIMPs). The three
  neutrino types are the
  only WIMP candidates within the Standard Model, but considering
  the known upper limits on their masses, could only account for very
  small fraction of dark matter. 
  
  
* **unexplained matter-antimatter asymmetry**: as discussed in
  Section [-@sec:standard_model], each matter particle in the Standard
  Model has an anti-matter parner that is identical but with opposite quantum
  numbers. Because pair creation and anhilation processes are symmetric, but
  our univese is manifestly dominated by what we refer as matter, some
  asymmetric interaction proceses ought to exist. Within the SM, some
  electroweak processes are known to violate CP-symmetry and potentially
  explain a small part of the observed matter-antimatter asymmetry. New
  unkwnown CP-symmetry processes, potentially through interactions not
  included in the SM, are needed to resolve this disparity.

* **origin of neutrino masses**:

* **mismatch between vacuum energy and Dark Energy**: in addition of providing
  evidence for dark matter, astrophysical observations such as studies of the
  properties of the Cosmic Microwave Background [cite] or the red shift of
  type Ia supernovae [cite], consistently point to the hyphothesis of
  an accerating expansion of the current universe. The simplest way to account
  for this in cosmological models is to include a cosmological constant,
  which be understood of an intrinsic energy density of the vacuum, exerting
  a negative pressure and therefore driving the observed expansion of the
  universe. In fact, in order to reconcile the theoretical models with
  experimental observations, about $68\%$ of the total energy in the
  present universe would correspond to these type of unknown energy
  density, generally referred as *dark energy*. In most quantum field theories,
  such as the Standard Model, some non-zero zero-point
  energy originating from quantum fluctuations is expected. However,
  modern attempts to predict energy densities from QFT are at variance
  with the observed energy vacuum energy density, some of them differing in
  120 orders of magnitude [cite].
  
  
* **naturalness, hierarchy and fine-tunning concerns**:

Other possible issues have also been raised, that likely can be adressed once
the higher precision measurements of the SM become available,
such as the apparent vacuum meta-stability [cite] or
the strong CP problem [cite].

### Possible Extensions

## Phenenomenology of proton collisions {#sec:pheno}

Once the properties and limitations of the theoretical model that best
describes the current understanding of the fundamental structure and
dynamics of nature have been described,
we can delve into how to model proton-proton collisions from a 
quantitative perspective, so theoretical predictions
can be contrasted with experimental results at the LHC. The focus
of section then is to make sense of the various outcomes of high-energy
proton-proton collisions and how we can predict their relative
rates of ocurring given some initial state
conditions of the interaction.

A related consideration that is useful as an introduction to the
aforementioned topic is the question of what outcomes can
originate as a result of proton-proton collisions.
An answer somehow circular but compatible with our
current interpretation of the universe
is that everything that could be produced would be produced,
meaning that any outcome that can happen
in a way that is consistent with the underlying propierties
of nature is possible. Even though the true description
the properties of nature is not kwown, as discussed in Section
[-@sec:standard_model], the Standard Model
provides an effective model and restricts considerably the space
of possible outcomes, in a way that can be compared with experimental
observations. It is worth noting that alternative descriptions of
nature, such as those motivated by the known limitations of the SM
and reviewed in Section [-@sec:sm_alternatives], can provide alternative
mechanisms for the production of outcomes that are not allowed by the SM,
and hence often drive the experimental searches for evidence of New Physics.

For those physical processes that could happen as a product of a proton-proton
collision, under the assumption of validity of a particular theoretical model,
their total expected rate of ocurrence is one the most relevant
quantities to predict and compare with observation.
To ease its experimental interpretation,
the rate of ocurrence of certain process is commonly
expressed as as a cross section $\sigma$,
which has dimensions of area and is typically expressed in submultiples
of barn ($1 \textrm{barn} = 10^{-28} \textrm{m}^2$). The advantage of cross
sections over rates is that their value is independent from the density
of the incident particle fluxes. The rate, or probability per unit of time,
of a process ocurring can be computed simply by multiplying its cross
section by the instantaneous luminosity $\mathcal{L}(t)$, which
correspoonds to the number of particles per unit of area per unit of time
crossing in opposite directions in the collision volume.

Another related concept, which is specially important for simulating
interactions,
is the differential cross section $d\sigma$. While the initial state
conditions are fixed, the rate of
ocurrence of a physical process can be expressed as as a function of
some final-state
variables, such as the angle and energy of outgoing particles. While these
variables can be integrated over to compute total cross sections $\sigma$,
the integrand is proportional to the probability density of each
outcome happening as a function of final-state variables so is
crucial for modelling their multi-dimensional distributions
via random sampling. In fact, we will be dealing
with differential cross sections instead of total process cross section
in this section for generality.

A complication that has not been addressed yet is that protons are
composite particles, formed by two up-type quarks
and one down-type quarks bound together via the strong force.
The dynamics of proton-proton scaterring are therefore dictated by quantum
chromodynamics (QCD), which cannot be adressed perturbatively for low
energies, limiting the first principles computation of relevant
observables for the most common interactions. Luckily for us,
the most promising territory being explored in energy colliders correspond
to higher energies, where relevant interaction outcomes come from the
hard scattering of proton constituents (referred as partons)
at high energies, and predictions can
be perturbatively approximated under the assuming asymptotic
freedom.

Even for modelling hard scattering processes, non-perturbative input is
required, mainly the probability of finding a particular proton constituent
with a certain momentum fraction inside each of the colliding protons,
refferred as the parton distribution function (PDF).
The model of the proton as three quarks coupled by strong force 
is too simplisticfor modelling proton-proton scattering realistically,
specially at high energies. The continous exchange of gluons between the three 
constituent quarks effectively generates
a sea of virtual quark-antiquark pairs from which other partons can
scatter off. Consequently, in the interaction of two protons, not only
the constituent quarks, referred as valence quarks, can take part in the
hard scattering process but also gluons and sea quarks. At time of writing,
PDFs are not computable from first principles so they
have to be parametrized and extrapolated from various experimental sources
including fixed-target proton deep inelastic scattering (DIS) and previous
collider studies. It is worth noting that the distribution functions depend
strongly in the energy scale of the process, but the evolution for parton
densities can be modelled theoretically [cite DGLAP]. Given their relevance
for computing observables in high-energy colliders,
several research collaborations such as NNPDF [cite] provide accurate
estimations that can be readily used for simulation and prediction. In
Figure [include], the parton distribution functions at two different
energy scales estimated by one of those collaborations are shown, at lower
energy scales the valence quarks (up and down) dominate while when we
extrapolate at higher energies, gluon scattering become the most likely
outcome for the interaction.


<!--- TODO: include GOOD parton distribution function figure -->
 


Let us consider the computation the differential cross section for a hard
scattering process $pp \rightarrow X$, which will be denoted as
$d\sigma(pp \rightarrow X)$, for two protons colliding head on
at center of mass energy $s$. Here
$X$ denotes a possible outcome for the interaction, not necesarialy a single
particle (e.g. a Higgs boson $X=H$) but a set of particles (e.g. a bottom
quark-antiquark pair $X=b\hat{b}$). According to the QCD factorisation
theorem [cite], the differential cross section for $d\sigma(pp \rightarrow X)$
can be expressed as a sum of functions of the partonic cross section 
$d\hat{\sigma}_{ij \rightarrow X}$:  

$$d\sigma(pp \rightarrow X) = \sum_{i,j} \int
f_i(x_1, \mu_F^2) f_j(x_2, \mu_F^2)
d\hat{\sigma}_{ij\rightarrow X} (s x_1 x_2,\mu_R^2,\mu_F^2)
  d x_1 d x_2$$ {#eq:qcd_factorisation} 


where $i$ and $j$ being the partons involved (e.g. a certain type of quark or
a gluon), $f_i(x_1, \mu_F^2)$ and  $f_j(x_2, \mu_F^2)$ are their parton distribution
functions for given momentum fractions $x_1$ and $x_2$ respectively, $\mu_F$ is
the factorisation scale and $\mu_R$ is the renormalisation scale. The
differential partonic cross section $d\hat{\sigma}_{ij\rightarrow X}$ for
at center of mass energy of the interacting partons $\hat{s}=s x_1 x_2$,
can be calculated perturbatively at different expansion orders from
the Lagrangian density as hinted in Section [-@sec:standard_model]. The
total cross section  $\sigma(pp \rightarrow X)$ can
then be attained by integrating out all final state quantities, commonly
referred as phase space variables, in the differential cross section element
$d\sigma(pp \rightarrow X)$.






