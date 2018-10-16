# Experiments at Particle Colliders {#sec:experiment}

\epigraph{Measure what is measurable and make measurable
   what is not so.}{Galileo Galilei (attributed)}

In Chapter [-@sec:theory], the most successful testable theory to date
describing the properties and dynamics of our universe at the most
fundamental scales has been reviewed.
Nevertheless, clear limitations of the Standard Model as it is currently
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
directions to ultra-relativistic velocities, so then can be collimated
and made interact at high-energies around several specified collision
points inside specially designed detectors.
The LHC machine complex is located at the European
Organisation for Nuclear Research (CERN) laboratories around
the Switzerland-France border near Geneva, its most distinctive element being
a circular ring of superconductive magnets and accelerating structures
installed along a 26.7 km underground tunnel inherited from the
Large Electro Positron (LEP) collider [cite], as depicted in Figure
[-@fig:LHC_overall]. The setup was designed
to achieve center-of-mass energies up to 14 TeV for nominal instantaneous
luminosities reaching $\times 10^{34} \textrm{cm}^{-1} \textrm{s}^{-1}$
for proton-proton collisions, and hence explore the high-energy frontier of
particle physics.


![LHC Overall
](gfx/102_chapter_2/LHC_overall.pdf){
#fig:LHC_overall width=70%}

The main reason for building a high-energy proton-proton collider such as the
LHC instead of a more powerful electron-positron, given the difficulties
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
as of 2018 are summarised in Figure [-@fig:fig:CERN_Acc_complex].
The purpose of this section
is to outline the sequence of steps followed to obtain the high energy
proton bunches that are used for high-energy collisions at the LHC.


![CERN Accerator Complex
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
hadrons with gas molecules. The proton trajectories are bended
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
LHC, lasting between 2015-2018). Given that each cavity can
provide about 60 keV per revolution, it takes about 20 minutes
of *ramp* time to reach collision energies.

During the whole acceleration process, specialised dipole magnets
are used to kept the beams separated at the four interactions points
(IPs) and hence avoid collisions during that time.
With the purpose of maximising
the interaction rates, the beams are made more compact (commonly
referred as *squeezed*) at the interaction region
right before switching to collision mode. Once
the characteristics of the proton beam are suitable, the quadrupoles
align the beam trajectories and *physiscs* collisions begin. A stable
configuration is then adopted by the LHC machine, providing about 7 keV 
of energy to the beam to account for synchrotron radiation losses using
the RF cavities. If not unexpected problems occur, the proton beams are kept
circling the LHC ring and colliding at the IPs for several hours until
the bunch properties are degraded beyond correction,
a period that typically is referred as a LHC *fill*. The *fill* is
finalised when some problem occurs or when all the proton bunches
inside the ring are *dumped* (made collide) against graphite absorbers
tangent to the beam pipe.
 
### Operation Parameters

One of the most relevant parameters for a particle collider is the
instantaneous luminosity $\mathcal{L}(t)$, which already appeared in
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
$$ \mathcal{L} = \frac{n_p^2 n_b f_r \gamma_r}{ 4 \pi \epsilon_n \beta^{*}}
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
The average values of some these parameters and the peak instantaneous
luminosities for the different years of proton-proton data acquisition periods
(also known as *runs*)
at the LHC are summarised in Table [create], which can
be compared with the peak design luminosity of the LHC  of $\times 10^{34} \textrm{cm}^{-1} \textrm{s}^{-1}$.

From Equation [-@eq:lumi_beam] it can be inferred that that value of
instantaneous luminosity varies between LHC *fills* depending on the beam
parameters. In fact, it also varies within a single *fill* with time,
mainly because the number of average protons per bunch $n_p$ decreases
due to the collisions at all the interaction points. For convenience,
a quantity referred as integrated luminosity $\mathcal{L}_\textrm{int}$
that is computed by integrating over the instantaneous luminosity for a
given time period $\Delta T = t_1 - t_0$, such as stable collision period
within a a *fill*, is used:
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

### Multiple Interactions


### Experiments

Around the collision volume at each of the interaction points, large
detectors are positioned in order to reveal and quantitatively
study the outcomes of the highly-energetic particle scattering,
which can in turn be used to obtain information about the properties
of fundamental interactions. Four large particle
experiments are installed at the LHC interaction points:

* **ATLAS** (A Toroidal LHC ApparatuS) [@ATLAS:2008JINST]:
  the largest experiment at the LHC, designed as a
  general-purpose detector to study the various products of high-energy
  interactions, specially those of high-luminosity proton-proton collisions.
  While one of the most important 
  scientific goals of the ATLAS experiment was to discover Higgs boson
  and provide a detailed study of its properties, it was also build with
  the aim of extensive testing of Beyond the Standard Model (BSM) theories.

* **CMS** (Compact Muon Solenoid) [@CMS:2008JINST]:
  the other general-purpose experiment at the LHC, sharing most of the
  research goals with ATLAS, but opting for an alternative
  design and a different choice of detector technologies
  making it considerably more compact. It is the
  detector that collected the data use in the analysis in Chapter
  [-@sec:lhc_analysis] and
  hence is described extensively in Section [-@sec:cms].

* **LHCb** (Large Hadron Collider beauty) [@LHCb:2008JINST]:
  operating at a lower range of luminosity than ATLAS or CMS,
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
  a better understanding of color confinement and other relevant
  QCD problems,
  as well as shedding some light on the processes that took
  a few microseconds after the Big Bang.
  

Additionally, three smaller experiments are built around the mentioned
detectors with specific research purposes: TOTEM [@TOTEM:2008JINST],
LHCf [@LHCf:2008JINT] and MoEDAL [@MoEDAL:2014PP]. Both TOTEM and LHCf
are built investigate features of forward physics interactions, where
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
rather simple, it can be reduced to the detection of the outgoing
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
can be compared with the expected theoretical predictions
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

![CMS detector
](gfx/102_chapter_2/CMS_detector.pdf){
#fig:CMS_detector width=90%}

### Experimental Geometry

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
and are measured with more accurately as
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

Since that would complicate the statistical analysis
and the definition of derived observables, an alternative observable
can be defined based on the rapidity $y$, which is defined as:
$$y = \frac{1}{2} \ln \left ( \frac{E+p_z}{E-p_z} \right ) $$ {#eq:rapidity}
and whose value on a under a $z$-axis boost can be easily obtained by adding
an additive factor
$y'=y-\textrm{tanh}^{-1} \beta$, and hence differences on rapidity between
two particles in a collision $\Delta y = | y_b - y_a |$ are invariant to
Lorentz boost in the $z$ direction. Because the rapidity depends on
the total energy/momentum of the particle, which might not be possible to
measure to high precisions in hadron collider detectors,
it is more suitable to approximate it using
the *pseudo-rapidity* $\eta$, defined as: 
$$\eta = - \ln \left ( \tan \frac{\theta}{2} \right ) $$ {#eq:pseudo_rapidity}
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
limit, and would be particularly practical to cluster the products of the
hadronization of quarks and gluons as detailed in Section [-@sec:event].

### Magnet {#sec:cms_magnet}

The sole purpose of the CMS magnet is to curve
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
Furthermore, the direction of the curvature, is determined by the
sign of the particle charge. For more realistic scenarios, like
the magnetic field not being not completely homogenous
or the particle momentum decreasing along its trajectory due
to interaction with the detecting elements, the Equation [-@eq:lorentz_eq]
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
referred as *tracks*, for all charged particles and for escaping
muons are reviewed in Sections [-@sec:cms_tracking] and [-@sec:cms_muon],
respectively.


### Tracking System {#sec:cms_tracking}

The inner tracking system is the detector that is the closest to the
interaction point, and its functions include the estimation of
the charged particles trajectories, used to provide a measurement
of their momenta as described in Section [-@sec:cms_magnet],
as well as allowing the positional determination of interaction
or decay vertices by extrapolating the trajectories inside
the interaction region. The detection charged particle trajectories,
or *tracks* for short, it is carried out by several silicon
detector layers placed non-uniformly around the collision volume,
as shown in Figure [-@fig:CMS_tracker]. The placement is of layers is
symmetric in $\phi$, the outermost layers contained within
a supporting cylindrical structure of 2.5 m of diameter and 5.8 m
of length.

![CMS Tracking System
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
property is commonly referred as *high-granularity*, and allows to
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
arrangement) layers, located at radii of 4.4 cm ,7.3 cm and 10.2
cm respectively, and two forward disk at each side at
distance of 34.5 cm and 46.6 cm from the nominal interaction point.

The rest of the tracking system, placed outside the pixel detector just
described, is constituted of several
silicon strip detector modules organised in different sub-detectors,
as shown in Figure [-@fig:CMS_tracker].


### Electromagnetic Calorimeter


### Hadronic Calorimeter

### Muon System {#sec:cms_muon}


### Trigger and Data Acquisition

## Event Data Analysis {#sec:event}

### Simulation

### Reconstruction




