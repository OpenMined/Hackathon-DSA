<div>

Products utilizing enterprise operators deliver social data to you based
on filtering rules you set up. Rules are made up of one or more
'clauses', where a clause is a keyword, exact phrase, or one of the many
enterprise operators. Before beginning to build rules with enterprise
operators, be sure to review the syntax described below, look through
the list of available operators, and understand the restrictions around
building rules. You should also be sure to understand the nuances of how
rules are evaluated logically, in the \" [Order of
operations](#orderofoperations) \" section.

Multiple clauses can be combined with both \"and\" and \"or\" logic.

**Please note:** \"And\" logic is specified with a space between
clauses, while or logic is specified with an upper-case ` OR ` .

Each rule can be up to 2,048 characters long with no limits on the
number of positive clauses (things you want to match or filter on) and
negative clauses (things you want to exclude and not match on).\

### Building rules and queries

**Keyword match**

Keyword matches are similar to queries in a search interface. For
example, the following enterprise operator rule would match activities
with the term \"social\" in the text body.

` social `

**ANDing terms with white space**

Adding another keyword is the same as adding another requirement for
finding matches. For example, this rule would only match activities
where both \"social\" and \"media\" were present in the text, in either
order -- *having a space between terms operates as boolean AND logic* .
If you include an explicit AND in your rule, it will rejected by the
rules endpoint.

` social media `

**ORing terms with upper-case OR**

Many situations actually call for boolean OR logic, however. This is
easily accomplished as well. *Note that the OR operator must be
upper-case and a lower-case 'or' will be treated as a regular keyword.*

` social OR data `

**Negating terms**

Still other scenarios might call for excluding results with certain
keywords (a boolean NOT logic). For instance, activities with 'happy',
but excluding any with 'birthday' in the text.

` social -personality `

**Grouping with parentheses**

These types of logic can be combined using grouping with parentheses,
and expanded to much more complex queries.

` (social OR data) (academic OR research) -personality -information -university `

This is just the beginning though -- while the above examples rely
simply on tokenized matching for keywords, enterprise products also
offer operators to perform different types of matching on the text.

**Exact match**

` "social media research" `

**Substring match**

` contains:info `

**Proximity match**

` "social media research"~3 `

\
Further, other operators allow you to filter on unique aspects of social
data, besides just the text.

**The user who is posting a Tweet**

` from:twitterdev `

**Geo-tagged Tweets within 10 miles of Pearl St. in Boulder, CO, United
States**

` point_radius:[-105.27346517 40.01924738 10.0mi] `

**Putting it all together**

These can be combined with text filters using the same types of logic
described above.

` (social OR data) (academic OR research OR "social media research") point_radius:[-105.27346517 40.01924738 10.0mi] lang:en -personality -information -university `

###  Boolean Syntax

The examples in the previous section, utilized various types of boolean
logic and grouping. See the table below for additional detail regarding
the syntax and requirements for each.

+-----------------------+-----------------------+-----------------------+
| **Logic type**        | **Operator syntax**   | Description           |
+-----------------------+-----------------------+-----------------------+
| AND                   | [ social data         | Whitespace between    |
|                       | ]{.code-inline}       | two operators results |
|                       |                       | in AND logic between  |
|                       |                       | them Matches          |
|                       |                       | activities containing |
|                       |                       | both keywords         |
|                       |                       | (\"social\",          |
|                       |                       | \"data\").            |
|                       |                       |                       |
|                       |                       | **Do not use AND      |
|                       |                       | explicitly in your    |
|                       |                       | rule. Only use        |
|                       |                       | whitespace. An        |
|                       |                       | explicit AND will be  |
|                       |                       | treated like a        |
|                       |                       | regular keyword.**    |
+-----------------------+-----------------------+-----------------------+
| OR                    | [ social OR data      | To OR together two    |
|                       | ]{.code-inline}       | operators, insert an  |
|                       |                       | all-caps OR, enclosed |
|                       |                       | in whitespace between |
|                       |                       | them Matches          |
|                       |                       | activities with       |
|                       |                       | EITHER keyword        |
|                       |                       | (\"social\" OR        |
|                       |                       | \"data\")             |
|                       |                       |                       |
|                       |                       | Note that if you      |
|                       |                       | combine OR and AND    |
|                       |                       | functionality in a    |
|                       |                       | single rule, you      |
|                       |                       | should understand the |
|                       |                       | order of operations   |
|                       |                       | described in our \"   |
|                       |                       | [Order of             |
|                       |                       | operations            |
|                       |                       | ](#OrderOfOperations) |
|                       |                       | \" section, and       |
|                       |                       | consider grouping     |
|                       |                       | non-negated operators |
|                       |                       | together using        |
|                       |                       | parentheses as        |
|                       |                       | described below to    |
|                       |                       | ensure your rule      |
|                       |                       | behaves as expected.  |
|                       |                       |                       |
|                       |                       | You must use          |
|                       |                       | upper-case \"OR\" in  |
|                       |                       | your rule. Lower-case |
|                       |                       | \'or\' will be        |
|                       |                       | treated as a regular  |
|                       |                       | keyword.              |
+-----------------------+-----------------------+-----------------------+
| NOT                   | ::: code-inline       | Insert a ` - `        |
|                       | social data -apple    | character immediately |
|                       | -android -phone       | in front of the       |
|                       | :::                   | operator or group of  |
|                       |                       | operators. The        |
|                       |                       | example rule shown    |
|                       |                       | matches activities    |
|                       |                       | containing keyword    |
|                       |                       | \"social\", but       |
|                       |                       | excludes those which  |
|                       |                       | contain the keyword   |
|                       |                       | \"data.\"             |
|                       |                       |                       |
|                       |                       | Negated ORs are not   |
|                       |                       | allowed where the     |
|                       |                       | rule would request    |
|                       |                       | \"everything in the   |
|                       |                       | firehose except the   |
|                       |                       | negation.\" For       |
|                       |                       | example,              |
|                       |                       | ` apple OR -ipad ` is |
|                       |                       | invalid because it    |
|                       |                       | would match all       |
|                       |                       | activities except     |
|                       |                       | those mentioning      |
|                       |                       | \"ipad\".             |
+-----------------------+-----------------------+-----------------------+
| Grouping              | [ (social OR data)    | Parentheses around    |
|                       | -twitterdev           | multiple operators    |
|                       | -twitterapi           | create a functional   |
|                       | ]{.code-inline}       | \"group\".            |
|                       |                       |                       |
|                       |                       | Groups can be         |
|                       |                       | connected to clauses  |
|                       |                       | in the same manner as |
|                       |                       | an individual clause  |
|                       |                       | via whitespace (AND)  |
|                       |                       | or ORs. However, note |
|                       |                       | that it is a best     |
|                       |                       | practice to not group |
|                       |                       | together negations by |
|                       |                       | applying the negating |
|                       |                       | [ - ]{.code-inline}   |
|                       |                       | to the entire group.  |
|                       |                       | Instead, you should   |
|                       |                       | negate each           |
|                       |                       | individual operator,  |
|                       |                       | stringing them        |
|                       |                       | together via          |
|                       |                       | whitespace (AND).     |
|                       |                       |                       |
|                       |                       | For example, instead  |
|                       |                       | of using [ -(iphone   |
|                       |                       | OR imac OR macbook)   |
|                       |                       | ]{.code-inline} , use |
|                       |                       | the following: [      |
|                       |                       | -iphone -imac         |
|                       |                       | -macbook              |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | Grouping is           |
|                       |                       | especially important  |
|                       |                       | where a single rule   |
|                       |                       | combines AND and OR   |
|                       |                       | functionality, due to |
|                       |                       | the order of          |
|                       |                       | operations used to    |
|                       |                       | evaluate the rule.    |
|                       |                       | See below for more    |
|                       |                       | details.              |
+-----------------------+-----------------------+-----------------------+

**Please note:** that operators may be either positive or negative.

**Positive Operators** define what you want to **include** in the
results. E.g. the ` has:hashtags ` operator says "I want activities
containing hashtags."

**Negative Operators** define what you want to **exclude** from the
results, and are created by using the Boolean NOT logic described above.
For example, ` -has:hashtags ` says "Exclude any activities containing
hashtagss, even if they otherwise match my rule."

Premum operator products have no restriction on the number of positive
and negative clauses, subject to a maximum length of 2,048 characters.\

#### []{#orderofoperations} Order of Operations

When combining AND and OR functionality in a single rule, the following
order of operations will dictate how your rule is evaluated.

1.  Operators connected by AND logic are combined first
2.  Then, operators connected with OR logic are applied

**Example:**

-   ` apple OR iphone ipad ` would be evaluated as
    ` apple OR (iphone ipad) `
-   ` ipad iphone OR android ` would be evaluated as
    ` (iphone ipad) OR android `

To eliminate uncertainty and ensure that your rules are evaluated as
intended, group terms together with parentheses where appropriate. For
example:

-   ` (apple OR iphone) ipad `
-   ` iphone (ipad OR android) `

####  Punctuation, Diacritics, and Case Sensitivity

If you specify a keyword or hashtag rule with character accents or
diacritics for enterprise operators, it will match Tweet text honoring
the diacritics (hashtags or keywords). Rule with a keyword
` Diacr `**`í`**` tica ` or hashtag ` #cumplea `**`ñ`**` os ` will match
\"Diacr **í** tica\" or \"#cumplea **ñ** os\" but not \"Diacritica\" or
\"#cumpleanos\" without the tilde **í** or **eñe** .

Characters with accents or diacritics are treated the same as normal
characters and are not treated as word boundaries. For example, a rule
of cumplea **ñ** os would only match activities containing the word
cumpleaños and would not match activities containing cumplea, cumplean,
or os.

All operators are evaluated in a case-insensitive manner. For example,
the rule ` Cat ` will match all of the following: \"cat\", \"CAT\",
\"Cat\".

####  PowerTrack rule tags

As described on our \" [Matching
rules](/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules)
\" page, each rule may be created with a tag. These tags have no effect
on filtering, but can be used to create logical groupings of rules
within your app. Each rule may have only one tag, with a maximum of 255
characters. Tags are included with the JSON formatted rule at the time
of creation via the API, as described on our \"Matching rules\" page.

####  Putting Rules in JSON Format

In order to add or delete a rule from a stream via the API, the rules
must utilize JSON format. Essentially, this requires putting each rule
into the following structure:

` {"value":"insert_rule_here"} `

**Rules with double-quotes**

If the rule contains double-quote characters ( ` “ ` ) associated with
exact-match or other operators, they must be escaped using a backslash
to distinguish them from the structure of the JSON format.

` "social data" @twitterdev `

The JSON formatted rule would be:

` {"value":"\"social data\" @twitterdev"} `

**Rules with double-quote string literals**

To include a double-quote character as a string literal within an
exact-match, it must be double-escaped. For example, for a rule matching
on the exact phrase \"Toys "R" Us\", including the double-quotes around
\"R\", the plain-text representation of this would look like the
following:

` "Toys \"R\" Us" `

Translating this to JSON format, you should use the following structure:

` {"value":"\"Toys \\\"R\\\" Us\""} `

**Rules with Tags**

To include an optional tag with your rule, as described above, simply
include an additional ` tag ` field with the rule value.

` {"value":"\"social data\" @twitterdev","tag":"RULE-TAG-01"} `

**Formatting for API Requests**

When adding or deleting rules from the stream via the API, multiple JSON
formatted rules should be comma delimited, and wrapped in a JSON "rules"
array, as shown below:

` {"rules":[{"value":"from:twitterdev"},{"value":"\social data\" @twitterdev","tag":"RULE-TAG-01"}]} `

####  Operators that match Quote Tweets

When using the [PowerTrack
API](/en/docs/twitter-api/enterprise/powertrack-api) and [Historical
PowerTrack
API](/en/docs/twitter-api/enterprise/historical-powertrack-api) , the
operators below will match on content from both the original Tweet that
was quoted and the new Quote Tweet.

However, if you are using the [Search
API](/en/docs/twitter-api/enterprise/search-api) , these operators will
only match the contents of the Quote Tweet, and will not match on any
content from the original Tweet that was quoted.

-   ` Keywords `
-   ` Phrases `
-   ` Proximity `
-   ` #hashtags `
-   ` @mentions `
-   ` $cashtags `
-   ` url: `
-   ` url_contains: `
-   ` has:links `
-   ` has:mentions `
-   ` has:hashtags `
-   ` has:media `
-   ` has:symbols `
-   ` is:quote `
-   ` is:reply `

</div>
