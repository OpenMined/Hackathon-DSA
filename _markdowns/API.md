::: mw-page-container-inner
::: {#content .mw-body role="main"}
::: {.mw-body-header .vector-page-titlebar}
:::

::: {#bodyContent .vector-body}
::: {#mw-content-text .mw-body-content}
::: {.mw-content-ltr .mw-parser-output}
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------
  ![](//upload.wikimedia.org/wikipedia/commons/thumb/f/f6/API_-_The_Noun_Project.svg/30px-API_-_The_Noun_Project.svg.png){.mw-file-element srcset="http://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/API_-_The_Noun_Project.svg/45px-API_-_The_Noun_Project.svg.png 1.5x, http://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/API_-_The_Noun_Project.svg/60px-API_-_The_Noun_Project.svg.png 2x" width="30"}       This page is part of the [MediaWiki Action API](/wiki/Special:MyLanguage/API:Main_page) documentation.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------

This page provides an overview of the MediaWiki **Action API** ,
represented by the ` api.php ` endpoint. This page is intended for
technical contributors and software developers who wish to understand
and use the MediaWiki Action API.

## [ Quick Start ]{#Quick_Start .mw-headline}

Get the contents of an article on English Wikipedia in HTML:

### [ Endpoint ]{#Endpoint .mw-headline}

**All Wikimedia wikis have endpoints that follow this pattern:**
` https://www.example.org/w/api.php `

To see the endpoint URL on a particular wiki, see section \"Entry point
URLs\" on the Special:Version page.

## [ Introduction ]{#Introduction .mw-headline}

The MediaWiki Action API is a [web
service](https://en.wikipedia.org/wiki/Web_service){.extiw} that allows
access to some wiki features like authentication, page operations, and
search. It can provide [meta
information](/wiki/Special:MyLanguage/API:Meta) about the wiki and the
logged-in user.

### [ Uses for the MediaWiki Action API ]{#Uses_for_the_MediaWiki_Action_API .mw-headline}

-   Monitor a MediaWiki installation
-   [Create a
    bot](https://en.wikipedia.org/wiki/Wikipedia:Creating_a_bot){.extiw}
    to maintain a MediaWiki installation
-   Log in to a wiki, access data, and post changes by making HTTP
    requests to the web service

### [ Getting started with MediaWiki Action API ]{#Getting_started_with_MediaWiki_Action_API .mw-headline}

Before you start using the MediaWiki Action API, you should review the
following pages:

## [ API documentation ]{#API_documentation .mw-headline}

<div>

<div>

::: {.apihelp-block .apihelp-flags}
-   [ Source: MediaWiki ]{.apihelp-source}
-   [ License: [ GPL-2.0-or-later
    ](/wiki/Special:Version/License/MediaWiki) ]{.apihelp-license}
:::

**Status:** The MediaWiki API is a mature and stable interface that is
actively supported and improved. While we try to avoid it, we may
occasionally need to make breaking changes; subscribe to [the
mediawiki-api-announce mailing
list](https://lists.wikimedia.org/hyperkitty/list/mediawiki-api-announce@lists.wikimedia.org/){.external
.text} for notice of updates.

**Erroneous requests:** When erroneous requests are sent to the API, an
HTTP header will be sent with the key \"MediaWiki-API-Error\" and then
both the value of the header and the error code sent back will be set to
the same value. For more information see [API: Errors and
warnings](/wiki/Special:MyLanguage/API:Errors_and_warnings) .

**Testing:** For ease of testing API requests, see
[Special:ApiSandbox](/wiki/Special:ApiSandbox) .

::: {.apihelp-block .apihelp-parameters}

[ action ]{#main:action}

:   Which action to perform.

     [abusefiltercheckmatch](/w/api.php?action=help&modules=abusefiltercheckmatch) 
    :   Check to see if an AbuseFilter matches a set of variables, an
        edit, or a logged AbuseFilter event.

     [abusefilterchecksyntax](/w/api.php?action=help&modules=abusefilterchecksyntax) 
    :   Check syntax of an AbuseFilter filter.

     [abusefilterevalexpression](/w/api.php?action=help&modules=abusefilterevalexpression) 
    :   Evaluates an AbuseFilter expression.

     [abusefilterunblockautopromote](/w/api.php?action=help&modules=abusefilterunblockautopromote) 
    :   Unblocks a user from receiving autopromotions due to an
        abusefilter consequence.

     [abuselogprivatedetails](/w/api.php?action=help&modules=abuselogprivatedetails) 
    :   View private details of an AbuseLog entry.

     [acquiretempusername](/w/api.php?action=help&modules=acquiretempusername) 
    :   Acquire a temporary user username and stash it in the current
        session, if temp account creation is enabled and the current
        user is logged out. If a name has already been stashed, returns
        the same name.

     [aggregategroups](/w/api.php?action=help&modules=aggregategroups) 
    :   Manage aggregate message groups.

     [antispoof](/w/api.php?action=help&modules=antispoof) 
    :   Check a username against AntiSpoof\'s normalisation checks.

     [block](/w/api.php?action=help&modules=block) 
    :   Block a user.

     [centralauthtoken](/w/api.php?action=help&modules=centralauthtoken) 
    :   Fetch a centralauthtoken for making an authenticated request to
        an attached wiki.

     [centralnoticecdncacheupdatebanner](/w/api.php?action=help&modules=centralnoticecdncacheupdatebanner) 
    :   Request the purge of banner content stored in the CDN
        (front-end) cache for anonymous users, for the requested banner
        and language

     [centralnoticechoicedata](/w/api.php?action=help&modules=centralnoticechoicedata) 
    :   Get data needed to choose a banner for a given project and
        language

     [centralnoticequerycampaign](/w/api.php?action=help&modules=centralnoticequerycampaign) 
    :   Get all configuration settings for a campaign.

     [changeauthenticationdata](/w/api.php?action=help&modules=changeauthenticationdata) 
    :   Change authentication data for the current user.

     [changecontentmodel](/w/api.php?action=help&modules=changecontentmodel) 
    :   Change the content model of a page

     [checktoken](/w/api.php?action=help&modules=checktoken) 
    :   Check the validity of a token from [
        [action=query&meta=tokens](/w/api.php?action=help&modules=query%2Btokens)
        ]{.kbd} .

     [cirrus-config-dump](/w/api.php?action=help&modules=cirrus-config-dump) 
    :   Dump of CirrusSearch configuration.

     [cirrus-mapping-dump](/w/api.php?action=help&modules=cirrus-mapping-dump) 
    :   Dump of CirrusSearch mapping for this wiki.

     [cirrus-profiles-dump](/w/api.php?action=help&modules=cirrus-profiles-dump) 
    :   Dump of CirrusSearch profiles for this wiki.

     [cirrus-settings-dump](/w/api.php?action=help&modules=cirrus-settings-dump) 
    :   Dump of CirrusSearch settings for this wiki.

     [clearhasmsg](/w/api.php?action=help&modules=clearhasmsg) 
    :   Clears the ` hasmsg ` flag for the current user.

     [clientlogin](/w/api.php?action=help&modules=clientlogin) 
    :   Log in to the wiki using the interactive flow.

     [compare](/w/api.php?action=help&modules=compare) 
    :   Get the difference between two pages.

     [createaccount](/w/api.php?action=help&modules=createaccount) 
    :   Create a new user account.

     [createlocalaccount](/w/api.php?action=help&modules=createlocalaccount) 
    :   Forcibly create a local account. The central account must exist.

     [delete](/w/api.php?action=help&modules=delete) 
    :   Delete a page.

     [deleteglobalaccount](/w/api.php?action=help&modules=deleteglobalaccount) 
    :   Delete a global user.

     [discussiontoolsedit](/w/api.php?action=help&modules=discussiontoolsedit) 
    :   Post a message on a discussion page.

     [discussiontoolsfindcomment](/w/api.php?action=help&modules=discussiontoolsfindcomment) 
    :   Find a comment by its ID or name.

     [discussiontoolsgetsubscriptions](/w/api.php?action=help&modules=discussiontoolsgetsubscriptions) 
    :   Get the subscription statuses of given topics.

     [discussiontoolssubscribe](/w/api.php?action=help&modules=discussiontoolssubscribe) 
    :   Subscribe (or unsubscribe) to receive notifications about a
        topic.

     [echomarkread](/w/api.php?action=help&modules=echomarkread) 
    :   Mark notifications as read for the current user.

     [echomarkseen](/w/api.php?action=help&modules=echomarkseen) 
    :   Mark notifications as seen for the current user.

     [echomute](/w/api.php?action=help&modules=echomute) 
    :   Mute or unmute notifications from certain users or pages.

     [edit](/w/api.php?action=help&modules=edit) 
    :   Create and edit pages.

     [editmassmessagelist](/w/api.php?action=help&modules=editmassmessagelist) 
    :   Edit a mass message delivery list.

     [emailuser](/w/api.php?action=help&modules=emailuser) 
    :   Email a user.

     [expandtemplates](/w/api.php?action=help&modules=expandtemplates) 
    :   Expands all templates within wikitext.

     [fancycaptchareload](/w/api.php?action=help&modules=fancycaptchareload) 
    :   Get a new FancyCaptcha.

     [featuredfeed](/w/api.php?action=help&modules=featuredfeed) 
    :   Returns a featured content feed.

     [feedcontributions](/w/api.php?action=help&modules=feedcontributions) 
    :   Returns a user\'s contributions feed.

     [feedrecentchanges](/w/api.php?action=help&modules=feedrecentchanges) 
    :   Returns a recent changes feed.

     [feedthreads](/w/api.php?action=help&modules=feedthreads) 
    :   Return a feed of discussion threads.

     [feedwatchlist](/w/api.php?action=help&modules=feedwatchlist) 
    :   Returns a watchlist feed.

     [filerevert](/w/api.php?action=help&modules=filerevert) 
    :   Revert a file to an old version.

     [flow](/w/api.php?action=help&modules=flow) 
    :   Allows actions to be taken on Structured Discussions pages.

     [flow-parsoid-utils](/w/api.php?action=help&modules=flow-parsoid-utils) 
    :   Convert text between wikitext and HTML.

     [flowthank](/w/api.php?action=help&modules=flowthank) 
    :   Send a public thank-you notification for a Flow comment.

     [globalblock](/w/api.php?action=help&modules=globalblock) 
    :   Globally block or unblock a user.

     [globalpreferenceoverrides](/w/api.php?action=help&modules=globalpreferenceoverrides) 
    :   Change local overrides for global preferences for the current
        user.

     [globalpreferences](/w/api.php?action=help&modules=globalpreferences) 
    :   Change global preferences of the current user.

     [globaluserrights](/w/api.php?action=help&modules=globaluserrights) 
    :   Add/remove a user to/from global groups.

     [groupreview](/w/api.php?action=help&modules=groupreview) 
    :   Set message group workflow states.

     [help](/w/api.php?action=help&modules=help) 
    :   Display help for the specified modules.

     [imagerotate](/w/api.php?action=help&modules=imagerotate) 
    :   This module has been disabled.

     [import](/w/api.php?action=help&modules=import) 
    :   Import a page from another wiki, or from an XML file.

     [jsonconfig](/w/api.php?action=help&modules=jsonconfig) 
    :   Allows direct access to JsonConfig subsystem.

     [languagesearch](/w/api.php?action=help&modules=languagesearch) 
    :   Search for language names in any script.

     [linkaccount](/w/api.php?action=help&modules=linkaccount) 
    :   Link an account from a third-party provider to the current user.

     [login](/w/api.php?action=help&modules=login) 
    :   Log in and get authentication cookies.

     [logout](/w/api.php?action=help&modules=logout) 
    :   Log out and clear session data.

     [managetags](/w/api.php?action=help&modules=managetags) 
    :   Perform management tasks relating to change tags.

     [massmessage](/w/api.php?action=help&modules=massmessage) 
    :   Send a message to a list of pages.

     [mergehistory](/w/api.php?action=help&modules=mergehistory) 
    :   Merge page histories.

     [move](/w/api.php?action=help&modules=move) 
    :   Move a page.

     [newslettersubscribe](/w/api.php?action=help&modules=newslettersubscribe) 
    :   Subscribe to or unsubscribe from a newsletter.

     [opensearch](/w/api.php?action=help&modules=opensearch) 
    :   Search the wiki using the OpenSearch protocol.

     [options](/w/api.php?action=help&modules=options) 
    :   Change preferences of the current user.

     [paraminfo](/w/api.php?action=help&modules=paraminfo) 
    :   Obtain information about API modules.

     [parse](/w/api.php?action=help&modules=parse) 
    :   Parses content and returns parser output.

     [patrol](/w/api.php?action=help&modules=patrol) 
    :   Patrol a page or revision.

     [protect](/w/api.php?action=help&modules=protect) 
    :   Change the protection level of a page.

     [purge](/w/api.php?action=help&modules=purge) 
    :   Purge the cache for the given titles.

     [query](/w/api.php?action=help&modules=query) 
    :   Fetch data from and about MediaWiki.

     [removeauthenticationdata](/w/api.php?action=help&modules=removeauthenticationdata) 
    :   Remove authentication data for the current user.

     [resetpassword](/w/api.php?action=help&modules=resetpassword) 
    :   Send a password reset email to a user.

     [revisiondelete](/w/api.php?action=help&modules=revisiondelete) 
    :   Delete and undelete revisions.

     [rollback](/w/api.php?action=help&modules=rollback) 
    :   Undo the last edit to the page.

     [rsd](/w/api.php?action=help&modules=rsd) 
    :   Export an RSD (Really Simple Discovery) schema.

     [searchtranslations](/w/api.php?action=help&modules=searchtranslations) 
    :   Search translations.

     [setglobalaccountstatus](/w/api.php?action=help&modules=setglobalaccountstatus) 
    :   Hide or lock (or unhide or unlock) a global user account.

     [setnotificationtimestamp](/w/api.php?action=help&modules=setnotificationtimestamp) 
    :   Update the notification timestamp for watched pages.

     [setpagelanguage](/w/api.php?action=help&modules=setpagelanguage) 
    :   Change the language of a page.

     [shortenurl](/w/api.php?action=help&modules=shortenurl) 
    :   Shorten a long URL into a shorter one.

     [sitematrix](/w/api.php?action=help&modules=sitematrix) 
    :   Get Wikimedia sites list.

     [spamblacklist](/w/api.php?action=help&modules=spamblacklist) 
    :   Validate one or more URLs against the spam block list.

     [streamconfigs](/w/api.php?action=help&modules=streamconfigs) 
    :   Exposes event stream config. Returns only format=json with
        formatversion=2.

     [strikevote](/w/api.php?action=help&modules=strikevote) 
    :   Allows admins to strike or unstrike a vote.

     [tag](/w/api.php?action=help&modules=tag) 
    :   Add or remove change tags from individual revisions or log
        entries.

     [templatedata](/w/api.php?action=help&modules=templatedata) 
    :   Fetch data stored by the TemplateData extension.

     [thank](/w/api.php?action=help&modules=thank) 
    :   Send a thank-you notification to an editor.

     [threadaction](/w/api.php?action=help&modules=threadaction) 
    :   Allows actions to be taken on threads and posts in threaded
        discussions.

     [titleblacklist](/w/api.php?action=help&modules=titleblacklist) 
    :   Validate a page title, filename, or username against the
        TitleBlacklist.

     [torblock](/w/api.php?action=help&modules=torblock) 
    :   Check if an IP address is blocked as a Tor exit node.

     [transcodereset](/w/api.php?action=help&modules=transcodereset) 
    :   Users with the \'transcode-reset\' right can reset and re-run a
        transcode job.

     [translationaids](/w/api.php?action=help&modules=translationaids) 
    :   Query all translations aids.

     [translationreview](/w/api.php?action=help&modules=translationreview) 
    :   Mark translations reviewed.

     [translationstats](/w/api.php?action=help&modules=translationstats) 
    :   Fetch translation statistics

     [ttmserver](/w/api.php?action=help&modules=ttmserver) 
    :   Query suggestions from translation memories.

     [unblock](/w/api.php?action=help&modules=unblock) 
    :   Unblock a user.

     [undelete](/w/api.php?action=help&modules=undelete) 
    :   Undelete revisions of a deleted page.

     [unlinkaccount](/w/api.php?action=help&modules=unlinkaccount) 
    :   Remove a linked third-party account from the current user.

     [upload](/w/api.php?action=help&modules=upload) 
    :   Upload a file, or get the status of pending uploads.

     [userrights](/w/api.php?action=help&modules=userrights) 
    :   Change a user\'s group membership.

     [validatepassword](/w/api.php?action=help&modules=validatepassword) 
    :   Validate a password against the wiki\'s password policies.

     [watch](/w/api.php?action=help&modules=watch) 
    :   Add or remove pages from the current user\'s watchlist.

     [webapp-manifest](/w/api.php?action=help&modules=webapp-manifest) 
    :   Returns a webapp manifest.

     [webauthn](/w/api.php?action=help&modules=webauthn) 
    :   API Module to communicate between server and client during
        registration/authentication process.

     [wikilove](/w/api.php?action=help&modules=wikilove) 
    :   Give WikiLove to another user.

     [bouncehandler](/w/api.php?action=help&modules=bouncehandler) 
    :   [ Internal. ]{.apihelp-internal} Receive a bounce email and
        process it to handle the failing recipient.

     [categorytree](/w/api.php?action=help&modules=categorytree) 
    :   [ Internal. ]{.apihelp-internal} Internal module for the
        CategoryTree extension.

     [collection](/w/api.php?action=help&modules=collection) 
    :   [ Internal. ]{.apihelp-internal} API module for performing
        various operations on a wiki user\'s collection.

     [cspreport](/w/api.php?action=help&modules=cspreport) 
    :   [ Internal. ]{.apihelp-internal} Used by browsers to report
        violations of the Content Security Policy. This module should
        never be used, except when used automatically by a CSP compliant
        web browser.

     [discussiontoolscompare](/w/api.php?action=help&modules=discussiontoolscompare) 
    :   [ Internal. ]{.apihelp-internal} Get information about comment
        changes between two page revisions.

     [discussiontoolspageinfo](/w/api.php?action=help&modules=discussiontoolspageinfo) 
    :   [ Internal. ]{.apihelp-internal} Returns metadata required to
        initialize the discussion tools.

     [discussiontoolspreview](/w/api.php?action=help&modules=discussiontoolspreview) 
    :   [ Internal. ]{.apihelp-internal} Preview a message on a
        discussion page.

     [jsondata](/w/api.php?action=help&modules=jsondata) 
    :   [ Internal. ]{.apihelp-internal} Retrieve localized JSON data.

     [managegroupsynchronizationcache](/w/api.php?action=help&modules=managegroupsynchronizationcache) 
    :   [ Internal. ]{.apihelp-internal} Manage group synchronization
        cache.

     [managemessagegroups](/w/api.php?action=help&modules=managemessagegroups) 
    :   [ Internal. ]{.apihelp-internal} Add a message as a rename of an
        existing message or a new message in the group during imports

     [oathvalidate](/w/api.php?action=help&modules=oathvalidate) 
    :   [ Internal. ]{.apihelp-internal} Validate a two-factor
        authentication (OATH) token.

     [parser-migration](/w/api.php?action=help&modules=parser-migration) 
    :   [ Internal. ]{.apihelp-internal} Parse a page with two different
        parser configurations.

     [readinglists](/w/api.php?action=help&modules=readinglists) 
    :   [ Internal. ]{.apihelp-internal} Reading list write operations.

     [sanitize-mapdata](/w/api.php?action=help&modules=sanitize-mapdata) 
    :   [ Internal. ]{.apihelp-internal} Performs data validation for
        Kartographer extension

     [scribunto-console](/w/api.php?action=help&modules=scribunto-console) 
    :   [ Internal. ]{.apihelp-internal} Internal module for servicing
        XHR requests from the Scribunto console.

     [securepollauth](/w/api.php?action=help&modules=securepollauth) 
    :   [ Internal. ]{.apihelp-internal} Allows a remote wiki to
        authenticate users before granting access to vote in the
        election.

     [stashedit](/w/api.php?action=help&modules=stashedit) 
    :   [ Internal. ]{.apihelp-internal} Prepare an edit in shared
        cache.

     [timedtext](/w/api.php?action=help&modules=timedtext) 
    :   [ Internal. ]{.apihelp-internal} Provides timed text content for
        usage by \<track\> elements

     [translationcheck](/w/api.php?action=help&modules=translationcheck) 
    :   [ Internal. ]{.apihelp-internal} Validate translations.

     [translationentitysearch](/w/api.php?action=help&modules=translationentitysearch) 
    :   [ Internal. ]{.apihelp-internal} Search for message groups and
        messages

     [ulslocalization](/w/api.php?action=help&modules=ulslocalization) 
    :   [ Internal. ]{.apihelp-internal} Get the localization of ULS in
        the given language.

     [ulssetlang](/w/api.php?action=help&modules=ulssetlang) 
    :   [ Internal. ]{.apihelp-internal} Update user\'s preferred
        interface language.

     [visualeditor](/w/api.php?action=help&modules=visualeditor) 
    :   [ Internal. ]{.apihelp-internal} Returns HTML5 for a page from
        the Parsoid service.

     [visualeditoredit](/w/api.php?action=help&modules=visualeditoredit) 
    :   [ Internal. ]{.apihelp-internal} Save an HTML5 page to MediaWiki
        (converted to wikitext via the Parsoid service).

     [wikimediaeventsblockededit](/w/api.php?action=help&modules=wikimediaeventsblockededit) 
    :   [ Internal. ]{.apihelp-internal} Log information about blocked
        edit attempts

:   One of the following values: [ abusefiltercheckmatch
    ](/w/api.php?action=help&modules=abusefiltercheckmatch) , [
    abusefilterchecksyntax
    ](/w/api.php?action=help&modules=abusefilterchecksyntax) , [
    abusefilterevalexpression
    ](/w/api.php?action=help&modules=abusefilterevalexpression) , [
    abusefilterunblockautopromote
    ](/w/api.php?action=help&modules=abusefilterunblockautopromote) , [
    abuselogprivatedetails
    ](/w/api.php?action=help&modules=abuselogprivatedetails) , [
    acquiretempusername
    ](/w/api.php?action=help&modules=acquiretempusername) , [
    aggregategroups ](/w/api.php?action=help&modules=aggregategroups) ,
    [ antispoof ](/w/api.php?action=help&modules=antispoof) , [ block
    ](/w/api.php?action=help&modules=block) , [ centralauthtoken
    ](/w/api.php?action=help&modules=centralauthtoken) , [
    centralnoticecdncacheupdatebanner
    ](/w/api.php?action=help&modules=centralnoticecdncacheupdatebanner)
    , [ centralnoticechoicedata
    ](/w/api.php?action=help&modules=centralnoticechoicedata) , [
    centralnoticequerycampaign
    ](/w/api.php?action=help&modules=centralnoticequerycampaign) , [
    changeauthenticationdata
    ](/w/api.php?action=help&modules=changeauthenticationdata) , [
    changecontentmodel
    ](/w/api.php?action=help&modules=changecontentmodel) , [ checktoken
    ](/w/api.php?action=help&modules=checktoken) , [ cirrus-config-dump
    ](/w/api.php?action=help&modules=cirrus-config-dump) , [
    cirrus-mapping-dump
    ](/w/api.php?action=help&modules=cirrus-mapping-dump) , [
    cirrus-profiles-dump
    ](/w/api.php?action=help&modules=cirrus-profiles-dump) , [
    cirrus-settings-dump
    ](/w/api.php?action=help&modules=cirrus-settings-dump) , [
    clearhasmsg ](/w/api.php?action=help&modules=clearhasmsg) , [
    clientlogin ](/w/api.php?action=help&modules=clientlogin) , [
    compare ](/w/api.php?action=help&modules=compare) , [ createaccount
    ](/w/api.php?action=help&modules=createaccount) , [
    createlocalaccount
    ](/w/api.php?action=help&modules=createlocalaccount) , [ delete
    ](/w/api.php?action=help&modules=delete) , [ deleteglobalaccount
    ](/w/api.php?action=help&modules=deleteglobalaccount) , [
    discussiontoolsedit
    ](/w/api.php?action=help&modules=discussiontoolsedit) , [
    discussiontoolsfindcomment
    ](/w/api.php?action=help&modules=discussiontoolsfindcomment) , [
    discussiontoolsgetsubscriptions
    ](/w/api.php?action=help&modules=discussiontoolsgetsubscriptions) ,
    [ discussiontoolssubscribe
    ](/w/api.php?action=help&modules=discussiontoolssubscribe) , [
    echomarkread ](/w/api.php?action=help&modules=echomarkread) , [
    echomarkseen ](/w/api.php?action=help&modules=echomarkseen) , [
    echomute ](/w/api.php?action=help&modules=echomute) , [ edit
    ](/w/api.php?action=help&modules=edit) , [ editmassmessagelist
    ](/w/api.php?action=help&modules=editmassmessagelist) , [ emailuser
    ](/w/api.php?action=help&modules=emailuser) , [ expandtemplates
    ](/w/api.php?action=help&modules=expandtemplates) , [
    fancycaptchareload
    ](/w/api.php?action=help&modules=fancycaptchareload) , [
    featuredfeed ](/w/api.php?action=help&modules=featuredfeed) , [
    feedcontributions
    ](/w/api.php?action=help&modules=feedcontributions) , [
    feedrecentchanges
    ](/w/api.php?action=help&modules=feedrecentchanges) , [ feedthreads
    ](/w/api.php?action=help&modules=feedthreads) , [ feedwatchlist
    ](/w/api.php?action=help&modules=feedwatchlist) , [ filerevert
    ](/w/api.php?action=help&modules=filerevert) , [ flow-parsoid-utils
    ](/w/api.php?action=help&modules=flow-parsoid-utils) , [ flow
    ](/w/api.php?action=help&modules=flow) , [ flowthank
    ](/w/api.php?action=help&modules=flowthank) , [ globalblock
    ](/w/api.php?action=help&modules=globalblock) , [
    globalpreferenceoverrides
    ](/w/api.php?action=help&modules=globalpreferenceoverrides) , [
    globalpreferences
    ](/w/api.php?action=help&modules=globalpreferences) , [
    globaluserrights ](/w/api.php?action=help&modules=globaluserrights)
    , [ groupreview ](/w/api.php?action=help&modules=groupreview) , [
    help ](/w/api.php?action=help&modules=help) , [ imagerotate
    ](/w/api.php?action=help&modules=imagerotate) , [ import
    ](/w/api.php?action=help&modules=import) , [ jsonconfig
    ](/w/api.php?action=help&modules=jsonconfig) , [ languagesearch
    ](/w/api.php?action=help&modules=languagesearch) , [ linkaccount
    ](/w/api.php?action=help&modules=linkaccount) , [ login
    ](/w/api.php?action=help&modules=login) , [ logout
    ](/w/api.php?action=help&modules=logout) , [ managetags
    ](/w/api.php?action=help&modules=managetags) , [ massmessage
    ](/w/api.php?action=help&modules=massmessage) , [ mergehistory
    ](/w/api.php?action=help&modules=mergehistory) , [ move
    ](/w/api.php?action=help&modules=move) , [ newslettersubscribe
    ](/w/api.php?action=help&modules=newslettersubscribe) , [ opensearch
    ](/w/api.php?action=help&modules=opensearch) , [ options
    ](/w/api.php?action=help&modules=options) , [ paraminfo
    ](/w/api.php?action=help&modules=paraminfo) , [ parse
    ](/w/api.php?action=help&modules=parse) , [ patrol
    ](/w/api.php?action=help&modules=patrol) , [ protect
    ](/w/api.php?action=help&modules=protect) , [ purge
    ](/w/api.php?action=help&modules=purge) , [ query
    ](/w/api.php?action=help&modules=query) , [ removeauthenticationdata
    ](/w/api.php?action=help&modules=removeauthenticationdata) , [
    resetpassword ](/w/api.php?action=help&modules=resetpassword) , [
    revisiondelete ](/w/api.php?action=help&modules=revisiondelete) , [
    rollback ](/w/api.php?action=help&modules=rollback) , [ rsd
    ](/w/api.php?action=help&modules=rsd) , [ searchtranslations
    ](/w/api.php?action=help&modules=searchtranslations) , [
    setglobalaccountstatus
    ](/w/api.php?action=help&modules=setglobalaccountstatus) , [
    setnotificationtimestamp
    ](/w/api.php?action=help&modules=setnotificationtimestamp) , [
    setpagelanguage ](/w/api.php?action=help&modules=setpagelanguage) ,
    [ shortenurl ](/w/api.php?action=help&modules=shortenurl) , [
    sitematrix ](/w/api.php?action=help&modules=sitematrix) , [
    spamblacklist ](/w/api.php?action=help&modules=spamblacklist) , [
    streamconfigs ](/w/api.php?action=help&modules=streamconfigs) , [
    strikevote ](/w/api.php?action=help&modules=strikevote) , [ tag
    ](/w/api.php?action=help&modules=tag) , [ templatedata
    ](/w/api.php?action=help&modules=templatedata) , [ thank
    ](/w/api.php?action=help&modules=thank) , [ threadaction
    ](/w/api.php?action=help&modules=threadaction) , [ titleblacklist
    ](/w/api.php?action=help&modules=titleblacklist) , [ torblock
    ](/w/api.php?action=help&modules=torblock) , [ transcodereset
    ](/w/api.php?action=help&modules=transcodereset) , [ translationaids
    ](/w/api.php?action=help&modules=translationaids) , [
    translationreview
    ](/w/api.php?action=help&modules=translationreview) , [
    translationstats ](/w/api.php?action=help&modules=translationstats)
    , [ ttmserver ](/w/api.php?action=help&modules=ttmserver) , [
    unblock ](/w/api.php?action=help&modules=unblock) , [ undelete
    ](/w/api.php?action=help&modules=undelete) , [ unlinkaccount
    ](/w/api.php?action=help&modules=unlinkaccount) , [ upload
    ](/w/api.php?action=help&modules=upload) , [ userrights
    ](/w/api.php?action=help&modules=userrights) , [ validatepassword
    ](/w/api.php?action=help&modules=validatepassword) , [ watch
    ](/w/api.php?action=help&modules=watch) , [ webapp-manifest
    ](/w/api.php?action=help&modules=webapp-manifest) , [ webauthn
    ](/w/api.php?action=help&modules=webauthn) , [ wikilove
    ](/w/api.php?action=help&modules=wikilove) , [[ bouncehandler
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=bouncehandler)
    , [[ categorytree
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=categorytree)
    , [[ collection
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=collection)
    , [[ cspreport
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=cspreport)
    , [[ discussiontoolscompare
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=discussiontoolscompare)
    , [[ discussiontoolspageinfo
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=discussiontoolspageinfo)
    , [[ discussiontoolspreview
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=discussiontoolspreview)
    , [[ jsondata
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=jsondata)
    , [[ managegroupsynchronizationcache
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=managegroupsynchronizationcache)
    , [[ managemessagegroups
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=managemessagegroups)
    , [[ oathvalidate
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=oathvalidate)
    , [[ parser-migration
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=parser-migration)
    , [[ readinglists
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=readinglists)
    , [[ sanitize-mapdata
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=sanitize-mapdata)
    , [[ scribunto-console
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=scribunto-console)
    , [[ securepollauth
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=securepollauth)
    , [[ stashedit
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=stashedit)
    , [[ timedtext
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=timedtext)
    , [[ translationcheck
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=translationcheck)
    , [[ translationentitysearch
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=translationentitysearch)
    , [[ ulslocalization
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=ulslocalization)
    , [[ ulssetlang
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=ulssetlang)
    , [[ visualeditor
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=visualeditor)
    , [[ visualeditoredit
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=visualeditoredit)
    , [[ wikimediaeventsblockededit
    ]{.apihelp-internal-value}](/w/api.php?action=help&modules=wikimediaeventsblockededit)

:   Default: help

[ format ]{#main:format}

:   The format of the output.

     [json](/w/api.php?action=help&modules=json) 
    :   Output data in JSON format.

     [jsonfm](/w/api.php?action=help&modules=jsonfm) 
    :   Output data in JSON format (pretty-print in HTML).

     [none](/w/api.php?action=help&modules=none) 
    :   Output nothing.

     [php](/w/api.php?action=help&modules=php) 
    :   Output data in serialized PHP format.

     [phpfm](/w/api.php?action=help&modules=phpfm) 
    :   Output data in serialized PHP format (pretty-print in HTML).

     [rawfm](/w/api.php?action=help&modules=rawfm) 
    :   Output data, including debugging elements, in JSON format
        (pretty-print in HTML).

     [xml](/w/api.php?action=help&modules=xml) 
    :   Output data in XML format.

     [xmlfm](/w/api.php?action=help&modules=xmlfm) 
    :   Output data in XML format (pretty-print in HTML).

:   One of the following values: [ json
    ](/w/api.php?action=help&modules=json) , [ jsonfm
    ](/w/api.php?action=help&modules=jsonfm) , [ none
    ](/w/api.php?action=help&modules=none) , [ php
    ](/w/api.php?action=help&modules=php) , [ phpfm
    ](/w/api.php?action=help&modules=phpfm) , [ rawfm
    ](/w/api.php?action=help&modules=rawfm) , [ xml
    ](/w/api.php?action=help&modules=xml) , [ xmlfm
    ](/w/api.php?action=help&modules=xmlfm)

:   Default: jsonfm

[ maxlag ]{#main:maxlag}

:   Maximum lag can be used when MediaWiki is installed on a database
    replicated cluster. To save actions causing any more site
    replication lag, this parameter can make the client wait until the
    replication lag is less than the specified value. In case of
    excessive lag, error code ` maxlag `{.sample} is returned with a
    message like ` Waiting for $host: $lag seconds lagged `{.sample} .\
    See [Manual: Maxlag
    parameter](/wiki/Special:MyLanguage/Manual:Maxlag_parameter) for
    more information.

:   Type: integer

[ smaxage ]{#main:smaxage}

:   Set the ` s-maxage ` HTTP cache control header to this many seconds.
    Errors are never cached.

:   Type: integer

:   The value must be no less than 0.

:   Default: 0

[ maxage ]{#main:maxage}

:   Set the ` max-age ` HTTP cache control header to this many seconds.
    Errors are never cached.

:   Type: integer

:   The value must be no less than 0.

:   Default: 0

[ assert ]{#main:assert}

:   Verify that the user is logged in (including possibly as a temporary
    user) if set to [ user ]{.kbd} , *not* logged in if set to [ anon
    ]{.kbd} , or has the bot user right if [ bot ]{.kbd} .

:   One of the following values: anon, bot, user

[ assertuser ]{#main:assertuser}

:   Verify the current user is the named user.

:   Type: user, by any of username and Temporary user

[ requestid ]{#main:requestid}

:   Any value given here will be included in the response. May be used
    to distinguish requests.

[ servedby ]{#main:servedby}

:   Include the hostname that served the request in the results.

:   Type: boolean ( [details](#main/datatype/boolean) )

[ curtimestamp ]{#main:curtimestamp}

:   Include the current timestamp in the result.

:   Type: boolean ( [details](#main/datatype/boolean) )

[ responselanginfo ]{#main:responselanginfo}

:   Include the languages used for ` uselang `{.variable} and
    ` errorlang `{.variable} in the result.

:   Type: boolean ( [details](#main/datatype/boolean) )

[ origin ]{#main:origin}

:   When accessing the API using a cross-domain AJAX request (CORS), set
    this to the originating domain. This must be included in any
    pre-flight request, and therefore must be part of the request URI
    (not the POST body).

    For authenticated requests, this must match one of the origins in
    the ` Origin ` header exactly, so it has to be set to something like
    [ [https://en.wikipedia.org](https://en.wikipedia.org){.external
    .free} ]{.kbd} or [
    [https://meta.wikimedia.org](https://meta.wikimedia.org){.external
    .free} ]{.kbd} . If this parameter does not match the ` Origin `
    header, a 403 response will be returned. If this parameter matches
    the ` Origin ` header and the origin is allowed, the
    ` Access-Control-Allow-Origin ` and
    ` Access-Control-Allow-Credentials ` headers will be set.

    For non-authenticated requests, specify the value [ \* ]{.kbd} .
    This will cause the ` Access-Control-Allow-Origin ` header to be
    set, but ` Access-Control-Allow-Credentials ` will be ` false ` and
    all user-specific data will be restricted.

[ uselang ]{#main:uselang}

:   Language to use for message translations. [
    [action=query&meta=siteinfo](/w/api.php?action=help&modules=query%2Bsiteinfo)
    ]{.kbd} with [ siprop=languages ]{.kbd} returns a list of language
    codes, or specify [ user ]{.kbd} to use the current user\'s language
    preference, or specify [ content ]{.kbd} to use this wiki\'s content
    language.

:   Default: user

[ variant ]{#main:variant}

:   Variant of the language. Only works if the base language supports
    variant conversion.

[ errorformat ]{#main:errorformat}

:   Format to use for warning and error text output

     plaintext 
    :   Wikitext with HTML tags removed and entities replaced.

     wikitext 
    :   Unparsed wikitext.

     html 
    :   HTML

     raw 
    :   Message key and parameters.

     none 
    :   No text output, only the error codes.

     bc 
    :   Format used prior to MediaWiki 1.29. ` errorlang `{.variable}
        and ` errorsuselocal `{.variable} are ignored.

:   One of the following values: bc, html, none, plaintext, raw,
    wikitext

:   Default: bc

[ errorlang ]{#main:errorlang}

:   Language to use for warnings and errors. [
    [action=query&meta=siteinfo](/w/api.php?action=help&modules=query%2Bsiteinfo)
    ]{.kbd} with [ siprop=languages ]{.kbd} returns a list of language
    codes, or specify [ content ]{.kbd} to use this wiki\'s content
    language, or specify [ uselang ]{.kbd} to use the same value as the
    ` uselang `{.variable} parameter.

:   Default: uselang

[ errorsuselocal ]{#main:errorsuselocal}

:   If given, error texts will use locally-customized messages from the
    MediaWiki namespace.

:   Type: boolean ( [details](#main/datatype/boolean) )

[ centralauthtoken ]{#main:centralauthtoken}

:   When accessing the API using a cross-domain AJAX request (CORS), use
    this to authenticate as the current SUL user. Use [
    [action=centralauthtoken](/w/api.php?action=help&modules=centralauthtoken)
    ]{.kbd} on this wiki to retrieve the token, before making the CORS
    request. Each token may only be used once, and expires after 10
    seconds. This should be included in any pre-flight request, and
    therefore should be included in the request URI (not the POST body).
:::

::: {.apihelp-block .apihelp-permissions}

writeapi
:   Use of the write API
:   Granted to: all, user and bot

apihighlimits
:   Use higher limits in API queries (slow queries: 500; fast queries:
    5000). The limits for slow queries also apply to multivalue
    parameters.
:   Granted to: bot and sysop
:::

</div>

</div>

## [ Other APIs ]{#Other_APIs .mw-headline}

If you do not find what you are looking for in this API documentation,
there are many other APIs related to Wikimedia projects.

For the REST API included with MediaWiki 1.35 and later, see [API:REST
API](/wiki/Special:MyLanguage/API:REST_API) [](/wiki/API:REST_API) .

## [ Code stewardship ]{#Code_stewardship .mw-headline}
:::
:::
:::
:::
:::
