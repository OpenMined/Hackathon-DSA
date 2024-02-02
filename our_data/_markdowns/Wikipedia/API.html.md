
API:Main page - MediaWiki

Jump to content

Main menu

Main menu
move to sidebar
hide

 Navigation

* Main page
* Get MediaWiki
* Get extensions
* Tech blog
* Contribute

 Support

* User help
* FAQ
* Technical manual
* Support desk
* Communication

 Development

* Developer portal
* Code statistics

 mediawiki.org

* Community portal
* Recent changes
* Translate content
* Random page
* Village pump
* Sandbox

 In other languages

* English
* Français

Edit links

Search

Search

* English

* Create account
* Log in

Personal tools

* Create account
* Log in

 Pages for logged out editors learn more

* Contributions
* Talk

Contents
--------

move to sidebar
hide
* Beginning
* 1Quick Start

Toggle Quick Start subsection
	+ 1.1Endpoint
* 2Introduction

Toggle Introduction subsection
	+ 2.1Uses for the MediaWiki Action API
	+ 2.2Getting started with MediaWiki Action API
* 3API documentation
* 4Other APIs
* 5Code stewardship

Toggle the table of contents

API:Main page
=============

* API
* Discussion

English

* Read
* View source
* View history

Tools

Tools
move to sidebar
hide

 Actions

* Read
* View source
* View history

 General

* What links here
* Related changes
* Upload file
* Special pages
* Permanent link
* Page information
* Cite this page
* Get shortened URL
* Wikidata item

 Print/export

* Create a book
* Download as PDF
* Printable version

 In other projects

* Wikipedia

From mediawiki.org

Translate this pageLanguages:* Bahasa Indonesia
* Bahasa Melayu
* Cymraeg
* Deutsch
* Deutsch (Sie-Form)
* English
* Esperanto
* Nederlands
* Taqbaylit
* Tiếng Việt
* Türkçe
* azərbaycanca
* català
* dansk
* español
* français
* italiano
* latviešu
* lietuvių
* polski
* português
* português do Brasil
* română
* svenska
* čeština
* български
* русский
* српски / srpski
* українська
* עברית
* العربية
* تۆرکجه
* فارسی
* پښتو
* मराठी
* हिन्दी
* বাংলা
* ಕನ್ನಡ
* ไทย
* မြန်မာဘာသာ
* ᏣᎳᎩ
* 中文
* 文言
* 日本語
* 粵語
* ꯃꯤꯇꯩ ꯂꯣꯟ
* 한국어

|  |  |
| --- | --- |
|  | This page is part of the MediaWiki Action API documentation. |

| **MediaWiki Action API** |
| --- |
| Basics |
| * Etiquette and usage guidelines
* All Query modules
* Get properties of pages
* List pages matching a criterion
* Get module parameters information
* Get meta information about the wiki and user
 |
| Authentication |
| * Get tokens for data modifying operations
* Login
* Logout
* Verifying authentication (assertions)
 |
| Accounts and Users |
| * Create an account
* Block or unblock a user
* Get info about the current user
* Get the current user's watchlist as a feed
* Change user options
* Change user group membership
* Send an email
 |
| Page Operations |
| * Create and edit a page
* Get the contents of a page
* Upload a file
* Import a page
* Delete a page
* Parse content of a page
* Watch or unwatch a page
* Purge cache for page(s)
* Rollback a page
* Move a page
* Patrol a page or revision
* Restore revisions of a deleted page
* Change a page's protection level
* Change a page's language
* More...
 |
| Search |
| * Search wiki pages by title (OpenSearch)
* Advanced search for wiki pages by title or text
* Search wiki pages near a location
* Search for a language name
* Perform a prefix search for page titles
 |
| Developer Utilities |
| * Access libraries
* Cross-site requests
* Creating an API module in an extension
* Using the API in MediaWiki and extensions
* Restricting API usage
* Localisation
* Implementation Strategy
 |
| Tutorials |
| * Action API Tutorial
* Article ideas generator
* Nearby places viewer
* Picture of the day viewer
* Holidays viewer
 |
| v **·** d **·** e |

This page provides an overview of the MediaWiki **Action API**, represented by the `api.php` endpoint.
This page is intended for technical contributors and software developers who wish to understand and use the MediaWiki Action API.

Quick Start
-----------

Get the contents of an article on English Wikipedia in HTML:

**api.php?action=parse&page=Pet\_door&format=json** [try in ApiSandbox]

### Endpoint

**All Wikimedia wikis have endpoints that follow this pattern:** `https://www.example.org/w/api.php`

Examples of Wikimedia Wiki Endpoints
| API Endpoint
 | Wiki
 |
| --- | --- |
|  `https://www.mediawiki.org/w/api.php`  | MediaWiki API
 |
|  `https://meta.wikimedia.org/w/api.php`  | Meta-Wiki API
 |
|  `https://en.wikipedia.org/w/api.php`  | English Wikipedia API
 |
|  `https://nl.wikipedia.org/w/api.php`  | Dutch Wikipedia API
 |
|  `https://commons.wikimedia.org/w/api.php`  | Wikimedia Commons API
 |
| `https://test.wikipedia.org/w/api.php` | Test Wiki API
 |

To see the endpoint URL on a particular wiki, see section "Entry point URLs" on the Special:Version page.

Introduction
------------

The MediaWiki Action API is a web service that allows access to some wiki features like authentication, page operations, and search. It can provide meta information about the wiki and the logged-in user.

### Uses for the MediaWiki Action API

* Monitor a MediaWiki installation
* Create a bot to maintain a MediaWiki installation
* Log in to a wiki, access data, and post changes by making HTTP requests to the web service

### Getting started with MediaWiki Action API

Before you start using the MediaWiki Action API, you should review the following pages:

* API etiquette and usage guidelines
* Frequently asked questions
* Input and output formats
* Errors and warnings
* Any policies that apply to the wiki you want to access, such as Wikimedia Foundation wikis' terms of use and trademark policy. These terms apply to you when you access or edit using the API, just as they do when you use your web browser.

API documentation
-----------------

---

|  |  |
| --- | --- |
|  | The following documentation is the output of Special:ApiHelp/main, automatically generated by the pre-release version of MediaWiki that is running on this site (MediaWiki.org). |

Main module
-----------

* Source: MediaWiki
* License: GPL-2.0-or-later

* Documentation
* Etiquette & usage guidelines
* FAQ
* Mailing list
* API Announcements
* Bugs & requests

**Status:** The MediaWiki API is a mature and stable interface that is actively supported and improved. While we try to avoid it, we may occasionally need to make breaking changes; subscribe to the mediawiki-api-announce mailing list for notice of updates.

**Erroneous requests:** When erroneous requests are sent to the API, an HTTP header will be sent with the key "MediaWiki-API-Error" and then both the value of the header and the error code sent back will be set to the same value. For more information see API: Errors and warnings.

**Testing:** For ease of testing API requests, see Special:ApiSandbox.

Specific parameters:actionWhich action to perform.

abusefiltercheckmatch
Check to see if an AbuseFilter matches a set of variables, an edit, or a logged AbuseFilter event.
abusefilterchecksyntax
Check syntax of an AbuseFilter filter.
abusefilterevalexpression
Evaluates an AbuseFilter expression.
abusefilterunblockautopromote
Unblocks a user from receiving autopromotions due to an abusefilter consequence.
abuselogprivatedetails
View private details of an AbuseLog entry.
acquiretempusername
Acquire a temporary user username and stash it in the current session, if temp account creation is enabled and the current user is logged out. If a name has already been stashed, returns the same name.
aggregategroups
Manage aggregate message groups.
antispoof
Check a username against AntiSpoof's normalisation checks.
block
Block a user.
centralauthtoken
Fetch a centralauthtoken for making an authenticated request to an attached wiki.
centralnoticecdncacheupdatebanner
Request the purge of banner content stored in the CDN (front-end) cache for anonymous users, for the requested banner and language
centralnoticechoicedata
Get data needed to choose a banner for a given project and language
centralnoticequerycampaign
Get all configuration settings for a campaign.
changeauthenticationdata
Change authentication data for the current user.
changecontentmodel
Change the content model of a page
checktoken
Check the validity of a token from `action=query&meta=tokens`.
cirrus-config-dump
Dump of CirrusSearch configuration.
cirrus-mapping-dump
Dump of CirrusSearch mapping for this wiki.
cirrus-profiles-dump
Dump of CirrusSearch profiles for this wiki.
cirrus-settings-dump
Dump of CirrusSearch settings for this wiki.
clearhasmsg
Clears the `hasmsg` flag for the current user.
clientlogin
Log in to the wiki using the interactive flow.
compare
Get the difference between two pages.
createaccount
Create a new user account.
createlocalaccount
Forcibly create a local account. The central account must exist.
delete
Delete a page.
deleteglobalaccount
Delete a global user.
discussiontoolsedit
Post a message on a discussion page.
discussiontoolsfindcomment
Find a comment by its ID or name.
discussiontoolsgetsubscriptions
Get the subscription statuses of given topics.
discussiontoolssubscribe
Subscribe (or unsubscribe) to receive notifications about a topic.
echomarkread
Mark notifications as read for the current user.
echomarkseen
Mark notifications as seen for the current user.
echomute
Mute or unmute notifications from certain users or pages.
edit
Create and edit pages.
editmassmessagelist
Edit a mass message delivery list.
emailuser
Email a user.
expandtemplates
Expands all templates within wikitext.
featuredfeed
Returns a featured content feed.
feedcontributions
Returns a user's contributions feed.
feedrecentchanges
Returns a recent changes feed.
feedthreads
Return a feed of discussion threads.
feedwatchlist
Returns a watchlist feed.
filerevert
Revert a file to an old version.
flow
Allows actions to be taken on Structured Discussions pages.
flow-parsoid-utils
Convert text between wikitext and HTML.
flowthank
Send a public thank-you notification for a Flow comment.
globalblock
Globally block or unblock a user.
globalpreferenceoverrides
Change local overrides for global preferences for the current user.
globalpreferences
Change global preferences of the current user.
globaluserrights
Add/remove a user to/from global groups.
groupreview
Set message group workflow states.
help
Display help for the specified modules.
imagerotate
This module has been disabled.
import
Import a page from another wiki, or from an XML file.
jsonconfig
Allows direct access to JsonConfig subsystem.
languagesearch
Search for language names in any script.
linkaccount
Link an account from a third-party provider to the current user.
login
Log in and get authentication cookies.
logout
Log out and clear session data.
managetags
Perform management tasks relating to change tags.
massmessage
Send a message to a list of pages.
mergehistory
Merge page histories.
move
Move a page.
newslettersubscribe
Subscribe to or unsubscribe from a newsletter.
opensearch
Search the wiki using the OpenSearch protocol.
options
Change preferences of the current user.
paraminfo
Obtain information about API modules.
parse
Parses content and returns parser output.
patrol
Patrol a page or revision.
protect
Change the protection level of a page.
purge
Purge the cache for the given titles.
query
Fetch data from and about MediaWiki.
removeauthenticationdata
Remove authentication data for the current user.
resetpassword
Send a password reset email to a user.
revisiondelete
Delete and undelete revisions.
rollback
Undo the last edit to the page.
rsd
Export an RSD (Really Simple Discovery) schema.
searchtranslations
Search translations.
setglobalaccountstatus
Hide or lock (or unhide or unlock) a global user account.
setnotificationtimestamp
Update the notification timestamp for watched pages.
setpagelanguage
Change the language of a page.
shortenurl
Shorten a long URL into a shorter one.
sitematrix
Get Wikimedia sites list.
spamblacklist
Validate one or more URLs against the spam block list.
streamconfigs
Exposes event stream config. Returns only format=json with formatversion=2.
strikevote
Allows admins to strike or unstrike a vote.
tag
Add or remove change tags from individual revisions or log entries.
templatedata
Fetch data stored by the TemplateData extension.
thank
Send a thank-you notification to an editor.
threadaction
Allows actions to be taken on threads and posts in threaded discussions.
titleblacklist
Validate a page title, filename, or username against the TitleBlacklist.
torblock
Check if an IP address is blocked as a Tor exit node.
transcodereset
Users with the 'transcode-reset' right can reset and re-run a transcode job.
translationaids
Query all translations aids.
translationreview
Mark translations reviewed.
translationstats
Fetch translation statistics
ttmserver
Query suggestions from translation memories.
unblock
Unblock a user.
undelete
Undelete revisions of a deleted page.
unlinkaccount
Remove a linked third-party account from the current user.
upload
Upload a file, or get the status of pending uploads.
userrights
Change a user's group membership.
validatepassword
Validate a password against the wiki's password policies.
watch
Add or remove pages from the current user's watchlist.
webapp-manifest
Returns a webapp manifest.
webauthn
API Module to communicate between server and client during registration/authentication process.
wikilove
Give WikiLove to another user.
bouncehandler
Internal. Receive a bounce email and process it to handle the failing recipient.
categorytree
Internal. Internal module for the CategoryTree extension.
collection
Internal. API module for performing various operations on a wiki user's collection.
cspreport
Internal. Used by browsers to report violations of the Content Security Policy. This module should never be used, except when used automatically by a CSP compliant web browser.
discussiontoolscompare
Internal. Get information about comment changes between two page revisions.
discussiontoolspageinfo
Internal. Returns metadata required to initialize the discussion tools.
discussiontoolspreview
Internal. Preview a message on a discussion page.
fancycaptchareload
Internal. Get a new FancyCaptcha.
jsondata
Internal. Retrieve localized JSON data.
managegroupsynchronizationcache
Internal. Manage group synchronization cache.
managemessagegroups
Internal. Add a message as a rename of an existing message or a new message in the group during imports
oathvalidate
Internal. Validate a two-factor authentication (OATH) token.
parser-migration
Internal. Parse a page with two different parser configurations.
readinglists
Internal. Reading list write operations.
sanitize-mapdata
Internal. Performs data validation for Kartographer extension
scribunto-console
Internal. Internal module for servicing XHR requests from the Scribunto console.
securepollauth
Internal. Allows a remote wiki to authenticate users before granting access to vote in the election.
stashedit
Internal. Prepare an edit in shared cache.
timedtext
Internal. Provides timed text content for usage by <track> elements
translationcheck
Internal. Validate translations.
translationentitysearch
Internal. Search for message groups and messages
ulslocalization
Internal. Get the localization of ULS in the given language.
ulssetlang
Internal. Update user's preferred interface language.
visualeditor
Internal. Returns HTML5 for a page from the Parsoid service.
visualeditoredit
Internal. Save an HTML5 page to MediaWiki (converted to wikitext via the Parsoid service).
wikimediaeventsblockededit
Internal. Log information about blocked edit attemptsOne of the following values: abusefiltercheckmatch, abusefilterchecksyntax, abusefilterevalexpression, abusefilterunblockautopromote, abuselogprivatedetails, acquiretempusername, aggregategroups, antispoof, block, centralauthtoken, centralnoticecdncacheupdatebanner, centralnoticechoicedata, centralnoticequerycampaign, changeauthenticationdata, changecontentmodel, checktoken, cirrus-config-dump, cirrus-mapping-dump, cirrus-profiles-dump, cirrus-settings-dump, clearhasmsg, clientlogin, compare, createaccount, createlocalaccount, delete, deleteglobalaccount, discussiontoolsedit, discussiontoolsfindcomment, discussiontoolsgetsubscriptions, discussiontoolssubscribe, echomarkread, echomarkseen, echomute, edit, editmassmessagelist, emailuser, expandtemplates, featuredfeed, feedcontributions, feedrecentchanges, feedthreads, feedwatchlist, filerevert, flow-parsoid-utils, flow, flowthank, globalblock, globalpreferenceoverrides, globalpreferences, globaluserrights, groupreview, help, imagerotate, import, jsonconfig, languagesearch, linkaccount, login, logout, managetags, massmessage, mergehistory, move, newslettersubscribe, opensearch, options, paraminfo, parse, patrol, protect, purge, query, removeauthenticationdata, resetpassword, revisiondelete, rollback, rsd, searchtranslations, setglobalaccountstatus, setnotificationtimestamp, setpagelanguage, shortenurl, sitematrix, spamblacklist, streamconfigs, strikevote, tag, templatedata, thank, threadaction, titleblacklist, torblock, transcodereset, translationaids, translationreview, translationstats, ttmserver, unblock, undelete, unlinkaccount, upload, userrights, validatepassword, watch, webapp-manifest, webauthn, wikilove, bouncehandler, categorytree, collection, cspreport, discussiontoolscompare, discussiontoolspageinfo, discussiontoolspreview, fancycaptchareload, jsondata, managegroupsynchronizationcache, managemessagegroups, oathvalidate, parser-migration, readinglists, sanitize-mapdata, scribunto-console, securepollauth, stashedit, timedtext, translationcheck, translationentitysearch, ulslocalization, ulssetlang, visualeditor, visualeditoredit, wikimediaeventsblockededitDefault: helpformatThe format of the output.

json
Output data in JSON format.
jsonfm
Output data in JSON format (pretty-print in HTML).
none
Output nothing.
php
Output data in serialized PHP format.
phpfm
Output data in serialized PHP format (pretty-print in HTML).
rawfm
Output data, including debugging elements, in JSON format (pretty-print in HTML).
xml
Output data in XML format.
xmlfm
Output data in XML format (pretty-print in HTML).One of the following values: json, jsonfm, none, php, phpfm, rawfm, xml, xmlfmDefault: jsonfmmaxlagMaximum lag can be used when MediaWiki is installed on a database replicated cluster. To save actions causing any more site replication lag, this parameter can make the client wait until the replication lag is less than the specified value. In case of excessive lag, error code `maxlag` is returned with a message like `Waiting for $host: $lag seconds lagged`.  
See Manual: Maxlag parameter for more information.

Type: integersmaxageSet the `s-maxage` HTTP cache control header to this many seconds. Errors are never cached.

Type: integerThe value must be no less than 0.Default: 0maxageSet the `max-age` HTTP cache control header to this many seconds. Errors are never cached.

Type: integerThe value must be no less than 0.Default: 0assertVerify that the user is logged in (including possibly as a temporary user) if set to `user`, *not* logged in if set to `anon`, or has the bot user right if `bot`.

One of the following values: anon, bot, userassertuserVerify the current user is the named user.

Type: user, by any of username and Temporary userrequestidAny value given here will be included in the response. May be used to distinguish requests.

servedbyInclude the hostname that served the request in the results.

Type: boolean (details)curtimestampInclude the current timestamp in the result.

Type: boolean (details)responselanginfoInclude the languages used for uselang and errorlang in the result.

Type: boolean (details)originWhen accessing the API using a cross-domain AJAX request (CORS), set this to the originating domain. This must be included in any pre-flight request, and therefore must be part of the request URI (not the POST body).

For authenticated requests, this must match one of the origins in the `Origin` header exactly, so it has to be set to something like `https://en.wikipedia.org` or `https://meta.wikimedia.org`. If this parameter does not match the `Origin` header, a 403 response will be returned. If this parameter matches the `Origin` header and the origin is allowed, the `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials` headers will be set.

For non-authenticated requests, specify the value `\*`. This will cause the `Access-Control-Allow-Origin` header to be set, but `Access-Control-Allow-Credentials` will be `false` and all user-specific data will be restricted.

uselangLanguage to use for message translations. `action=query&meta=siteinfo` with `siprop=languages` returns a list of language codes, or specify `user` to use the current user's language preference, or specify `content` to use this wiki's content language.

Default: uservariantVariant of the language. Only works if the base language supports variant conversion.

errorformatFormat to use for warning and error text output

plaintext
Wikitext with HTML tags removed and entities replaced.
wikitext
Unparsed wikitext.
html
HTML
raw
Message key and parameters.
none
No text output, only the error codes.
bc
Format used prior to MediaWiki 1.29. errorlang and errorsuselocal are ignored.One of the following values: bc, html, none, plaintext, raw, wikitextDefault: bcerrorlangLanguage to use for warnings and errors. `action=query&meta=siteinfo` with `siprop=languages` returns a list of language codes, or specify `content` to use this wiki's content language, or specify `uselang` to use the same value as the uselang parameter.

Default: uselangerrorsuselocalIf given, error texts will use locally-customized messages from the MediaWiki namespace.

Type: boolean (details)centralauthtokenWhen accessing the API using a cross-domain AJAX request (CORS), use this to authenticate as the current SUL user. Use `action=centralauthtoken` on this wiki to retrieve the token, before making the CORS request. Each token may only be used once, and expires after 10 seconds. This should be included in any pre-flight request, and therefore should be included in the request URI (not the POST body).

Examples:Help for the main module.api.php?action=help [open in sandbox]All help in one page.api.php?action=help&recursivesubmodules=1 [open in sandbox]
Permissions:writeapiUse of the write APIGranted to: all, user and botapihighlimitsUse higher limits in API queries (slow queries: 500; fast queries: 5000). The limits for slow queries also apply to multivalue parameters.Granted to: bot and sysop

Other APIs
----------

If you do not find what you are looking for in this API documentation, there are many other APIs related to Wikimedia projects.

For the REST API included with MediaWiki 1.35 and later, see API:REST API.

This table: view **·** talk **·** edit
| API
 | Availability
 | URL base
 | Example
 |
| --- | --- | --- | --- |
|  ****MediaWiki Action API**** | Included with MediaWiki
Enabled on Wikimedia projects
 | /api.php
 | https://en.wikipedia.org/w/api.php?action=query&prop=info&titles=Earth |
|  **MediaWiki REST API** | Included with MediaWiki 1.35+
Enabled on Wikimedia projects
 | /rest.php
 | https://en.wikipedia.org/w/rest.php/v1/page/Earth |
|  **Wikimedia REST API** | Not included with MediaWiki
Available for Wikimedia projects only
 | /api/rest
 | https://en.wikipedia.org/api/rest\_v1/page/title/Earth |
|  For commercial-scale APIs for Wikimedia projects, see **Wikimedia Enterprise** |

Code stewardship
----------------

* Maintained by API Platform Team.
* Live chat (IRC): #mediawiki-core connect
* Issue tracker: Phabricator MediaWiki-Action-API (Report an issue)

Retrieved from "https://www.mediawiki.org/w/index.php?title=API:Main\_page&oldid=6161467"
Categories: * MediaWiki action API
* MediaWiki development
* Manual
* Documentation
* New contributors

* This page was last edited on 20 October 2023, at 21:32.
* Text is available under the Creative Commons Attribution-ShareAlike License;
additional terms may apply.
See Terms of Use for details.

* Privacy policy
* About mediawiki.org
* Disclaimers
* Code of Conduct
* Developers
* Statistics
* Cookie statement
* Mobile view

* 
* 

* Toggle limited content width