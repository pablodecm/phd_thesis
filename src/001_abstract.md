
# Abstract {.unnumbered}

Advances in data analysis techniques could play a decisive role on the
discovery reach of particle collider experiments, yet
expertise from other data-centric
disciplines such as machine learning and statistics
encounters significant
barriers, mainly due to the use of domain-specific language
and constructs.
A large part of this document, also serving as an introduction
for an analysis searching for non-resonant
Higgs pair production using data acquired by the CMS detector
at the LHC, is thus devoted to the redefinition of the relevant
concepts and problems in experimental particle physics in a way
they can be linked with those in other research fields, so
their findings can be repurposed.

The formal exploration of
the properties of the statistical models at particle colliders
is useful to highlight the main challenges when carrying out
inference: their multi-dimensional generative-only nature
and the effect of known unknowns. The first issue can
be linked with the notion of likelihood-free inference
and the role of low-dimensional summary statistics, that
can be constructed using machine learning techniques or using
physically motivated variables. The use of supervised
machine learning methods (and more generally event reconstruction) could
be understood as an approximate regression of
hidden variables of the generative model using simulated
observations.
The second concern, i.e. the misspecification
of the generative model that is addressed by the inclusion of nuisance
parameters,
reduces the usefulness of machine learning based summaries.

A subset of the data analysis techniques that were formally studied
in the introductory section are also exploited
to study the non-resonant
$\textrm{pp} \rightarrow \textrm{HH} \rightarrow
\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$
process at the LHC in the context of the SM
and its EFT extensions based on anomalous couplings. A total
of $35.9\ \textrm{fb}^{-1}$ of data
collected in 2016 by the CMS detector are used to set an observed 95\%
confidence upper limit of $847\ \textrm{fb}$ on the SM production cross section
$\sigma \left( \textrm{pp} \rightarrow \textrm{HH} \rightarrow
\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}} \right )$. Upper limits
are also obtained for a representative set of EFT points. The combination
of the results with other Higgs pair decay channels is also discussed.

In addition, some realisations from the exercise of rephrasing the goal of high
energy physics analysis as a statistical inference problem are combined with
modern machine learning technologies to develop a new technique.
The technique,
referred to as inference-aware neural optimisation, produces
summary statistics that directly minimise the expected uncertainty of
the parameters of interest, accounting for the effect of nuisance
parameters. Early results in a synthetic problem demonstrate that the summary
statistics obtained with this method are considerably more effective than
those obtained by supervised learning approaches when the effect
of nuisance parameters is significant. If it scales to real-world data scenarios
at the LHC, extensions of this technique could
be instrumental for analyses dominated by systematic uncertainties.

