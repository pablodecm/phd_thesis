# Introduction {.unnumbered}

\epigraph{Every new beginning comes from some other beginning's end.}{Seneca the Younger}

Humans strive for understanding the world by seeking explanations
to the varied natural phenomena happening around them,
and accumulating the resulting knowledge in models that
can be used to predict and shape the future reality.
The scientific method provides a formal framework for carrying out these
investigations and checking the validity of the current description of
our environment. Recorded experience of assumed known origin,
also known as data, has a central role in updating these explicative
theories, because it can provide quantitative or qualitative
support to some candidate explanations over others.

Direct sensory perception and personal information processing has a
limited investigative reach and it is easily affected by subjective
conditions. Well understood and calibrated instruments of
measurement can be used instead for data acquisition, in controlled
settings referred to as scientific experiments, so that
quantifiability and precision are enhanced. The same
applies to theoretical modelling and experimental data analysis, where robust
mathematical and computational procedures empower researchers
to construct more accurate
descriptions of the world we live in. These establish a
strong coupling between technology and science, by which technical
and conceptual innovations allow the development of better tools,
which in turn lead to more scientific knowledge.

The universe is filled with an abundance of
interesting situations occurring at very
different time and space scales, so curious observers might
face a difficult choice when deciding what to focus their scientific
attention on. Nevertheless, there seems to be a complexity hierarchy
whereby larger physical systems are composed by simpler parts, and
the properties of the former can be explained by means of those of the latter.
Hence, a worthy path of exploration can
start with the study of the most fundamental components of nature and
their dynamics. At our current level of understanding,
we can reason this would be a quest motivated solely by curiosity, pushed
by our desire of making sense of the structure of reality, and not
a pragmatic proxy for the development of technological applications.
That will be our motivation to delve into experimental particle
physics, a discipline dealing with the practical study of the
most elementary constituents of matter and their interactions.

It is important to remark that the elementary quality of the chosen subject
of study does not
imply that the journey towards valuable scientific knowledge in this area
will be a simple one. On the contrary, as the following chapters
will make evident, this undertaking poses grand technical
and non-technical challenges which in many cases require novel solutions.
Furthermore, the problems at hand are often closely related with those
present in other research or technological fields, so their findings
and innovations can be repurposed. Oftentimes this can even be a
bidirectional relation, where the obstacles are challenging or
original enough that solutions have to go beyond the state of
the art in the relevant applied domain. In general, the pursuance of fundamental
explanations does require solutions to a multitude of practical problems.

Advances and expertise from other disciplines can accelerate
significantly the rate of progress in a fundamental research domain
such as experimental particle physics.
This is specially
relevant in areas such as data analysis,
where the infrastructure changes required in evolving environments are low.
Yet, some
barriers exist against the proliferation of interdisciplinarity, such as field
specific language (also known as jargon) and seemingly unclear
problem descriptions for collaborators with different backgrounds.
This document, in addition to presenting the main research
results of the projects I have been involved in the recent past,
will attempt to reduce this communication gap by trying to clearly
state the main
data analysis challenges we face in experimental particle physics in a way
they can be linked to other data-centric disciplines such as statistics
and machine learning.

The general methodology considered in this work consists on breaking the
main research goals in a series of applied problems, express them in a
domain-generic way, and understand what is their role in view of the
final aim. When possible, the presented concepts and methods will be
illustrated with simple use cases which can be a
great help to understand their working principles.
The mentioned perspective shift combined with the use of practical but
minimal examples has been really useful to identify possible shortcomings
on the way data analysis is carried out at the LHC, as well as to
develop new techniques
capable of addressing them. Nevertheless, I am of the opinion that the
projects mentioned and presented here are nothing but the first step
of what is possible; and the evolution of data analysis techniques
and tools could be a promising route for the advancement of our understanding
of basic building blocks of the universe.

This thesis is organised as follows.
[Chapter @sec:theory] provides
an overview of our current comprehension of the
properties and interactions of the fundamental constituents of nature,
followed by a summary of the limitations of our understanding
together with the main proposed testable alternative explanations.
The links between the mathematical description of our universe
and the computation of experimental observables will
be highlighted when describing the theoretical foundations.

The focus shifts in [Chapter @sec:experiment] towards how these
theories can be experimentally validated through scientific experiments. In
particular, the discussion verses around how the design and characteristics of
general purpose experiments at high-energy colliders are relevant for
the attainment of valuable data that yields new insights on the
fundamental properties of the cosmos. The Compact Muon Experiment (CMS)
detector at the Large Hadron Collider (LHC) serves as the default
example of such an instrument,
because it is the scientific experiment that provided
the academic context during my graduate (and late undergraduate)
years and the main driver
of some of the projects included in this report. Experimental modelling and
simulation will be emphasised in this chapter, due to their importance when
extracting knowledge from the acquired data.

Indeed, the problem of obtaining useful information from data is so involved
in modern scientific experiments that a standalone chapter will be centered
on statistical inference concepts and techniques. In fact, it could 
be argued that inference is the ultimate goal of particle
physics experiments, providing a key connection between
theory and experiment. In [Chapter @sec:statinf]
we review the problem at hand in particle colliders form
a formal statistical perspective as well
list the main approaches for making quantitative statements based
on data and their shortcomings. Two domain-specific aspects of data analysis
in high energy physics will be remarked: the generative-only characteristic
of accurate experimental models and the challenges of dealing with known unknowns
we are not interested in, commonly referred as nuisance parameters.

Advancements in computational power coupled with
extensive research effort at the intersection between computer science and
statistics during last decades have contributed
to the development of techniques that deal with the automatic
improvement of certain objective tasks given some data. An introduction to this
family of methods, generally referred to as machine learning techniques,
and a review of their
usefulness for tackling some common data analysis problem in experimental
particle physics, are included in [Chapter @sec:machine_learning]. Some
non-trivial connections between the use of those techniques and the
details of the underlying statistical issues will be stressed.

The first four chapters, as outlined above, offer a multi-disciplinary survey
of the theoretical and experimental
foundations of our understanding of nature and the relevant
techniques that allow the extract valuable information from the data.
In contrast,
[Chapter @sec:higgs_pair] presents a complete example of an analysis
at the LHC that applies those techniques to a real-world scenario.
Specifically, the use
case will be the search for evidence of anomalous non-resonant
Higgs boson pair production
using CMS data at the LHC, which can be a smoking gun pointing to alternative
explanations to the current theoretical comprehension of the fundamental
interactions and constituents of the universe.

The aforementioned example will be useful to epitomise the main statistical
and methodological challenges on the way LHC analyses are carried out. In
[Chaper @sec:inferno], we try to shed some light on these issues,
and demonstrate how a novel machine learning technique we have developed
can deal with one of the most relevant concerns:
learning summary statistics using inference-aware
losses that account for the effect of nuisance parameters. The limitations of
the proposed method as well as alternative solutions to increase the discovery
potential of the LHC will be explored.

This document will conclude with [Chapter @sec:conclusions], where
the main contributions and outcomes
of this work will be summarised
together with some ideas for future
extensions and improvements.

<!-- mention the prioritisation of ideas over technical details -->
