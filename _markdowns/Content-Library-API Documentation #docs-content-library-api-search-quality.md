::: {._4-u3 ._588p}
We expect our methodology to measure search quality to evolve over time.
Here we outline a set of initial tests of search quality in the Meta
Content Library and API. The systems which underlie search are complex
and the data models as well as privacy rules which determine content
visibility evolve over time, meaning that quality regressions can occur.
Furthermore, as we develop the product, we welcome feedback about bugs
or unexpected behavior from the user community. See
[Appendix](#appendix) on this page for details on reporting issues.

### Methods

#### Initial test queries

We generated test search results for each endpoint (Facebook Pages,
groups, events, and posts, and Instagram business and creator accounts,
and posts) using a sample of 130 terms chosen to span a breadth of set
size (for example, obscure words such as *stopthesteal* and common words
such as *spray* ), polarization (for example, neutral words such as
*sugar* and socially charged words such as *transphobic* ), as well as
most queried keywords by researchers in Meta platforms. These initial
test queries consisted of single terms all in English without non-Latin
characters or any symbols (for example ', #, \$ or @). Additional query
parameters for each endpoint are listed in [Test search scope for
endpoints](#scope) . Test queries resulting in \> 100,000 results were
excluded from further analysis.

#### Validation data

Lists of expected entities for test queries were generated from
regex-based full-text searches on a SQL-like database backend. Tables in
this database are built from periodic snapshots of logged platform
content and thus are known to differ slightly from what is available in
Meta Content Library and API at search time due to time lags and
incomplete visibility filters. This dataset thus constitutes a secondary
validation channel rather than source of truth and regressions in
quality metrics may be a composite of both true indexing errors and/or
measurement noise. See [Caveats and known limitations](#caveats) .

### Recall

In principle, entities should be returned when (a) there is an exact
match with search term(s), (b) the content is eligible to be retrieved,
and (c) the total corpus of matching results does not exceed the
technical query limit of 100,000 results.

We measured recall as follows:

(entities returned) ∩ (entities expected) / (entities expected)

The following table shows the average of daily recall values across test
queries from November 8th, 2023 to November 15th, 2023.

::: _57-c
Endpoint
:::
:::

20th percentile recall

Median

Facebook Page

96%

98%

Facebook group

93%

96%

Facebook event

90%

93%

Facebook post

85%

92%

Instagram account

98%

99%

Instagram post

90%

94%

### Rank recall

Results which represent the *top N* results ordered by creation time or
views should also be complete. For Meta Content Library, which returns a
truncated list of ranked results, we generated a *ranked* version of
recall which is calculated as follows:

(top N entities) ∩ (top N expected entities) / (top N expected entities)

The following table shows the average of daily recall values for the top
1000 results ranked by creation time and view across test queries from
November 8th, 2023 to November 15th, 2023.

::: _57-c
Endpoint
:::

20th percentile ranked recall

Median ranked recall

Facebook post (ranked by creation time)

86%

92%

Instagram post (ranked by creation time)

64%

75%

Facebook post (ranked by view)

52%

63%

Instagram post (ranked by view)

62%

73%

### Precision

Only results which exactly match search terms should be returned,
excluding, for instance, partial index matches (broom → broomstick) or
fuzzy matches (broom → mop). Precision was measured as:

(returned entities matching query exactly) / (all returned entities)

The following table shows the range in average daily precision values
across test queries by endpoint from November 8th, 2023 to November
15th, 2023.

::: _57-c
Endpoint
:::

20th percentile precision

Median precision

Facebook Page

99%

99%

Facebook group

99%

99%

Facebook event

99%

99%

Facebook post

99%

99%

Instagram account

97%

98%

Instagram post

98%

99%

### Representativeness

In cases where incomplete results are returned (recall \< 100%), results
may be useful provided they are not overly biased (that is, they are
consistent with a random uniform sample of the complete results). We
measured representativeness using a series of statistical tests for bias
at the individual query level.

#### Query-level bias

For each test query we compared whether a summary statistic (mean, for
example) calculated using the results from the Meta Content Library API
reasonably approximated results obtained from the validation dataset
(which has high recall). Across several data dimensions including
engagement, exposure, and creator demographics, we performed a series of
t-tests comparing means derived from the Meta Content Library API to
means derived from the validation dataset. We then calculated the
percent of queries which lacked statistically significant evidence of
bias (p \> 0.05). Finally, we calculated the mean of metrics across all
dimensions.

We performed two versions of this test using methods which differed in
their level of sensitivity to small differences between Meta Content
Library API results and validation data. In the first version, we used a
Welch's T-test, which is appropriate for detecting major distributional
differences between datasets that might affect inference about
population-level traits. It is less sensitive to small differences
between datasets and we expect most appropriate for research use cases
involving trends and summaries.

The following table shows average daily percent of test queries
generating non-biased results using a Welch's T-test across endpoints
from November 8th, 2023 to November 15th, 2023.

::: _57-c
Endpoint
:::

Representativeness - Welch t-test

Facebook Page

96%

Facebook group

86%

Facebook event

78%

Facebook post

86%

Instagram account

97%

Instagram post

96%

In the second version of the query-level bias test we compared Meta
Content Library API and validation datasets using a pairwise t-test
(incorporating covariance between samples). This test is more powered to
detect differences between datasets and appropriate for assessing
whether small subsets of entities may be missing or over-represented.
For instance, this metric could highlight significant bias even with 98%
recall and a negligible difference in means, due to any imbalance in the
remaining data. Given known issues with the validation dataset failing
to exclude some ineligible entities based on visibility criteria, we
expect these measures to be more conservative and likely underestimates
of representativeness.

The following table shows percent of test queries generating non-biased
results using a paired t-test across endpoints from November 8th, 2023
to November 15th, 2023.

::: _57-c
Endpoint
:::

Representativeness - paired t-test

Facebook Page

80%

Facebook group

54%

Facebook event

41%

Facebook post

53%

Instagram account

74%

Instagram post

64%
