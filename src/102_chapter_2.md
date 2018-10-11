# Experiments at Particle Colliders {#sec:experiment}

\epigraph{Measure what is measurable and make measurable
   what is not so.}{Galileo Galilei (attributed)}

In Chapter [-@sec:theory], the most succesful testable theory to date
describing succesfully the properties and dynamics of our universe at the most fundamental scales has been reviewed.
Nevertheless, clear limitations of the Standard Model as it is currently
formulated are known,
such as the complete omission of gravity forces or the absence of viable
dark matter candidates, motivating the quest for alternative
unified descriptions of the physical world. A direct
path to verify the predictions of the Standard Model up to high acurracy
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

The Large Hadron Collider (LHC) is the largest and most poweful particle
accelerator on operation at the time of writing. Its main purpose is to
accelerate bunches of protons and other heavier nuclei in opposite
directions to ultra-relativistic velocities, so then can be collimated
and made interact at high-energies around several specified collision
points inside specially design detector.
The LHC machine complex is located at the European
Organisation for Nuclear Research (CERN) laboratories around
the Switzerland-France border near Geneva, its most distinctive element being
a circular ring of superconductive magnets and accelerating structures
installed along a 26.7 km underground tunnel inherited from the
Large Electro Positron (LEP) collider [cite], as depicted in Figure
[-@fig:LHC_overall]. The setup was designed
to achieve center-of-mass energies up to 14 TeV for nominal instantaneous
luminosities reaching $10 \times 10^{34} \textrm{cm}^{-1} \textrm{s}^{-1}$
for proton-proton collisions, and hence explore the high-energy frontier of
particle physics.


![LHC Overall
](gfx/102_chapter_2/LHC_overall.pdf){
#fig:LHC_overall width=70%}

The main reason for building a high-energy proton-proton collider such as the
LHC instead of more powerful electron-positron, given the difficulties
when computing observables, due to protons being composite particles as described
in Section [-@sec:pheno], is that proton are considerably more massive
and hence their synchroton radiation loss is greaty reduced, so the
accelerated to higher energies and more efficiently. Another
practical advantage of proton colliders is that very high
collisions rates (i.e. instantaneous
luminosities) can be technically achieved, which makes them suitable for
the discovery of rare but interesting physical proceses.
While the LHC and most of its detectors can also be used with to study
collisions
of nuclei from heavier atoms, such as $\textrm{Pb}$, $\textrm{Au}$ 
or $\textrm{Xe}$ ions,
which have important scientific use cases such as recreating
the conditions present in the early universe, in this work we will
be focussing on proton-proton collisions.


### LHC Injection and Acceleration Chain

In order to achieve beam energies of the TeV order, protons have to
follow several stages of synchronised accelerations through a variety
subcomponents of the CERN accelerator complex, whose main subcomponents
as of 2018 are summarised in Figure [add]. The purpose of this section
is to outline the sequence of steps followed to obtain the high energy
proton bunches that are used for high-energy collisions at the LHC.


![CERN Accerator Complex
](gfx/102_chapter_2/CERN-accelerator-complex.pdf){
#fig:CERN_Acc_complex width=70%}


The process begins with the extractions a low-energy beam of protons by
filling a duoplasmatron device
[@wolf2017handbook] with
gas from a hydrogen $\textrm{H}_2$ bottle. Those protons are then injected
into to a linear accelerator, named LINAC2, which boosts them to an energy
of 50 MeV. The next step of acceleration occurs at the Proton Synchrotron
Booster (PSB), which receives beams splitted from the
LINAC2 beam line and increases their energy to 1.4 GeV using four
superimposed synchroton rings. Promply after, the Proton Synchrotron (PS) 
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
of the proton bunches, additional 392 quadrupole magnets are
placed around the ring. Higher-order multipoles are also interleaved
to provide finer corections of the beam directio and field geometry.
Additonal energy to the protons is provided in each revolution
using 8 radio frequency (RF) cavities per beam line, until the
protons reach the desired energy (6.5 TeV during the Run II of the
LHC, lasting between 2015-2018). Given that each cavity can
provide about 60 keV per revolution, it takes about 20 minutes
of *ramp* time to reach collision energies.

During the whole acceration proces, specialised dipole magnets
are used to kept the beams separated at the four interactions points
(IPs) and thus avoid collisions. With the purpose of maximising
the interaction rates, the beams are made more compact (commonly
referred as *squeezed*) right before switching to collision mode. Once
the characteristics of the proton beam are suitable, the quadrupoles
align the beam trayectories and *physiscs* collisions can begin. A stable
configuration is then adopted by the LHC machine, providing about 7 keV 
of energy to the beam to account for synchroton radiation losses using
the RF cavities. If not unexpected problems occur, the proton beams are kept
circling the LHC ring and colliding at the IPs for several hours until
the bunch properties are degraded beyond correction,
a period that typically is referred a LHC *fill*. The *fill* is
finalised when some problem ocurrs on when all the proton bunches
are *dumped* (made collide) against graphite absorbers tangent
to the beam pipe.
 
### LHC Collisions and Detectors




## The Compact Muon Solenoid Detector

## CMS Data Pipelines




