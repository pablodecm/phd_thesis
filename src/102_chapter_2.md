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
 
### Operation Parameters {#sec:op_pars}

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
be compared with the peak design luminosity of the LHC  of
$1 \times 10^{34} \textrm{cm}^{-1} \textrm{s}^{-1}$.

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

### Multiple Hadron Interactions {#sec:pile_up}

Given the high density of protons in each bunch at the collision
points, several proton-proton interactions are very likely
to happen in each crossing, a phenomenon that is commonly referred to
as *pileup*. After multiple interactions occur,
the products of all interactions go through the surrounding
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
about 25 *soft* scattering interactions (i.e. low momentum transfer),
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
a total of 2808 proton bunches in each beam, corresponding to a bunch
separation of only approximately 7.5 m. Hence the time separation between bunch
crossing is about 25 ns, which is of the same order than the response time
of many of the detector technologies used at the LHC. The readout from a
a particular bunch crossing can therefore be affected by the detector occupation
caused by the previous or subsequent crossings, in what is referred to
as *out-of-time pileup*, that becomes an important consideration for detector
design in high-luminosity environments.



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
silicon strip detector modules organised in different four sub-detectors,
referred as TIB, TID, TOB and TEC in Figure [-@fig:CMS_tracker].
The inner part of the strip tracker, adjacent to the pixel detector,
is composed of four barrel layers of strip modules
constituting the tracker inner
barrel (TIB) section, and 3 module layers arranged in disks at at each side
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
and $z$ in the endcap disks. In order to provide information about
the unknown coordinate in each case, some layers of the tracker
(in blue colour in Figure [-@fig:CMS_tracker]) are composed of
two modules instead on one, with a small tilt of 0.1 rad that allows
to obtain a precise 3D coordinate for a track hit by combining the
two local coordinates and their module positions. 


### Electromagnetic Calorimeter

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

![CMS Electromagnetic Calorimeter
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
effectively all the energy is deposited in inside the detectors.

Another advantage of  lead tungstate crystals it is that $\textrm{PbWO}_4$
is also a scintillating material,
thus the resulting shower energy is absorbed and partially emitted back
as visible light, with a yield spectrum maximum in the blue-violet range
around 430 nm. The reemission process is also very fast, about 80% of the
scintillating light is emitted within 25 ns of absorption, which
is the time until the next LHC bunch crossing occurs. The scintillator
light propagates through the crystal effectively due to its high
transparency and reaches the photodetectors attached to the end
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
decayed to two closely-spaced photons.



### Hadronic Calorimeter

The purpose of the hadron calorimeter (HCAL) is to measure the energy
and position of all long-lived neutral or charged mesons and baryons
produced as a result of the collision, typically including pions, kaons,
protons and neutrons. The main detecting elements of this sub-detector
are an assortment of sampling calorimeters, interleaving brass plates as
absorber material and a plastic scintillator tiles as active
medium, the former causing the deposition of energy in the form of secondary
particles by means of interactions with the material nuclei and the latter
converting a part of that energy to visible light. The light from each tile
is captured by a thin optical fibre and carried to a photodetector, producing
electric signal that can be used to measure the total amount of deposited
energy with the help of careful calibration.  

![CMS Hadronic Calorimeter
](gfx/102_chapter_2/HCAL.pdf){
#fig:CMS_hcal width=70%}

The different segments of the CMS HCAL are shown in Figure [-@fig:CMS_hcal].
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
light, over 65% of the total amount of emitted light within 25 ns (i.e. period
between bunch-crossing). The light is collected and guided through thin optical
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
allowing a near hermetic (full solid angle) coverage, and hence allow the
estimation of missing energy in the event such that corresponding to
neutrinos leaving CMS undetected, as will be discussed in Section [-@sec:event].
Because the radiation fluxes are extremely high in the forward region and
there a no depth constraints, a different detector design is used,
based on 165 cm of steel absorber plates and quartz fibres aligned of the
z-axis, each with an effective detecting
area of $\Delta\eta\times\Delta\phi= 0.17\times0.17$.


The fibres running along the HF detect and guide the Cherenkov light of the
charged secondary particles produced in the showers to photomultipliers
tubes (PMT) placed behind a 40 cm thick steel and polyethylene shield.
In this pseudo-rapidity range, the also HF serves also as an electromagnetic
calorimeter, and being able to disentangle the energy contributions
from electromagnetic and hadronic showers is quite useful for
many physics data analysis use cases. Given that electromagnetic showers
are much shorter than hadronic showers, only half of the fibres
start close to the face of the absorber plates closest to the IP,
the rest other starting at a depth of 22 cm. By comparing the readouts
of long and short fibres, the type of shower can be inferred.


### Muon System {#sec:cms_muon}

The scientific objective of the CMS muon sub-system, or outer tracker,
it is to identify, determine the charge and measure the momenta of high
energy muons, that can pass through all the other detector systems
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

![CMS Muon Detectors
](gfx/102_chapter_2/cms_muon.pdf){#fig:CMS_muon width=70%}

The muon system is the most external sub-detector of CMS
and it is based on gaseous tracking detector technologies,
given the large volumes covered. The principle of action of
gaseous detectors is rather simple, charged particles
passing through the gas ionise gas molecules in their path,
which start moving due to a high electric field between
conducing wires, producing an electrical signal
that can be readout. The time dependency of the signal
on the different readout wires can be used to inferred
the particle trajectory with high precision, an in some
cases built-in signal amplification can be achieved
due to secondary ionisation by
the choice of a gas mixture combined with high electric
field gradients.

An overview of the various detectors
of the muons system and their geometrical placement
around the solenoid magnet cylinder is depicted
in Figure [-@fig:CMS_muon]. Due to a combination
of criteria regarding uniformity and strength
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


### Trigger and Data Acquisition

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
each 25 ns amounts to a large amount of data, due to the total number
of sub-system channels, even if efficient techniques for 
representation and compression of information are used. Given that technical
limitations on the amount of data that can be recorded exist,
a practical choice for data acquisition is keeping only the detailed detector
information of collisions that could be maximally useful to study the properties
of fundamental interactions in subsequent data analyses. The decision system
that makes the choice of wether to record or filter out the detailed detector
readouts for a given collision, is commonly referred as *trigger*, 
and is based on a fast and possibly asynchronous analysis of those readouts. In
particular, such process is typically focussed on the most relevant properties
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
or simplifications or simplifications thereof. This is because for practical
purposes, statistical independence between events can be assumed with
some caveats (e.g. out-of-time pile-up or detector malfunctioning). Therefore,
data analyses are reduced to the task of comparison between the observations
and the expected predicted frequencies of events with different
characteristics.

The dimensionality of an event evidently depends on its data representation,
simpler representations being lower-dimensional and easing the comparison
with theoretical predictions, at the cost of possibly losing
some useful information. A principled way to obtain lower dimensional
representations of an event given its raw detector readouts
is to attempt to infer all the primary particles that were produced
in the main proton-proton interaction of the collision and as well as 
estimate their main properties,
done through a process generally referred as *event reconstruction*.
Nevertheless, 
for carrying out successfully the aforesaid task it is convenient to
being able to have a detailed model of the detector readout output that is
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


### A Generative View

When two high-density proton bunches in opposite directions
pass through each other inside the collision region of CMS,
several proton-proton interactions can occur as discussed
in Section [-@sec:pile_up]. While most of the interactions will
correspond to a small energy transfer between the interacting
partons, given that the total interaction cross section is
heavily dominated by soft scattering processes, a small fraction
of collisions would include physically interesting process
such as the production of heavy intermediate particles (e.g. a
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
accounted for using the techniques mentioned in
Section [-@sec:parton_showers]. The end result of the mentioned
procedures is a large dataset of simulated particle
outcomes for a specific process, each example including
a set of stable or sufficiently long-lived particles and their
kinematics properties that would propagate through the detector.

![Transverse view of a section of the CMS detector, adapted from [@Sirunyan:2017ulk].
](gfx/102_chapter_2/CMS_transverse.pdf){
#fig:CMS_transverse width=70%}

### Detector Simulation

### Event Reconstruction




