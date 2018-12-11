# Experiments at Particle Colliders {#sec:experiment}

\epigraph{Measure what is measurable \\
 and make measurable what is not so.}{Galileo Galilei (attributed)}

In Chapter [-@sec:theory], we reviewed the most successful testable
theory to date
describing the properties and dynamics of our universe at the most
fundamental scales.
Clear limitations of the Standard Model as it is currently
formulated are known,
such as the complete omission of gravity forces or the absence of viable
dark matter candidates, motivating the quest for alternative
unified descriptions of the physical world. A direct
path to verify the predictions of the Standard Model up to high accuracy
and test alternative theoretical models is to collide high energy particles
in a controlled setting and quantitatively study the properties scattering
particles produced. That is the aim of the Large Hadron Collider (LHC) and the
experiments set up around its collision points. In this chapter, the main
design characteristics of a general purpose high-energy physics experiment,
namely the Compact Muon Solenoid (CMS) detector at the LHC, will be explored.
Given the data-centric nature of the next chapters, particular significance
will be given to the acquisition, processing and simulation of individual
experimental observations, commonly referred to as events.


## The Large Hadron Collider

The Large Hadron Collider (LHC) is the largest and most powerful particle
accelerator on operation at the time of writing. Its main purpose is to
accelerate bunches of protons and other heavier nuclei in opposite
directions to ultra-relativistic velocities, so they can be collimated
and made interact at high energies in several specified collision
points inside specially designed detectors.
The LHC machine complex is located at the European
Organisation for Nuclear Research (CERN) laboratories at
the Switzerland-France border near Geneva, its most distinctive element being
a circular ring of superconductive magnets and accelerating structures
installed inside a 26.7 km underground tunnel inherited from the
Large Electron Positron (LEP) collider, as depicted in Figure
[-@fig:LHC_overall]. The setup was designed
to achieve center-of-mass energies up to 14 TeV for nominal instantaneous
luminosities reaching $1 \times 10^{34} \textrm{cm}^{-1} \textrm{s}^{-1}$
for proton-proton collisions, and hence explore the high-energy frontier of
particle physics, extending by a factor of seven the reach at the
highest collision energy, formerly achieved by the Tevatron collider at
Fermilab.


![Depiction of the placement of LHC tunnel and the main experiments
places at its collision points (ATLAS, ALICE, CMS and LHCb) relative
to Geneva and the French-Swiss border.
Image adapted from [@Servicegraphique:1708849].
](gfx/102_chapter_2/LHC_overall.pdf){
#fig:LHC_overall width=70%}

The main reason for building a high-energy proton-proton collider such as the
LHC instead of an electron-positron more powerful than LEP, given the difficulties
when computing observables due to protons being composite particles as described
in Section [-@sec:pheno], is that protons are considerably more massive
and thus their synchrotron radiation loss is greatly reduced, so they can be
accelerated to higher energies more efficiently. Another
practical advantage of proton colliders is that very high
collisions rates (i.e. instantaneous
luminosities) are technically achievable, which makes them suitable for
the discovery of rare but interesting physical processes.
While the LHC and most of its detectors can also be used with to study
collisions
of nuclei from heavier atoms, such as $\textrm{Pb}$, $\textrm{Au}$ 
or $\textrm{Xe}$ ions,
which have important scientific use cases such as recreating
the conditions present in the early universe, in this work we will
be focussing on proton-proton collisions.


### Injection and Acceleration Chain

In order to achieve beam energies of the TeV order, protons have to
follow several stages of synchronised accelerations through a variety
subcomponents of the CERN accelerator complex, whose main subcomponents
as of 2018 are summarised in Figure [-@fig:CERN_Acc_complex].
The purpose of this section
is to outline the sequence of steps followed to obtain the high energy
proton bunches that are used for high-energy collisions at the LHC.


![Schematic representation of the CERN Accerator Complex, including the
the relative placement of the experiments as well as the main
elements of the LHC accelerating chain: LINAC2, PSB, PS, SPS
and the LHC ring. Figure credit to
[Forthommel(CC BY-SA 3.0 license)](https://commons.wikimedia.org/wiki/File:Cern-accelerator-complex.svg).
](gfx/102_chapter_2/CERN-accelerator-complex.pdf){
#fig:CERN_Acc_complex width=70%}


The process begins with the extraction of a low-energy beam of protons by
filling a duoplasmatron device
[@wolf2017handbook] with
gas from a hydrogen $\textrm{H}_2$ bottle. Those protons are then injected
into to a linear accelerator, named LINAC2, which boosts them to an energy
of 50 MeV. The next step of acceleration occurs at the Proton Synchrotron
Booster (PSB), which receives beams split from the
LINAC2 beam line and increases their energy to 1.4 GeV using four
superimposed synchrotron rings. Promptly after, the Proton Synchrotron (PS) 
further splits and boosts the energy of proton bunches to 25 GeV. The
penultimate step of the chain is the Super Proton Synchrotron (SPS) which
accelerates the proton bunches to 450 GeV and injects them in opposite
directions in the LHC ring.

The main LHC machine is composed by two adjacent proton beam lines
(also referred as beam pipes) kept at an ultra-high
vacuum ($10^{-10}-10^{-11}~\textrm{mbar}$), in order to reduce
the likelihood of spurious collisions of the highly-boosted
hadrons with gas molecules. The proton trajectories are bent
around the ring using a total of 1232 super-conducting dipole 
electromagnets,
each 15 m long and kept at a temperature of 1.9 K using
superfluid helium, capable of providing very strong magnetic
fields (up to 8.3 T for a 11.8 kA current). For collimation
of the proton bunches, 392 additional quadrupole magnets are
placed around the ring. Higher-order multipoles are also interleaved
to provide finer corrections of the beam direction and field geometry.
Additional energy to the protons is provided in each revolution
using 8 radio frequency (RF) cavities per beam line, until the
protons reach the desired energy (6.5 TeV during the Run II of the
LHC, which took place between 2015-2018). Given that each cavity can
provide about 60 keV per revolution, it takes about 20 minutes
of *ramp* time to reach collision energies.

During the whole acceleration process, specialised dipole magnets
are used to keep the beams separated at the four interactions points
(IPs) and hence avoid collisions during that time.
With the purpose of maximising
the interaction rates, the beams are made more compact (commonly
referred as *squeezed*) at the interaction region
right before switching to collision mode. Once
the characteristics of the proton beam are suitable, the quadrupoles
align the beam trajectories and collisions begin. A stable
configuration is then adopted by the LHC machine, providing about 7 keV 
of energy per turn to the beam to account for synchrotron radiation losses using
the RF cavities. If unexpected problems do not occur, the proton beams are kept
circling the LHC ring and colliding at the IPs for several hours until
the bunch properties are degraded beyond correction,
a period that typically is referred as a LHC *fill*. The *fill* is
finalised when some problem occurs or when all the proton bunches
inside the ring are *dumped* (made collide) against graphite absorbers
tangent to the beam pipes.
 
### Operation Parameters {#sec:op_pars}

One of the most relevant parameters for a particle collider is the
instantaneous luminosity $\mathcal{L}_\textrm{inst}(t)$, which already appeared in
Section [-@sec:pheno] and corresponds to the number of particles
per unit of area per unit of time crossing each other in the
interaction volume. Given a certain physical process characterised
by a cross section $\sigma$, the number of collisions $n_c$ expected
to occur by unit of time, also known as the rate of such collisions,
can be expressed as:
$$ \frac{dn_c}{dt} = \mathcal{L}(t) \cdot \sigma$$ {#eq:lumi_rate}
thus the luminosity $\mathcal{L}$ is proportional to the number of
expected interactions of any given process. For studing rare
scattering processes, corresponding to very small cross sections $\sigma$,
the luminosity would be crucial factor, because it determines the
expected total amount such collisions produced per time unit. The
instantaneous luminosity at the interaction region at a given time
can be estimated from the characteristics of the proton beams as:
$$ \mathcal{L}_\textrm{inst} = \frac{n_p^2 n_b f_r \gamma_r}{ 4 \pi \epsilon_n \beta^{*}}
    \mathcal{F}$$ {#eq:lumi_beam}
where $n_p$ is the number of particles per bunch, $n_b$ is the number
of bunches per beam, $f_r$ is the beam revolution frequency, $\gamma_r$
is a relativistic suppression factor, $\epsilon_n$ is the normalised
beam emittance, $\beta^{*}$ is the transverse size of the beam, and
$\mathcal{F}$ is an additional luminosity reduction factor. The main
contribution to the reduction factor $\mathcal{F}$ comes from a
small tilt of the beams at the crossing point, characterised by
the crossing angle $\phi_c$, which avoids parasitic interactions
between bunches but reduces the luminosity by approximately:
$$ \mathcal{F} = \left (  1 +
 \left ( \frac{\phi_c \sigma_z}{2\sigma^{*}} 
 \right )^2 \right )^{-1/2} $$ {#eq:lumi_factor}
where $\sigma_z$ is the root mean square (RMS) bunch length and $\sigma^{*}$
is the RMS of the beam in the transverse direction at the interaction volume.
The peak instantaneous luminosities per day 
for the different years of proton-proton data acquisition periods
(also known as *runs*)
at the LHC are summarised in [Figure @fig:peak_lumi] , which can
be compared with the peak design luminosity of the LHC of
$\mathcal{L}_\textrm{design} = 10^{34}\ \textrm{cm}^{-2} \textrm{s}^{-1} = 10\ \textrm{Hz}/\textrm{nb}$.

![Peak luminosity per day as measured using the CMS detector for the
all the proton-proton data-taking periods of the LHC to date. Figure from
[CMS Public Luminosity Results](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults#Multi_year_plots).
](gfx/102_chapter_2/peak_lumi_pp.pdf){
#fig:peak_lumi width=100%}

From Equation [-@eq:lumi_beam] it can be inferred that that value of
instantaneous luminosity varies between LHC *fills* depending on the beam
parameters. In fact, it also varies within a single *fill* with time,
mainly because the number of average protons per bunch $n_p$ decreases
due to the collisions at all the interaction points. For convenience,
a quantity referred as integrated luminosity $\mathcal{L}_\textrm{int}$
that is computed by integrating over the instantaneous luminosity for a
given time period $\Delta T = t_1 - t_0$, such as stable collision period
within a *fill*, is used:
$$
  \mathcal{L}_\textrm{int} = \int_{t_0}^{t_1} \mathcal{L}(t) dt
$$ {#eq:int_lumi}
which is proportional to the number of collisions for a given process
during that period and thus can be used to quantify the amount of data
acquired. When studying data from different time periods jointly, integrated
luminosity is additive, even if the beam conditions (e.g. proton
density) are different as long as the beam energies are matching. Such notion
will be particularly useful when talking about the amount of data collected
by a detector during a year or a longer data acquisition period.

<!-- TODO: add something about measurement of luminosity maybe -->
<!-- TODO: find out a way to link well to detectors -->

### Multiple Hadron Interactions {#sec:pile_up}

Given the high density of protons in each bunch at the collision
points, every bunch crossing generates a few dozen proton-proton interactions,
a phenomenon that is commonly referred to
as *pileup*. 
The products of all these interactions go through the surrounding
detectors at the almost the same time, which complicates
the interpretation of the detector readouts as the product of a
single interaction. The number of proton-proton
interactions for each crossing is effectively a random variable,
however its expected value is proportional to the instantaneous luminosity
and the total cross section of processes that produce detectable
remnants in the detectors, mainly originating from low-energy inelastic proton
scattering processes.

![Multiple interactions in a single bunch crossing as recorded
by the CMS detector during a special high-pile up luminosity
at the end of 2016 [@McCauley:2231915].
The reconstructed primary interaction vertices are shown using orange
circles while the yellow lines represent the trajectories
of charged particles.
](gfx/102_chapter_2/highpileup1_4.png){#fig:pileup width=70%}

In fact, at the collision point of one of the general purpose detectors at
the LHC,
the most likely outcome of any given bunch crossing at the nominal design
luminosity of $1 \times 10^{34} \textrm{cm}^{-1} \textrm{s}^{-1}$ is
about 25 *soft* scattering interactions (i.e. ones
characterised by a low momentum transfer),
producing hundreds of low energy particles all around the collision
region, as depicted in Figure [-@fig:pileup].
Quite rarely, given the small relative cross section of *hard*
scattering processes in comparison with the total scattering
cross section as discussed in Section [-@sec:pheno],
one of the produced interactions might involve a large momentum 
transfer between partons,
which is characteristic of the fundamental
physical processes of special interest at the LHC,
such as the production of a Higgs boson. The probability of two or more
hard interactions happening in the same bunch crossing is really low,
and can be safely neglected for any practical purposes.
Nevertheless, the outcome of each hard interaction of interest
will be overlapping in the detector volume with the product of
all other soft interaction that occurred on the same bunch crossing,
greatly complicating the task of *event reconstruction* as will
be discussed in Section [-@sec:event]. This also motivates the use
of *pileup mitigation* techniques, heavily based on accurate
detectors that can extrapolate and differentiate the primary
interaction vertices of the collisions from the charged particle
trajectories.

In addition to multiple hadron interactions per bunch crossing, the goal
of recording the outcome of a very high number of proton interactions
leads to a different experimental complication. As illustrated in
Equation [-@eq:lumi_rate], a simple way to increase the
luminosity is to increase the number of total proton bunches per beam $n_b$.
This fact is exploited in the nominal proton fill scheme of the LHC by having
a total of 2808 proton bunches in each beam, corresponding to a
separation between most of the bunches of only approximately 7.5 m.
Hence the time separation between
consecutive bunch
crossing is about 25 ns, which is of the same order as the response time
of many of the detector elements used at the LHC. The readout from a
a particular bunch crossing can therefore be affected by the detector occupation
caused by the previous or subsequent crossings, in what is referred to
as *out-of-time pileup*, that becomes an important consideration for detector
design in high-luminosity environments.



### Experiments {#sec:lhc_experiments}

Around the collision volume at each of the interaction points, large
detectors are positioned in order to reveal and quantitatively
study the outcomes of the highly-energetic particle scattering,
which can in turn be used to obtain information about the properties
of fundamental interactions. Four large particle
experiments are installed at the LHC interaction points:

* **ATLAS** (A Toroidal LHC ApparatuS) [@ATLAS:2008JINST]:
  the largest experiment at the LHC, designed as a
  general-purpose detector to study the various products of high-energy
  interactions, especially those of high-luminosity proton-proton collisions.
  While one of the most important 
  scientific goals of the ATLAS experiment was to discover Higgs boson
  and provide a detailed study of its properties, it was also built with
  the aim of extensive testing of Beyond the Standard Model (BSM) theories.

* **CMS** (Compact Muon Solenoid) [@CMS:2008JINST]:
  the other general-purpose experiment at the LHC, sharing most of the
  research goals with ATLAS, but opting for an alternative
  design and a different choice of detector technologies
  making it considerably more compact. It is the
  detector that collected the data use in the analysis in Chapter
  [-@sec:higgs_pair] and
  hence is described extensively in Section [-@sec:cms].

* **LHCb** (Large Hadron Collider beauty) [@LHCb:2008JINST]:
  operating at a lower range of luminosity than ATLAS or CMS
  by deliberately separating the beams, this experiment
  focusses on very accurate precision measurements of the
  properties and rate decays of b-quark and c-quark hadrons
  as well as the search for indirect evidence of new physics
  leading to CP violation in heavy flavour physics phenomena.

* **ALICE** (A Large Ion Collider Experiment) [@ALICE:2008JINST]:
  a heavy-ion collisions detector, designed to study the dynamics
  quark-gluon plasma,
  a high energy density state of strongly interacting matter,
  as it expands and cools down. Such studies can lead to
  a better understanding of colour confinement and other relevant
  QCD problems,
  as well as shedding some light on the processes that took
  a few microseconds after the Big Bang.
  

Additionally, three smaller experiments are built around the mentioned
detectors with specific research purposes: TOTEM [@TOTEM:2008JINST],
LHCf [@LHCf:2008JINT] and MoEDAL [@MoEDAL:2014PP]. Both TOTEM and LHCf
are built to investigate features of forward physics interactions, where
scattering products remain the original proton trajectories,
and hence they are set up tangent to the LHC beam line at the sides of
CMS and ATLAS interactions points respectively. MoeDAL is instead built
at the same experimental space than LHCb and its main aim is to search
for evidence of production of magnetic monopoles and other highly ionising
stable massive particles.


## The Compact Muon Solenoid {#sec:cms}

The Compact Muon Solenoid (CMS) is a general purpose detector placed
about 100 meters underground around one of the collision points of the
Large Hadron Collider (LHC) ring. It has been designed to carry out
experimental research on a wide range of high-energy physics phenomena,
including searching for the Higgs boson and studying its properties,
testing alternative explanations of nature such as extra dimensions
or supersymmetry, and looking for evidence of direct production of particle
dark matter candidates.

In spite of having such ambitious research goals,
the principle of operation of CMS is
rather simple, as it can be reduced to the detection of the outgoing
particles produced as a result of high-energy interactions between
protons and the identification and measurement of their most
relevant properties, such as momenta and energies. These is done
by putting together the information acquired by a large number of
simple detecting elements, placed in layers around the
collision region. The properties
and kinematics of several of those final state detected
particles can often be combined to compute observables of
more complex objects, such as the invariant mass of an
intermediate particle. After collecting data from a large
number of collisions, a subset of relevance of the data
can be compared with the expected theoretical predictions,
and statistical inference in the form of interval estimates
on parameters of interest or hypothesis testing 
of alternative explanations can be performed.

The CMS detector is built inside and around a large cylindrical coil of
superconductive wire, forming a 6 m diameter solenoid magnet that can
provide an homogenous magnetic field of 3.8 T. Particle detection
and identification are achieved using several layers of sub-detectors with
specialised functions, almost covering the full solid angle around the
interaction region, as depicted in Figure [-@fig:CMS_detector]. Inside
the solenoid volume, a particle tracker made of silicon pixel and strip
detectors, a lead tungstate crystal electromagnetic calorimeter (ECAL)
and a brass-scintillator hadronic calorimeter (HCAL) are placed, each of
the composed of a barrel and two endcap sections. A large muon detection
system, composed of cathode strip chambers (CSC),
resistive plate chambers (RPC) and drift tubes (DT),
is embedded in the steel flux-return yoke outside the solenoid. Furthermore,
extensive forward calorimetry complements the coverage provided by
the barrel and endcap sections.
A more detailed review of the detection principles and capabilities
for each detector component are included
in the following, yet the detector performance
technical design report [@CMS:TDR_Detector_Performance]
and references therein are recommended
for a more specialised account.

![Cutaway view of the CMS detector, based on a three-dimensional representation,
an highlighting the main detecting systems and characteristics.
Image has been adapted from [@sakuma2014detector].
](gfx/102_chapter_2/CMS_detector.pdf){
#fig:CMS_detector width=90%}

### Experimental Geometry {#sec:exp_geom}

Given the geometry of the detector, the coordinate system used is
centred at the nominal interaction point
inside the detector. The $x$ axis point inwards towards the LHC ring
origin, while the $y$ axis points vertically upward toward the terrestrial
surface. The $z$ axis is thus tangent to the beam line, increasing in the
counter-clockwise direction when looking at the LHC ring from above.
Considering
the expected symmetries for particle production,
spherical coordinates are a convenient representation, where $\phi$ is the
angle from the $x$ axis in transverse plane (i.e. $x$-$y$ plane), and $\theta$
is the polar angle with respect to the LHC plane using a consistent sign
convention with the previous definition of the $z$ and $y$ axes.

As mentioned before, particle momentum is the main observable of the detected
particles. The energy is simply a function of the momentum and the mass of
the particle, as shown by the relation $E^2 = p^2 + m^2$, expressed in
natural units ($c=1$). 
Because the $x$ and $y$ momentum components
are insensitive
to the initial state boost in the $z$ direction due to the stochastic
differences in parton momenta in the initial state,
and are measured more accurately as
a result of
the design of the detector, it is common to refer separately to the total
transverse momentum quantity $p_T = \sqrt{p_x^2 + p_y^2} = |p| \sin \theta$
and its transverse plane angle $\phi$. While the $z$ component of the momentum
could be specified directly either by using $p_z$ or by the angle $\theta$,
the differences of any of those observables between two particles detected
on an event depend
on the initial parton state boost $\beta$ on the $z$ direction,
which varies between different
collisions and it is hard to estimate precisely in the laboratory
frame of reference.

Since the dependence on the initial state $z$ boost 
would complicate the statistical analysis
and the definition of derived observables, an alternative observable
can be defined based on the rapidity $y$, which is defined as:
$$y = \frac{1}{2} \ln \left ( \frac{E+p_z}{E-p_z} \right ) $$ {#eq:rapidity}
and whose value on a under a $z$-axis boost can be easily obtained by adding
an additive factor
$y'=y-\textrm{tanh}^{-1} \beta$, and hence differences in rapidity between
two particles in a collision $\Delta y = | y_b - y_a |$ are invariant to
Lorentz boost in the $z$ direction. Because the rapidity depends on
the total energy/momentum of the particle, which might not be possible to
measure to high precisions in hadron collider detectors,
it is more suitable to approximate it using
the *pseudo-rapidity* $\eta$, defined as: 
$$\eta = \frac{1}{2} \ln \left ( \frac{p+p_z}{E-p_z} \right ) =
 \ln \left ( \tan \frac{\theta}{2} \right )
 $$ {#eq:pseudo_rapidity}
that only depends on the polar angle $\theta$ with respect to the LHC plane.
The *pseudo-rapidity* $\eta$
and it is equal to the rapidity $y$ for massless particles, and a very
effective approximation in the highly-relativistic limit, when $E\gg m$.
It is useful observing that for particle produced in the transverse
plane, thus $\theta=\pi/2$, their *pseudo-rapidity* is $\eta=0$. Instead, in
the limit of fully forward particles, when $\theta \rightarrow 0$ or
$\theta \rightarrow \pi$, their *pseudo-rapidity* becomes
$\eta \rightarrow  +\infty$ and $\eta \rightarrow  -\infty$, respectively.

Oftentimes, angular distances between two particles in an event are very
powerful observables to cluster observed particles or
isolate interesting collisions. The distances between two particles, indentified
with $a$ and $b$ subindexes, in the transverse $\Delta \phi$ and
forward direction $\Delta \eta$ can be computed as:
$$\Delta \phi = \min \left( | \phi_b-\phi_a|,
  2 \pi - | \phi_b - \phi_a| \right) \quad \textrm{and} \quad
  \Delta \eta = | \eta_b - \eta_a| $$ {#eq:delta_phi_eta}
while the total angular distance $\Delta R$ between the two particles
is instead defined as:
$$ \Delta R = \sqrt{ (\Delta \eta)^2 + (\Delta \phi)^2 }$$ {#eq:delta_r}
which is invariant to boosts in the $z$ direction in the highly-relativistic
limit, and is particularly practical to cluster the products of the
hadronization of quarks and gluons as detailed in Section [-@sec:event].

### Magnet {#sec:cms_magnet}

The purpose of the CMS magnet is to curve
the trajectories of charged particles coming out the interaction region,
so their transverse momenta $p_T$ can be accurately estimated, and the
sign of their charge determined. In order to understand how such
momentum measurement can be carried out,
let us assume a solenoidal magnetic field that is fully homogenous
and pointing in the $z$ direction $\vec{B}=B \hat{z}$. Due
to Lorentz force, a particle with a transverse momentum  $p_T$
and a forward momentum $p_z$ would describe an helicoidal trajectory,
where the curvature radius in the transverse plane $r_T$ and the
transverse momentum are related:
$$r_T = \frac{p_T}{qB}  \quad 
  \Longrightarrow \quad p_T
  [\textrm{GeV/c}] =  0.3 \cdot q[\textrm{e}] \cdot B[\textrm{T}]
  \cdot r_T[\textrm{m}]  $$ {#eq:lorentz_eq}
where $q$ is the particle charge, and the second equation correspond
to a simplification using units denoted inside the brackets
adjacent to each quantity ($\textrm{e}$ are electron charge units).
These simple proportionality relation indicates that the higher
the momentum of a particle, the larger its radius of curvature.
Furthermore, the direction of the curvature is determined by the
sign of the particle charge. For more realistic scenarios, like
the magnetic field not being completely homogenous
or the particle momentum decreasing along its trajectory due
to interaction with the detecting elements, Equation [-@eq:lorentz_eq]
is only an approximation and the trajectory path can be obtained
by solving a differential equation.

In the case of CMS, the magnet is generated by a large
superconducting solenoid, contained inside a hollow cylinder
about 13 m long and with an outer radius of 3 m. Very
high currents, up to 19 kA, circulate along $\textrm{NbTi}$
wires kept at 4.5 K using a liquid helium cooling system,
providing an almost homogenous field at the centre
of the solenoid up to 3.8 T in the $z$ direction. In addtion
to the solenoid, the
magnetic flux lines are closed by a 10000 ton return yoke,
composed by a series of magnetised iron blocks interleaved
with the muon detectors in the outer part of CMS, providing
a magnetic field about 2T in the opposite direction.
The remaining elements of the CMS magnetic spectrometer,
which are the 
detector systems used to estimate the curved particle
trajectories, commonly
referred to as *tracks*, for all charged particles and for escaping
muons are reviewed in Sections [-@sec:cms_tracking] and [-@sec:cms_muon],
respectively.


### Tracking System {#sec:cms_tracking}

The inner tracking system is the detector that is the closest to the
interaction point, and its functions include the estimation of
the charged particles trajectories, used to provide a measurement
of their momenta as described in Section [-@sec:cms_magnet],
as well as allowing the positional determination of interaction
or decay vertices by extrapolating the trajectories inside
the interaction region. The detection of charged particle trajectories,
or *tracks* for short, is carried out by several silicon
detector layers placed non-uniformly around the collision volume,
as shown in Figure [-@fig:CMS_tracker]. The placement is of layers is
symmetric in $\phi$, the outermost layers contained within
a supporting cylindrical structure of 2.5 m of diameter and 5.8 m
of length.

![Cross sectional view of the CMS detector inner tracker
detector in the $r-z$ plane, detailing the position
of detecting layers
as well as the main detector sub-components.
The tracker is symmetric around
$r=0$, so only the top half is shown. Figure has been adapted
from [@Chatrchyan:2014fea].
](gfx/102_chapter_2/tracker_colour.pdf){
#fig:CMS_tracker width=90%}

The detector is composed of two main parts: a silicon pixel detector
system situated very close to the interaction point and
a much larger strip detector arrangement
placed outside the former. The disposition on the detecting layers allows
to detect tracks within a pseudo-rapidity range defined by $|\eta| < 2.5$.
Both systems have to deal with the efficient tracking of
hundred of charged particles, at a rate of
40 MHz, typically produced from each bunch crossing. A successful
apparatus in such a environment requires a short response time, as
well as to be composed of many small detecting elements.  The latter
property is commonly referred as *high granularity*, and allows to
keep the number of detected track points (i.e. *hits*) per detector
unit at acceptable levels.

Being so close to the collision region, the set-up has to
sustain very high particle fluxes during long periods of time,
up $1 \textrm{MHz}/\textrm{mm}^{2}$ at the first pixel layer. Therefore,
resistance to radiation damage of the detecting elements and the
accompanying electronics, dubbed as *radiation-hardness*,
is an essential specification. Additionally, the amount of material
present in the particle trajectories has to be kept to a minimum,
to avoid stochastic secondary interactions that would degrade the
precision and efficiency of track determination. The use of silicon
semiconductor detector technologies [@spieler2005semiconductor]
in the CMS tracking system is thus motivated
by a combination of all previously mentioned reasons. In total,
the CMS tracking system is composed of 1440 pixel detector modules
and 15148 strip detector modules, accounting for an active
area over $200 \textrm{m}^2$.

The pixel detector, the innermost detecting system of the CMS
experiment, is comprised by a total of 66 million silicon
cells placed in 1440 modules around the collision region. Each pixel
cell has an area of $100\times150\mu\:\textrm{m}^2$ and a thickness
of $285\:\mu\textrm{m}$, and provides two-dimensional local
track hit coordinates with a resolution around in the cell surface
plane about $20\:\mu\textrm{m}$, that can in turn be used
to compute the
global three-dimensional hit location with high accuracy after
accounting for the precise location of the detecting
module. As depicted in Figure [-@fig:CMS_tracker], the pixel
detector is composed by three *barrel* (i.e.
placed around the collision region in an cylindrical
arrangement) layers, located at radii of 4.4 cm, 7.3 cm and 10.2
cm respectively, and two forward disk at each side at
distance of 34.5 cm and 46.6 cm from the nominal interaction point.

The rest of the tracking system, placed outside the pixel detector,
is constituted of several
silicon strip detector modules organised in four different sub-detectors,
referred as TIB, TID, TOB and TEC in Figure [-@fig:CMS_tracker].
The inner part of the strip tracker, adjacent to the pixel detector,
is composed of four barrel layers of strip modules
constituting the tracker inner
barrel (TIB) section, and three module layers arranged in disks at at each side
forming the tracker inner disk (TID). Further away from the interaction
region, the outer strip tracker, comprising of six barrel layers in
the tracker outer barrel (TOB) and nine disks at each side forming
the tracker endcaps (TEC). The strip specifications varies depending
on the sub-detector, with thicknesses ranging from $320\:\mu\textrm{m}$
to $500\:\mu\textrm{m}$, and pitches (i.e. distances between
strips) from $80\:\mu\textrm{m}$ to $184\:\mu\textrm{m}$.

The strips
are placed longitudinally parallel to the beam line in the barrel
modules and radially
in the perpendicular plane in the endcap disks, with
silicon strip lengths ranging from 10 cm to 20 cm, and in an overlapping
tiled setting (see Figure [-@fig:CMS_tracker])
Each strip layer provides a single local coordinate for a particle track
hit, aligned with $\phi$ both the barrel and the endcap disk. A second
coordinate can be easily obtained taking into account the placement
on the module, thus obtaining the $r$ coordinate in the barrel
and $z$ in the endcap disks. In order to provide information on
the unknown coordinate in each case, some layers of the tracker
(in blue colour in Figure [-@fig:CMS_tracker]) are composed of
two modules instead on one, with a small tilt of 0.1 rad that allows
to obtain a precise 3D coordinate for a track hit by combining the
two local coordinates and their module positions. 


### Electromagnetic Calorimeter {#sec:cms_ecal}

The function of the CMS Electronic Calorimeter (ECAL) is to measure
the total energy of the electrons, positrons
and photons that reach that part
of the detector, by means of their *electromagnetic showers*. In order
attain such task, scintillating lead tungstate
$\textrm{PbWO}_4$ transparent crystals are
placed inside the solenoid magnet, right outside the tracking system,
covering the solid angle around the interaction point as depicted
in Figure [-@fig:CMS_ecal].
When a high energy electron or a positron enters the dense crystal
material, it rapidly decelerates and emits photons through bremsstrahlung
radiation. High energy photons from electron/positron deceleration or
directly from the collision region, instead produce a positron-electron
pairs through matter interaction, that in turn radiate photon through
bremsstrahlung processes. The chain of processes, referred as
*electromagnetic shower* keeps occurring until the energy of the
photons goes below the pair production threshold or the energy
loss of the electrons/positrons happens through alternative
mechanisms. The resulting low energy photons from the electromagnetic
shower produce visible range light in the scintillating but
transparent crystal, which is detected, amplified and collected by
photodetectors placed at the end of each lead tungstate crystal.

![Cutaway view of the CMS electromagnetic calorimeter, based on a
tree-dimensional model of the detector geometry. The placement
of the lead tungstate crystal is shown for part of
the barrel and endcaps. Figure has been adapted from [@CERN-LHCC-97-033].
](gfx/102_chapter_2/ecal_from_tdr.pdf){
#fig:CMS_ecal width=90%}

The ECAL is composed of two main parts, the barrel calorimeter (EB) 
section covering pseudo-rapidities up to $|\eta| < 1.479$, and two
symmetrically positioned endcap calorimeters (EE) further
extending the coverage to $|\eta|< 3.0$. The trapezoid-shaped
crystals are placed radially around the collision region, a total
of 61200 blocks in the EB and another 7324 blocks for each EE part.
The sides facing the IP in the barrel section have dimensions
of $22\times22\ \textrm{mm}^2$ and a length of 23 cm, while the
front-facing sides of those in the endcaps are slightly larger at
$28.6\times28.6\ \textrm{mm}^2$ with a length of 22 cm. The
advantages of using lead tungstate crystal include its very short
radiation length $\mathcal{X}_0=0.89\textrm{cm}$, which characterises the
longitudinal energy loss profile $E(E) = E_0 e^{x/\mathcal{X}_0}$, as well
as its small Moliere radius of 2.19 cm, which defines the radius
containing average transversal radius
containing 90% of the shower energy, leading to narrow showers
which contributes to improved position and
energy resolution. The lengths of the crystal blocks in the EB and EE amount
to $25.8\mathcal{X}_0$ and $24.7\mathcal{X}_0$, which ensures that
effectively all the energy is deposited inside the detectors.

Another advantage of  lead tungstate crystals is that $\textrm{PbWO}_4$
is also a scintillating material,
thus the resulting shower energy is absorbed and partially emitted back
as visible light, with a yield spectrum maximum in the blue-violet range
around 430 nm. The reemission process is also very fast, since about 80% of the
scintillating light is emitted within 25 ns of absorption, which
is the time until the next LHC bunch crossing occurs. The scintillator
light propagates effectively through the crystal due to its high
transparency, and reaches the photodetectors attached to the end
of the crystal trapezoids. Avalanche photodiodes (APD) are used for
light detection and amplification at the barrel crystals while
vacuum phototriodes (VPT) are used for the endcaps, given
their different radiation hardness and sensitivity to
magnetic fields. 

In addition to the EE and EB, a sampling
detector referred as pre-shower electromagnetic calorimeter,
based on two layers of lead absorber followed by two layers
of silicon strip
detectors, is placed right before the lead tungstate crystals
in the endcap to provide higher granularity in the forward
region. The main purpose of the pre-shower extension is to
distinguish high-energy photons coming directly from the
collision region and high energy neutral pions that have
decayed into two closely-spaced photons.



### Hadronic Calorimeter {#sec:cms_hcal}

The purpose of the hadron calorimeter (HCAL) is to measure the energy
and position of all long-lived neutral or charged mesons and baryons
produced as a result of the collision, typically including pions, kaons,
protons and neutrons. The main detecting elements of this sub-detector
are an assortment of sampling calorimeters, interleaving brass plates as
absorber material and plastic scintillator tiles as active
medium, the former causing the deposition of energy in the form of secondary
particles by means of interactions with the material nuclei and the latter
converting a part of that energy to visible light. The light from each tile
is captured by a thin optical fibre and carried to a photodetector, producing
electric signal that can be used to measure the total amount of deposited
energy with the help of careful calibration.  

![Cross sectional view of the CMS detector hadronic calorimeter (HCAL)
detector in the $r-z$ plane, depicting the positioning of the various
detector segments relative to the beam line and the solenoid magnet.
The HCAL is symmetric around
$r=0$, so only the top half is shown. Figure adapted from
[@Chatrchyan:2009ag].
](gfx/102_chapter_2/HCAL.pdf){
#fig:CMS_hcal width=70%}

The different segments of the CMS HCAL
are shown in [Figure @fig:CMS_hcal].
After the ECAL but still inside the solenoid volume,
the barrel section of the hadronic calorimeter (HB) as
well as two endcap sections (HE) at each side are placed, providing
pseudo-rapidity coverages of $|\eta| < 1.3$ and  $1.3 < |\eta| < 3.0$,
respectively. Both the HB and HE section are composed of a stack of brass
plates with plastic scintillator tiles in between, providing a total of
$5.6\lambda_I$ at $\eta=0$ and $11.8\lambda_I$ at $\eta=3$,
where $\lambda_I$ is the hadronic interaction length. Given that the limited
space inside the solenoid and the fact that about 11$\lambda_I$ are required
to absorb about 99% of the total energy of the hadrons at the expected energy
ranges, the hadronic calorimeter system is complemented by an outer
detector (HO) outside of the solenoid. The HO is composed of five rings
of scintillator tiles, effectively using the solenoid material as
absorbing material. Because the absorbing material path length is shorter
around $\eta=0$, the central ring is shielded by a large iron plates and 
an additional layer of scintillating material, yielding a total
absorber length over $11.8\lambda_I$ and therefore improving its measuring
capabilities.

Over 70000 thin plastic scintillator tiles are placed between
and after absorber plates. The size of those plates depends on
their geometrical placement and are aligned according to their angular
coordinates between layers, so each longitudinal projection corresponds to
an approximate area $\Delta\eta\times\Delta\phi= 0.087\times0.087$ within
the HB coverage region and $\Delta\eta\times\Delta\phi= 0.17\times0.17$ 
outside it. When secondary particles go through the scintillating tiles,
part of the energy is absorbed and promptly released as violet-blue visible
light, over 65% of the total amount of emitted light within 25 ns.
The light is collected and guided through thin optical
wavelength-shifting fibres that change the light to the green spectrum
region, then through standard optical fibres until reaching readout boxes
that contain hybrid photodiodes (HPD). The optical signal for each alignment
of tiles are added optically to a single readout for most of the radial
projections, with the
exception of those in the intersections between the barrel and endcaps, that
are kept in two or three separate channels in order to ease calibration
procedures.

The last element in the HCAL system is the forward hadronic calorimeter (HF),
situated 11.15 m at each side of the interaction point, adjacent to the
beam pipe, and providing detection capabilities for particles with
pseudo-rapidities in the range $3.0 < |\eta| < 5.2$. The HF greatly increases
the pseudo-rapidity energy measurement for charged and neutral particles,
allowing a near hermetic (full solid angle) coverage, and hence allowing the
estimation of missing energy in the event such that corresponding to
neutrinos leaving CMS undetected, as will be discussed in
[Section @sec:event].
Because the radiation fluxes are extremely high in the forward region and
there are no depth constraints, a different detector design is used,
based on 165 cm of steel absorber plates and quartz fibres aligned of the
z-axis, each with an effective detecting
area of $\Delta\eta\times\Delta\phi= 0.17\times0.17$.


The fibres running along the HF detect and guide the Cherenkov light of the
charged secondary particles produced in the showers to photomultipliers
tubes (PMT) placed behind a 40 cm thick steel and polyethylene shield.
In this pseudo-rapidity range, the HF serves also as an electromagnetic
calorimeter, and being able to disentangle the energy contributions
from electromagnetic and hadronic showers is quite useful for
many physics data analysis use cases. Given that electromagnetic showers
are much shorter than hadronic showers, only half of the fibres
start close to the face of the absorber plates closest to the IP,
the rest other starting at a depth of 22 cm. By comparing the readouts
of long and short fibres, the type of shower can be inferred.


### Muon System {#sec:cms_muon}

The scientific objective of the CMS muon sub-system, or outer tracker,
is to identify, determine the charge and measure the momenta of high
energy muons, which are not only charged particles capable
of passing through all the other detector systems
without a significant energy loss. While the trajectory can be
detected in the inner tracker, the around of energy loss due to
bremsstrahlung is much smaller than that of electron or positrons
due to its much heavier mass
(given that $\sigma_{\textrm{bremsstrahlung}} \propto 1/m^2$) 
and hence the do not
deposit a significant fraction of their energy in the ECAL or
the HCAL. The simplest way then to augment the amount of information
about muons obtained from the tracker is to place additional
tracking detectors outside the solenoid, while sustaining a high
magnetic field that can curve the muon trajectories by using
large blocks of ferromagnetic material as *flux-return yokes*.

![Cross sectional view of the layout of CMS detector
in the $r-z$ plane, focussing
on the components of muon system components.
The detector is symmetric around
$r=0$ axis and the $z=0$ plane,
so only the top quarter is shown.
Figure adapted from [@Sirunyan:2018fpa].
](gfx/102_chapter_2/cms_muon.pdf){#fig:CMS_muon width=70%}

The muon system is the most external sub-detector of CMS
and it is based on gaseous tracking detector technologies,
given the large volumes covered. The principle of action of
gaseous detectors is rather simple, charged particles
passing through the gas ionise gas molecules in their path,
which start moving due to a high electric field between
conducing wires, producing an electrical signal
that can be read out. The time dependence of the signal
on the different readout wires can be used to infer
the particle trajectory with high precision, and in some
cases built-in signal amplification can be achieved
due to secondary ionisation by
the choice of a gas mixture combined with high electric
field gradients.

An overview of the various detectors
of the muons system and their geometrical placement
around the solenoid magnet cylinder is depicted
in Figure [-@fig:CMS_muon]. Due to a combination
of criteria regarding uniformity and
strength of the magnetic field, expected radiation
fluxes and signal readout times, three different
types of gaseous detectors are used: drift tubes (DT),
cathode strip chambers (CSC) and resistive place chambers (RPC).
In the barrel section where the particle flux is not
expected to be very high, four layers of drift tubes (DT)
are arranged cylindrically around the solenoid magnet,
covering a pseudo-rapidity range $|\eta| < 1.2$. On the endcap
section instead, due to higher radiation fluxes and magnetic
field non-uniformity, multi-wire cathode strip chambers (CSC)
are used, with a detecting pseudo-rapidity coverage of
$0.9 < |\eta| < 2.4$. Both DT and CSC detectors can achieve
very high position resolution, but their signal
readout time and time resolution is not as good, thus a series
of fast but resistive plate chambers (RPC) are positioned both
in the barrel and the endcap sections, up pseudo-rapidities
$|\eta| < 1.6$.


### Trigger and Data Acquisition {#sec:trigger}

As discussed in Section [-@sec:pheno], the occurrence of
relevant processes that can provide information about the physical
properties of fundamental interaction in
proton-proton collisions is purely stochastic given some initial conditions,
plus their relative frequency is
very rare compared with known
phenomena. In order increase the expected chances of 
recording interesting phenomena, the LHC collides 40 million 
high-density proton bunches every second inside the CMS
detector. Furthermore, 
as discussed in Section [-@sec:pile_up], tens of
proton-proton interactions typically happen 
within each bunch crossing.
The CMS sub-systems are hence detecting a good fraction of 100s of particles
produced as a result of the interactions at each bunch crossing,
in addition of being subjected to instrumental noise or external radiation
sources such as cosmic rays. 

The combined readout of all sub-detectors
each 25 ns amounts to a large data size, due to the total number
of sub-system channels, even if efficient techniques for 
representation and compression of information are used. Given that technical
limitations on the amount of data that can be recorded exist,
a practical choice for data acquisition is to keep only the detailed detector
information of collisions that could be maximally useful to study the properties
of fundamental interactions in subsequent data analyses. The decision system
that makes the choice of whether to record or filter out the detailed detector
readouts for a given collision, is commonly referred as *trigger*, 
and is based on a fast and possibly asynchronous analysis of those readouts. In
particular, such decision criteria is typically focussed on the most
relevant properties
of one or a subset of detected particles, such as their type, charge or
the magnitude and direction of their momenta.

A flexible and sparse representation of all CMS detector readouts
for a given collision that keeps sufficient information for detailed
analyses is of the order of a few megabytes (i.e. $\mathcal{O}(1)\ \textrm{MB}$).
Because of the technical capabilities of the storage system,
the total data acquisition rate is limited to less that 10 Gb/s,
hence the trigger system has to reduce the rate of collision
readouts from 40 MHz to about 1 kHz. As a compromise between processing
speed and requirement adaptability, the trigger system of CMS is divided
in two stages: the level 1 trigger (L1), which is a custom-hardware based
solution that reduces the detector readout rate to 100 kHz, and the high-level
trigger (HLT), a a second step reducing it to the required 1 kHz and that
is instead carried out by a computer farm.


## Event Simulation and Reconstruction {#sec:event}

The raw account of the readout of all detectors after a single bunch crossing,
as well as any derived representation of it, is commonly
referred to as *an event*, and is the most fundamental type of observation
in high-energy data analyses. All approaches to extract
useful conclusions from CMS data are based on this information unit
or simplifications thereof. This is because for practical
purposes, statistical independence between events can be assumed, barring
possible caveats (e.g. out-of-time pile-up or detector malfunctioning). Therefore,
data analyses are reduced to the task of comparison between the observations
and the predicted frequencies of events with different
characteristics.

The dimensionality of an event evidently depends on its data representation,
simpler representations being lower-dimensional and easing the comparison
with theoretical predictions, at the cost of possibly losing
some useful information. A principled way to obtain lower dimensional
representations of an event given its raw detector readouts
is to attempt to reconstruct all the primary particles that were produced
in the main proton-proton interaction of the collision and as well as 
estimate their main properties,
through a process generally referred as *event reconstruction*.
Nevertheless, 
for carrying out successfully the aforesaid task it is convenient to
be able to have a detailed model of the detector readout output that is
expected for a given set of particles produced in a collision.
Realistic modelling of high-energy physics collisions in high-dimensional
representations  can be achieved through simulation.

In this section, a generative view of the main physical mechanisms
that are happening both in the proton-proton collisions and when particles
propagate through the CMS detector is first included. Such overview doubles as
an introduction of the next section, where a description
of how realistic simulations of the detector readouts (i.e. events)
can be obtained using computational tools is provided. 
Afterwards, the inverse process is tackled, which is considerably harder
and often ill-defined, namely how can we estimate the
set of primary particles that were produced in the collision given the
detector readout, through event reconstruction techniques.


### A Generative View {#sec:gen_view}

When two high-density proton bunches travelling in opposite directions
pass through each other inside the collision region of CMS,
several proton-proton interactions can occur as discussed
in Section [-@sec:pile_up]. While most of the interactions will
correspond to a small energy transfer between the interacting
partons, given that the total interaction cross section is
heavily dominated by soft scattering processes, a small fraction
of collisions would include physically interesting process
such as the production of heavy particles (e.g. a
Higgs boson). The absolute and differential rates 
for such *hard* processes can be predicted as outlined
in Section [-@sec:factorisation]. Therefore, for a specific process
in a proton-proton interaction, realistic high-dimensional
modelling of the intermediate particles can be
obtained by repeated sampling of the parton distribution
functions and phase space differential cross sections. Subsequent
decay, hadronization and radiation processes as well as more
subtle effects and higher order
corrections, can be then
accounted for using the methods mentioned in
Section [-@sec:parton_showers], generally
referred to as *Monte Carlo event generation* techniques.
The end result of the mentioned
procedures is a large dataset of simulated particle
outcomes for a specific process, each example including
a set of stable or sufficiently long-lived particles and their
kinematics properties that would propagate through the detector.

![Transverse view of a section of the CMS detector and the interactions
of the various particle types with the detecting sub-components.
Figure has been adapted from [@Sirunyan:2017ulk].
](gfx/102_chapter_2/CMS_transverse.pdf){
#fig:CMS_transverse width=70%}

In addition to the set of particles in the hard proton-proton
interaction, the effect of pileup interactions can be accounted for by 
adding the particle outcome of a random number of randomly sampled
soft interactions matching their approximately expected distribution
in the collisions given the instantaneous luminosity conditions.
This final set of long-lived particles produced in the interaction
region represents a possible particle outcome for a collision assuming
a given *hard* process occurred. While they cannot be directly
observed, but only indirectly inferred through the detector readouts,
it is assumed that an analogous set of particles
is produced as result of each collision in the actual experiment.
Based on the expected readout that they produce in the different
CMS detector subcomponents, five main types of detectable particles
are distinguished: muons, electrons, charged hadrons, neutral hadrons
and photons.

The traces that each of the mentioned particle types leave in each
detector sub-system is depicted in Figure [-@fig:CMS_transverse].
Even though muons are unstable particles, their long mean lifetime
$\tau_\mu = 2.2 \mu s$ allows them to travel very large distances
when highly boosted, as is the case for all the high-energy
muons coming out from the interaction region. Hence, for the purposes
of studying LHC collisions they can be considered stable, given
the unlikeliness of their decay in the detector volume at
the range of energies studied. Because muons are charged particles,
they leave hits in detector layers of the inner tracker following
their curved trajectories However,
due to their high mass, energy loss due to bremsstrahlung is
not high enough to produce significant
EM showering in the ECAL.
After passing through the HCAL without interacting notably, muons
reach the outer tracking system providing additional trajectory
points.

The trajectories of high-energy electrons 
are also recorded by the CMS inner tracker,
but as mentioned in Section [-@sec:cms_ecal], their interactions
differs from those caused by muons
they lose energy
rapidly due to bremsstrahlung when they reach the ECAL, producing subsequent
electromagnetic showers. It is worth noting that within CMS reconstruction
and analysis, it is common to simply use the term *electron* 
to refer both to electrons and positrons, their charge inferred from the
curvature sign of their trajectories. Charged hadrons, the term
here largely referring to charged pions, kaons and protons, behave
similarly to electrons in the
tracking detector but instead generate much larger hadronic showers
in the hadronic calorimeter.

Long-lived neutral hadrons, including neutrons and the neutral kaon $K_L^0$,
follow instead straight lines in the inner detector volume because they
are not affected by the magnetic field and do not leave any traces when
passing through the tracking detectors. It is not until neutral hadrons
reach the calorimeter detectors, chiefly the HCAL, that nuclear interactions
produce large hadronic showers producing measurable signals that can
be correlated with the energy deposited. Photons are massless
and neutral particles, and at the ranges of energies of interest as
the outcome of particle collisions they are not expected to deposit
enough energy in the thin inner tracking layers to produce significant
signal, thus they follow a straight line trajectory to the calorimetry
sub-systems. In contrast, when photons reach the electromagnetic calorimeter,
electron-positron pair-production processes are bound to occur, producing in turn
electromagnetic showers which can be readout as a ECAL detector signal.

The previous classification of particles based on their detectable energy
remnants in the different detectors, patently disregards a common outcome
of high energy collisions: neutrinos. Neutrinos only interact via
weak and gravitational forces, hence the probability of
interaction with the detecting elements of CMS is negligible. They thus escape
the experimental area undiscovered. The production of high-energy
neutrinos, or other weakly-interacting unknown 
hypothetical particles (e.g. dark matter candidates), can
nevertheless be inferred by the total transverse energy imbalance. While
the initial longitudinal momentum in
the laboratory frame is unknown due to the
proton compositeness, the initial total transverse momentum 
is very close to zero given that the collision occurs head-on. Given
that the CMS detecting structures have a near complete angular
coverage around the interaction points, with the exception of
very low transverse momentum particles that are lost near
the beam pipe, the total transverse collision momentum of all detectable
particles simply by summing the estimation of their transverse momenta
estimation. Ergo, the quantity $E_T^{\textrm{miss}}= || - \sum \vec{p}_T ||$
is referred to
as total missing transverse energy or by the acronym MET, and can
be used to infer the production of non-detected particles particles such as
neutrinos.

In summary, the physical characteristics of each category of particle
previously stated
cause different signatures in the various detector sub-systems, that often
can be used to distinguish between each type. It is also worth pointing
out the main attributes each individual detector element readout, which are
principally
the angular position in $\eta$ and $\phi$, the distance to
the interaction point which is given by the detecting element placement
or the $z$ coordinate,
and the amount of deposited energy. The latter is especially relevant
for calorimeter detecting units. The precision of the angular location
coordinates greatly varies between different detector types depending
in their granularity, tracking detectors providing more accurate
position measurements given that their used to extract information
directly from the particle trajectories.

### Detector Simulation {#sec:detector_simulation}

While the simplified map between the particle outcome of a given collision
and the corresponding detector readouts presented in the previous section
is extremely useful for obtaining a general understanding
the operation of the CMS detector, it is not detailed enough to
realistically model the detector readouts given a set of particles generated
in a collision. Most of the relevant dynamics for modelling, 
such as interactions between protons, the produced particles and the
detector material or the detector response, are of stochastic nature,
hence they have to be specified either by sampling
approximated probability distributions or by a complex probabilistic program
that goes through a mechanistic simulation of the underlying physical
processes actually occurring.

A detailed simulation a is found to be the most accurate approach,
given the many subtleties
affecting the detector readout for a given set of generated particles, including
possible various particle decays and material interactions that can occur when
the particle is travelling through the detector, the non-uniformity of the magnetic
field and its effect on the particle trajectories, and
the intricacy of the detector geometry and their electric response. All these
effects can be accounted for, to a high degree of validity,
in a simulator program considering the
non-deterministic propagation of the particles produce through the
detector volume. The propagation of each particle through magnetic and
electric fields can often be treated independently
though a stochastic chain of time steps, that can an any point branch
out to produce
new particles through decays and other secondary particle generating 
physical processes, so local energy deposits in the different detector
structures can be recorded. After propagating all particles, the
combination of all energy deposits in the detecting volumes can
be used to produce realistic detector responses.

The type of detector simulation is referred to as *full simulation*,
or *fullsim* for short, and it is carried out for CMS generated
events using a custom implementation of the geometry, properties
and response of the different detectors as well as the magnetic
field details, heavily reusing components from the
GEANT4 toolkit [-@Agostinelli:2002hh] for the simulation
of the passage of particles
through matter. Additional modules are used to incorporate
relevant modelling details such as the distribution of
the interaction vertices in the interaction region, referred to
as *vertex smearing*, and the addition of particles coming
from additional soft interactions in the same collision
or from adjacent bunch crossings, denoted as *pileup mixing*,
which can affect the readouts and subsequent
interpretation due to the overlapping of detector deposits
and detector sensitivity dead-times.

As can be conjectured by its level of detail, such 
simulation processes are very time consuming, taking several
minutes of CPU time give current available computing
technologies for producing a realistic detector readout for
each initial set of particles produced at a primary *hard* interaction.
Given that oftentimes billions of generated events (i.e. simulated
observations) of common processes are needed
in order to obtain a realistic modelling of known types of interaction,
alternative simulation techniques
are sometimes used. By trading off some accuracy with simulation speed,
the modelling of the physical processes and detector responses
can be simplified, achieving reducing running times considerably,
up to two orders of magnitude [@Abdullin:2011zz]. Alternatively, as
initially stated at the beginning of this section, detailed
simulation can be used to directly parametrise
low-dimensional summaries of the detector readout, such as the reconstructed
main quantities that will be presented in the next section, by using approximate
conditional probability density functions. While this approach, implemented
in software packages such as DELPHES [@deFavereau:2013fsa],
is limited by the flexibility and accuracy of the modelling
of the conditional probabilities,
it is very useful as a very fast substitute of the full simulation
chain for simplified studies that aim to obtain an approximate
estimate the expected sensitivity reach or measurement accuracy
of a given analysis.


### Event Reconstruction {#sec:event_reco}

In the previous sections, the generative mechanisms by which
particles produced signals in the different detectors, as well as
the techniques used to procedurally simulate them with high fidelity,
were summarised. In contrast with simulated events,
the set of underlying particles that were produced in the
interaction region, and subsequently detected, are not known a priori
in real collisions. A very helpful task to understand the nature of
the fundamental interaction that likely happened in a collision is
to infer the type and properties of the particles that were probably
produced on a given collision given the detector output. Such procedure
is generally referred to as *event reconstruction*. The underlying problem
for achieving such goal is mainly the assignment of detector readouts
to the produced particles
is not an easy one, given that the total number or the relative multiplicities
of the different particle categories in a given event is unknown, but expected
to be large given the high-energy and luminosity conditions of proton-proton
collisions.

#### Reconstruction at CMS: Particle-Flow Algorithm

A somehow hierarchical strategy is followed to perform event reconstruction
at CMS experiments. First, the combined properties of
small groups of low-level readouts for each sub-detector in
collision are used to construct higher-level summaries that distill
the information regarding the origin, direction or energy
of the particles. In a second step, such high level constructs are linked
by an algorithm based on the expected properties of each particle type,
to obtain a list of *physics objects* and their relevant attributes,
which would probably correspond to those that actually were generated in
the collision. Such approach, that is referred to as *particle-flow * (PF) event
reconstruction [@Sirunyan:2017ulk] within CMS data analysis techniques,
has proven very effective to obtain a lower dimensional transformation of
the detector readout that greatly simplifies the interpretation
and categorisation of events based on their particle content.

As mentioned before, the first reconstruction stage encompasses
the combination of detector traces in each sub-detector system to create
higher level constructs. In the tracking detector, this amounts to associate
the location estimate for the signals detected in all layers of the
pixel and strip detector, referred to as  *hits*,
to trajectories of charged particles, simply called *tracks*. This inverse
measurement problem is tackled in CMS by using a combinatorial
extension of the Kalman Filter
algorithm [@Billoir:1990we; @Mankel:334615; @Chatrchyan:2014fea]. In broad terms, 
the algorithm
starts by selection sets of two-hit and three-hit associations from
the inner layers, referred to
as *seeds*, which are then extrapolated outwards and used to gather hits
in the the other layers by consecutive prediction and update steps, keeping
all combinations that are deemed compatible. An additional step is then carried
out, that filters out all candidate tracks under some pre-defined quality
threshold and removes possible duplicates. Once the set of hits that define
each track are found, their parameters are fitted again using a more detailed
prediction step in the Kalman filter, thus obtaining more accurate estimates
for their origin, momentum and direction.

<!-- could mention iterative tracking, multiple seeding, and muon/electron
tracking-->

The reconstructed charged particle trajectories can be used to identify
the spatial locations where proton-proton interactions occurred
in each bunch crossing, dubbed *primary vertices*, by
extrapolating them back to the collision region and looking for
overlapping subsets. In practice, a custom algorithm for vertex
adaptive fitting
[@Fruhwirth:2007hz] is used in combination with deterministic annealing,
to identify and compute the vertices location and their
uncertainty more accurately. Most primary vertices
correspond to soft scattering processes (pileup), and can be used
to characterise the position and size of the interaction region. In collisions
where a hard interaction occur, the main primary vertex can often be identified
with the one whose linked tracks transverse momenta squared sum $\sum p_T^2$
is the largest. The distinction of a main primary vertex is useful to
mitigate the effect of pile-up interactions in reconstruction by
removing the contributions from particles linked to pileup vertices. 

Regarding the calorimeter detector readouts, the initial step comprises
the clustering low-level deposits in each sub-detector, so it has to identify
the energy remnants left by each individual particle. The clustering procedure
starts by finding the calorimeter cells where the amount of deposited energy
are local maxima, referred to as *seed* deposits.
The deposits in contiguous energy cells are grouped together until
their energy is smaller than twice the expected noise level,
forming larger *topological clusters*. Because such clusters the results of
the overlapping of the energy deposited by two or more particles, the final
clusters are identified by fitting a Gaussian-mixture model via
the expectation-maximisation algorithm, using the number of initial
seeds present in the cluster as the number of Gaussian components in the
mixture. The fitted cluster amplitudes are thus expected to be
heavily correlated with energy deposited by an individual particle, but
an extensive calibration based on a detailed simulation of the detector
and the assumed particle type. The resulting calibrated clusters in each
sub-detector (ECAL, HCAL and HF) will be instrumental for improve the energy
measurement of charged hadrons, identifying measure the energy of neutral
hadrons and photons and as well as to facilitate the identification and
reconstruction of electrons.

Once the basic *elements* for event reconstruction have been constructed,
charged particle tracks and calorimeter cluster are linked together
to form *blocks*. This step is an attempt to group the various
traces that particle can leave in the various sub-detectors, by linking
pairs of elements based on their distance in the $(\eta,\phi)$ plane
and other properties depending of the specific sub-systems considered. When
considering links between inner tracker and the calorimeter clusters,
the curvature of the tracks and details regarding the detector
geometry are taken into account. Calorimeter cluster-to-cluster
links between the HCAL and ECAL, and between the ECAL and the pre-shower
clusters are also sought. Additionally, ECAL clusters possibly created by
bremsstrahlung photons can also be linked to electron-like tracks if they
are consistent with an extrapolation of the track tangent. Finally, links
between two tracks due subsequent photon conversion via pair production
also considered if the sum of track momenta matches the mentioned
electron-like track tangent.

The outcome of the aforementioned procedure is a set of blocks of elements
for a given collision readout,
formed by associating elements that have been directly linked or share
a common link with other elements. The following reconstruction step
is referred to as *object identification*, and its based in the
association of blocks to a list of particle candidates, also known as
*physics objects*. This is done sequentially, starting out by the
objects that more easily identified (e.g. muons) and progressively
masking out the blocks that are considered for each object until
all particles candidates have been reconstructed. The reconstruction
process is rather conservative, given that most CMS data analysis
share the same reconstructed *physics objects*, therefore it is
common to specify additional selection criteria based on over the
resulting set of objects based on their properties within each analysis
to reduce the rate of fake or wrong reconstruction.
The rest of this section is devoted
to discuss in more detail the identification, calibration and common
selection requirements on the main reconstructed objects
that are used within
physical analyses.

#### Muon Reconstruction

Muons can be thought of as the easiest object to identify given the
observed detector readouts, because they are the only particle expected
to reach the outer tracking systems (i.e. muon detecting system).
Furthermore, the detecting volume far away from the interaction region
is much larger and hence the density of
particle trajectories are considerably lower. The sparse particle hits
in each of the muon detector systems are linked to form tracks that
can be combined using a Kalman filter, similarly to what is done
for the inner tracker as described earlier this section. To increase
the measurement accuracy and reduce the fake rate, in analysis
directly studying final states including muons, oftentimes
a matching between the track segments in the muon detectors and
a those in the inner tracker is required. The details and performance of the
reconstruction procedure depend on the momenta of the muon, and
are described in more detail the following
reference [@Chatrchyan:2014fea].

The main challenges of muon reconstruction include the
dismissal of muons produced by cosmic rays hitting the
atmosphere and going through the CMS detector, simply dubbed
as *cosmic muons*, as well as
the rejection of signals from very energetic
hadrons produced in the collision that are able to transverse
the dense calorimeter and magnet section and still produce a response
in the muon detectors, that are referred to as *punch-through* hadrons.
In addition, muons are a common product of the decay of hadrons and it
thus is important to differentiate between muons likely produce in
the primary interaction, or *prompt muons*, and those produced
in a secondary decay of another particle. The amount of energy
deposited around the muon trajectory, called *muon isolation*, as well
as the distance to the primary vertex are important variables for
such distinction.

#### Electron and Photon Reconstruction

Electron reconstruction is more challenging because it uses
the readouts from the inner tracker and the ECAL, both detector
being sensitive to additional charged particles coming
out from the detector volume, and the latter also to high-energy photons.
Furthermore, electrons lose energy in their curved trajectories
through the tracker, thereby complicating an accurate track
reconstruction. The
latter can be accounted for during the track reconstruction by
using a Gaussian-Sum filter extension fo the Kalman filter
[@Adam:2005bya] algorithm, which can be used to model the
previously mentioned non-linearities. The procedural details
of the identification and property measurement for electrons
depend on their transverse momenta. Lower energy electrons are
more accurately indentified using the inner tracker hits, while
the electromagnetic calorimeter is more useful at higher energy ranges.
These and other details regarding electron reconstruction are discussed
in the following
reference [@Khachatryan:2015hwa].

The electron momentum direction is measured using the
track information, while the energy is estimated by combining both
information from the tracking and calorimeter detectors. In order
to obtain precise energy and momentum estimates, under 5% in the
full pseudo-rapidity range, a calibration step is required to correct
for non-clustered energy deposits and pile-up contributions. Similarly
to what is done for muons, additional quality criteria can be applied to
distinguish between the electrons produced in the primary interaction
and those coming from hadronic decays or converted photons, including
conditions of several track-based and calorimeter-based observables
as well as isolation requirements, the latter ensuring that no
significant energy from hadrons was deposited around the electron
trajectory.

High-energy photons are identified and reconstructed using
only the calorimeter [@Khachatryan:2015iwa],
when the energy distribution in the ECAL
calorimeter cells is consistent with that expected from a photon
shower. Energy isolation requirements are also essential
to distinguish photons
coming from hadron or secondary radiative decays, which
will be discussed together with hadrons, from those
originated as a direct product of the primary interaction. Additional
quality and fine-tuned calibration is often used, for example in the
$H \rightarrow \gamma \gamma$ analysis, to reduce the fake rate
and obtain higher momentum resolution.

#### Jet Reconstruction and B-Tagging {#sec:jet_btag}

Once muons, electrons and isolated photons in the event have been
identified, the remaining particle-flow blocks (i.e. linked tracks
and/or calorimeters deposits) are interpreted as either as
neutral or charged *PF candidates* [@Sirunyan:2017ulk].
These physics object candidates
account for charged and neutral hadrons coming from the hadronisation
of partons produced in the collision or their subsequent decays,
as well as non-isolated photons radiated during those processes.
When the aim is studying high-energy fundamental interactions
that produce partons or other parton-decaying intermediate particles
(e.g. $H \rightarrow b \bar{b}$), such reconstructed objects are not
directly practical because their individual momenta cannot be linked
with original parton momentum. This is because the processes of
fragmentation, hadronisation, decays 
and associated radiation are stochastic, producing
tree-like structures with multiple leafs as discussed
in Section [@sec:parton_showers],
difficulting attempts to uniquely identify each parton with its
decay chain. In addition, contributions from additional
soft pileup interaction can further complicate the mentioned assignment,
while this factor is lessen by charged hadron subtraction techniques (CHS)
[@CMS:2014ata] based on removing candidates not associated with a
primary vertex.


A possible way to construct simpler observables that can be
linked with the original partons is to create composite objects based
the remaining candidates through clustering. These objects,
referred to as *jets*, are an attempt to represent the chain of hadrons
and radiated energy produced, so the original parton energy and momentum
can be recovered from the summed of the components. They can be
geometrically viewed as cones coming from the interaction region,
covering an angular area $\Delta R$ of a given size in an outwards
direction, that contains 
a collimated set of hadrons and radiated photons flying away a
direction similar to the original parton. Several jet clustering
algorithms exist, each characterised by a given a size or resolution
parameter $R$ and a recombination scheme, defining how
candidates are combined to create the composite clustered object.

Due to
the properties of hadronisation and QCD radiation processes,
a common requirement
for such clustering algorithms is that they do not change significantly
when a particle is split in two collinear ones (i.e. they
are *collinear safe*)
or additional soft radiation is produced by one of the clustered
particles (i.e. they are *infrared safe*), which greatly simplifies
direct comparison with generation level observables. In
particular, in the analysis described in Chapter [-@sec:higgs_pair],
the default jet CMS reconstruction is extensively used, which is
based on the $\textrm{anti-k}_T$ algorithm [@Cacciari:2008gp]. This
is a sequential algorithm, also classified as
hierarchical agglomerative clustering in statistical language,
starting assigning each candidate to each cluster and successively 
merging them according to the following distances between two
jets indexes as i and j respectively:
$$ d_{ij} = \min ( p_{Ti}^{2a}, p_{Tj}^{2a}) \frac{\Delta R_{ij}^2}{R^2}
\quad \textrm{and} \quad
d_{iB} = p_{Ti}^{2a}
$$ {#eq:antikt_distance}
where $\Delta R_{ij}^2$ is the $\eta-\phi$ plane distance as defined
in Section [-@sec:exp_geom],  $p_{Ti}^{2a}$ and $p_{Tj}^{2a}$
are the transverse momenta of each jet, $R$ is the size parameter
and $a=-1$ for the $\textrm{anti-k}_T$ algorithm. The algorithm
starts by computing all distances $d_{ij}$ and $d_{iB}$ for all
initial candidates, which are placed in a list. If the minimum
corresponds to given distance between two candidates $d_{ij}$
then both candidates are removed from the candidate list
and group together by summing their
four momenta forming a composite object, which is in turn 
added to the list. Alternatively, if the minimum distance
is $d_{iB}$, the $i$ candidate is assigned as a jet and removed
from the list. Such procedure is recursively applied until
the list is empty, because all single and composite candidates
have been grouped with other candidates or defined as a jets of 
a given size $R$. The choice of the parameter $R$ has to provide
a balance between covering all the radiation from the initial
parton and being increasingly affected by noise produced by soft
particles. During the data taking period considered in
Chapter [-@sec:higgs_pair], a cone size $R=0.4$ was used for the
default jet collection, used in the analysis. Larger jet (e.g. $R=0.8$)
cones are used in analyses
that include final states with highly boosted intermediate
particles, that produce a collimated set of hadrons and radiation
when they decay, commonly with internal structure
that can be exploited to improve the sensitivity.
Various sequential clustering 
algorithms can be defined by considering a different value
of $a$ in Equation [-@eq:antikt_distance]. If a negative choice
for the exponent $a$, as used in the $\textrm{anti-k}_T$ algorithm,
higher transverse momenta particles are clustered first and thus
the final jet outcome is less sensitive to soft pileup contributions
and radiation.

The energy and momenta of the resulting jets is not expected
to match accurately that of the original partons, due to the compound
effect of detector readout and or non-linearities, as well
as effect from pileup contribution. This motivates the
application of a set of corrections, referred to as
*jet energy corrections* (JECs) [@Khachatryan:2016kdb],
that greatly reduce this discrepancies by
sequentially shifting and rescaling the jet four-momenta based
on extensive calibrations obtained from simulation.

<!-- could expand a little bit in energy calibration and quote
expected uncertainties -->

So far, jets have been defined as an experimental simplification
of hadronisation, decay and fragmentation chains
in order to estimate  the energy and the momenta
of initial partons produced in the collision, and we have ignored
the other properties of the original parton. In particular, information
regarding the flavour of the initial parton can be instrumental
to distinguish event containing jets coming from high-energy
processes with physical interesting intermediate
particles like a Higgs boson $H$ or top quarks/antiquarks,
which predominantly decay to $b$ quarks. Heavy flavour $b$ quarks,
and to a lesser extent also for $c$ quarks, hadronise producing $B$ (and
$C$) hadrons that have lifetimes long enough to fly away from the
primary vertex before decaying. 

![Schematic representation of the features of a heavy-flavour jet
that can be used for jet tagging including the presence charged tracks, with
a large impact parameter (IP), that is not compatible with the primary vertex
(PV),
and a reconstructed secondary vertex (SV), both due to the decay of $\textrm{B}$
or $\textrm{C}$ hadrons. Figure has been adapted from [@Sirunyan:2017ezt].
](gfx/102_chapter_2/Figure_001.pdf){
#fig:CMS_btag_scheme width=50%}

Some properties of the decay of $B$ and $C$ hadrons can be used to
distinguish heavy flavour jets from those produced by light quarks and gluon
hadronisation processes. In particular, the lifetimes of heavy flavour hadrons
are often long enough that they move several millimetres  away from
the primary vertex where they were produce before decaying, when
highly boosted. Thus, heavy flavour jets are associated with the presence
of displaced charged tracks and secondary vertices (SV) within the jet,
as depicted by [Figure @fig:CMS_btag_scheme]. In addition, both
$\textrm{B}$
or $\textrm{C}$ hadron decays are characterised by a large decay multiplicity
(average 5 charged daughters) and a high probability (36\%) of producing
a lepton in their decays chain. Flavour tagging techniques, often referred
to as b-tagging or c-tagging when the purpose is to identify a jets
originating from a particular type of parton, combine quantitative information
related with the various properties previously mention to distinguish the
flavour of the parton that generated a given jet.

![Misidentification probability (in log scale) for jets
originating from $c$ (dashed line) and light quarks or gluons (solid line)
versus b-tagging efficiency, for different b-tagging algorithms available
in CMS during 2016. The misspecification probabilistic and efficiencies
are obtained from the subset of reconstructed jets with a $p_T>20\ \textrm{GeV}$
from a large $\textrm{t}\bar{\textrm{t}}$ simulated sample.
Figure has been adapted from [@Sirunyan:2017ezt].
](gfx/102_chapter_2/Figure_016.pdf){
#fig:CMS_btag_comp width=70%}

Heavy flavour tagging, particularly b-tagging can very useful for analyses
considering jets in  final states, such as the search for Higgs pair production
with CMS data described in [Chapter @sec:higgs_pair]. The misidentification
versus efficiency curve of the main b-tagging
algorithms that were available in 2016 for high-energy jets is shown
in [Figure @fig:CMS_btag_comp]. They differ in the subset of information
associated to the jet that is considered and the specifics of the 
multivariate techniques used to construct the final discriminator. The simplest
b-tagging algorithm, referred to as jet probability (JP) is only based a
calibrated estimation of the displaced track probabilities. The b-tagging
discriminators pertaining to the combined secondary vertex (CSV) family
combine displaced track information with reconstructed secondary vertex.
The improvement between different CSV-based b-tagging algorithms
is due to the use of more advanced statistical learning techniques
and additional discriminating variables [@Sirunyan:2017ezt]. The CMVAv2
algorithm, which is used in the analysis included in [Chapter @sec:higgs_pair],
combines the output from JP and CSVv2 algorithms with two taggers that
combine the information from non-isolated electrons and muons inside
the jet.

In [Section @eq:particle_id_reg], the role of recent advances in machine
learning techniques for particle identification and regression are
discussed in more detail, focussing on the development and integration
on a new deep learning based multi-category jet tagger referred
as DeepJet. The DeepJet
tagger outperforms both CMVAv2 and DeepCSV (which also leverages
deep learning technologies), while
providing additional discrimination capabilities (e.g. gluon-quark
separation). It worth mentioning that jet tagging techniques
can also be applied for identifying substructure in larger radius
jets, which are very relevant for analysis where highly boosted
intermediate objects are expected, but are not discussed in
this work.

#### Missing Transverse Energy {#sec:met_pf}

As hinted in Section [-@sec:gen_view], neutrinos can be
produced at high-energy proton-proton collisions, and they leave the detector
undetected. Nevertheless, the presence of neutrinos
(or other hypothetically weakly-interacting particles) can be
inferred by the total momentum imbalance in the transverse plane
of the event. Within the Particle-Flow reconstruction framework,
this accounts to computing the vectorial sum of the transverse
momenta of all PF reconstructed objects:
$$ \vec{p}_T^\textrm{miss} =  \sum \vec{p}_{Ti}^\textrm{miss}$$ {#eq:met_pf}
where $\vec{p}_T^\textrm{miss}$ is the total missing transverse
momentum, whose Euclidean norm modulo is the missing 
transverse energy $E_T^\textrm{miss}$, and $\vec{p}_{Ti}^\textrm{miss}$ is
the transverse momentum each PF candidate.

It is worth remarking that some hadron decay processes can produce
neutrinos and therefore of a non-zero transverse
missing energy $E_T^\textrm{miss}$ does not necessarily mean that
weakly-interacting particles were produced in the hard
interaction or by its direct products. Furthermore, any mis-detections
or mis-measurements of the momenta of some of the produced particles
can lead to transverse energy imbalances.


