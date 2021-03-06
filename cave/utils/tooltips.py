def get_tooltip(header):
    tooltips = {
        "Meta Data": """
Meta data, i.e. number of instances and parameters as well as configuration budget.
Statistics apply to the best run, if multiple configurator runs are compared.""",

        "Best configuration": """
Comparing parameters of default and incumbent.
Parameters that differ from default to incumbent are presented first.""",

        "Performance Analysis": """
Contains different ways of analyzing
the final incumbent and the performance of
the algorithm's default parameter
configuration.""",

        "Performance Table": """
*CAVE* uses three kinds of scores: PAR1, PAR10 and number of timeouts. PAR
stands for Penalized Average Runtime. This is applicable on scenarios that
optimize runtimes with a cutoff. Since it is not clear how long the algorithm
would have run without the cutoff (or whether it would have terminated at all),
the cutoff is multiplied by a factor. PAR1 does not penalize (multiplicator of
1), while PAR10 penalizes with factor 10.

If there are multiple runs on the same configuration-instance pair (with
different seeds), some resulting in timeouts and some not, the majority decides here.

The resulting difference of default and incumbent is tested for significance
using a paired permutation test with 10000 iterations
and tests against the null-hypothesis that the mean
of performance between default and incumbent is equal.""",

        "Scatterplot": """
Scatter plots show the costs of the default and
optimized parameter
configuration on each instance. Since this
looses detailed information about the individual
cost on each instance by looking at aggregated cost
values in tables, scatter plots provide a more
detailed picture. They provide insights whether
overall performance improvements can be explained
only by some outliers or whether they are due to
improvements on the entire instance set. On the
left side the training-data is scattered, on the
right side the test-data is scattered.""",

        "empirical Cumulative Distribution Function (eCDF)": """
Depicts cost distributions over the set of instances.
Since these are empirical distributions,
the plots show step functions. These plots provide insights into
how well configurations perform up to a certain threshold. For
runtime scenarios this shows the probability of solving all
instances from the set in a given timeframe. On the
left side the training-data is scattered, on the
right side the test-data is scattered.""",

        "Algorithm Footprints": """
The instance features are projected into a
two/three dimensional space using principal
component analysis (PCA) and the footprint
of each algorithm is plotted, i.e., on which
instances the default or the optimized
configuration performs well. In contrast
to the other analysis methods in this
section, these plots allow insights into
which of the two configurations performs
well on specific types or clusters of
instances. Inspired by Smith-Miles.""",

        "Default 3d": """
Projection of feature space into three dimensions, different viewpoints for
enhanced explanation.""",

        "Incumbent 3d": """
Projection of feature space into three dimensions,
different viewpoints for enhanced explanation.""",

        "Configurator's behavior": """
Analysis of the trajectory and the
runhistory returned by a configurator
to gain insights into how the configurator
tried to find a well-performing
configuration.""",

        "Configurator Footprint": """
Analysis of the iteratively sampled configurations during the optimization procedure.
Multi-dimensional scaling (MDS) is used to reduce dimensionality of the
search space and plot the distribution of evaluated configurations. The larger the
dot, the more often the configuration was evaluated on instances from the set.
Configurations that were incumbents at least once during optimization are marked as red squares.
Configurations acquired through local search are marked with a 'x'.
The downward triangle denotes the final incumbent, whereas the orange upward triangle
denotes the default configuration.
The heatmap and the colorbar correspond to the predicted performance
in that part of the search space.""",

        "Cost over time": """
Depicts the average cost of the best so far
found configuration (using all trajectory data)
over the time spent by the configurator
(including target algorithm runs and the overhead
generated by the configurator)
If the curve flattens out early, it indicates that
too much time was spent for the configurator run;
whereas a curve that is still improving at the
end of the budget indicates that one should
increase the configuration budget. The plotted standard
deviation gives the uncertainty over multiple configurator
runs.""",

        "Parallel Coordinates": """
Previously used by Golovin et al.
to study the frequency of chosen parameter
settings in black-box-optimization.
Each line corresponds to one configuration in
the runhistory and shows the
parameter settings and the corresponding
(estimated) average cost. To
handle large configuration spaces with
hundreds of parameters,
the (at most) 10 most important parameters
based on a fANOVA parameter
importance analysis are plotted.
To emphasize better
configurations, the performance is encoded
in the color of each line,
ranging from blue to red. These plots provide
insights into whether the configurator
focused on specific parameter values and
how these correlate to their costs.""",

        "Parameter Importance": """
Parameter Importance analysis to determine
which of the parameters most influence the
analysed algorithms performance.""",

        "fANOVA": """
fANOVA (functional analysis of variance) computes the
fraction of the variance in the cost space explained by
changing a parameter by marginalizing over
all other parameters, for each parameter (or for pairs
of parameters). Parameters with high importance scores
will have a large impact on the performance.
To this end, a random forest is trained as
an empirical performance model on the
available empirical data from the available runhistories.""",

        "Forward Selection": """"
Forward Selection is a generic method to
obtain a subset of parameters to achieve the
same prediction error as with the
full parameter set.
Each parameter is scored by how much the
out-of-bag-error of an empirical
performance model based on a random
forest is decreased.""",

        "Ablation": """
Ablation Analysis is a method to determine parameter
importance by comparing two parameter configurations,
typically the default and the optimized configuration.
It uses a greedy forward search to determine the order
of flipping the parameter settings from default
configuration to incumbent such that in each step
the cost is maximally decreased.""",

        "Local Parameter Importance (LPI)": """
Using an empirical performance model, performance changes of a
configuration along each parameter are calculated. To quantify
the importance of a parameter value, the variance of
all cost values by changing that parameter are predicted and then
the fraction of all variances is computed. This analysis is
inspired by the human behaviour to look for improvements in the
neighborhood of individual parameters of a configuration.""",

        "Feature Analysis": """
Analysis of the instance features to gain
insights into the instance set that
was used during the optimization.""",

        "Violin and Box Plots": """
Box and Violin Plots show the distribution
of each feature value across the instances.
Box plots show the quantiles of
the distribution and violin plots show the
approximated probability density of the
feature values. Such plots are useful to
inspect the instances and to detect
characteristics of the instances. For
example, if the distributions have two or
more modes, it could indicate that the
instance set is heterogeneous which could
cause problems in combination
with racing strategies configurators
typically use. NaN values
are removed from the data.""",

        "Feature Importance": """
Reduction of the out-of-the-bag root
mean squared error of the random
forest empirical performance model
by applying forward selection on the set of
instance features. Using this method, we can
identify a set of instance features that
suffices to obtain prediction accuracy
comparable to using the full set of
features.""",

        "Correlation": """
Correlation of features based on the Pearson
product-moment correlation. Since instance
features are used to train an empirical
performance model in model-based
configurators, it can
be important to remove correlated features in a
pre-processing step
depending on the machine-learning algorithm.
Darker fields
corresponds to a larger correlation
between the features.""",

        "Clustering": """
Clustering instances in 2d; the color encodes the
cluster assigned to each cluster. Similar to ISAC, we
use a k-means to cluster the instances in the feature
space. As pre-processing, we use standard scaling and
a PCA to 2 dimensions. To guess the number of
clusters, we use the silhouette score on the
range of 2 to 12 in the number of clusters""",
                }

    if header in tooltips:
        return tooltips[header]
    else:
        return False
