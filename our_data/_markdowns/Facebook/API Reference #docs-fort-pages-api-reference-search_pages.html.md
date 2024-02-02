Content Library and API - Documentation - Meta for Developers

Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Meta Content Library and API
============================

**Version v2.0**

Welcome to Meta Content Library and API. This page provides a broad-level overview of these products and acquaints you with the documentation resources that are available. To learn about obtaining access, see Get Access.

* **Content Library**: a web-based tool that allows researchers to explore and understand data across Facebook and Instagram by offering a comprehensive visual and searchable collection of publicly accessible content.
* **Content Library API**: an API for querying and analyzing Meta's full public content archive. The API supports data analysis in Python and R in Meta's Researcher Platform, a secure digital cleanroom. VPN connection is required for Researcher Platform. The API can also be used in an approved third-party cleanroom. Each third-party cleanroom environment has its own user interface, the documentation of which is outside the scope of Meta Content Library and API documentation.

Content Library and API are controlled-access environments and do not allow data to be exported to a researcher’s own machine for analysis. You can perform deeper analysis of the public content from the library by using Content Library API in Researcher Platform or in an approved third-party cleanroom environment.

Available Facebook and Instagram data
-------------------------------------

Both tools use the same database of near real-time public content from Facebook and Instagram. Details about the content, such as the post owner and the number of reactions and shares, are also available. Information and content from the public entities listed below are available; however, certain data that could potentially identify users (such as tags) is redacted or omitted.

* Facebook Page
* Facebook group
* Facebook event
* Facebook post
* Instagram business, creator, or personal account
* Instagram post

Note that public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy set to public and have either a verified badge or 50,000 or more followers. A verified badge in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription.
**Post view data**

The number of times the post was onscreen, which can shed light on questions relating to exposure and popularity of the content.

**Geographical data**

Content Library surfaces content from most countries and territories. Content from the following countries and territories is currently excluded: Australia, Belarus, China, Crimea, Cuba, Hong Kong, Iran, Iraq, North Korea, Russia, South Korea, Syria, Togo, Ukraine (Luhansk and Donetsk regions) and Venezuela. This list of excluded countries and territories is subject to change.

Content Library highlights
--------------------------

**Searching and filtering**

Searching all public posts across Facebook or Instagram is easy with comprehensive sorting and filtering options. Post results can be filtered by language, view count, media type, content producer and more. Search results can be shown in card view or table view.

**Multimedia**

Photos, videos and reels are available for dynamic search, exploration and analysis.

**Producer lists**

You can apply custom producer lists to a search query to surface public content from specific creators on Facebook or Instagram.

**Get API Code tool**

You can generate an API query in Python or R directly from your search query. The code can be pasted into the Content Library API in Researcher Platform to retrieve search results and perform deeper analysis.

**Trends in posts created**

Researchers can explore a graph showing a normalized trend of how often content matching their search keywords was posted on Facebook and Instagram within their chosen date range.

**Documentation resources**

* The Content Library "About" tabhas comprehensive documentation right in the UI.
* Content Library documentationhas the same information, but does not require access to the Content Library UI.
* Quick linksprovides quick access to key topics of interest to Content Library and API users.
Content Library API highlights
------------------------------

**Endpoints and data fields**

With six dedicated endpoints, Content Library API searches over 100 data fields across Instagram accounts and posts, and Facebook Pages, posts, groups and events.

**Search indexing and results**

The API has powerful search capabilities and can return up to 100,000 results per query.

**Asynchronous search**

In addition to synchronous search, you can submit asynchronous queries in Content Library API. This means a search can run in the background while you submit other queries or work on other tasks.

**Documentation resources**

* Content Library API documentation.
* Quick linksprovides quick access to key topics of interest to Content Library and API users.
Researcher Platform highlights
------------------------------

Researcher Platform is a virtual data cleanroom that provides secure access to Facebook and Instagram datasets and tools designed for researchers.

**Free computation**

Computation and data analysis on Researcher Platform are free. The platform supports researchers collaborating on terabyte- to petabyte-scale datasets.

**JupyterHub environment**

Researcher Platform runs a modified, access-controlled version of JupyterHub—an open source tool that supports R, Python, SQL and a range of standard statistical packages. It offers both CPU and GPU servers.

**Research outputs**

You can export your research outputs under agreed-upon terms and conditions. Research outputs can consist of code, figures, tables, graphs and statistics.

**Documentation resources**

* Researcher Platform documentation.