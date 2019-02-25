
# Abstract {.unnumbered}

Advances in data analysis techniques may play a decisive role in the
discovery reach of particle collider experiments. However,
the importing of expertise and methods from other data-centric
disciplines such as machine learning and statistics
faces significant hurdles, mainly due to the established use of different
language
and constructs.
A large part of this document, also conceived as an introduction
to the description of an analysis searching for non-resonant
Higgs pair production in data collected by the CMS detector
at the Large Hadron Collider (LHC), is therefore devoted to a
broad redefinition of the relevant
concepts for problems in experimental particle physics.
The aim is to better connect these issues
with those in other fields of research, so the
solutions found can be repurposed.

The formal exploration of
the properties of the statistical models at particle colliders
is useful to highlight the main challenges posed by statistical
inference in this context: the multi-dimensional nature
of the models, which can be studied only in a generative
manner
via forward simulation of observations, and the
effect of nuisance parameters. The first issue
can be tackled with likelihood-free inference methods coupled
with the use of low-dimensional summary statistics, which may
be constructed either with machine learning techniques or through
physically motivated variables (e.g. event reconstruction).
The second, i.e. the misspecification
of the generative model which is addressed by
the inclusion of nuisance
parameters, reduces the effectiveness of summary statistics
constructed with machine-learning techniques.

A subset of the data analysis techniques formally discussed
in the introductory part of the document are also exploited
to study the non-resonant production process
$\textrm{pp} \rightarrow \textrm{HH} \rightarrow
\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}}$
at the LHC in the context of the Standard Model (SM)
and its extensions in effective fields theories (EFT),
based on anomalous couplings of the Higgs field. Data collected in 2016
by the CMS detector and corresponding to a total
of $35.9\ \textrm{fb}^{-1}$ of proton-proton collisions are
used to set an 95\% confidence upper limit at $847\ \textrm{fb}$
on the production cross section
$\sigma \left( \textrm{pp} \rightarrow \textrm{HH} \rightarrow
\textrm{b}\bar{\textrm{b}}\textrm{b}\bar{\textrm{b}} \right )$
in the SM. Upper limits
are also obtained for the cross sections corresponding
to a representative set of points of the parameter space of EFT.
The combination of those results with the ones obtained
from the study of other decay channels of HH pairs is also discussed. 

In addition, the exercise of reformulating the goals of high
energy physics analysis as a statistical inference problem is combined with
modern machine learning technologies to develop a new technique,
referred to as inference-aware neural optimisation.
The technique produces
summary statistics which directly minimise the expected uncertainty on
the parameters of interest, optimally accounting for the effect of nuisance
parameters.
The application of this technique to a synthetic problem demonstrates that
the obtained summary statistics are considerable more effective than those
obtained with standard supervised learning methods, when the effect of
the nuisance parameters is significant.
Assuming its scalability to LHC data scenarios, this technique
has ground-breaking potential for analyses dominated by systematic uncertainties.
