
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
multijet QCD processes, which motivates the use of machine learning techniques
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


## Anomalous Couplings Extensions

$$
\begin{aligned}
\mathcal{L}_\textrm{H} = 
\frac{1}{2} \partial_{\mu}\, \textrm{H} \, \partial^{\mu} \textrm{H} -
\frac{1}{2} m_\textrm{H}^2 \textrm{H}^2 -
\kappa_\lambda \,  \lambda_\textrm{SM} v\, \textrm{H}^3 \\
- \frac{m_\textrm{t}}{v}(v+ {\kappa_\textrm{t}} \,  \textrm{H} +
 \frac{c_2}{v} \textrm{HH} ) \,( \bar{\textrm{t}}_\textrm{L} \textrm{t}_\textrm{R} + \textrm{h.c.}) \\ 
+ \frac{1}{4} \frac{\alpha_\textrm{S}}{3 \pi v} ( c_\textrm{g} \, \textrm{H} -
 \frac{ c_\textrm{2g}}{2 v} \,  \textrm{HH}) \,  G^{\mu \nu}G_{\mu\nu}\,
\end{aligned}
$$ {#eq:eft_lag}

![Set of HH production Feynman diagrams, representing
all gluon-gluon fusion at leading order. The interactions
depicted by (a) and (b) represent processes that are
expected within the SM, while the contact interactions between
the Higgs bosons and gluons (c) and (d), as well the contact interaction
of two Higgs bosons with top quarks (e),
are effective diagrams of BSM interactions.
](gfx/105_chapter_5/HH_feynman_diagrams.pdf){
#fig:HH_feyman_diagrams width=100%}



## Trigger and Datasets


## Analysis Strategy

## Event Selection

## Data-Driven Background Estimation {#sec:bkg_est}

## Systematic Uncertainties

## Results