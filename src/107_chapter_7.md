
# Conclusions and Prospects {#sec:conclusions}

\epigraph{So Long,\\ and Thanks for All the Fish.}{Douglas Adams}

A large part of this thesis has dealt with the role of statistical
learning techniques in the context of particle collider analyses,
and their usefulness from a statistical inference perspective. After a broad
introduction to the theoretical models of fundamental interactions and a summary of
the main characteristics and working principles of the Compact Muon Solenoid (CMS)
detector at the Large Hadron Collider (LHC), the fundamentals for statistical
modelling at the LHC been discussed. The relation between the
theoretical parameters of interest and the experimental observations
can only be modelled accurately by means of a complex simulation chain
of the underlying physical processes and expected detector response. The
generative-only nature of the simulation-based model combined with its
high-dimensionality make the definition of the probability density
or likelihood function intractable, thus classical inference techniques
cannot be applied to carry out statistical inference based on the
acquired observations.

The statistical model for particle colliders can be often described
by a mixture model, each component originating
due to a given type of physical process. The latent variable structure of
the generative model can be mapped to the different simulation
steps in the simulation: process type, parton-level four-momenta,
parton-shower outcome and detector readout. While the dimensionality
of the latent space of the latent structure greatly increases for each
subsequent step, the joint distribution can be factorised as
a produce off conditionals, the information about the parameters
of interest being compactly expressed by the lowest dimensional latent
variables. An efficient way to reduce the dimensionality of the data
is thus to approximate the latent variables using the observations. These
can be done by a well-calibrated combination of the different detector
readouts, as done when using event reconstruction techniques, or
by directly estimating the latent variables using supervised learning
techniques trained on simulated observations.

Recent advances in supervised learning techniques have led to more accurate
latent variable estimation that can scale to more data and use advance non-linear
transformations to obtain better performance in complex tasks,
both in the context of classification and regression. Signal versus background
probabilistic classification, a common conceptual framework
for simplifying the event selection
problem and constructing low-dimensional summaries in high-energy physics,
has been formally shown
to produce sufficient summary statistics for the mixture coefficients
when the generative model is fully defined. The usefulness of probabilistic
classification for such tasks, even in the optimal classifier case, cannot
be guaranteed when nuisance parameters affect significantly the distribution
of observed samples. In addition, particle identification and regression
problems that augment the reconstruction output and can tackled with machine
learning techniques are also discussed. The use of deep learning
techniques for advanced jet flavour tagging in CMS are used to exemplify
the previous use case, which demonstrates the possible performance improvements
due to the combined use of deep neural networks and non-standard input
transformations that can deal with sequences.
