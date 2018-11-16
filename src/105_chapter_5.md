
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
cross section for 13 TeV proton-proton collisions can be theoretically
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
 


## Anomalous Couplings Extensions


## Trigger and Datasets


## Analysis Strategy

## Event Selection

## Data-Driven Background Estimation

## Systematic Uncertainties

## Results