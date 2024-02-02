
Search quality - Content Library and API - Documentation - Meta for Developers










Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Search quality approach
=======================


This document describes Meta's approach to search quality for Meta Content Library and API.


Definitions
-----------


* **Entities** Objects in the social graph returned by Meta Content Library and Meta Content Library API which generate or contain content and are associated with a unique ID in internal systems. Includes Facebook Pages, groups, events and posts, as well as Instagram accounts and posts.
* **Content** Text and other data associated with entities, returned as fields in Meta Content Library and API.
* **Eligible / Visible** Entities or content permitted to be returned in Meta Content Library and API which meet privacy commitments and legal requirements. See Frequently asked questions for details.
* **Endpoint** Meta Content Library or API endpoint corresponding to a specific type of entity.


Search overview
---------------


Queries in Meta Content Library and API are powered by a version of Facebook’s search engine infrastructure, which relies on a combination of indexing and ranking to return relevant entities. The retrieval function combines matched and ranked IDs from a query using the same distributed memory caching layer which serves live platform content. This ensures that results represent the most current state of content on the platform and meet privacy-preserving visibility criteria (see Frequently asked questions for details).


As content is created or modified on Meta platforms, associated entities are registered to a search index built from individual words extracted from text fields as *tokens*. Tokenization generally isolates words separated by spaces or punctuation ( ?@$%^\*()+=~[{}];:"<>|. ), with some URL normalization and locale-specific adjustments for non-English languages. Tokenization is exact, in that it does not introduce additional word variants ("cats" will not be tokenized to "cat"). Direct mentions of users or other platform entities (via @) are not tokenized and are scrubbed from returned text fields, and are thus not searchable.


At query time, relevant content is identified by exact matching between tokens and individual search terms. Candidate matches are then subject to additional filtering via Boolean query logic (see Advanced search) and other selected filters. Matching is performed independently by word in a query, meaning that searching by phrase is not supported (queries “All for one” and “One for all” are equivalent).


Initial testing
---------------


We expect our methodology to measure search quality to evolve over time. Here we outline a set of initial tests of search quality in the Meta Content Library and API. The systems which underlie search are complex and the data models as well as privacy rules which determine content visibility evolve over time, meaning that quality regressions can occur. Furthermore, as we develop the product, we welcome feedback about bugs or unexpected behavior from the user community. See Appendix on this page for details on reporting issues.


### Methods


#### Initial test queries


We generated test search results for each endpoint (Facebook Pages, groups, events, and posts, and Instagram business and creator accounts, and posts) using a sample of 130 terms chosen to span a breadth of set size (for example, obscure words such as *stopthesteal* and common words such as *spray*), polarization (for example, neutral words such as *sugar* and socially charged words such as *transphobic*), as well as most queried keywords by researchers in Meta platforms. These initial test queries consisted of single terms all in English without non-Latin characters or any symbols (for example ‘, #, $ or @). Additional query parameters for each endpoint are listed in Test search scope for endpoints. Test queries resulting in > 100,000 results were excluded from further analysis.


#### Validation data


Lists of expected entities for test queries were generated from regex-based full-text searches on a SQL-like database backend. Tables in this database are built from periodic snapshots of logged platform content and thus are known to differ slightly from what is available in Meta Content Library and API at search time due to time lags and incomplete visibility filters. This dataset thus constitutes a secondary validation channel rather than source of truth and regressions in quality metrics may be a composite of both true indexing errors and/or measurement noise. See Caveats and known limitations.


### Recall


In principle, entities should be returned when (a) there is an exact match with search term(s), (b) the content is eligible to be retrieved, and (c) the total corpus of matching results does not exceed the technical query limit of 100,000 results.


We measured recall as follows:


(entities returned) ∩ (entities expected) / (entities expected)


The following table shows the average of daily recall values across test queries from November 8th, 2023 to November 15th, 2023.




 
 Endpoint
  | 
 20th percentile recall
  | 
 Median
  || Facebook Page | 96% | 98% |
| Facebook group | 93% | 96% |
| Facebook event | 90% | 93% |
| Facebook post | 85% | 92% |
| Instagram account | 98% | 99% |
| Instagram post | 90% | 94% |

### Rank recall


Results which represent the *top N* results ordered by creation time or views should also be complete. For Meta Content Library, which returns a truncated list of ranked results, we generated a *ranked* version of recall which is calculated as follows:


(top N entities) ∩ (top N expected entities) / (top N expected entities)


The following table shows the average of daily recall values for the top 1000 results ranked by creation time and view across test queries from November 8th, 2023 to November 15th, 2023.




 
 Endpoint
  | 
 20th percentile ranked recall
  | 
 Median ranked recall
  || Facebook post (ranked by creation time) | 86% | 92% |
| Instagram post (ranked by creation time) | 64% | 75% |
| Facebook post (ranked by view) | 52% | 63% |
| Instagram post (ranked by view) | 62% | 73% |

### Precision


Only results which exactly match search terms should be returned, excluding, for instance, partial index matches (broom → broomstick) or fuzzy matches (broom → mop). Precision was measured as:


(returned entities matching query exactly) / (all returned entities)


The following table shows the range in average daily precision values across test queries by endpoint from November 8th, 2023 to November 15th, 2023.




 
 Endpoint
  | 
 20th percentile precision
  | 
 Median precision
  || Facebook Page | 99% | 99% |
| Facebook group | 99% | 99% |
| Facebook event | 99% | 99% |
| Facebook post | 99% | 99% |
| Instagram account | 97% | 98% |
| Instagram post | 98% | 99% |

### Representativeness


In cases where incomplete results are returned (recall < 100%), results may be useful provided they are not overly biased (that is, they are consistent with a random uniform sample of the complete results). We measured representativeness using a series of statistical tests for bias at the individual query level.


#### Query-level bias


For each test query we compared whether a summary statistic (mean, for example) calculated using the results from the Meta Content Library API reasonably approximated results obtained from the validation dataset (which has high recall). Across several data dimensions including engagement, exposure, and creator demographics, we performed a series of t-tests comparing means derived from the Meta Content Library API to means derived from the validation dataset. We then calculated the percent of queries which lacked statistically significant evidence of bias (p > 0.05). Finally, we calculated the mean of metrics across all dimensions.


We performed two versions of this test using methods which differed in their level of sensitivity to small differences between Meta Content Library API results and validation data. In the first version, we used a Welch’s T-test, which is appropriate for detecting major distributional differences between datasets that might affect inference about population-level traits. It is less sensitive to small differences between datasets and we expect most appropriate for research use cases involving trends and summaries.


The following table shows average daily percent of test queries generating non-biased results using a Welch’s T-test across endpoints from November 8th, 2023 to November 15th, 2023.




 
 Endpoint
  | 
 Representativeness - Welch t-test
  || Facebook Page | 96% |
| Facebook group | 86% |
| Facebook event | 78% |
| Facebook post | 86% |
| Instagram account | 97% |
| Instagram post | 96% |

In the second version of the query-level bias test we compared Meta Content Library API and validation datasets using a pairwise t-test (incorporating covariance between samples). This test is more powered to detect differences between datasets and appropriate for assessing whether small subsets of entities may be missing or over-represented. For instance, this metric could highlight significant bias even with 98% recall and a negligible difference in means, due to any imbalance in the remaining data. Given known issues with the validation dataset failing to exclude some ineligible entities based on visibility criteria, we expect these measures to be more conservative and likely underestimates of representativeness.


The following table shows percent of test queries generating non-biased results using a paired t-test across endpoints from November 8th, 2023 to November 15th, 2023.




 
 Endpoint
  | 
 Representativeness - paired t-test
  || Facebook Page | 80% |
| Facebook group | 54% |
| Facebook event | 41% |
| Facebook post | 53% |
| Instagram account | 74% |
| Instagram post | 64% |

Search quality measurement expansion
------------------------------------


While in initial testing we focused on English to measure the search quality, in our expansion, we extended the exact same methodology to other languages and advanced search (search with logic operators AND, OR and NOT).


### Other languages


We used the same methodology to measure the search quality of the queries in Arabic, German and Hindi. These languages were selected based on the language features that the team believe are most likely to impact search quality. The features that the team considered are diacritics (such as accents), non-Roman characters, and right-to-left. We also wanted to cover at least one non-English European language.


Based on the analysis, we learned:


* The overall search quality of all the new languages is about the same level as English single keywords.
* The precision is over 95% for all endpoints in new languages.
* Since the search quality is reasonable for these languages, we expect to see very similar results for most other languages too.


The following table shows all metric values across test queries by language and endpoint from November 8th, 2023 to November 15th, 2023. Representativeness is an average across all dimensions that are mentioned in the representativeness section.




 
 Language
  | 
 Endpoint
  | 
 Recall
  | 
 Precision
  | 
 Representativeness - paired t-test
  | 
 Representativeness - Welch t-test 

  || Arabic | Facebook Page | 96% | 99% | 93% | 99% |
| Arabic | Facebook group | 92% | 99% | 41% | 61% |
| Arabic | Facebook event | 82% | 99% | 80% | 97% |
| Arabic | Facebook post | 91 | 99% | 70% | 94% |
| Arabic | Instagram account | 93% | 99% | 87% | 91% |
| Arabic | Instagram post | 80% | 99% | 85% | 97% |
| German | Facebook Page | 97% | 99% | 96% | 99% |
| German | Facebook group | 95% | 99% | 76% | 95% |
| German | Facebook event | 95% | 99% | 67% | 94% |
| German | Facebook post | 88 | 99% | 73% | 96% |
| German | Instagram account | 99% | 99% | 95% | 99% |
| German | Instagram post | 91% | 98% | 88% | 99% |
| Hindi | Facebook Page | 96% | 99% | 93% | 99% |
| Hindi | Facebook group | 96% | 99% | 39% | 61% |
| Hindi | Facebook event | 87% | 99% | 77% | 96% |
| Hindi | Facebook post | 92 | 99% | 71% | 95% |
| Hindi | Instagram account | 97% | 99% | 94% | 100% |
| Hindi | Instagram post | 73% | 99% | 80% | 96% |

We are also aware of a few limitations that our system has for other languages. The limitations are as follows:


* Meta Content Library API does not read any keywords with “ß” in German or semi-space (half-space) in Arabic.
* In Arabic, a word can be written with and without diacritics. Content Library API can only find the exact match for each form. Thus, if a researcher wants to find all posts related to that keyword, they have to search all forms of those keywords to get full results. For example, if a researcher need to find all post related to term مهاجر, they need to search مُهاجِر or مُهاجر or مهاجِر or مهاجر to get all the results.


### Advanced search


Advanced search includes searching keyword combinations with logic operators AND, OR and NOT. 
The following table shows all metric values across advanced search test queries by endpoint from November 8th, 2023 to November 15th, 2023. Representativeness is an average across all dimensions that are mentioned in the representativeness section.




 
 Entity type
  | 
 Recall
  | 
 Representativeness - Paired t-test
  | 
 Representativeness - Welch t-test

  || Facebook Page | 95% | 77% | 94% |
| Facebook group | 93% | 71% | 93% |
| Facebook event | 90% | 59% | 83% |
| Facebook post | 83% | 70% | 93% |
| Instagram account | 98% | 79% | 99% |
| Instagram post | 78% | 83% | 99% |

Caveats and known limitations
-----------------------------


#### Why would results be inconsistent from one time point to another?


Inconsistencies between identical searches made at separate time points can be caused by entity visibility changes over time, which may be due to content being created, deleted or modified. There may also occasionally be short lags between when content is created or modified and when it is indexed.


#### Why am I not seeing an entity I can find on the platform?


Apart from coverage gaps or delivery issues mentioned below (see Factors affecting recall), it is possible the content is not eligible to be visible in the Meta Content Library and API. The visibility rules for content are complex and constantly evolving with new policies and regulations, making it possible that some content could be theoretically viewed by an individual on platform but not exposed via the Meta Content Library and API. For instance, visibility of some content is geographically restricted to users from the country where the content was produced. Also, direct mentions (via @) are not searchable, meaning that a result will not be returned if a matching term is only found in a direct mention.


#### Why would a search result not match my query?


Apart from tokenization issues listed below (see Factors affecting precision), it is possible that the content actually does contain the search terms, but they are found in different text fields or far apart within the text. Search matches query terms independently and scans all text fields visible from the UI. It also does not support phrase searching. Thus a search for “Walter Payton” could match a page listing basketball players “Walter Williams” and “Gary Payton” without reference to a “Walter Payton” anywhere in the text.


### Factors affecting recall


* False positives in the validation data (denominator of recall equation). In our tests, we have found that the validation dataset may occasionally include non-eligible entities for a given search term due to lags between real-time content visibility and privacy status and their representation in the databases used for validation (see validation data presented earlier). This means that true recall estimates are likely underestimated.
* Edge cases or gaps in coverage (true negatives). Indexing data at the scale which Meta operates means that occasionally some content may be imperfectly indexed or missed. Furthermore, internal data models may change, such as when new features for creating and sharing content on platform are added. Thus there may be a lag between when content is available on platform and when it is indexed. As we improve and scale the product, we appreciate any reported cases of missing data from search (see Appendix on this page for details).
* Asynchronous delivery issues. The Meta Content Library and API’s entity loading mechanisms are complex and memory-intensive at scale. Occasionally, the loading process for an entity can become too memory-intensive and fail, resulting in the exclusion of that entity from the returned results.


### Factors affecting precision


* String-matching used to validate precision is unable to approximate tokenization rules. Precision is checked using basic regular expression searches with strict definitions of word boundaries. However tokenization may be more flexible, especially with different language localizations, text involving unicode, URLs, and other patterns. The existence of these edge cases means that precision will be under-estimated to some extent.
* The search term was tokenized in a context-specific way. Occasionally words with unicode symbols, non-English characters, accent marks or URLs may be tokenized in a form that differs from its presented value. For instance, the content with the French word `congrégation` may be returned for a query on the English word `congregation`, despite the literal difference between the acute accented e and its English counterpart.
* The index has matched text not returned by the Meta Content Library or API. In some cases, content with complex, nested data models such as reshares may contain text fields that are tokenized and indexed but not returned by the Meta Content Library or API. We appreciate user feedback identifying such cases (see Appendix on this page for details).
* For the Facebook posts endpoint, there is a known issue involving post reshare text being indexed but not returned in the Meta Content Library API. These posts may either have no visible text (since they are reshares), or the text returned may not contain any mention of the query term. We are exploring this issue further.


### Factors affecting representativeness


* Representativeness issues generally stem from the same factors affecting recall. In these cases there is a population of entities which are either (a) not returned by the Meta Content Library API due to gaps in indexing / delivery, or (b) incorrectly included in the validation dataset adding noise to the calculation. If these groups of entities have similar properties along the data dimensions tested they can influence the representativeness metrics
* The per-query bias test uses a probabilistic statistical test which uses an alpha = 0.05 cutoff by convention. Thus for each test term there is a 5% probability that the test will be a false positive (Type I error rate).


Appendix
--------


### Disclosures


Data governance and sources described in this document may change from time to time and the metrics presented here may not be representative of current operations at Meta. Due to issues such as erroneously logging the data sources from which these metrics are created, these metrics may suffer from fluctuating data quality and incompleteness, which may lead to fluctuating accuracy. We disclose known fluctuations where possible.


Researchers using this data are responsible for conducting standard and thorough data cleaning processes, and are responsible for ensuring that their analyses are accurate. It is expected that researchers may find issues with the data when conducting their analysis. We encourage researchers to share any findings with us. This may include, but is not necessarily limited to, data quality, validity, or fidelity issues. Given the historical nature of the data and lapsed retention periods, we may not be able to fix the issues identified, but in such cases we will work to disclose them. Please reach out to us through Direct Support.


### Disclaimers


Meta works diligently and utilizes a variety of quality assurance measures to improve the accuracy, quality, and reliability of the data it shares for research purposes. However, given the volume of data released and the imperfection of any quality assurance process, inaccuracies persist. Meta makes no representation or warranty, express or implied, including without limitation, any warranties of fitness for a particular purpose or warranties as to the quality, accuracy or completeness of data or information. By accessing this data, researchers acknowledge that the data may contain some nonconformities, defects, or errors. Meta does not warrant that the data will meet the researcher's needs or expectations, that the use of the data will be uninterrupted, or that all nonconformities, defects, or errors can or will be corrected.


### Test search scope for endpoints


The following table summarizes the test search scope for all endpoints




 
 Endpoint
  | 
 Test search scope
  || Facebook Page | Eligible Facebook pages created within the year prior to the query date |
| Facebook group | All eligible Facebook groups |
| Facebook event | Eligible Facebook events created within the year prior to the query date |
| Facebook post | Eligible posts created within two days prior to the given query date |
| Instagram account | Eligible Instagram Creator and Business accounts created within a year prior to the query date |
| Instagram post | Eligible posts created within a day prior to the given query date |

Learn more
----------


* Facebook’s search engine infrastructure
* Distributed memory caching layer
* Advanced search
* Frequently asked questions


































 
