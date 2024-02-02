::: is-table-default
The questions below are specific to the context annotations element of
Tweet annotations. For more details, please see the
[Overview](/en/docs/twitter-api/annotations/overview.html) page.

**How does Twitter context annotations work?**

Twitter classifies Tweets semantically, meaning that we curate lists of
keywords, hashtags, and \@handles that are relevant to a given topic. If
a Tweet contains the text we've specified, it will be labeled
appropriately. This differs from a machine learning approach where a
model is trained specifically to classify text (in this case, Tweets)
and produce a probability score alongside the output/classification.

**How do I know that your data is complete and trustworthy?**\

Twitter\'s annotations are curated by domain experts using research and
QA processes that have been refined over the course of several years.
The process is supported by custom tooling to scale data tracking as far
as we are able to maintain excellent precision and recall. In addition,
our data is audited regularly by an internal team, having received a
precision score of \~80% for the past several quarters.

**How do you ensure precision?**

Team members QA our entities on a daily basis to ensure high precision
and recall. Additionally, our work is audited quarterly by an internal
team, which manually reviews 10,000 Tweets across all of our domains to
calculate a precision score.

**How do you decide what to track?**

For some domains, like sports and TV, we rely on automated ingest to
build out our graph. In the News domain, we track data around stories
published by the Twitter Moments team. Otherwise, the team uses a
variety of research methods to identify topics to track that garner a
high amount of conversation on the platform.

**What historical support is available with Tweet Annotations?**

Data tracking begins the moment an entity is published; therefore, we do
not annotate Tweets that were published prior to a given entity being
tracked. For example, if an upstart brand/company is added to the
taxonomy, we will not retroactively annotate Tweets about that brand
prior to when the annotation was added.

**Is Twitter able to annotate Tweets in non-english languages? If so,
which languages and does the coverage of Tweets being annotated
change?**

Yes. Language coverage can vary depending on the domain and the market.
English and Japanese are included in the majority of the biggest
entities. Below, is a list of the languages and main markets that are
covered today:

1.  English (US, UK)
2.  Japanese (Japan)
3.  Portuguese (Brazil)
4.  Spanish (Argentina, Mexico, Spain)
5.  Hindi (India)
6.  Arabic (Saudi Arabia)
7.  Turkish (Turkey)
8.  Indonesian (Indonesia)
9.  Russian (Russia)
10. French (France)

Coming soon (\~H2 2021):

1.  German (Germany)
2.  Tamil (India)

Below is a table of the top 15 countries ordered by the most coverage of
annotated Tweets:

  ------ -------------- --------------- ------------------------
  Rank   Country code   Country         \% of Tweets annotated
  1      IN             India           41%
  2      VN             Vietnam         36%
  3      GB             Great Britain   36%
  4      EC             Ecuador         35%
  5      PE             Peru            33%
  6      US             United States   32%
  7      CA             Canada          32%
  8      AU             Australia       31%
  9      JP             Japan           31%
  10     PH             Philippines     30%
  11     SG             Singapore       30%
  12     MY             Malaysia        30%
  13     MX             Mexico          30%
  14     gb             Great Britain   29%
  15     NG             Nigeria         29%
  ------ -------------- --------------- ------------------------

**What underlying \"semantics\" does Twitter rely on to annotate a
Tweet?**

Tweet annotations consist of the following semantics to annotate a
Tweet:

-   Accounts - we can annotate tweets from a given handle or mentioning
    this handle
-   Hashtags
-   Keywords/phrases

For customers that are familiar with the filtered steaming APIs such as
PowerTrack, the semantics used by annotations are similar in principle
to the boolean rules defined to filter a stream of Tweets. If a Tweet
matches the underlying semantic conditions, it will be tagged
accordingly.

**Why do some Tweets have entities associated with them while others do
not?**

The goal is to annotate as many Tweets as possible; however, there are
several reasons why some Tweets are not annotated:

-   Some Tweets aren\'t semantically rich enough to be labelled and
    can\'t be tagged with our current annotation rules
-   Some Tweets aren\'t topical
-   The Tweet is about a very ephemeral topic that\'s not in our graph
-   We don\'t cover the language/market
-   We cover the language/market but we\'re missing a topic or a
    specific term/account/hashtag related to a topic we already track\"

**When there are multiple domains (for example, \[3,30\]), does the
Entity ID remain the same?**

An entity can be part of multiple domains. The domain IDs will change
but the entity ID remains the same. Donald Glover is a person (domain
10), an actor (domain 56)  and a musician (domain 54) but his entity ID
is still 875072662527029248.

**Do you have an established timeline for show/movie tracking? In other
words, how long is a show/movie tracked before/after release?**

Tracking starts a month prior to the release. For popular blockbusters,
like a Marvel movie, we can start tracking them as soon as they start
teasing about an upcoming release.

**Do movies have a locale filter similar to the one for TV shows?**

No, they do not.
:::
