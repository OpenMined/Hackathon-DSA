::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The matching rules enrichment is an object of metadata that indicates
which rule or rules matched the Tweets received. This is most commonly
used with the PowerTrack stream.

Matching will be done via exact match on the terms contained in a rule,
scanning the content of the activity with and without punctuation.
Matching is not case sensitive. When the content is found to contain all
terms defined in the rule, there will be a root-level
a matching_rules object indicating the rule(s) that led to the match.

## PowerTrack

Tweets delivered through PowerTrack (realtime, Replay, and Historical)
will contain the matching_rules object as follows:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 "matching_rules": [{
        "tag": null,
        "id": 907728589029646336,
        "id_str": "907728589029646336"
    }]
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
In PowerTrack, the [ matching_rules ]{.code-inline} object reflects
*all* rules that matched the given result. In other words, if more than
one rule matches a specific Tweet, it will only be delivered once, but
the [ matching_rules ]{.code-inline} element will contain all the rules
that matched.
:::
:::
:::
:::
:::
:::
:::
:::
