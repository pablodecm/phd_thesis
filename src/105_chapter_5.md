
# Search for Anomalous Higgs Pair Production with CMS {#sec:higgs_pair}

\epigraph{All Life
  is Problem Solving.}{Karl Popper}

In this chapter, the concepts and techniques from the previous sections are
applied in the search for non-resonant production of Higgs boson pairs,
using data from proton-proton collisions at a centre-of-mass energy of 13 TeV
collected in 2016 by the CMS detector at the LHC, 
corresponding to a total integrated luminosity of $35.9\ \textrm{fb}^{-1}$.
The most probably decay channel for the Higgs boson pairs, where
each Higgs boson leads to a a $\textrm{b}\bar{\textrm{b}}$, is considered.
While the aforementioned final state is the most frequent by a considerably
margin, a large background of similar events is expected from
multi-jet QCD processes, which motivates the use of machine learning techniques
to construct a summary statistic that can exploit the fine differences
between signal and background for statistical inference. In fact, the
expected background is so copious that insufficient simulated observations can
be generated to obtain the required level of modelling accuracy, thus
we have to resort to the development of a new data-driven background estimation
technique referred to as hemisphere mixing [@DeCastroManzano:2017yqy].
In addition to setting upper limits of the standard model (SM) production
of Higgs boson pairs,
the data analysis framework is also used to set upper limits in
the context of effective field (EFT) theories of anomalous
couplings, that parametrise possible deviations from the SM. The
main results presented in this section have been carry out within
the CMS Collaboration, and have been made public and published [@Sirunyan:2018tki].

## Introduction

After the discovery of the Higgs boson (H) in 2012 with the LHC experiments
[@higgs2012cms; @higgs2012atlas; @Chatrchyan:2013lba], a detailed
study of its properties has become an important topic in fundamental
physics. The experimental determinations of its couplings and rates
of production by the CMS and ATLAS
collaborations [@Aad:2015zhl; @Khachatryan:2016vau], including
the recent observations of the associated production of the Higgs
boson with a
$\textrm{t}\bar{\textrm{t}}$ quark pair [@Sirunyan:2018hoz; @Aaboud:2018urx],
are found to be compatible with the standard model (SM) theoretical
predictions. That said, several predicted properties remain unmeasured
because the difficulty of their experimental determination, the Higgs boson
self-coupling being one of the most relevant parameters
because it can modified by physics beyond the standard 
model (BSM) [@Dib:2005re; @Grober:2010yv;
@Contino:2012xk; @Dolan:2012ac; @Dawson:2015oha] .

A principled way to determine the Higgs self-coupling, and thus reconstruct
the scalar potential of the Higgs field that is responsible for spontaneous
symmetry breaking, is to measure the production of Higgs boson pairs (HH)
[@Baglio:2012np]. The SM prediction for the inclusive HH production
cross section for 13 TeV proton-proton collisions, assuming
a $m_\textrm{H}=125.09\ \textrm{GeV}$ [@Aad:2015zhl; @Sirunyan:2017exp],
can be theoretically
calculated [@deFlorian:2016spz; @deFlorian:2013jea;
@Dawson:1998py; @Borowka:2016ehy; @deFlorian:2015moa] obtaining:
$$
\sigma(pp \rightarrow HH + jets) = 33.49^{+4.3\%}_{-6.0\%} (\textrm{scale})
\pm 2.3\% (\alpha_S) \pm 2.1\% (\textrm{PDF})\ \textrm{fb}
$$ {#eq:higgs_pair_xs}
where the sources
of uncertainties listed correspond to factorisation $\mu_\textrm{R}$ and
renormalisation $\mu_\textrm{F}$ scales, uncertainties in the
strong coupling constant $\alpha_S$ and as well as the uncertainty
associated with the parton distribution functions (PDF) respectively. The
predicted cross section of the HH production process
in the SM is very small,
several orders or magnitude smaller those of single Higgs production,
and thus has not been directly observed the LHC data yet and will likely
require a dedicated studies at the HL-LHC or other future colliders.
New physics effects beyond the SM can enhance the HH production
total and differential cross sections, e.g. as can be modelled by effective
theories of anomalous couplings [@Carvalho:2016rys], in a way so
HH production could be observed with the data
already collected at the LHC.
 
The search of possible beyond the enhancements of HH production motivated
early searches using $\sqrt{s} = 8\ \textrm{TeV}$ LHC data
[@Aad:2015uka; @Sirunyan:2017tqo], as well
as several analyses using data collected during 2015 and 2016 at
the LHC experiments, including
the one presented in this work. Several
analysis looking for an resonant enhancement of HH production, leading
to a peak in the reconstructed invariant mass of the Higgs pair due to
decay of hypothetical mediating particle, have also been performed
while that type of HH production is not considered in this analysis.
Regarding non-resonant
production of HH pairs at at $\sqrt{s} = 13\ \textrm{TeV}$,
both ATLAS and CMS collaborations have carried out searches for different
decay channels including
$\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$ [@Aaboud:2018knk],
$\textrm{b}\bar{\textrm{b}}\textrm{l} \nu\textrm{l} \nu$ [@Sirunyan:2017guj],
$\textrm{b}\bar{\textrm{b}} \tau \tau$ [@Sirunyan:2017djm] and
$\textrm{b}\bar{\textrm{b}} \gamma \gamma$ [@Sirunyan:2018iwt]. In all
the mentioned analysis, one of the Higgs bosons decays to a
$\textrm{b}\bar{\textrm{b}}$ quark pair, which its the most likely
decay (with a branching fraction of 57.7\% for
$m_\textrm{H}=125\ \textrm{GeV}$ Higgs boson), in order
to consider a large fraction of expected HH events. The CMS Collaboration
has also carried out an analysis complementary to the one presented
in this report, where one of the $\textrm{b}\bar{\textrm{b}}$ is
highly boosted and thus reconstructed a single large-area jet
[@Sirunyan:2018qca]. The most stringent expected upper limit on the
SM HH production cross section to date, about 19 times the SM
prediction, corresponds to the CMS
$\textrm{b}\bar{\textrm{b}} \gamma \gamma$
channel search [@Sirunyan:2017djm], which yielded an observed upper
limit of 22 times the SM. The ATLAS
$\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$ channel 
search has a similar experimental reach [@Aaboud:2018knk], studying the
same final
state considered in this analysis, however with a different methodology
regarding their summary statistic and background estimation.


A detailed description of the main characteristics and results
of an analysis searching for
HH production using CMS experiment data, with both Higgs
bosons decaying into $\textrm{b}\bar{\textrm{b}}$ quark pairs,
is included in this chapter. The data considered was acquired 
by the CMS detector during the year 2016, corresponding to
an integrated luminosity of $35.9\ \textrm{fb}^{-1}$. In the final
state considered, each of the four $\textrm{b}$ quark results in a
distinct reconstructed jet. While it is the most likely
decay mode for the Higgs pair, a much larger quantity of similar events with
four and more jets are expected from hard quantum chromodynamics (QCD)
interactions. The differences between signal and background are used to
increase the sensitivity by using as a summary statistic the prediction
of a multivariate probabilistic classifier.
Because the expected contribution from the QCD multi-jet
processes is so abundant, it could
not be modelled with the required precision with the available simulations,
and a method for carrying out a fully data-driven background estimation
was developed,
and is described in [Section @sec:bkg_est].

## Higgs Pair Production and Anomalous Couplings {#sec:higgs_pair_prod}

At proton-proton colliders, the main production mechanism for a Higgs
pair is *gluon fusion*. Even at leading order, the interaction includes
a fermion loop as depicted in the top diagrams of
[Figure @fig:HH_feynman_diagrams], explaining the low expected
production rate listed in [Equation @eq:higgs_pair_xs],
which is largely dominated by the contribution from
top and bottom quarks.
The most common production mode, labelled as (b) in
[Figure @fig:HH_feynman_diagrams], features a triangular fermion loop
followed by the production of an off-self Higgs boson, that in turn
decays on two on-shell Higgs bosons via a triple Higgs boson interaction
vertex. In addition, is also possible within the SM at leading order
to produce a pair of Higgs bosons through a fermion box loop diagram,
as shown in diagram (a) of [Figure @fig:HH_feynman_diagrams], which
evidently does not depend on the Higgs self-coupling. Both
box and triangle loop contributions destructively interfere in the SM
to give rise to the total HH production amplitude.


![Set of HH production Feynman diagrams, representing
all gluon-gluon fusion at leading order. The interactions
depicted by (a) and (b) represent processes that are
expected within the SM, while the contact interactions between
the Higgs bosons and gluons (c) and (d), as well the contact interaction
of two Higgs bosons with top quarks (e),
are effective diagrams of BSM interactions.
](gfx/105_chapter_5/HH_feynman_diagrams.pdf){
#fig:HH_feynman_diagrams width=100%}

New physics at higher energy scales can affect processes and
observables at the electroweak scale, such as Higgs pair production.
As reviewed
in [Section @sec:possible_ext], the effective field theory (EFT) approach
is a way to calculate observables of possible extensions of the SM
without being tied to a certain class of BSM model, by adding
non-renormalisable local interactions. In the context of Higgs
pair production, the effect of new operators can be parametrised
by the following effective Lagrangian: 
$$
\begin{aligned}
\mathcal{L}_\textrm{H} = 
\frac{1}{2} \partial_{\mu}\, \textrm{H} \, \partial^{\mu} \textrm{H} -
\frac{1}{2} m_\textrm{H}^2 \textrm{H}^2 -
{\color{red} \kappa_\lambda} \,  \lambda_\textrm{SM} v\, \textrm{H}^3 \\
- \frac{m_\textrm{t}}{v}(v+ {\color{red}\kappa_\textrm{t}} \,  \textrm{H} +
 \frac{{\color{red}c_2}}{v} \textrm{HH} ) \,( \bar{\textrm{t}}_\textrm{L} \textrm{t}_\textrm{R} + \textrm{h.c.}) \\ 
+ \frac{1}{4} \frac{\alpha_\textrm{S}}{3 \pi v} ( {\color{red}c_\textrm{g}} \, \textrm{H} -
 \frac{ {\color{red}c_\textrm{2g}}}{2 v} \,  \textrm{HH}) \,  G^{\mu \nu}G_{\mu\nu}\,
\end{aligned}
$$ {#eq:eft_lag}

where $v=246\ \textrm{GeV}$ is the vacuum expectation value of the
Higgs field. After neglecting the enhanced coupling of the Higgs boson
with bottom quarks due its experimental constraints and the presence
of new light particles,
a total of five EFT parameters remain, which are
highlighted by red colour in [Equation @eq:eft_lag]. The factors
$\kappa_\lambda = \lambda_\textrm{HHH}/\lambda_\textrm{SM}$ and
$\kappa_\textrm{t}= y_\textrm{t}/y_\textrm{SM}$ account for possible
deviations from the SM of the Higgs boson trilinear coupling and the
top quark Yukawa coupling, thus effectively
modifying the relative weight of the SM Feynman diagrams described
at the beginning of the section. The absolute parameters $c_g$, $c_2g$
and $c_2$ instead lead to new contact interactions not expected
within the SM, represented in the (c), (d) and (e) Feynman diagrams
of [Figure @fig:HH_feynman_diagrams], and which could arise by mediation of heavy particles
beyond the electroweak scale.
The previous parametrisation is commonly referred to as
dimension-six non-linear or anomalous couplings EFT,
however alternative approaches exist,
such as the linear EFT which is more appropriate to
model smaller BSM effects [@Falkowski:2001958].

A theoretical prediction for the differential and total cross section
for each point in the mentioned five-dimensional EFT parameter space
$(\kappa_\lambda, \kappa_\textrm{t}, c_2, c_\textrm{g}, c_\textrm{2g})$
can be computed as outlined in [Section @sec:pheno]. The distribution
of the final state kinematical variables, i.e. the relative angle and
momenta of the Higgs pair, can depend substantially on the value of some
of these couplings. A naive grid or random scan of the
full five-dimensional space would require simulated samples
of observations at too many EFT points and hence it is not
feasible. While this signal modelling issue could be tackled by means of
event re-weighting, as described in [Section @sec:re-weighting], it is
useful to consider a efficient methodology to represent the main
properties of the anomalous couplings parameter space where only a reduced
number of EFT points are considered.

For the analysis presented in this work, a total of twelve EFT 
points referred to as *benchmarks* are considered, which have
been chosen via a agglomerative 
clustering procedure so they represent the main kinematical
typologies in the parameter space. The details of the
clustering methodology are detailed in [@Carvalho:2015ttv], but they
amount to the construction of a distance between the main kinematic
distributions at generator level of each pair of EFT. The parameters
corresponding to each of the benchmarks, as well as those corresponding to
the SM model and the case where Higgs boson self coupling is zero,
are included in \autoref{table:benchmarks}.

\begin{table}[htbp]
\caption{Effective field theory parameters for the anomalous couplings
benchmarks considered in this analysis, as defined in \cite{Carvalho:2015ttv},
as well as the modified couplings corresponding to the standard model.}
 \centering
 \begin{tabular}{l c c c c c }
\hline
Benchmark point & $\kappa_\lambda$ &
$\kappa_\textrm{t}$ & $c_2$ & $c_\textrm{g}$ & $c_\textrm{2g}$ \\
\hline
1 & 7.5 & 1.0 & -1.0 & 0.0 & 0.0 \\
2  & 1.0 & 1.0 & 0.5 & -0.8 & 0.6\\ 
3 & 1.0 & 1.0 & -1.5 & 0.0 & -0.8\\ 
4 & -3.5 & 1.5 & -3.0 & 0.0 & 0.0\\ 
5  & 1.0 & 1.0 & 0.0 & 0.8 & -1.0\\ 
6  & 2.4 & 1.0 & 0.0 & 0.2 & -0.2\\ 
7 & 5.0 & 1.0 & 0.0 & 0.2 & -0.2\\ 
8 & 15.0 & 1.0 & 0.0 & -1.0 & 1.0\\ 
9 & 1.0 & 1.0 & 1.0 & -0.6 & 0.6  \\ 
10 & 10.0 & 1.5 & -1.0 & 0.0 & 0.0\\ 
11  & 2.4 & 1.0 & 0.0 & 1.0 & -1.0\\ 
12 & 15.0 & 1.0 & 1.0 & 0.0 & 0.0 \\ 
Box & 0.0 & 1.0 & 0.0 & 0.0 & 0.0 \\
\hline
SM & 1.0 & 1.0 & 0.0 & 0.0 & 0.0 \\
\hline
\end{tabular}
\label{table:benchmarks}
\end{table}

## Analysis Strategy {#sec:analisis_strategy}

The goal of this analysis is to carry out statistical inference on
the occurrence of
$\textrm{pp} \rightarrow \textrm{HH}\rightarrow
\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$, as predicted by the
SM or in BSM effective field theory extensions, based on experimental data
acquired by the CMS detector on 2016. The type of statistical
inference applicable to a search is hypothesis testing, as introduced in
[Section @sec:hypo_test]. In principle, we would like to test whether
the null hypothesis $H_0$ corresponding to the SM without HH production
hypothesis can be rejected. If the previous $H_0$ hypothesis cannot be
rejected, which is
expected given the previous experimental results, the objective
instead becomes setting exclusion upper limits on the signal
cross section for a given model including Higgs pair production,
thus considering as the null
hypothesis $H_0$ the SM and BSM models of HH production considered.
In either case, we would like adapt an analysis strategy
that maximises the sensitivity to the presence of HH production, which
amounts to minimising the Type II error rate for a given fixed Type I error
rate in statistical terms.

The event selection in this analysis will include some custom online requirements,
which were set at trigger level to reduce the total rate of data collection
while keeping a large fraction of events relevant for this analysis,
as well as an offline selection to reduce the contribution
of background processes that are not well modelled and simplify the
construction of powerful summary statistics. The online trigger requirements
as well as the characteristics of the datasets considered in this analysis
are described in [Section @sec:online_and_datasets], while the event
selection adopted is included in detail in [Section @sec:event_selection].

After a basic event selection, mainly comprising the filtering of
events with four or more b-tagged
jets, a subset including four of the reconstructed jets within each event is
paired to construct two *di-jet candidates*, as an attempt to recover
the kinematic properties of the intermediate Higgs boson particles, including
their reconstructed masses. 
The information from the two di-jet candidates can in turn be combined
to compute variables that can approximate the features of the Higgs
pair system, which are also quite useful for inference. A set of variables
from the selected jets, the H candidates and the HH system, are combined in
a single discriminating variable obtained by training a probabilistic
classification machine learning model, specifically one based on boosted decision
trees, to separate signal from background, in a analogous manner to what
was described in [Section @sec:sig_vs_bkg].

The statistical inference in this analysis is based on constructing
a binned likelihood of the expected distribution of the classifier
output for events originated from signal and background processes
in comparison with the observed data, which also accounts for the
effect of nuisance parameters as discussed in
[Section @sec:synthetic_likelihood]. While both the SM and the
various BSM signal models can be modelled using simulated observations,
the main background of the analysis, multi-jet QCD production, is hard
to model by simulation. Thus a data-driven background estimation method,
described in detail in [Section @sec:bkg_est],
is used both for training the probabilistic classifier and for modelling
the background contribution in the binned likelihood.

After including the effect of the relevant sources of systematic
uncertainty, which are listed in [Section @sec:syst_unc],
expected and observed upper limits are obtained for
the $\textrm{pp} \rightarrow \textrm{HH}\rightarrow
\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$ cross section for each
of the benchmarks listed in \autoref{table:benchmarks}, as well as for the
SM HH production process. The results, which are contained in
[Section @sec:results], are include the upper limit on the mentioned
cross section a function of the Higgs self-coupling factor parameter
$\kappa_\lambda$ when $\kappa_\textrm{t}=1$ and the other EFT
parameters are null. While the analysis could be redone for
any arbitrary EFT point by recomputing the limits
for the particular model, the results can also be more
easily reinterpreted by assuming the limit obtained for
the closest benchmark.

## Trigger and Datasets {#sec:online_and_datasets}

The experimental data considered in this analysis was collected by
the CMS detector in 2016 from proton-proton collisions at
centre-of-mass energy $\sqrt{s} = 13\ \textrm{TeV}$. The total integrated
luminosity at the CMS interaction point corresponding to the certified set
of datasets used in this analysis is $35.9\ \textrm{fb}^{-1}$, i.e.
including only a the subset of
data corresponding to periods when the relevant detecting systems were
running regularly and no problematic anomalies were discovered.

Because the rates for the main background of
this analysis, events originating from QCD multi-jet events,
are expected to be much higher that those of the signal,
an efficient online trigger selection is essential
for maximising the sensitivity of the analysis. While standard trigger
paths that select events with several high-energy jets are available
in CMS, a more practical strategy is to include some b-tagging
requirements within the high-level trigger sequence. Hence, this
analysis re-uses the multi-jet trigger paths that were developed for
the resonant $\textrm{pp} \rightarrow \textrm{X} \rightarrow \textrm{HH} \rightarrow
\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$ [@Sirunyan:2018zkk], where $X$
is a heavy mediating particle, both requiring that at least three jets
have are b-tagged by the online version of the Combined Secondary
Vertex (CSV) algorithm [@Sirunyan:2017ezt].

The full specification trigger selection used is rather complex, but
is represented by a logical OR of the 
following two HLT trigger paths that were in place
during the CMS 2016 data taking period:

  - HLT_DoubleJet90_Double30_TripleBTagCSV_p087
  - HLT_QuadJet45_TripleBTagCSV_p087 

which represent a particular online selection sequence at the HLT, which is
preceded by a given set of L1 trigger seeds, as conceptually reviewed in
[Section @sec:trigger]. The L1 trigger paths depend on each of the paths,
but are logical OR between several conditions requiring a certain number
of L1 jets over a given energy or the total deposited energy on the
calorimeter $H_T$ to be over a certain threshold. At the HLT, both paths
require some quality criteria on the primary vertex reconstructed 
and at least 4 reconstructed jets within a pseudo-rapidity range
defined by $|\eta| < 2.6$. The first path requires the momenta of two
of the reconstructed jets $p_T>90\ \textrm{GeV}$, while for other two
$p_T>30\ \textrm{GeV}$. The second path instead requires at least
four reconstructed jets with $p_T>45\ \textrm{GeV}$. As mentioned,
both paths include a b-tagging requirement, mainly that the value
of the online CSV discriminator is larger than a working point of 0.87,
for three of the eight most energetic reconstructed jets in the event.

Samples of simulated observations from Higgs pair production are
simulated using MadGraph5_aMC@NLO [@Alwall:2014hca] at leading-order,
following the relevant prescriptions, including the loop
factor on an event-by-event basis detailed in [@Hespel:2014sla]. A total
of 300000 events have been simulated for the SM model production component,
as well as an older version of the clustering benchmarks discussed
in [Section @sec:higgs_pair_prod]
and the $\kappa_\lambda=0$ box model. Regading the parton
distribution function used for generation, the NNPDF30\_LO\_AS\_0130\_NF\_4 n 
set [@Ball:2014uwa] was used for all samples.

The samples for the benchmark samples listed in \autoref{table:benchmarks},
or any other EFT point for that matter, can be generated from the
previous samples by means of generator re-weighting. As described in
[Section @sec:re-weighting], the latent variables of the simulator can
be used to model a different sample by computing observables after
assigning to each event a weight proportional to the ratio between
probability density functions. In this case, at parton level at leading
order, the effect of varying EFT parameters in [Equation @eq:eft_lag]
can be fully characterised by two
variables: the Higgs pair invariant mass $m_\textrm{HH}$ and the
$\lvert \cos \theta^{*} \rvert$, where $\theta^{*}$ is the polar angle of any
one of the Higgs bosons with the respect to the beam axis. Once this
two variables are specified, the rest of the simulation does not
depend on the EFT parameters, this a set of HH production
simulated events generated for a given vector of EFT parameters
$\boldsymbol{\theta}_\textrm{EFT}=(\kappa_\lambda, \kappa_\textrm{t}, c_2, c_\textrm{g}, c_\textrm{2g})$
re-weighted by:
$$
w \left ( m_\textrm{HH}, \lvert \cos \theta^{*} \rvert \right ) =
\frac{p \left ( m_\textrm{HH}, \lvert \cos \theta^{*} \rvert  \ \mid \ {\boldsymbol{\theta}'}_\textrm{EFT} \right )}{
p(m_\textrm{HH}, \lvert \cos \theta^{*} \rvert \ \mid \ {\boldsymbol{\theta}}_\textrm{EFT})}
$$ {#eq:eft_weight}
to model events generated at the EFT point ${\boldsymbol{\theta}'}_\textrm{EFT}$,
as long as the both the numerator and denominator are not zero. The previous
concept can be extend to any arbitrary probability distribution
of $p \left ( m_\textrm{HH}, \lvert \cos \theta^{*} \rvert \right )$, e.g. a large
sample uniformly distributed in the mentioned 2D-space could be re-weighted
to model any EFT parameter point. While the density ratio in [Equation @eq:eft_weight]
can also be estimated exactly as the ratio between the matrix elements [@Wertz:2632195],
a non-parametric density estimation approach was adopted in this analysis.

A large sample of HH production events was formed by concatenating
all non-resonant Higgs pair events simulated from each of the 14 samples,
creating what will be referred to as the *pangea* sample. For all the EFT
points of interest, 50000 events (300000 for the SM production) 
were generated at parton level, which is rather inexpensive. The per-event
weight in [Equation @eq:eft_weight] is estimated by the ratio of 2D-histograms,
which effectively approximate the mentioned density ratio. The
*weighted pangea* sample can represent any EFT parameter point at leading order
by this procedure, so it is used to model the signal characteristics of
all the models considered in this work.


## Event Selection {#sec:event_selection}

Given the the final state studied in this analysis is characterised
by the presence of four highly energetic b quarks, the physics objects
of relevance  are reconstructed jets. The details of the reconstruction
procedure at CMS were already discussed in [Section @sec:event_reco].
Advanced jet flavour tagging, in particular b-tagging, is also essential
to distinguish jets that originate from b quarks from those originating
from lighter quarks and gluons, and thus very useful to reduce
the contribution from a large number of QCD multi-jet processes.

The subset of collected events that pass the trigger requirements,
as well as all the simulated observations, as listed at the beginning
of [Section @sec:online_and_datasets] undergo a process of
event reconstruction, producing a representation of the detector
readout that attempt to recover the latent particle features
at parton level, as discussed in [Section @sec:event_reco_stat].
The fist step of the offline event selection
is to consider for each event the set of reconstructed particle-flow
jets with $p_T > 30\ \textrm{GeV}$ and $\lvert \eta \rvert < 2.4$. An event
is only selected if four or more jet passing those requirement are found.

After filtering out jets with lower energy or out of the inner tracker
acceptance, at least four of the remaining jets are required to be
b-tagged to consider the event in the final selection. The medium
working point of the CMVA discriminator [@Sirunyan:2017ezt], defined
as the value of the discriminator for which the expected mis-identification
of light quarks and gluons is 1\% is used as b-tagging criteria. The object
selection efficiency for jets originating from the b quarks produced in
the decay of the Higgs boson pairs has been estimated from simulated
samples to be around 65\%. The absolute and relative selection efficiencies
of the trigger and offline selection ,
and the total number of expected events per $\textrm{fb}^{-1}$,
for the SM HH production process are included in \autoref{tab:sigEff},
as estimated from the simulated observations.

\begin{table}[htb]
 \caption{Event selection efficiency and number of events expected per
 each integrated $\textrm{fb}^{-1}$ of integrated luminosity for the standard model
 $\textrm{pp}\rightarrow \textrm{HH}
 \rightarrow \textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$
 production process, as estimated from using simulated observations.}
\centering
 \small
\begin{tabular}{r l l  c c}
  \hline
                             & Produced  & Trigger & $\geq 4 \ \textrm{b}$tags \\
  \hline
   N events / fb     & 11.4     & 3.9   & 0.22 \\
   Relative eff.              &          & 34\%  & 5.6\% \\
   Efficiency                 &          & 34\%  & 1.9\% \\
  \hline
 \end{tabular}    
 \label{tab:sigEff}
\end{table}

The goal of the previous selection is to reduce the contribution from
QCD multi-jet processes and to isolate the set of signal events where
all the jets from the Higgs pair decays can be fully reconstructed.
After such selection, the most often occurring value for
number of jet in the selected subset of events is five. The four
jets with highest CMVA discriminant are chosen as candidates for being
the decay products of the Higgs bosons. In order to reconstruct
features of the Higgs boson candidates, a pairing between the selected
jets has to be defined. The pairing used in this analysis is rather
simple, the invariant masses for the two Higgs candidates $M_{\textrm{H}_1}$
and $M_{\textrm{H}_2}$ are computed for the three possible combinations
of the four jets picked, and the invariant mass difference
${\Delta M}_{(\textrm{H}_1,\textrm{H}_2)}$ is computed
for each combination:
$$
{\Delta M}_{(\textrm{H}_1,\textrm{H}_2)} = \lvert M_{\textrm{H}_1} - M_{\textrm{H}_2} \rvert
$$ {#eq:inv_mass_pair}
so the combination with the smallest mass difference is taken. Alternative
decay candidates selection and pairing techniques were considered and tested,
but the fact that these procedure does not explicitly use the mass of the
Higgs boson, made it very effective to avoid conditioning also the
distributions of the background processes. The aforementioned procedure
correctly pairs the jets to form Higgs candidates for approximately 54\%
of the events. To distinguish between the two Higgs candidates during the
rest of this repost, leading Higgs $\textrm{H}_1$ will referred to the
reconstructed Higgs
candidates with the largest invariant mass while trailing Higgs $\textrm{H}_1$
to the other candidate.

In this analysis, the final summary statistic considered for inference
is based on the output of classifier that discriminates signal and background
observations, which will approximate the likelihood ratio or a
sufficient summary statistic if the signal and background components are fully
specified, as discussed in [Section @sec:sig_vs_bkg]. The machine learning
classification technique used is based on gradient boosted decision trees (BDT),
a technique that was summarised in [Section @sec:boosted_decision_trees]. The
implementation from the XGBOOST software library [@chen2016xgboost] was used
to train a probabilistic classifier using a simulated samples corresponding
to SM Higgs pair production (i.e. 60\% of the weighted pangea observations) and
background observation resulting from the data-driven procedure which will
be described in [Section @sec:bkg_est].

The set of features, or input variables, feed to the probabilistic classifier
are listed in \autoref{tab:mvaVars}, including both high-level and
low-level summaries. The set of variables are divided in three subgroups,
the first corresponding to variables related with the properties
of the reconstructed Higgs pair HH system, including it invariant
mass $M_\textrm{HH}$, its total transverse momenta
$p_T^{\textrm{H}_1 \textrm{H}_2}$ and
$\cos \theta_{\textrm{H}_1 \textrm{H}_2 -\textrm{H}_1}^{\star}$, where
$\theta_{\textrm{H}_1 \textrm{H}_2 -\textrm{H}_1}^{\star}$ is the angle
between the HH system and the leading Higgs boson candidate. Another feature
that is found to increase the discrimination power of the classifier
is the $M_\textrm{X}$ variables, defined as:
$$
M_\textrm{X} = M_\textrm{HH}
- \left ( M_{\textrm{H}_1} -  M_\textrm{H} \right )
- \left ( M_{\textrm{H}_2} -  M_\textrm{H} \right )
$$ {#eq:mx_classifier}
where $M_\textrm{H}=125\ \textrm{GeV}$ is the Higgs boson mass. The second
group of features includes variables associated individually with each
Higgs boson candidate, such as the reconstructed mass of each paired
di-jet system $M_{\textrm{H}_1}$ and $M_{\textrm{H}_2}$. The reconstructed
Higgs candidate masses have the largest discrimination power, because
its marginal distributions are expected to peak
around $M_\textrm{H}=125\ \textrm{GeV}$ for the subset of well-paired signal
events while more spread for background observations. Other features in
this sub-group include the tranverse momenta of the reconstructed
Higgs candidates $p_T^{\textrm{H}_1}$ and $p_T^{\textrm{H}_2}$,
the angular distances between their component jets
$\Delta R_{jj}^{\textrm{H}_1}$, $\Delta R_{jj}^{\textrm{H}_2}$,
$\Delta \phi_{jj}^{\textrm{H}_1}$, $\Delta \phi_{jj}^{\textrm{H}_2}$,
and $\cos \theta_{\textrm{H}_1 \textrm{H}_2 -\textrm{H}_1}^{\star}$,
where $\theta_{\textrm{H}_1 \textrm{H}_2 -\textrm{H}_1}^{\star}$ is the
angle between the leading Higgs boson candidate and the leading jet.
The last group includes variables directly associated to the reconstructed
jets, including the transverse momenta $p_{T_j}^{(i=1-4)}$ and
pseudo-rapidity $\eta_{T_j}^{(i=1-4)}$
of the first four jets, ordered by their value of the CMVA b-tagging
discriminant as well as the scalar sum of their transverse momenta $H_T$.
Finally, the scalar $p_T$ sum of all the jets that not used for the
reconstruction of the Higgs pair system $H_T^{\textrm{rest}}$ and the b-tagging CMVA
discriminant value for the third and fourth jet 
$\textrm{CMVA}_3$, $\textrm{CMVA}_4$ are also used.

\begin{table}[htbp]
 \caption{List of reconstruction-based features used as input of the
 probabilistic classifier.}
 \centering
 \begin{tabular}{l l l}
   \hline
   HH system     &  H candidates      & Jet variables \\
   \hline
   $M_\textrm{X}$, $M_\textrm{HH}$, &
   $M_{\textrm{H}_1}$, $M_{\textrm{H}_2}$  &
   $p_{T_j}^{(i=1-4)}$, $\eta_{T_j}^{(i=1-4)}$,  \\
   $p_T^{\textrm{H}_1 \textrm{H}_2}$        &
   $p_T^{\textrm{H}_1}$, $p_T^{\textrm{H}_2}$ &
   $H_T^{\textrm{rest}}$, $H_T$ \\
   $\cos \theta_{\textrm{H}_1 \textrm{H}_2 -\textrm{H}_1}^{\star}$ &
   $\cos \theta_{\textrm{H}_1 -j_1}^{\star}$ & 
   $\textrm{CMVA}_3$, $\textrm{CMVA}_4$, \\
   &
   $\Delta R_{jj}^{\textrm{H}_1}$, $\Delta R_{jj}^{\textrm{H}_2}$,
   $\Delta \phi_{jj}^{\textrm{H}_1}$, $\Delta \phi_{jj}^{\textrm{H}_2}$ & \\
   \hline
 \end{tabular}
 \label{tab:mvaVars}
\end{table}

The trained classifier combines the 25 variables from \autoref{tab:mvaVars}
in a single scalar value, that approximates the conditional probability
of belonging to the signal conditional on the input $p(y = 1| \boldsymbol{x})$,
which depends on the relative frequencies of signal and background
observation in the training dataset, as discussed in [Section @sec:supervised].
The hyper-parameters have been chosen based on a simple grid search, with
the help of the scikit-learn software library [@pedregosa2011scikit], based
on the area under the curve (AUC) of the resulting classifiers on
a validation hold-out dataset.

## Data-Driven Background Estimation {#sec:bkg_est}

The principal background of this analysis are events with several jets coming
from multiple quarks and gluon production from QCD processes. While simulated
observations of multi-jet QCD processes can be generated, and were in fact
readily available at the time this analysis was carried out,
they are in practice
not useful to realistically model the background contribution for the
purposes of this work. A set of large samples for inclusive QCD multi-jet
production were produced in the CMS simulation campaign, divided in various
consecutive range of total generator level scalar transverse momenta sum
$H_T^{\textrm{gen}}$. Leaving aside issues regarding the accuracy
of the modelling of high jet multiplicity event provided by current
leading order plus parton shower generators, the main obstacle for using
the simulated samples is that their equivalent luminosity in the
$H_T^{\textrm{gen}}$ relevant for this analysis is several orders of magnitude
smaller than the actual luminosity.

As a rule of thumb, to accurately model a mixture component using simulated
samples, the number of simulated events has to be at least 10 times more
than the number of expected events, or the modelling uncertainty due to
the limited simulation statistics will greatly degrade
subsequent inference. This problem is made worse when a significant fraction
of the simulated sample has to be used for training a probabilistic classifier
and thus cannot be used for modelling to avoid biased estimation of the
relevant expected values. A naive solution could be to simulate more events,
but given the large cross section of low energy QCD processes, the total
number of QCD inclusive simulated events required
would be well over 1 billion which is too many given the total simulation
budget available for the CMS experiment.

Another option, which was initially explored for modelling the
QCD background in this analysis, was to only simulate events that pass
a selection at parton level, e.g. with two or more high energy
b-quarks. This could provide a radical reduction on the total
computing time needed for simulation, specially
if combined with the approximate simulation techniques described
in [Section @sec:detector_simulation], because the associated cross section
can be greatly reduced. However, such generator level filtering is 
difficult to implement in a way that relevant events are not omitted
after the event selection, thus the desired level of modelling
accuracy was not achieved.

The previously mentioned reasons motivate using data directly
to estimate the background contribution, as discussed in
[Section @sec:data_driven]. Data-driven background estimation
can be notoriously difficult and often several assumptions
about the properties of the background have to be made. For example,
the ATLAS analysis with the same goal [@Aaboud:2018knk], models the background
contribution with an independent data sample characterised
by the same trigger and section but only two b-tagged reconstructed
jets, weighted by a factor that is also derived and validated
from a data side band where not significant signal is expected. While
that approach is proved effective when using the reconstructed
$M_\textrm{H}$ distribution for inference, it cannot be easily extended
when the output of a probabilistic classifier is used as the summary statistic. 

Consequently, a new data-driven background estimation method based
on the concept of hemisphere mixing and some assumptions of the phase
space characteristics of QCD multi-jet processes
was developed for this analysis [@DeCastroManzano:2017yqy]. The technique,
which is described in [Section @sec:hem_mixing],
directly attempts to create an artificial dataset using the the whole
original dataset as input, hence can be used both for training the
probabilistic classifier and to model the distribution of the
final summary statistic used for inference. Because some aspects of
the method are ad-hoc and cannot be formally demonstrated, it has been
calibrated and then validated using a signal-depleted control region,
procedure that is discussed in [Section @sec:syst_unc].


### Hemisphere Mixing {#sec:hem_mixing}

The basis of the data-driven background estimation method proposed is
to divide each event in two parts, referred to as hemispheres, so each
can be substituted by an hemisphere from a different event in order
to produce an artificial dataset. A graphical illustration of the
hemisphere mixing technique used in this work is provided in
[Figure @fig:hemisphere_mixing]. The transverse thrust axis, defined
as the axis in the $x-y$ plane for which the absolute value sum of the
projections of the transverse momenta of the selected
subset reconstructed jets is maximal, is used as a reference 
to divide each original event in two halves perpendicularly
to the mentioned axis. This procedure is carried out for
all the collected events that pass the selection described
in [Section @sec:event_selection], creating a dataset (or library)
of hemispheres with as many rows as double the number of
original events. Each half, or hemisphere, can be basically reduced
a set of reconstructed jets with their directions relative to
the trust axis. Once the hemisphere library has been created,
each hemisphere in the original event can be substituted
by a similar one by from the a different event, once
an appropriate distance metric has been defined, thus resulting
in a new artificial dataset.

![Schematic depiction of the hemisphere mixing background
estimation procedure. The red arrows represent b-tagged
jets and the blue arrows represent not b-tagged jets
in a event. The fist step includes finding the thrust axis in the $x-y$
plane, defined as that for the absolute value sum of the projections
of the transverse momenta $p_T$ of jets in the event is maximal. The event
is then divided in two hemispheres, each composed of a set of jets,
by the plane perpendicular to the thrust axis. All this hemispheres are
used to create a dataset (or library) of hemispheres. For each original
event, a artificial event can be created by substituting each original
hemisphere by some of the close neighbours, once a distance metric
for hemispheres has been defined.
](gfx/105_chapter_5/hemisphere_mixing.pdf){
#fig:hemisphere_mixing width=100%}

The hemisphere distance criteria is a function of the set of reconstructed
events contained, and is a combination of discrete and
continuous variables. The discrete requirement for matching original hemispheres
with those in the library is that they have the same number of jets $N_j^h$ and
b-tagged jets $N_b^h$, which ensures a similar jet multiplicity distributions
for the artificial data. The previous condition also avoid creating 
artificial events that do not pass the event selection, e.g. by combining
an hemisphere with 2 b-tagged jets with another one including only one
b-tagged jet, thus resulting in less that four b-tagged jets in the 
artificial combination. For infrequent jet and b-jet multiplicity categories,
the discrete condition is relaxed by considering a unique category
when four jets or b-jets are present in the hemisphere. In addition to
the mentioned categorisation, the following continuous distance metric
between the original hemisphere $\boldsymbol{h}_o$ and each hemisphere from
the library $\boldsymbol{h}_q$ is defined as a measure of similarly:
$$
\begin{aligned}
d(\boldsymbol{h}_o,\boldsymbol{h}_q)^2 =
\frac{ \left ( M_\textrm{t}(\boldsymbol{h}_o) - M_\textrm{t}(\boldsymbol{h}_q) \right )^2}{
\textrm{Var}(M_\textrm{t})} +
\frac{ \left ( T(\boldsymbol{h}_o) - T(\boldsymbol{h}_q) \right )^2}{
\textrm{Var}(T)} \\ +
\frac{ \left ( T_a(\boldsymbol{h}_o) - T_a(\boldsymbol{h}_q) \right )^2}{
\textrm{Var}(T_a)} +
\frac{ \left ( P_z(\boldsymbol{h}_o) - P_z(\boldsymbol{h}_q) \right )^2}{
\textrm{Var}(P_z)}
\end{aligned}
$$ {#eq:hem_metric}
where $M_\textrm{t}(\boldsymbol{h})$ is the invariant mass of the system composed of all
the jets contained in the hemisphere, $T(\boldsymbol{h})$ is the scalar
sum of all the transverse momenta projection of the all jets of an hemisphere to the thrust
axis,  $T_a(\boldsymbol{h})$ is instead the scalar sum of the
transverse momenta projections over a axis orthogonal to the thrust
axis, and $P_z(\boldsymbol{h})$ is the absolute value of the
projection of the vectorial sum
of the jet momenta along the beam axis. The denominators in
[Equation @eq:hem_metric] are the variance for each of the variables
and discrete category, as estimated directly from the library of hemispheres,
in order to reduce the effect of the scale of magnitude of each component
to the distance metric.

The substitute for each original hemisphere is found by finding
the $k^\textrm{th}$ nearest-neighbour hemisphere in the library. The
closest hemisphere ($k=0$), corresponding to zero distance,
would be the very same original hemisphere which is present in the library.
Therefore, it makes sense to consider to consider substituting the
hemisphere witht the $k\geq 1$ nearest neighbour. Assuming forward-backward
symmetry in the $z$ direction and $\phi$ rotational symmetries, and given
that the distance metric $d(\boldsymbol{h}_o,\boldsymbol{h}_q)^2$ does
not depend on the sign and absolute magnitude of those quantities,
all the jets in the hemisphere can be rotated in $\phi$ or their
$p_z$ sign to match the original hemisphere properties. It is possible to
considering different $k$ neighbours for each hemisphere, obtaining a different
artificial dataset in each case. Each of this artificial datasets can be labelled
by a tuple $(k_1, k_2)$, where $k_1$ is neighbour used as the substitute
for the original hemisphere corresponding to a $\Delta \phi >0$ with respect
to the thrust vector rotated $\pi/2$ clock-wise, and $k_2$ to the
neighbour substituting the other original hemisphere. Consequently, if up to
$k_\textrm{max}$ neighbours are considered for each hemispheres, a
total of $k_\textrm{max}^2$ artificial datasets, each with the same
size than the original dataset, could be composed by considering all
the permutations.

The previous technique can be understood taking unto account the QCD
multi-jet production at leading-order basically amounts to a $2 \rightarrow 2$
parton scattering process, which is then affected by other phenomena
such as QCD radiation,
pileup or multiple interactions. By breaking the event in two hemispheres
using the transverse thrust, the aim is to separate the outcome of the
processes associated with each of the two final state partons in
the mentioned $2 \rightarrow 2$ approximation. The hemisphere
distance metric is attempts to preserve the main properties of the
event, while avoiding strong correlations between jets in the two
hemispheres. The goal of the hemisphere mixing procedure is then
to obtain an artificial sample where the contributions signal in
the original dataset are effectively removed. This has been tested
by injecting up to 100 times the expected SM contributions of
simulated HH production events to a dataset of simulated
QCD multi-jet events. The distributions of the various variables
after hemisphere mixing are compatible with the QCD multi-jet
component, which is the majority component and not affected by the
presence of signal.

The hemisphere mixing technique is applied to the data events
passing the selection described in [Section @sec:event_selection].
Artificial datasets up to $k_\textrm{max}=10$ have been
considered, and they are sub-divided in three sets used for training
the probabilistic classifier (training), 
validating and optimised the classifier (validation)
and to estimate the background distribution of the final summary
statistic (application). The last dataset is referred to as
application instead of test set because its purpose is not to obtain
unbiased estimates of the classifier performance but unbiased estimates
of the classifier output distribution of background events. All the
artificial datasets are not independent, e.g. the $(1,1)$ and $(1,2)$
dataset use the same first hemisphere, thus some careful choices are required
when splitting the mixed datasets. The dataset splitting considered in
this analysis, using the $(k_1, k_2)$ notation described before, correspond
to:

  - *training set*: concatenation of $(1,1)$, $(1,2)$, $(2,1)$ and $(2,2)$ mixed datasets
  - *validation set*: concatenation of $(3,4)$, $(5,6)$, $(7,8)$ and $(9,10)$ mixed datasets
  - *application set*: concatenation of $(4,3)$, $(6,5)$, $(8,7)$ and $(10,9)$ mixed datasets

noting that the observation in the training set are not fully independent,
but it is expected that reusing hemispheres in the training sample at most
might degrade slightly the classifier performance, but does not bias in any way
the inference results if an independent set is used. The next section
is devoted to the validation of the background model in data control regions
and the development of a methodology to correct for possible biases
in the final summary statistic expectations. For completion, a comparison
of the distribution of relevant variables, that are used as input
to the probabilistic classifier, between
the QCD multi-jet simulations available and
those estimated using hemisphere mixing are shown in [Figure @fig:Figure_003].
The overall agreement is good, yet the statistical uncertainties
coming from the low $H_T$ range simulated QCD samples is large, as discussed
as the beginning of this section.


::: {#fig:Figure_003 .subfigures}
![first jet transverse momenta $p_{T_j}^1$
](gfx/105_chapter_5/Figure_003-a.pdf){#fig:Figure_003_a width=49%}
![first jet pseudo-rapidity $\eta_{j}^1$
](gfx/105_chapter_5/Figure_003-b.pdf){#fig:Figure_003_b width=49%}
\
![Higgs candidate transverse momenta $p_{T}^{\textrm{H}_1}$
](gfx/105_chapter_5/Figure_003-c.pdf){#fig:Figure_003_c width=49%}
![Higgs candidate pair system mass $M_\textrm{HH}$
](gfx/105_chapter_5/Figure_003-d.pdf){#fig:Figure_003_d width=49%}

Comparison between the background model obtained with the hemisphere
mixing technique and the simulated observations from QCD processes
for a set of relevant reconstructed variables. A correction factor
obtained from the binned classifier distribution, as described
in [Section @sec:bkg_validation], has been applied as a weight to the mixed
dataset. Only statistical uncertainties are shown.
:::

\FloatBarrier

### Background Validation {#sec:bkg_validation}

One of the drawbacks of using data-driven methods, is that they are often
based on a series of implicit assumptions regarding the underlying statistical
model of the data, which are difficult to demonstrate directly. Therefore,
a more practical approach to verify the validity of a given background model
is usually taken, studying its validity in a set of data control region
where the component under study dominates and the contribution from
the signal is negligible. For studying the hemisphere mixing method
in this analysis, two data control regions (CRs) are defined:

- *mass control region* ($M_\textrm{H}$ CR): using the same selection described
  in in [Section @sec:event_selection], but removing all events around the
  Higgs candidate masses $90 < M_{\textrm{H}_1} < 150\ \textrm{GeV}$ and
  $80 < M_{\textrm{H}_1} < 140\ \textrm{GeV}$. This cut in the reconstructed
  Higgs masses plane considerably reduces the signal contribution, which
  is expected to peak around $M_\textrm{H} = 125\ \textrm{GeV}$.
  
- *b-tag control region* (b-tag CR): b-tagged jets are defined using
  the loose working point of CMVA, which has a misidentification rate of 10\%
  and a b-tagging efficiency around 85\% for jets originating from the Higgs pair
  decay, while filtering out events with any event with medium working
  point CMVA b-tagged jets.

The relative signal contribution in each of these control regions is
greatly reduced, and the multi-jet QCD component is the dominant
background. While for carrying out the mass control region comparison
is enough to apply an additional cut over the selection, the b-tag
control region study requires redoing the hemisphere mixing procedure
on the new set of event with different b-tag jet selection. For both
control regions, all the relevant one-dimensional marginal distributions
are found to be in good agreement, as shown for a reduced
number of important variables that used as input for the classifier
in [Figure @fig:Figure_004] and [Figure @fig:Figure_005].

::: {#fig:Figure_004 .subfigures}
![first jet transverse momenta $p_{T_j}^1$
](gfx/105_chapter_5/Figure_004-a.pdf){#fig:Figure_004_a width=49%}
![first jet pseudo-rapidity $\eta_{j}^1$
](gfx/105_chapter_5/Figure_004-b.pdf){#fig:Figure_004_b width=49%}
\
![first Higgs candidate - first jet $\cos \theta^{*}_{\textrm{H}_1 - j_1}$
](gfx/105_chapter_5/Figure_004-c.pdf){#fig:Figure_004_c width=49%}
![lowest CMVA discriminator $\textrm{CMVA}_4$
](gfx/105_chapter_5/Figure_004-d.pdf){#fig:Figure_004_d width=49%}

Comparison between the background model obtained with the hemisphere
mixing technique and the data for the $M_\textrm{H}$c control region for
a set of reconstructed variables used as input of the classifier.
A correction factor
obtained from the binned classifier distribution, as described
in [Section @sec:bkg_validation], has been applied as a weight to the mixed
dataset. Only statistical uncertainties are shown.
:::


::: {#fig:Figure_005 .subfigures}
![first jet transverse momenta $p_{T_j}^1$
](gfx/105_chapter_5/Figure_005-a.pdf){#fig:Figure_005_a width=49%}
![first jet pseudo-rapidity $\eta_{j}^1$
](gfx/105_chapter_5/Figure_005-b.pdf){#fig:Figure_005_b width=49%}
\
![first Higgs candidate mass $M_{\textrm{H}_1}$
](gfx/105_chapter_5/Figure_005-c.pdf){#fig:Figure_005_c width=49%}
![second Higgs candidate mass $M_{\textrm{H}_2}$
](gfx/105_chapter_5/Figure_005-d.pdf){#fig:Figure_005_d width=49%}

Comparison between the background model obtained with the hemisphere
mixing technique and the data for the b-tag control region for
a set of reconstructed variables used as input of the classifier.
A correction factor
obtained from the binned classifier distribution, as described
in [Section @sec:bkg_validation], has been applied as a weight to the mixed
dataset. Only statistical uncertainties are shown.
:::

While each single variable is well-modelled, the goal of the technique
is obtain an adequate modelling accuracy in the higher dimensional
space considered as input of the probabilistic classifier. A way to check
the quality of such modelling is to compare the classifier output
distribution for the control region data with the background model. This
comparison is shown for the $M_\textrm{H}$ control region in
[Figure @fig:Figure_006]. The same comparison is not straightforward
to carry out for the b-tag control region, because the classifier was
trained using the lowest value of the CMVA classifiers, which was lower
bounded by the medium working point for the standard selection which
instead is upper bounded by same working point in the b-tag CR.
While [Figure @fig:Figure_006] shows an reasonable agreement overall,
a slight background model excess seems to exist in the lower classifier
output range.


![Left: Comparison of the BDT classifier output for data in the
$M_\textrm{H}$c control region, with the same output computed
using an artificial dataset by hemisphere mixing. Right: bin-by-bin
differences between the control region data and the hemisphere
mixing estimation, divided by their uncertainty, both before (top right)
and after the bias correction procedure. The pull distributions and its
parameters when fitted by a Gaussian are also shown. The uncertainty
after the bias correction has been increased conservatively in order
to obtain a unitary standard deviation for the residual pull distribution.
](gfx/105_chapter_5/Figure_006.pdf){
#fig:Figure_006 width=100%}


The previous mentioned issue has motivated a quantitative
study to assess and potentially
correct the hemisphere mixing based background model for the classifier output.
The bias assessment procedure, schematically depicted in [Figure @fig:Figure_011],
starts by constructing a very large artificial sample $M$
by concatenating all the permutations of the
$(k_1,k_2)$ datasets up to a $k_\textrm{max}=10$,
except those used for training the classifier. A total of 200 smaller datasets,
referred as replicas $M_i$,
with the same number of events than the original data are obtained by
subsampling without replacement $N$ times from the large mixed dataset $M$.
Each replica dataset is treated as in an analogous manner to
the original dataset, thus the
hemisphere mixing is applied again to create a set of new
artificial datasets $R_i$. The classifier output distribution is obtained
for all the new artificial datasets $R_i$ and compared with the reference
distribution of the large sample $M$, considering a histogram with 80 bins
of equal width in the full range of the classifier output $[0.0,1.0]$.

The median difference between
the distribution of the classifier output between the large dataset $M$
and each of the mixed replicas $R_i$ is shown in [Figure @fig:Figure_012]
for the final event selection. A small bias is found in the recovered
distribution, which is directly used as a correction to hemisphere mixing
technique prediction. Similar results are obtained in the
previously mentioned control region. The effect of the correction
in the $M_\textrm{H}$ check and pull distribution is also shown in
[Figure @fig:Figure_006]. The mean of the predicted values mius
the observed values are compatible with zero in both control regions,
while the root-mean-squared of the pull distribution is not compatible
with one in the $M_\textrm{H}$. The uncertainty on the background shape
per each bin is conservatively
enlarged until the standard deviation of the pull distribution
becomes one.

![Diagram describing the procedure used to estimate the background bias correction.
All possible combinations of mixed hemispheres except those used for training are
added together to create a large sample $N$ of $96N$ events from which we repeatedly
subsample without replacement 200 replicas $M_i$ of $N$ events. The hemisphere
mixing procedure is then carried out again for each of this replicas to produce
a set of re-mixed data replicas $R_i$.
The trained multivariate classifier trained is then evaluated over all the events
of $M$ and each $R_i$ and the histograms of the classifier output are
compared to obtain a the differences for each of the replicas.
The median difference is taken as bias correction.](gfx/105_chapter_5/Figure_011.pdf){
#fig:Figure_011 width=100%}


![Bias estimation by resampling, in relative units of the statistical
uncertainty of the predicted background, used to
correct the background estimation. The median (red line)
and the upper and lower one s.d. quantiles (green lines) have been computed
from 200 subsamples of the re-mixed data comparing the predicted background
$n^p_b$ with the observed $n^o_b$. The variability due to the limited number of
subsamples is estimated by bootstrap and it is shown for each estimation using
a coloured shadow around the quantile estimation.
The light yellow shadow represents the uncertainty
due to the limited statistics of the reference observed sample.
The separation between the one s.d. quantiles is compatible with the
expected variance if the estimation was Poisson or Gaussian distributed.](gfx/105_chapter_5/Figure_012.pdf){
#fig:Figure_012 width=100%}

\FloatBarrier

## Systematic Uncertainties {#sec:syst_unc}

## Results {#sec:results}