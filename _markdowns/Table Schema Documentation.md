<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This section describes the columns in the Ad Targeting, Ad Targeting
delta, and Ad Library data tables, and provides some related
clarifications.

## Ad Targeting table schema

In this table, the Type (data type) can be:

-   *String* : Sequence of characters, representing either a constant or
    a variable.

-   *Boolean* : One of two possible values (usually denoted true and
    false).

-   *BigInt* : Integer (numerical) value.

-   *List* : Series of values. Angle brackets indicate the data type of
    the values in the list.

-   *Map* : Series of key/value pairs. Angle brackets indicate the data
    type of the key and the data type of the value, separated by a
    comma.

::: _57-c
Column name
:::
:::
:::

</div>

Type

Description

Sample value

` age `

string

Age group targeted by the ad.

` 25 ` - ` 65+ `

` archive_id `

BigInt

Ad dataset ID.

` 2681789712070426 `

` ds `

string

Table partition date stamp.

` 2020-12-06 `

` exclude `

map\<string, string\>

Ad excludes people who are categorized by ANY of the items listed, which
can include behavior, field of study, education level, school, job
title, and many more.

` {"Civil service":"Interests","Government Employees (Global)":"Industry","Servidor público no Brasil":"Job title"} `

` exclude_audience_data_missing `

\

This column is new in the May 2022 dataset. See [Columns for Indicating
Missing Data](#missing-data) for more information.

Boolean

Indicates whether information is missing from the
exclude_custom_audience, exclude_data_file_custom_audience, or
exclude_lookalike column.

` True ` (data is missing)

\

` False ` (data is not missing)

` exclude_connection `

Boolean

Ad excludes ( ` True ` ) or does not exclude ( ` False ` ) people who
have liked a Page owned by the advertiser, responded to an event created
by the advertiser, or used an app owned by the advertiser.

` True `

` exclude_custom_audience `

Boolean

<div>

Ad excludes (\`True\`) or does not exclude (\`False\`) a [custom
audience](https://www.facebook.com/business/help/744354708981227)
created by the advertiser.

</div>

` True `

` exclude_data_file_custom_audience `

Boolean

` True `

` exclude_location `

map\<string, map\<string, mixed\>\>

Locations (cities, countries, zip codes) excluded by the ad, plus an
optional radius in miles.

\

See [Location data](#location-data) for additional information.

` {"United States":{"Nevada":{}}} `

` exclude_lookalike `

Boolean

<div>

Ad excludes (\`True\`) or does not exclude (\`False\`) a [lookalike
audience](https://www.facebook.com/business/help/164749007013531)
created by the advertiser.

</div>

` True `

` gender `

string

Gender targeted by the ad.

` Female `

` include `

list\<map\<string, string\>\>

Ad targets people who are categorized by ANY of the items listed, with
at least one item in each group. Items can include behavior, field of
study, education level, school, job title, and many more.

The following example shows two groups, each enclosed in curly braces.
Ad targets people with at least one item in each group.

``` {._5s-8 .prettyprint .lang-python}
[
  {
    "College grad": "Education level"
  },
  {
    "Wine": "Interests",
    "Golf": "Interests",
    "Organic food": "Interests",
    "Skiing": "Interests",
    "Security (finance)": "Interests",
    "Frequent Travelers": "Behaviors",
    "Sustainable development": "Interests",
    "Business and industry": "Interests",
    "Natural environment": "Interests",
    "Sailing": "Interests",
    "Running": "Interests",
    "SVT Play": "Interests",
    "Politics": "Interests"
  }
]
```

` include_audience_data_missing `

\

This column is new in the May 2022 dataset. See [Columns for indicating
missing data](#missing-data) for more information.

Boolean

Indicates whether information is missing from the
include_custom_audience, include_data_file_custom_audience, or
include_lookalike column.

` True ` (data is missing)

\

` False ` (data is not missing)

` include_connection `

Boolean

Ad targets ( ` True ` ) or does not target ( ` False ` ) people who have
liked a Page owned by the advertiser, responded to an event created by
the advertiser, or used an app owned by the advertiser.

` True `

` include_custom_audience `

Boolean

<div>

Ad targets (\`True\`) or does not target (\`False\`) a [custom
audience](https://www.facebook.com/business/help/744354708981227?id=2469097953376494)
created by the advertiser.

</div>

` True `

` include_data_file_custom_audience `

Boolean

` True `

` include_friend_connections `

Boolean

Ad targets ( ` True ` ) or does not target ( ` False ` ) friends of
people who have liked a Page owned by the advertiser or who have used an
app owned by the advertiser.

` True `

` include_location `

map\<string, map\<string, mixed\>\>

Locations targeted by the ad. Radius in miles included if specified by
the advertiser. Can be cities, countries, or zip codes, plus an optional
radius in miles.

\

See [Location data](#location-data) for additional information.

` {"Brazil":{"Minas Gerais":{"Santa Maria do Suaçuí":["< place>, Santa Maria do Suaçuí (+1 km)"]},"Glucínio Minas Gerais, Poaia Minas Gerais":{}}} `

` include_lookalike `

Boolean

Ad targets (\`True\`) or does not target (\`False\`) a [lookalike
audience](https://www.facebook.com/business/help/164749007013531)
created by the advertiser.

` True `

` language `

\

This column is new in the May 2022 dataset.

string

Languages targeted by the ad.

` English (UK), Greek, English (US) `

` location_type `

string

Ad targets people by their relationship to a location. The location is
the area selected by the advertiser upon ad creation and is identified
by the ` include_location ` column.

\

Possible values:

\

<div>

-   ` Location ` ---The ad targets people whose home or most recent
    location is within the selected area
-   ` Location - Living In ` ---The ad targets people whose home is
    within the selected area
-   ` Location - Recently In ` ---The ad targets people whose most
    recent location is within the selected area
-   ` Location - Traveling In ` ---The ad targets people whose most
    recent location is within the selected area but whose home is more
    than 125mi/200km away

See [Location data](#location-data) for additional information.

</div>

` Location - Living In `

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
The delta table lists ads that were reclassified as non-political (and
therefore, removed from the table) since the last table publication. It
is a single table to which we add data month to month.

::: _57-c
Column name
:::
:::
:::

Type

Description

Sample value

` archive_id `

BigInt

Ad dataset archive ID that was reclassified and removed.

` 2681789712070426 `

` status `

string

Type of change being reported.

` updated ` , ` deleted `

` column_name `

string

Name of column affected by the change. Can also be empty.

` include_location ` , ` exclude `

` current_value `

string

Value after the change. Can also be empty.

` <address> Ecatepec de Morelos (+22 km), Estado de México (+40 km) State of Mexico `

` ds `

string

Date the ad no longer appeared in the dataset.

` 2020-12-06 `

` previous_value `

string

Value before the change. Can also be empty.

` Estado de México (+40 km) State of Mexico `

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
As of November 1, 2021, we started tracking information about custom
audiences that were deleted sometime after the ads were initially run.
For data prior to that date, the Ad Targeting dataset might be missing
information about whether custom audiences, datafile custom audiences,
or lookalike audiences were used or not. By \"missing information\", we
mean that one of the affected columns could read False when it should
actually be True. If it already reads True, we know for sure that it is
True.

We have added two columns to the table schema where we indicate whether
data is missing. The following table lists the two new columns,
indicates the columns of data to which they pertain, and provides the
meaning of the possible values:

::: _57-c
:::
:::
:::

include_audience_data_missing column\

exclude_audience_data_missing column\

**Columns tracked**

` include_custom_audience `

\

` include_data_file_custom_audience `

\

` include_lookalike `

` exclude_custom_audience `

\

` exclude_data_file_custom_audience `

\

` exclude_lookalike `

**Value of True means\...**

Information is missing. At least one of the columns above could read
False when it should actually be True.

Information is missing. At least one of the columns above could read
False when it should actually be True.

**Value of False means\...**

No data is missing.

No data is missing.

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Throughout the Ad Targeting dataset, we provide the location targeting
chosen by an advertiser for the ad. Advertisers can input location
targeting in a number of ways, for example by selecting zip codes,
countries, Designated Market Areas (DMAs), pin drops (longitude and
latitude), addresses, and places within a specified radius. To prevent
inadvertently sharing granular location of people on Facebook, we\'ve
provided the location options chosen by advertisers when these levels
have been set to **zip code level or greater** . For smaller geographic
designations, we note the type of selection (such as an address, place,
or location pin drop), the city it falls in, and the radius specified by
the advertiser.

The following examples help illustrate the transformations. The left
column shows the targeting selection by the advertiser; the right column
shows the transformation found in the data set. You will see that
addresses, pin drops, and places are redacted and replaced by the text
\"\<address\>\", \"\<location\>\", and \"\<place\>\", respectively.

::: _57-c
Advertiser selection
:::
:::
:::

Transformed dataset value

Seattle + 5 miles

` Seattle (+5 miles) ` (no change)

38 North Almaden blvd, San Jose +5 miles

` <address>, San Jose (+5 miles) `

95110, San Jose

` 95110, San Jose ` (no change)

95110, San Jose +5 miles

` 95110, San Jose (+5 miles) ` (no change)

37.335080; -121.895480 + 5 miles

` <location>, San Jose (+5 miles) `

Acme park, San Jose (+1 mile)

` <place>, San Jose (+1 mile) `

Whenever we cannot report a specific location, we replace it with
` "Unknown Country" ` , ` <unknown location> ` , or ` <unknown place> `
as in this example:
` {"Unknown Country":{"":{"":["<unknown place> (+5 km)"]}}} ` . This can
happen for a number of reasons. A country, for example, could be unknown
because the location is too close to a border to classify accurately, or
because borders have changed. A place (such as a church or a school),
could become unknown because the Facebook page from which the place\'s
location was extracted was deleted.

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
An ad\'s ` archive_id ` in the Ad Targeting dataset maps to the ad\'s ID
in the Ad Library product, where researchers can access the ad creative,
the Page associated with the ad, who paid for the ad (\"Paid for by\"
disclaimer), a range of how much they spent, and the reach of the ad
across multiple demographics.

If an advertiser makes changes to an ad after it has been created, (such
as editing the creative, targeting logic, or spend limits), then our
system stores the updated version of the ad as a new distinct ID. This
means that distinct ` archive_id ` values in the dataset could relate to
a similar creative, such as if the only modification was to change the
targeting of the ad.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
The Ad Targeting dataset (refreshed monthly) contains data about
targeting selections for each ad, specified by \`archive_id\`. We also
provide the [Ad Library data](https://facebook.com/ads/library) table
that contains information about ad delivery, such as what pages ran the
ad, when it was created, how many users it reached, and so on. This
table is refreshed daily.

To get a complete picture of the advertisement and its content,
including both its targeting and its delivery, you need information from
both tables. See [Joining Ad Targeting dataset data with Ad Library
data](#joining-ad-library) .

::: _57-c
Column
:::
:::
:::

Type

Description

` fbid `

string

ID for the archived ad object.

` ad_archive_id `

string

Same as ` fbid ` but an older version of the column name (prior to April
21, 2021).

` ad_creation_time `

string

The UTC date and time when someone created the ad. This is not the same
time as when the ad ran. Includes date and time separated by T. Example:
2019-01-24T19:02:04+0000, where +0000 is the UTC offset.

` ad_creative_body `

list\< string\>

A list of the text that displays in each unique ad card of the ad. Some
ads run with multiple ad versions or carousel cards, each with its own
unique text. See [Ad
Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative/)
for more information.

` ad_creative_link_caption `

list\< string\>

A list of the captions that appear in the call to action section for
each unique ad card of the ad. Some ads run with multiple ad versions or
carousel cards, each with its own unique text that appears in the link.

` ad_creative_link_description `

list\< string\>

A list of text descriptions that appear in the call to action section
for each unique ad card of the ad. Some ads run with multiple ad
versions or carousel cards, each with its own unique text describing the
link.

` ad_creative_link_title `

list\< string\>

A list of titles that appear in the call to action section for each
unique ad card of the ad. Some ads run with multiple ad versions or
carousel cards, each with its own unique title text about the link.

` ad_delivery_start_time `

string

Date and time when an advertiser wants Facebook to start delivering an
ad. Provided in UTC as in ` ad_creation_time ` .

` ad_delivery_stop_time `

string

The time when an advertiser wants to stop delivery of their ad. If this
is blank, Facebook runs the ad until the advertiser stops it or they
spend their entire campaign budget. Provided in UTC.

` ad_snapshot_url `

string

String with URL link that displays the archived ad. This displays
uncompressed images and videos from the ad. Note that you cannot
currently download a batch of archived ads, however you can download ad
creative such as images and text for an individual ad. If you do so, it
must be for analysis and you must comply with the data storage terms in
[Facebook Terms of Service.](https://www.facebook.com/terms.php)

` funding_entity `

string

A string containing the name of the person, company, or entity that
provided funding for the ad. Provided by the purchaser of the ad.

` currency `

string

The currency used to pay for the ad, as an [ISO currency
code.](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.iso.org%2Fiso-4217-currency-codes.html%3Ffbclid%3DIwAR2dth6_P9G_7MsN9Vd_0KjbF_RfruHJjqUacKNZO-_i61kwVCQ75PVIlyQ&h=AT1SU4nG9Y1t7Pig_RhNQjtlJLeMmBAHC5R_SbTJul2XX9YCUINONn1NqmUuTD2YLPIH_FN2gMhCp7uZVYnVg_d58YnqwnU9lyyGmxHKX-epcKzrQ10OSWt97ImuN5gO78zcbaFYduwIyYEY)

` region_distribution `

[list\<
AudienceDistribution\>](https://developers.facebook.com/docs/graph-api/reference/audience-distribution/)

Regional distribution of people reached by the ad. Provided as a
percentage and where regions are at a sub-country level.

` demographic_distribution `

[list\<
AudienceDistribution\>](https://developers.facebook.com/docs/graph-api/reference/audience-distribution/)

The demographic distribution of people reached by the ad. Provided as
age ranges and gender.

-   Age ranges: 18-24, 25-34, 35-44, 45-54, 55-64, 65+

-   Gender: \"Male\", \"Female\", \"Unknown\"

` potential_reach `

[InsightsRangeValue](https://developers.facebook.com/docs/graph-api/reference/insights-range-value/)

Estimated Audience Size generally estimates how many people meet the
targeting and ad placement criteria that advertisers select while
creating an ad. [Learn
more.](https://www.facebook.com/business/help/1665333080167380?id=176276233019487)

` impressions `

[InsightsRangeValue](https://developers.facebook.com/docs/graph-api/reference/insights-range-value/)

A string containing the number of times the ad created an impression. In
ranges of:\< 1000, 1K-5K, 5K-10K, 10K-50K, 50K-100K, 100K-200K,
200K-500K, \>1M.

` languages `

list\< string\>

The list of languages contained within the ad. These are displayed in
[ISO 639-1 language
codes.](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.iso.org%2Fstandard%2F22109.html%3Ffbclid%3DIwAR3m8L9GO0eQRNpQ6JErJDiLs6n4U5nWZHp7ObPKwdO60O77MwULJ79rfCQ&h=AT3v_HC5yIyDTZrSUDiUgZltwCfT-_FCb9F2pLsGqPki4qMWJvj30jsBVpbXc3zrq8dmq8xO6PsGI2NOp1vuUttmL08f4dYZQIVIfI5cf__7bEsoWTiwcpcWAwEW85eiK94iKHcMQ0qAaPQt)

` page_id `

numeric string

ID of the Facebook Page that ran the ad.

` page_name `

string

Name of the Facebook Page that ran the ad.

` publisher_platforms `

list\< enum\>

A list of platforms where the archived ad appeared, such as Facebook or
Instagram.

` spend `

[InsightsRangeValue](https://developers.facebook.com/docs/graph-api/reference/insights-range-value/)

A string showing amount of money spent running the ad as specified in
currency. This is reported in ranges; \<100, 100-499, 500-999, 1K-5K,
5K-10K, 10K- 50K, 50K-100K, 100K-200K, 200K-500K, \>1M.

` is_active `

boolean

Whether the ad is currently actively running on any platform.

` reached_countries `

list\< string\>

List of countries (as ISO country codes) that ran the ad.

` media_type `

list\< string\>

A list of media types contained within the ad.

` ds `

string

Table partition date stamp.

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
If you want more information about an ad (its creative, spend, and so
on) and want to map the ad with its targeting information, perform a
join between the ` archive_id ` column of the
` ad_targeting_dataset_siep_aug_2020 ` table (the Ad Targeting dataset)
and the ` fbid ` column of the ` ad_archive_api ` table (the Ad Library
dataset) as shown in this example:

``` {._5s-8 .prettyprint .lang-python}
data_joined = execute("SELECT * FROM fbri_prod_atp.ad_archive_api AS a, fbri_prod_atp.ad_targeting_dataset_siep_aug_2020 AS b WHERE a.ds = b.ds AND a.fbid = b.archive_id")
```

::: {._57yz ._57z1 ._3-8p}
<div>

**Column name change notice**

The name of the ` fbid ` column of the ` ad_archive_api ` table was
` ad_archive_id ` prior to April 21, 2021. If you want to join on data
before that date, use the ` ad_archive_id ` column name.

</div>
:::

### **Inconsistencies between the Ad Targeting dataset table and the Ad Library data table**

If you perform a join between the two tables, you will see that there
are ads in the Ad Targeting dataset table that do not have a
corresponding entry in the Ad Library data table (or vice versa). This
happens because ads initially classified as political can be
reclassified as non-political after they have been run.

When a reclassification occurs, the Ad Library data table reflects the
change before the Ad Targeting dataset because the Ad Library data table
is updated daily and the Ad Targeting dataset is updated monthly.

Beginning with the second monthly update, there is an [Ad Targeting
dataset delta table](#delta-schema) that describes ads that were
reclassified as non-political (and therefore, removed from the dataset)
since the previous monthly update.
:::
:::
