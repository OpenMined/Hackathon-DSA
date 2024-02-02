::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The gnip object, within Activity streams format, contains the metadata
added by the active enrichments, as well as indication of the matching
rules for the activity.

+-----------------------+-----------------------+-----------------------+
| **Field**             | **Type**              | **Description**       |
+-----------------------+-----------------------+-----------------------+
| matching_rules        | array                 | Contains an array of  |
|                       |                       | matching rule objects |
|                       |                       | which indicate the    |
|                       |                       | rule which the        |
|                       |                       | activity matches on.\ |
|                       |                       | [                     |
|                       |                       | **\"matching_rules\": |
|                       |                       | \[** ]{.code-inline}  |
|                       |                       |                       |
|                       |                       | [ **{**               |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"tag\": null,**  |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"id\":**         |
|                       |                       | 1026514022567358500   |
|                       |                       | **,** ]{.code-inline} |
|                       |                       |                       |
|                       |                       | [ **\"id_str\":**     |
|                       |                       | \"                    |
|                       |                       | 1026514022567358464\" |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **}**               |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\]**              |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| urls                  | array                 | Contains an array of  |
|                       |                       | the links within the  |
|                       |                       | activity, and the     |
|                       |                       | expanded url metadata |
|                       |                       | for the \*\*\*URL     |
|                       |                       | unwinding enrichement |
|                       |                       |                       |
|                       |                       | [ **\"urls\": \[**    |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **{**               |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"url\":**        |
|                       |                       | \"http                |
|                       |                       | s://t.co/tGQqNxxyhU\" |
|                       |                       | **,** ]{.code-inline} |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | **\"expanded_url\":** |
|                       |                       | \"https://www.yout    |
|                       |                       | ube.com/channel/UCwUx |
|                       |                       | W2CV2p5mzjMBqvqLzJA\" |
|                       |                       | **,** ]{.code-inline} |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | **\                   |
|                       |                       | "expanded_status\":** |
|                       |                       | 200 **,**             |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | **\"ex                |
|                       |                       | panded_url_title\":** |
|                       |                       | \"Birdys Daughter\"   |
|                       |                       | **,** ]{.code-inline} |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | **\"expanded          |
|                       |                       | _url_description\":** |
|                       |                       | \"Premium,            |
|                       |                       | single-origin,        |
|                       |                       | handpicked Jamaica    |
|                       |                       | Blue Mountain         |
|                       |                       | Coffee\"              |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **}**               |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\]**              |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| profileLocations      | array of location     | Contains the derived  |
|                       | objects               | location object from  |
|                       |                       | the Profile Geo       |
|                       |                       | enrichment            |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | **                    |
|                       |                       | \"profileLocations\": |
|                       |                       | \[** ]{.code-inline}  |
|                       |                       |                       |
|                       |                       | [ **{**               |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"address\": {**  |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"country\":**    |
|                       |                       | \"Canada\" **,**      |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | **\"countryCode\":**  |
|                       |                       | \"CA\" **,**          |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"locality\":**   |
|                       |                       | \"Toronto\" **,**     |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"region\":**     |
|                       |                       | \"Ontario\"           |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **},**              |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [                     |
|                       |                       | **\"displayName\":**  |
|                       |                       | \"Toronto, Ontario,   |
|                       |                       | Canada\" **,**        |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"geo\": {**      |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"coordinates\":  |
|                       |                       | \[** ]{.code-inline}  |
|                       |                       |                       |
|                       |                       | [ -79.4163 **,**      |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ 43.70011            |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\],**             |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"type\":**       |
|                       |                       | \"point\"             |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **},**              |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\"objectType\":** |
|                       |                       | \"place\"             |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **}**               |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **\]**              |
|                       |                       | ]{.code-inline}       |
|                       |                       |                       |
|                       |                       | [ **}**               |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
   "gnip": {
    "matching_rules": [
      {
        "tag": null
      }
    ],
    "urls": [
      {
        "url": "https://t.co/Nx1XZmRCXA",
        "expanded_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
        "expanded_status": 200,
        "expanded_url_title": null,
        "expanded_url_description": null
      }
    ]
  }
    
```
:::
:::
:::
:::
:::
:::
:::
:::
:::
