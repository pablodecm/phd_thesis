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
[MissMJ (CC BY 3.0 license)](https://commons.wikimedia.org/wiki/File:Standard_Model_of_Elementary_Particles.svg).
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
from first principles, and thus can only be determined through
experimental measurements.

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
particles are understood as excitations of fields that extend through the whole
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
it is possible to obtain the relativistic field theory version of
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
minimising the action $\delta S=0$ can be used to obtain field equations
of motion that correspond to the Dirac equation [@Peskin:257493] for the
spinor field and its adjoint:
$$ i\gamma^\mu \partial_{\mu} \psi - m \psi=0 \quad \textrm{and} \quad
   i\gamma^\mu \bar{\psi} \partial_{\mu} + m\bar{\psi}=0
$$ {#eq:dirac_equation}
as well as the well-known Klein-Gordon equation component-wise
$(\partial^\mu \partial_\mu + m^2)\psi=0$,
where $\partial^\mu=\partial/\partial x^\mu$. Both Dirac and
Klein-Gordon equations were proposed in the context of a relativistic
formulation of quantum mechanics.

To shed some light on how a field like $\psi$ can represent actual fermions
in the universe, such as electrons or positrons, can be quantised
by considering a plane wave expansion and defining annihilation operators
$a_{\boldsymbol{p}}^s$ and $b_{\boldsymbol{p}}^s$, as well as 
creation $a_{\boldsymbol{p}}^{s\dagger}$ 
and $b_{\boldsymbol{p}}^{s\dagger}$ operators. The field and its adjoint,
which can also be thought of directly as operators in this context, can
then be expressed as:

$$
\psi(x) = \int \frac{d^3p}{(2\pi)^3} \frac{1}{\sqrt{2 E_{\boldsymbol{p}}}}
\sum_s \left ( a_{\boldsymbol{p}}^s u^s(p) e^{-ipx} +
b_{\boldsymbol{p}}^{s\dagger} u^s(p) e^{ipx} \right )
$$ {#eq:field_quant}

$$
\bar{\psi}(x) = \int \frac{d^3p}{(2\pi)^3} \frac{1}{\sqrt{2 E_{\boldsymbol{p}}}}
\sum_s \left ( b_{\boldsymbol{p}}^s \bar{v}^s(p) e^{-ipx} +
a_{\boldsymbol{p}}^{s\dagger} \bar{u}^s(p) e^{ipx} \right )
$$ {#eq:field_adjoint_quant}

where $u^s (p)$ and $v^s(p)$ and its adjoints are the free particle solutions of the
Dirac equation, $s$ is their spin and $E_{\boldsymbol{p}}$ their energy.
The operators in the previous quantisations
can be used to define arbitrary many-particle states. The vacuum
state $\ket{0}$ can be defined as the state for which
$a_{\boldsymbol{p}}^s\ket{0}=b_{\boldsymbol{p}}^s\ket{0}=0$. A single
free fermion state of momenta $\boldsymbol{p}$ and spin $s$
can be obtained by applying the creation operators on the vacuum state
$\ket{\boldsymbol{p}, s} = \sqrt{2E_{\boldsymbol{p}}}a_{\boldsymbol{p}}^{s\dagger}\ket{0}$ -
or alternatively an anti-fermion if the $b_{\boldsymbol{p}}^{s\dagger}$ is used
instead. Multi-particle free states in momenta representation
can analogously be defined by the successive application of creation operators
over momenta space.

In particle colliders, we are instead interested in interacting theories
rather than free theories, given the we aim to compute total
and differential cross sections. Interacting theories can also be characterised
by their Hamiltonian density
$\mathcal{H} = \mathcal{H}_\textrm{free}+ \mathcal{H}_\textrm{int}$, 
which can be expressed as a function the
Lagrangian density $\mathcal{H}= \pi^a \dot{\psi}_a - \mathcal{L}$,
where $\dot{\psi}_a$ is the time derivative of the field and 
$\pi^a$ is the conjugate momentum. The Hamiltonian density can
divided in $\mathcal{H}_\textrm{free}$, that is the part
corresponding to
the free theory and $\mathcal{H}_\textrm{int}$ that are the additional terms
due to interactions. In interacting theories, time-dependence becomes more
important and depends only on the $\mathcal{H}_\textrm{int}$ component.
Additionally, the ground state $\ket{\Omega}$ can be different
from the free theory vacuum state $\ket{0}$.

Let us denote by $\ket{i}=\ket{\psi(t \rightarrow - \infty)}$
and $\ket{f}=\ket{\psi(t \rightarrow + \infty)}$ some arbitrary
initial and final multi-particle states respectively, temporarily far before
and after the actual interaction being studied happened (i.e. around $t=0$).
The observables of interest, which are discussed in [Section @sec:pheno],
are a function of the transition amplitude $\bra{i} \mathcal{S} \ket{f}$
over all possible initial and final states. The transition probability
$|\bra{i} \mathcal{S} \ket{f}|^2$ is then a function of the $\mathcal{S}$
which describes the time-evolution from the initial states the final
state. The $\mathcal{S}$ matrix can be expressed as a perturbative
series using the Dyson expansion:
$$
\begin{aligned}
\mathcal{S} &=
T \left [ \exp \left ( -i  \int_{-\infty}^{\infty} d^4 x \mathcal{H}_\textrm{int} (x) \right ) \right ] \\
&= \sum_{n=0}^{\infty} \frac{(-i)^n}{n!} \int_{-\infty}^{\infty} d^4 x_1 ... 
\int_{-\infty}^{\infty} d^4 x_n T \left [ \mathcal{H}_\textrm{int} (x_1) ...
\mathcal{H}_\textrm{int} (x_n) \right ]
\end{aligned}
$$ {#eq:s_matrix}
where T is an operator ensuring that the Hamiltonian density factors
$\mathcal{H}_\textrm{int} (x_i)$ are
order in time. Each time-ordered term in the series can be written as a
sum of normal (i.e. not time ordered) products of permutations using
Wicks theorem [@wick1950evaluation], which can become rather tedious
for high orders. The
formalism of Feynman diagrams can be used to simplify the computation
of observables at a given order in the perturbative expansion.

Based on the previous perturbative series expansion, 
the transition amplitude $\bra{i} \mathcal{S} \ket{f}$
can be easily linked with scattering observables when denoted as:
$$
\bra{i} \mathcal{S} \ket{f} = \bra{i} \boldsymbol{1} \ket{f}
+ i \mathcal{M} (2\pi)^4 \delta^4 \left ( \sum p_i - \sum p_f \right )
$$ {#eq:matrix_element}
where the fist term corresponds to no interaction occurring
and the second includes the matrix element $\mathcal{M}$ 
including all orders in the perturbative orders and a factor
making explicit the conservation of momentum between the initial
and final state particles. The matrix element $\mathcal{M}$, which
can be computed perturbatively
as a function of the momenta of the particles
given final state considered, can be used to define the
differential cross section:
$$
\frac{d \sigma}{d \Phi} \sim | \mathcal{M} |^2 \ \textrm{where} \ 
d\Phi = (2\pi)^4 \delta^4 \left ( \sum p_i - \sum p_f \right )
\prod_f \frac{1}{2 E_f} \frac{d^3 \boldsymbol{p}_f}{(2\pi)^3}
$$ {#eq:diff_cross_section}
where the proportionality factor is a function of the initial state
particles momenta and $d\Phi$ is the full phase space
differential element for
which can be generally expressed as a product of the
final state particle momenta differential elements. Total scattering
rates can be obtained by summing over possible initial and final states
and integrating over final states. Both differential and total cross
sections can be truncated at a given perturbative order. The lowest
expansion order is referred as leading order (LO), yet considering
additional expansion can greatly increase the prediction accuracy
so one (NLO) or two (NNLO) orders are often considered, higher orders
often being too computationally challenging. A truncation at an additional
order $n$, relative to the lowest interaction order, will provide corrections
proportional to $\alpha=g^2/(4\pi)$, where $g$ is the coupling constant
characteristic of the interaction.


### Quantum Chromodynamics {#sec:qcd_detail}

In a hadron collider such as the LHC, strong interactions
between quark and gluons are dominant, and they can be modelled
using quantum chromodynamics (QCD). The theory of QCD can
be linked to a $SU(3)$ symmetry group and is described
by the following gauge invariant
Lagrangian density:

$$
\mathcal{L}_\mathrm{QCD} = \bar{\psi}
\left( \gamma^\mu D - m_f \right) \psi -
\frac{1}{4}G^a_{\mu \nu} G^{\mu \nu}_a, \quad 
\psi = 
\begin{bmatrix}
\psi_r \\ \psi_g \\ \psi_b
\end{bmatrix}
$$ {#eq:qcd_lagrangian}

where $\psi$ is a spinor quark field for a given
flavour
$f \in \{ \textrm{u}, \textrm{d}, \textrm{s},
\textrm{c}, \textrm{b}, \textrm{t}\}$ and quark mass $m_f$,
and each vector component represents a colour degree
of freedom. Assuming that the Gell-Mann matrices $\lambda^a$
are used to define a basis for the gluon field
$A_\mu = 1/2 \lambda^a \sum A_\mu^a$, the covariant
derivative can be defined as
$D^\mu= \partial_\mu  - i g_s \, A_\mu$, where
$g_s$ is the strong interaction coupling.
In turn, the gluon field strength
tensor $G^a_{\mu \nu}$ is also
related with the gluon field components:

$$
G^a_{\mu \nu} = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a
+ g_s f^{abc}  A_\mu^b A_\nu^c
$$ {#eq:qcd_gluon_tensor}
where $f^{abc}$ are the structure constants of the
$SU(3)$ gauge group. The last term accounts for the
self-interaction of the gluon, which are the massless
and electrically neutral force mediators. There are
two properties of QCD that play an important roles
from from a phenomenological standpoint:
*confinement* and *asymptotic freedom*.

The property of confinement has been postulated to explain why isolated
quarks and gluons are not found in nature. Quarks have only been found
as part of hadrons, that are colour-neutral composite particles. Even
though confinement has not been understood from first principles, because
the observables of bound states in QCD at low-energies cannot
be computed in a perturbative manner, there exist extensive evidence
both from lattice QCD calculations and experiments. In a bound state
between quarks, the effective potential includes a term that increases
proportional to their distance, so when the quarks are separated by
an external energetic interaction, the additional potential energy generates
an additional quark-antiquark pair and forming bound states. Similar
phenomena occur for isolated gluons, which generally is referred as
hadronization due to colour confinement. In particle colliders, successive
hadronization and radiation processes lead to parton showers
(see [Section @sec:parton_showers]).

Hadrons are then commonly in bound states which can be mesons, formed
by a quark-antiquark pair $\textrm{q}\bar{\textrm{b}}$, or baryons
that are composed of three quarks $\textrm{q}\textrm{q}\textrm{q}$. Charged and
neutral pions $\pi^{+}$ ($\textrm{u}\bar{\textrm{d}}$) and
$\pi^{0}$ ($(\textrm{u}\bar{\textrm{u}}-\textrm{d}\bar{\textrm{d}})/\sqrt{2}$),
kaons $\textrm{K}^{+}$ ($\textrm{u}\bar{\textrm{s}}$) and
$\textrm{K}^{0}$ ($\textrm{d}\bar{\textrm{s}}$) and the $\textrm{J}/\Psi$ meson
($\textrm{c}\bar{\textrm{c}}$) are among the most common mesons produced
at particle colliders. Baryons instead include the well-known proton
($\textrm{u}\textrm{u}\textrm{d}$) and neutron
($\textrm{u}\textrm{d}\textrm{d}$) that together with electrons are the
constituents of most of the known matter in the universe. Many more
short-lived baryons exist [@PhysRevD.98.030001], in addition to the
recently discovered exotic bound states referred as tetraquarks
[@PhysRevLett.112.222002]
and pentaquarks [@Aaij:2015tga]. A detailed description of the compositeness
of proton is an essential element for computing LHC observables,
as reviewed in [Section @sec:pdfs].

Asymptotic freedom is instead linked with the strength reduction of the
strong coupling constant when higher energy scales are considered. Let us
consider a renormalisation energy scale $\mu_R^2$, which has to be often defined
in order to compute physical observables which otherwise would be divergent
due higher order perturbative corrections which cannot be easily calculated.
This effect can be also understood as a coupling that varies with
the energy scale, which is referred to as a "running" coupling constant.
The strong force
coupling $\alpha_s=g_s^2/(4\pi)$ can thus be approximated as a function of
the renormalisation energy scale $\mu_R^2$ as follows:
$$
\alpha_s(\mu_R^2) = \frac{\alpha_s(\mu_0^2)}{1+\alpha_s(\mu_0^2)
\frac{33-2n_f}{12\pi} \ln \left ( \frac{\mu_R^2}{\mu_0^2} \right)}
$$ {#eq:running_coupling}
where $\alpha_s(\mu_0^2)$ is the measured coupling at a given energy
and $n_f$ is total number of quark flavours which are assumed to be
massless in this approximation. The strong interaction thus becomes
weaker at higher energies (or short distances) allowing
the perturbative computation of some observable related with high-energy
interactions, as discussed in [Section @sec:pheno].
The approximation from [Equation @eq:running_coupling] also provides a
lower bound for the energy scale at which QCD can be treated
perturbatively, i.e. the denominator becomes
zero for an energy scale around $200\ \textrm{MeV}$, leading
to a diverging coupling constant.

### Electroweak Interactions  {#sec:ew_detail}

The remaining two fundamental interactions between elementary particles
are the electromagnetic and the weak force. The description of
the electromagnetic interaction in terms of quantum fields and gauge
symmetries, leading to the development of quantum electrodynamics (QED)
in the late 1940s, prompted a quest for an analogous theory for the weak
force. The weak force,
known to be responsible for the beta decay at the time,
could effectively be modelled
using Fermi theory using four-fermion interactions [@fermi1934attempt]
but was not renormalisable and lacked the predictive capabilities
and elegance of QED. A large theoretical effort lead to an alternative
description based on a $SU(2) \otimes U(1)$ symmetry, which unified
electromagnetic and weak interactions
[@glashow1961partial; @SALAM1964168], and where the
weak interaction was mediated by means of charged $W^{\pm}$ and neutral $Z$
massive vector bosons. Nevertheless, the theory does not provide
an explanation for
the mass of the weak mediators, until the so-called
Brout-Englert-Higgs [@englert1964broken; @higgs1964broken; @guralnik1964global]
mechanism for spontaneous symmetry breaking (SSB) was conceived. Higgs
also noted explicitly that the mechanism would effectively create an additional
scalar field, associated with a new scalar boson, whose existence could
experimentally testable. The SSB mechanism was then combined with
$SU(2) \otimes U(1)$ unified theory [@weinberg1967model]
to give rise to what is now known as *electroweak theory*, which was then
proved to be renormalisable [@THOOFT1972189].

The different testable properties of electroweak phenomena were verified
by experiments including the existence of weakly-interacting neutral
charged and neutral currents [@hasert1974observation] and the discovery
of the massive
$W^{\pm}$ [@Arnison:1983rp; @Banner:1983jy] and $Z$
[@Arnison:1983mk; @Bagnaia:1983zx] bosons. Experimental evidence also
showed that weak interaction was parity violating [@Wu:1957my],
thus in the electroweak theory the fermion fields are separated in their
left-handed $\psi_\textrm{L}$ and right-handed $\psi_\textrm{R}$ 
chiral components as follows:
$$
\psi_\textrm{L} = \textrm{P}_\textrm{L} \psi= \frac{1}{2} (1 - \gamma_5) \psi \quad
\psi_\textrm{R} = \textrm{P}_\textrm{R} \psi = \frac{1}{2} (1 + \gamma_5) \psi
$$ {#eq:chiral_proj}
where $\textrm{P}_\textrm{L}$ and $\textrm{P}_\textrm{R}$ are the chiral
projection operators and $\gamma_5=i \gamma_0\gamma_1\gamma_2\gamma_3$ is
the product of the gamma or Dirac matrices. For massless particles,
chirality is equal to the helicity
$H=(\boldsymbol{p} \cdot \boldsymbol{s}) /  | \boldsymbol{p} |$
which is the sign of the scalar
product of momenta and spin. For massive particles, chirality is still defined
but is not identical to helicity which cannot be invariantly defined.

Within the electroweak theory, fermion fields are broken in into
their left-handed components, which can be expressed as doublets
that would transform under
$SU(2)$, and can be denoted as:
$$
L_q = \left \{
\begin{pmatrix} u  \\ d \end{pmatrix}_L ,
\begin{pmatrix} c \\  s \end{pmatrix}_L ,
\begin{pmatrix} t  \\ b \end{pmatrix}_L
 \right\} \quad 
 L_l = \left \{
 \begin{pmatrix} \nu_e \\ e\end{pmatrix}_L ,
 \begin{pmatrix} \nu_\mu \\ \mu \end{pmatrix}_L ,
 \begin{pmatrix} \mu_\tau \\ \tau \end{pmatrix}_L
 \right\}  
$$ {#eq:ew_left}
and their right handed components, that instead can be expressed as
singlets only transforming under $U(1)$:
$$
R_u = \left \{ u_R, c_R, t_R \right \} \quad
R_d = \left \{ d_R, s_R, b_R \right \} \quad
R_l = \left \{ e_R, \mu_R, \tau_R \right \}
$$ {#eq:ew_right}
where the right-handed neutrino components are omitted in the electroweak
theory (and the SM), given they are electrically neutral and would not
interact weakly when right-handed.

The electroweak interactions then can be made explicit by introducing
additional boson fields $W= \{ W^1, W^2, W^3 \}$ and $B$ which will
interact with the fermions. Similarly in structure to QED (and also
QCD as described in
[Section @sec:qcd_detail]), the electroweak Lagrangian before
spontaneous symmetry breaking is composed
by interaction terms for the previous doublet and singlet fields,
characterised by a covariant derivative, and kinematic terms for
both boson fields:
$$
\begin{aligned}
\mathcal{L_\textrm{EW}} =  &
\sum^{\psi \in \{ L_q, L_l \}} \bar{\psi} (i \gamma_\mu D_L^\mu)\psi +
\sum^{\psi \in \{ L_q, L_l \}} \bar{\psi} (i \gamma_\mu D_R^\mu)\psi \\
& - \frac{1}{4}  W_{\mu\nu}W^{\mu\nu} - \frac{1}{4} B_{\mu\nu}B^{\mu\nu}
\end{aligned}
$$ {#eq:lagrangian_ew_before}
where the covariant derivatives for left-handed $D_L^\mu$
and right-handed $D_R^\mu$ fermion fields are respectively defined as:
$$
\begin{aligned}
& D_L^\mu  = \partial^\mu - \frac{1}{2} g_B Y B_\mu  - \frac{1}{2} g_W \sigma W_\mu \\
&  D_R^\mu  = \partial^\mu - \frac{1}{2} g_B Y B_\mu
\end{aligned}
$$ {#eq:ew_cov_der}
where $\sigma = \{ \sigma_1 , \sigma_2, \sigma_3\}$ are the Pauli matrices
and $g_B$ and $g_W$ are the coupling constants. The $W_{\mu\nu}$ and
$B_{\mu\nu}$ field strength tensors from kinematic terms can in turn
be obtained as:
$$
\begin{aligned}
& W^i_{\mu\nu} = \partial_\mu  W^i_\nu - \partial_\mu  W^i_\mu
- g_W  \epsilon^{ijk} W^i_\mu W^k_\nu \\
& B_{\mu\nu} =  \partial_\mu  B_\nu - \partial_\mu  B_\mu
\end{aligned}
$$ {#eq:ew_field_tensors}
where $\epsilon^{ijk}$ is the Levi-Civita symbol for each permutation, which
is the structure constant for $SU(2)$.


### Symmetry Breaking and the Higgs Boson {#sec:ewsb_higgs}

The problem with the electroweak theory as described by the Lagrangian
from [Equation @eq:lagrangian_ew_before], which is based on Yang-Mills
gauge theory formulation, is that it is not possible to directly add mass
term for the fermions nor the weak bosons to the Lagrangian
density without breaking the $SU(2)$
invariance. At the time the mentioned theory was developed, there was
extensive evidence not only for lepton masses but also
for the weak bosons being massive; the mass required to explain why
the weak interaction was short-ranged.
The issue of lacking a theoretical mechanism that could explain the mass
of fermions and weak boson was solved by the spontaneous symmetry
breaking mechanism [@englert1964broken; @higgs1964broken; @guralnik1964global],
which is based on postulating the existence of an additional complex scalar
field $\phi$, which is a $SU(2)$ doublet with the following structure:
$$
\phi =
\begin{pmatrix} \phi^+ \\ \phi^0 \end{pmatrix} =
\begin{pmatrix} \phi_3 + i\phi_4  \\ \phi_1 + i\phi_2 
\end{pmatrix}
$$ {#eq:higgs_su_field}
where we made the component notation explicit because it will be
relevant later.
This scalar field is expected to interact with the electroweak fields
$W$ and $B$ by means of the following Lagrangian:
$$
\mathcal{L}_\textrm{scalar} = (D^H_\mu \phi)^\dagger (D^\mu \phi) - V(\phi)
$$ {#eq:scalar_lagrangian}
where the covariant derivate in this case is defined as:
$$
D_H^\mu  = \partial^\mu - \frac{1}{2} i g_B Y B_\mu  - \frac{1}{2} i g_W \sigma W_\mu.
$$ {#eq:scalar_cov_der}
The minimal form for scalar field potential $V(\phi)$,
constructed ad-hoc to provide a degenerate vacuum states
and a local maximum, a required condition for spontaneous symmetry breaking
can be expressed as:
$$
V(\phi) = - \mu^2 \phi^\dagger \phi + \frac{1}{2} \lambda (\phi^\dagger \phi )^2
$$ {#eq:scalar_potential}
where both the quadratic $\mu^2$ and the quartic
$\lambda$ self-interaction parameters are defined positive in this sign
convention. The resulting shape for the potential is often referred
as *mexican hat*, and is depicted in [Figure @fig:mexican_hat]. The presence
of a potential minimum different from the origin
gives rises to a non-zero vacuum expectation value for the scalar
field:
$$
\langle \phi \rangle_0 = \frac{\mu^2}{\lambda} = v^2
$$ {#eq:scale_vev}
whose values depends on the $V(\phi)$ potential parameters $\mu^2$ and
$\lambda$, and it is denoted as $v^2$ for convenience. The non-zero
vacuum expectation value is thus said to spontaneously break the
the $SU(2) \otimes U(1)$ symmetry, the consequences made more
clear when the field is expanding around the minimum:
$$
\phi = \frac{1}{\sqrt{2}} \exp(i \frac{\sigma \cdot G}{v})
\begin{pmatrix} 0\\ v + H \end{pmatrix}
$$ {#eq:scalar_expansion}
as a product of a scalar field $H$ and a complex exponential of the
scalar product of a three-component field $G=\{G_1, G_2, G_3\}$ with
the Pauli matrices $\sigma=\{\sigma_1, \sigma_2, \sigma_3\}$.
The complex exponential phase
can be then removed by a $SU(2)$ group rotation, a transformation
that is often referred as *unitary gauge*. The resulting scalar field
can simple be expressed as:
$$
\phi = \frac{1}{\sqrt{2}}
\begin{pmatrix} 0\\ v + H \end{pmatrix}
$$ {#eq:scalar_rotation}
where three of the four degrees of freedom in [Equation @eq:higgs_su_field],
which correspond the field $G$ which would otherwise give rise to the
so-called Goldstone bosons,
have been removed after the gauge transformation.

![Graphical depiction[^mexican_ref] of the mexican hat potential for
the scalar field
$\phi$. A local
maximum is present at the origin, but lower energy degenerate minima exist
arount it.
](gfx/101_chapter_1/mexican_hat.pdf){
#fig:mexican_hat width=60%}


Substituting the rotated scalar field from [Equation @eq:scalar_rotation]
in the Lagrangian described by [Equation @eq:scalar_lagrangian]
leads to mass-like terms for linear combinations of the $W$ and $B$
fields. In order to obtain the physical bosons observed in nature, the
mass terms have to be made independent by the following
transformations:
$$
W^\pm_\mu = \frac{1}{\sqrt{2}} \left ( W_\mu^1 \mp i W_\mu^2 \right)
\quad
\begin{pmatrix} Z_\mu \\ A_\mu \end{pmatrix} =
\begin{pmatrix} \cos \theta_W  & -\sin \theta_W \\
\sin \theta_W  & \cos \theta_W \end{pmatrix}
\begin{pmatrix} W^3_\mu \\ B_\mu \end{pmatrix}
$$ {#eq:ew_field_change}
where the field $W^\pm$ are associated with the charged weak bosons,
the field $Z$ with the neutral weak boson, the electromagnetic
field $A$ with the photon, and $g_W$ is the Weinberg angle
which is related with the electroweak couplings according
the relation $\tan \theta_W = g_B/g_W$. Omitting for now
the terms related with the $H$ field, the Lagrangian in
[Equation @eq:scalar_lagrangian] leads to the following
mass terms for the electroweak force mediators after
the unitary gauge and the transformation described
in [Equation @eq:ew_field_change] have been applied:
$$
\begin{aligned}
\mathcal{L}_\textrm{EW bosons} =&
\frac{1}{2} \underbrace{\left ( \frac{g_W^2 v^2}{4} \right )}_{m_{W^{+}}^2}
W^{+}_{\mu} W^{+\mu} +
\frac{1}{2} \underbrace{\left ( \frac{g_W^2 v^2}{4} \right )}_{m_{W^{-}}^2}
W^{-}_{\mu} W^{-\mu} + \\
& \frac{1}{2}
\underbrace{\left ( \frac{g_W^2 v^2}{4\cos \theta_W} \right )}_{m_Z^2}
 Z_{\mu} Z^{\mu} +
\frac{1}{2} \underbrace{(\ 0\ )}_{m_{\gamma}^2} A_{\mu} A^{\mu}
\end{aligned}
$$ {#eq:ew_bosons_masses}
resulting in mass terms for the massive weak bosons which are depend
to the weak coupling, the Weinberg angle and the vacuum
expectation value of the Higgs field. The last term for the electromagnetic
field has only been included to make explicit that no mass term is
associated with the electromagnetic force carrier $\gamma$. The terms
related with the scalar $H$ field (and Higgs boson) are discussed
later independently.

In addition to providing a mechanism that leads to mass terms for
the weak force bosons, additional interaction of the various
fermion fields with the scalar field $\phi$ can explain their masses.
These gauge invariant terms are generally referred to as Yukawa
interaction, and correspond to the following Lagrangian terms:
$$
\begin{aligned}
\mathcal{L}_\textrm{Yukawa} =
 &- \lambda_l (\bar{L}_l \phi R_l
 + \bar{R}_l \phi^\dagger L_l ) \\
 &- \lambda_d (\bar{L}_q \phi R_d
 + \bar{R}_d \phi^\dagger L_q )\\
 &- \lambda_u (\bar{L}_q i \sigma_2 \phi^\dagger R_u
 + \bar{R}_u i \sigma_2 \phi L_q )
\end{aligned}
$$ {#eq:Yukawa_Lagrangian}
where $\lambda_l$ , $\lambda_u$ and $\lambda_f$ are the Yukawa coupling
parameters. A charge-conjugate transformation
$\phi \rightarrow i \sigma_2 \phi^\dagger$ is used to give mass
to up-type quarks. For the quark sector,
the $\lambda_u$ and $\lambda_d$ couplings can
be expressed by a single non diagonal matrix in the flavour basis, referred to as
Cabibbo-Kobayashi-Maskawa (CKM matrix) [@Cabibbo:1963yz; @Kobayashi:1973fv],
which can in turn be parametrised
by three angles and a complex phase. The fact that the matrix is not
diagonal leads to flavour mixing, due to the mass eigenstates being different
from flavour eigenstates. Another relevant property of fermion masses
is that after spontaneous symmetry breaking, the fermion mass
is effectively proportional to its coupling with the Higgs scalar field, which
is useful to intuitively understand the dominant interactions and decays.

[^mexican_ref]: The figure was created by adapting the code
from [this TeX StackExchange answer](https://tex.stackexchange.com/a/229226).

In addition of giving masses to both weak bosons and fermions, the
remaining degree of freedom after electroweak symmetry breaking gives
rise to a scalar field $H$, whose Lagrangian can be obtained substituting
[Equation @eq:scalar_rotation] in [Equation @eq:scalar_lagrangian],
leading to the following terms:
$$
\mathcal{L}_{H} = \frac{1}{2} \partial_\mu H \partial^\mu -
- \mu^2 H^2 - \lambda v H^3 - \frac{\lambda}{4} H^3
$$ {#eq:higgs_lagrangian}
where the second (quardratic term) can be interpreted as a scalar boson
with a mass $\sqrt{2\mu^2}$, which is commonly referred as the Higgs
boson. A particle with a mass of $125.09(24)\ \textrm{GeV}$ [@Aad:2015zhl] 
and consistent with the expected properties for the Higgs boson was
discovered in 2012 by the CMS
and ATLAS collaborations [@higgs2012atlas; @higgs2012cms].
The cubic $\lambda v$ and quartic $\lambda$
terms will give rise to self-interaction interaction vertices. The so-called
cubic or trilinear Higgs coupling is discussed in a Higgs pair search
using data from the CMS experiment in [Chapter @sec:higgs_pair].
The direct determination of the Higgs self-coupling
is an relevant missing piece, and an important proof of consistency
of the spontaneous symmetry breaking mechanism.

<!-- ### Standard Model Lagrangian {#sec:sm_lagrangian} -->


## Beyond the Standard Model {#sec:sm_alternatives}

The experimental success of the Standard Model and its main 
subcomponents QED, QCD and EW unification and
symmetry breaking is clearly incontestable, ranging from the confirmation
of theoretical prognostication of the existence and some the properties
of new particles
(e.g. $Z$, $W^{\pm}$ and Higgs bosons or top quark) to
the agreement of precise predictions with meticulous experimental
observations. The fine structure constant $\alpha$ at zero energy scale
is an example of the latter, with its experimentally determined value being
compatible with its Standard Model based theoretical prediction down
to 12 significant digits [@hanneke2008new; @parker2018measurement].
In addition to describing natural phenomena
with unprecedented accuracy, the SM it is a self-consistent theory that 
provides non-divergent predictions at the highest energy scales probed to date.

### Known Limitations


In spite of the successes mentioned above,
several shortcomings of the Standard Model are known
and hence the theory is not considered as a complete theory of natural phenomena
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
  consensus seems to favour long-lived cold non-baryonic matter as an explanation,
  predominantly weakly-interacting massive particles (WIMPs). The three
  neutrino types are the
  only WIMP within the Standard Model, but considering
  the known upper limits on their masses, they can only account for a very
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
  that neutrinos were massless, yet is currently well established
  that neutrinos oscillate between different flavour eigenstates
  [@fukuda1998evidence; @sno2001measurement], implying 
  that flavour states mix and hence that neutrino masses are
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
  with the observed energy vacuum energy density, some of them differing by
  120 orders of magnitude [@adler1995vacuum].
  
  
* **Naturalness, hierarchy and fine-tuning concerns**: as discussed at the
  beginning of [Section @sec:standard_model], the SM can be thought of
  the most general theory based on  a set symmetries, and its
  19 parameters (or 26 accounting for neutrino masses
  and mixing angles)
  are not obtained from first principles but measured experimentally.
  Having such a large number of free
  parameters and observing large differences among their
  relative magnitude has been viewed as a theoretical concern from
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
have also been raised. On of them is
the apparent vacuum meta-stability [@degrassi2012higgs] or
the strong CP problem [@cheng1988strong]. Some of these questions
can be clarified
once the higher precision measurements of the SM become available, which
are mainly obtained in particle collider experiments.

### Possible Extensions {#sec:possible_ext}

The known limitations stated in the previous section have motivated
the development of alternative theories for describing fundamental
interactions. Given the quantitative success of the Standard Model,
most of the known proposed theoretical models are either extensions of
the SM or its associated predictions can be effectively
reduced to those of the SM at the energy range current being
explored in particle physics experiments. The set of alternatives
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

In addition to carrying out precision measurements and model-specific
searches, there exists a
practical way
to consider possible extensions due to New Physics phenomena occurring
at a higher energy scale $\Lambda$ than the one being probed $E$. The
model-independent approach often referred to as *effective field theory* (EFT) [@PhysRevD.11.2856;
@Buchmuller:1985jz] allows to compute
observables by extending the SM Lagrangian terms from [Section @sec:standard_model]
with additional operators:
$$
\mathcal{L}_\textrm{EFT} = \mathcal{L}_\textrm{SM}
+ \sum_i \frac{c_i} { \Lambda^{d_i - 4}} \mathcal{O}_i
$$ {#eq:eft_lagrangian_generic}
where $\mathcal{O}_i$ are referred to as *effective operators*, describing
the characteristics of the new interactions that are considered in the
extended theory and $c_i$ are the the *EFT or Wilson coefficients* that
parametrise the strength of those new interactions. The integer $d_i$
defines the dimension of the operator
$\textrm{dim} \left( \mathcal{O}_i \right) = \left[ E \right]^{d_i}$,
and while in principle 
an infinite set of operators with any dimension $d_i > 4$ can be considered,
their effects is expected to be suppressed by $(E/\Lambda)^{d_i - 4}$ thus
high-dimensional operators may be neglected when studying the dominant
effects of an EFT extension of the SM.

If all the EFT coefficients $c_i$ are zero or the new energy scale $\Lambda$
is infinite, the EFT theory reduces to the SM Lagrangian. Instead,
if $\Lambda \approx
E$, the effective 
approximation in [Equation @eq:eft_lagrangian_generic] does not hold,
and the interactions
have to realistic modelled using the a complete theoretical description
of the New Physics scenario. While in general effective field
theories are not renormalisable, observables and higher-order corrections
can be computed, because of the well-defined cutoff energy scale
$\Lambda$. The best-known example of an EFT that has been used in practice
is Fermi theory, which is a simplification to compute useful observables
at low-energies $E \approx 10\ \textrm{MeV}$ rather than an extension of
the SM, given that the detailed structure of electroweak
interactions due to $\textrm{W}^{\pm}$ boson mediating $\beta$ decays
was unknown at the time.

At the LHC and other collider experiments, the main use case of EFT
is to describe generic extensions of the SM that could arise
due to New Physics at energy scales that are not directly
accessible. From an experimental standpoint, the goal is thus to
constraint the values of the EFT operator 
coefficients using experimental data. Because the for $d_i=5$ the
only possible operator is relevant for neutrino
phenomenology [@weinberg1979baryon], the set
of Lagrangian operators of interest at collider experiments
often corresponds to $d_i=6$ dimension operators. The large set
of possible dimension six operators can be greatly reduced by requiring
that the main experimentally verified properties of the SM
are respected, such as the gauge and Poincaré symmetries, or
baryon number conservation.
In [Chapter @sec:higgs_pair],
a subset of dimension six EFT operators are used 
to study non-resonant extensions of Higgs pair
production in a model-independent manner.

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
the rate of occurrence of any given subnuclear is commonly
expressed as a cross section $\sigma$,
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
occurrence of a physical process can be expressed as a function of
some final-state
variables, such as the angle and energy of outgoing particles. While these
variables can be integrated over to compute total cross sections $\sigma$,
the integrand is proportional to the probability density of each
outcome happening as a function of final-state variables, hence its
evaluation is
crucial for a correct modelling of their multi-dimensional distributions
via random sampling. In fact, we will be dealing
with differential cross sections instead of total process cross section
in this section for generality.

### Parton Distribution Functions {#sec:pdfs}

A complication that has not been addressed yet is that protons are
composite particles, which within a static interpretation can be thought
of as the combination of two up-type quarks
and one down-type quark bound together via the strong force.
The dynamics of proton-proton scattering are then dictated by quantum
chromodynamics (see [@sec:qcd_detail]), which cannot be addressed using perturbation
theory for low
energies, limiting the first principles computation of relevant
observables for the most common interactions.
That said, predictions regarding the interaction outcomes from the
hard scattering of proton constituents (referred to as partons) can
be perturbatively approximated under the assumption of asymptotic
freedom at high energies. This allows the modelling of very high
energy collisions at particle colliders, which are the focus
of most LHC analyses, even if the details
about the parton structure cannot be calculated.


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

When modelling hard (i.e. high energy) scattering processes,
a non-perturbative input is
required, mainly the probability of finding a particular proton constituent
with a certain momentum fraction inside each of the colliding protons,
referred to as the parton distribution function (PDF).
The model of the proton as three quarks coupled by strong force 
is too simplistic for modelling proton-proton scattering realistically,
especially at high energies. The continuous exchange of gluons between the three 
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
strongly on the energy scale of the process, yet the evolution for parton
densities can be modelled theoretically
[@Altarelli:1977zs;@Dokshitzer:1977sg;@Gribov:1972ri]. Given their relevance
for computing observables in high-energy colliders,
several research collaborations such as NNPDF [@Ball:2017nwa] provide accurate
estimations that can be readily used for simulation and prediction. In
[Figure @fig:subfigs_pdfs] are shown the parton distribution functions at two different
energy scales estimated by one of those collaborations, at lower
energy scales the valence quarks (up and down) dominate while when we
extrapolate at higher energies, gluon scattering become the most likely
outcome for the interaction.


### Factorisation and Generation of Hard Processes {#sec:factorisation}


Let us consider the computation of the differential cross section for a hard
scattering process $pp \rightarrow X$, which will be denoted as
$d\sigma(pp \rightarrow X)$, for two protons colliding head on
at centre of mass energy $s$. Here
$X$ denotes a possible outcome for the interaction, not necessarily a single
particle and the proton remnants (e.g. a Higgs boson $X=H + \textrm{other}$),
but a set of particles (e.g. a bottom
quark-antiquark pair $X=\textrm{b}\bar{\textrm{b}} + \textrm{other}$).
According to the QCD factorisation
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
a centre of mass energy of the interacting partons $\hat{s}=s x_1 x_2$,
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
model to consider the problem
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
as well as the formation of hadrons from any
free parton due to colour confinement (see Section [-@sec:qcd_detail]).
Additional processes that affect the collision outcome include
secondary interactions between the protons, as well as the
decays of all generated unstable particles. 
An example of the typical complexity of the physical
processes occurring as a result of a single high-energy proton-proton
scattering is provided in [Figure @fig:event_shower].
These and additional minor effects
(e.g. colour reconnection) are accounted by *parton showering* (PS) programs,
that take as the input the generated particle outcome of the
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
the initial hadron remnants followed by light blue ellipses. For completeness,
an additional hard interaction within the same hadron-hadron process is
shown in purple,
which often has to be accounted for to obtain realistic simulations.
](gfx/101_chapter_1/event_shower.pdf){
#fig:event_shower width=70%}



