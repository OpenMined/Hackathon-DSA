v2 tools and libraries

Twitter-built v2 tools and libraries
------------------------------------

Twitter maintains a set of official libraries and SDKs, listed here.

We also include a list of [community-supported libraries](#community-libraries) lower on this page.

[Explore TwitterDev code on GitHub](https://github.com/twitterdev)

[Find Twitter samples on Glitch](https://glitch.com/@twitter)

[Find Twitter samples on Replit](https://replit.com/@twitter)

### v2 SDKs and sample code

* **[Twitter API Java SDK](https://github.com/twitterdev/twitter-api-java-sdk)** - Official Java SDK for the Twitter API v2
* **[Twitter API TypeScript/JavaScript SDK](https://github.com/twitterdev/twitter-api-typescript-sdk)** - Official TS/JS SDK for the Twitter API v2  
    
* [Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code) - Sample code in Javascript, Ruby, Python, and Java

### v2 API specification

* [**OpenAPI specification**](https://api.twitter.com/2/openapi.json) - Use this to exercise the API with tools like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/products/core).  
    

### Endpoint-specific scripts and libraries

* [**search-tweets Python**](https://github.com/twitterdev/search-tweets-python) - Python library for the v2 and enterprise search endpoints
* [**search-tweets Ruby**](https://github.com/twitterdev/search-tweets-ruby) - Ruby library for the v2 search endpoints
* **[compliant client](https://github.com/twitterdev/compliant-client)** \- A set of Python scripts for the v2 Tweet and User batch compliance endpoints
* **[Autohook](https://github.com/twitterdev/autohook)** \- JavaScript package to automatically setup and serve webhooks for the enterprise and premium Account Activity API

### Integrate with Cloud

* **[Twitter API Toolkit for Google Cloud: Recent Search](https://developer.twitter.com/en/docs/tutorials/developer-guide--twitter-api-toolkit-for-google-cloud)** - Process, analyze and visualize Tweets using Google Cloud and Recent Search Twitter API v2
* **[Twitter API Toolkit for Google Cloud: Filtered Stream](https://developer.twitter.com/en/docs/tutorials/developer-guide--twitter-api-toolkit-for-google-cloud1)** - Listen to Tweets in real-time, detect and monitor trends using Google Cloud and the Filtered Stream API v2

### No-code tools

* [**Postman collection**](https://t.co/twitter-api-postman) \- Explore the API using Postman, the visual REST client.
* [**V2 request builder**](https://developer.twitter.com/apitools/api) - Generate an API request by selecting an endpoint and parameters.
* [**V2 search and filtered stream query builder**](https://developer.twitter.com/apitools/query) - Easily craft working search queries or filtered stream rules.
* [**Migrate v1.1 search query to v2**](https://developer.twitter.com/apitools/migrate/query) - Quickly convert your standard v1.1 search queries into the v2 search query format.
* [**Download Tweet search results**](https://developer.twitter.com/apitools/downloader) (Academic researchers only) - Download potentially large batches of Tweets into CSV or JSON files.

### v1.1 to v2 migration tools

* [**Migrate v1.1 search query to v2**](https://developer.twitter.com/apitools/migrate/query) - Convert your standard v1.1 search queries into the v2 search query format.
* [**Migrate v1.1 data format to v2**](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/migrate/data-formats/visual-data-format-migration-tool) - Visually explore the differences between the v1.1 and v2 data formats.

### Command-line interface (CLI)

* [**twurl**](https://github.com/twitter/twurl) - Interact with the Twitter API, including OAuth authentication, via your command-line interface. Requires a Ruby runtime. twurl does not currently work with OAuth 2.0 Authorization Code with PKCE.

### Additional tools

* [**twemoji**](https://twemoji.twitter.com/) - Twitter’s free, open source emoji character set, including a JavaScript library for display.
* [**twitter-text**](https://github.com/twitter/twitter-text) - A collection of libraries to standardize parsing and tokenization of Tweet text. Available for Java, JavaScript (Node.JS), Objective-C & Ruby. [Learn more about counting characters in Tweets](https://developer-staging.twitter.com/en/docs/counting-characters).

Looking for even more code? You can find examples from our team on our [GitHub](https://github.com/twitterdev), and on [Glitch](https://glitch.com/@twitter).

Community tools and libraries for v2
------------------------------------

The libraries listed here have been built by members of the developer community. Note that they may be at different stages of API coverage.  

If you've built your own Twitter API library or useful tool, please [let us know](https://twittercommunity.com/c/libraries-and-sdks/63), and we'll add it to this list to help others to find it. We also have some [version badges](https://twbadges.glitch.me/) you can borrow, to use in your own README files.

Looking for inspiration? You can browse and search in the [Twitter](https://github.com/topics/twitter?o=desc&s=updated) and [twitter-api-v2](https://github.com/topics/twitter-api-v2?o=desc&s=updated) topics on GitHub to find helpful code examples from other developers.

**Jump to:** [C# / .NET](#csharp), [Dart / Flutter](#dart), [Go](#go), [Java](#java), [JavaScript (Node.JS) / TypeScript](#nodejs), [Kotlin](#kotlin), [PHP](#php), [PowerShell](#powershell), [Python](#python), [R](#r), [Ruby](#ruby), [Rust](#rust), [Swift](#swift)

### C# / .NET

* [**CoreTweet**](https://github.com/CoreTweet/CoreTweet) Yet Another .NET Twitter Library
* [**LinqToTwitter**](https://github.com/JoeMayo/LinqToTwitter) LINQ Provider for the Twitter API
* [**SocialOpinion**](https://github.com/jamiemaguiredotnet/SocialOpinion-Public) APIs written in C# that connect to the Twitter API
* [**Tweetinvi**](https://github.com/linvi/tweetinvi) an intuitive Twitter C# library
* [**TwitterSharp**](https://github.com/Xwilarg/TwitterSharp) C# wrapper around Twitter API V2

### Dart / Flutter

* [**twitter-api-v2**](https://github.com/twitter-dart/twitter-api-v2) a lightweight wrapper library for Twitter API v2.0 written in Dart and Flutter

### Go

* [**ctw**](https://github.com/0dayfall/ctw) a library for the Twitter API
* [**go-twitter**](https://github.com/g8rswimmer/go-twitter) a Go library for Twitter v2 API integration.
* [**gotwi**](https://github.com/michimani/gotwi) a library for the Twitter API v2 in Go
* [**gotwtr**](https://github.com/sivchari/gotwtr) a library for the Twitter API
* [**twitter-stream**](https://github.com/Fallenstedt/twitter-stream) a Go wrapper for Twitter's V2 Filtered Stream API
* [**twitter**](https://github.com/creachadair/twitter) a Go client for the Twitter API

### Java

* [**twittered**](https://github.com/redouane59/twittered) Twitter API client for Java developers
* [**twitter4j-v2**](https://github.com/takke/twitter4j-v2) a simple wrapper for Twitter API v2 that is designed to be used with Twitter4J
* [**twitter-compliance**](https://github.com/UCL/twitter-compliance) multi-module Jakarta EE application for syncing compliance events from Twitter
* [**JTW**](https://github.com/uakihir0/jtw) Twitter V2 API client library for Java

### JavaScript (Node.JS) / TypeScript

* [**node-twitter-api-v2**](https://github.com/PLhery/node-twitter-api-v2) strongly typed, full-featured, light, versatile yet powerful Twitter API client for Node.js
* [**twitter.js**](https://github.com/twitterjs/twitter.js) an object-oriented Node.js and TypeScript library for interacting with Twitter API v2
* [**twitter-types**](https://github.com/twitterjs/twitter-types) type definitions for the Twitter API
* [**twitter-v2**](https://github.com/HunterLarco/twitter-v2) An asynchronous client library for the Twitter APIs
* [**tweet-json-to-html**](https://github.com/wdl/tweet-json-to-html) converts Twitter API v2 Tweet JSON objects into HTML format

### Kotlin

* [**KTweet**](https://github.com/ChromasIV/KTweet) a Kotlin library that allows you to consume the Twitter API v2.
* [**Tweedle**](https://github.com/tyczj/Tweedle) a Kotlin-based Android library around the Twitter v2 API
* [**TwitterApiKit**](https://github.com/kojofosu/TwitterApiKit) saves you time creating data objects to access Twitter's API v2. This library is supported on Java, Kotlin, and Android

### PHP

* [**bird-elephant**](https://github.com/danieldevine/bird-elephant) PHP client library for the Twitter API v2 endpoints
* [**twifer**](https://github.com/ferrysyahrinal/twifer) Simple PHP Library for Twitter API Standard v1.1 & Twitter API v2
* [**twitter-api-v2-php**](https://github.com/noweh/twitter-api-v2-php) PHP package providing easy and fast access to Twitter API V2
* [**twitteroauth**](https://github.com/abraham/twitteroauth) PHP library for use with the Twitter API
* [**twitter-ultimate-php**](https://github.com/utxo-one/twitter-ultimate-php) PHP Wrapper for the Twitter v2 API
* [**Twitter Stream API**](https://github.com/redwebcreation/twitter-stream-api) consume the Twitter Stream API v2 in real-time

### PowerShell

* [**BluebirdPS**](https://github.com/thedavecarroll/BluebirdPS) a Twitter Automation Client for PowerShell 7. Tweet, Retweet, send Direct Messages, manage lists, and more

### Python

* [**tweepy**](https://github.com/tweepy/tweepy) Twitter for Python
* [**twarc**](https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/) a command line tool and Python library for collecting JSON data via the Twitter API, with a command (twarc2) for working with the v2 API
* [**python-twitter**](https://github.com/sns-sdks/python-twitter) a simple Python wrapper for Twitter API v2
* [**TwitterAPI**](https://github.com/geduldig/TwitterAPI) minimal Python wrapper for Twitter's APIs
* [**twitterati**](https://github.com/JeannieDaniel/twitterati) Wrapper for Twitter Developer API V2
* [**twitter-stream.py**](https://github.com/twitivity/twitter-stream.py) a Python API client for Twitter API v2
* [**twitivity**](https://github.com/twitivity/twitivity) Account Activity API client library for Python
* [**PyTweet**](https://github.com/TheFarGG/PyTweet) a synchronous Python wrapper for the Twitter API
* [**tweetkit**](https://github.com/ysenarath/tweetkit) a Python Client for the Twitter API for Academic Research
* [**tweetple**](https://github.com/dapivei/tweetple) a wrapper to stream information from the Full-Archive Search Endpoint, for Academic Research
* [**2wttr**](https://github.com/simonlindgren/2wttr) get Tweets from the v2 Twitter API, for Academic Research

### R

* [**academictwitteR**](https://github.com/cjbarrie/academictwitteR) R package to query the Twitter Academic Research Product Track v2 API endpoint
* [**RTwitterV2**](https://github.com/MaelKubli/RTwitterV2) R functions for Twitter's v2 API

### Ruby

* [**omniauth-twitter2**](https://github.com/unasuke/omniauth-twitter2) OmniAuth strategy for authenticating with Twitter OAuth2
* [**tweetkit**](https://github.com/julianfssen/tweetkit) Twitter v2 API client for Ruby
* [**twitter\_oauth2**](https://github.com/nov/twitter_oauth2) Twitter OAuth 2.0 Client Library in Ruby

### Rust

* [**twitter-v2**](https://github.com/jpopesculian/twitter-v2-rs) Rust bindings for Twitter API v2

### Swift

* [**Twift**](https://github.com/daneden/Twift/) An async Swift library for the Twitter v2 API
* [**TwitterAPIKit**](https://github.com/mironal/TwitterAPIKit) Swift library for the Twitter API v1 and v2

v1.1 tools and libraries

  
Official v1.1 tools and libraries
------------------------------------

The Twitter teams maintain a set of official libraries and SDKs, listed here. 

We also include a list of [community-supported libraries](#community-libraries) lower on this page. 

### JavaScript / Node.js

**Clients**

**\--**

**SDKs / Libraries**

**\--**

**Tools**

[**Autohook**](https://www.npmjs.com/package/twitter-autohook)

Get started with the Premium v1.1 Account Activity API

### Python

**Clients**

**[search-tweets-python](https://github.com/twitterdev/search-tweets-python)**

A client supporting v2, Premium v1.1 and Enterprise search

**SDKs / Libraries**

**\--**

**Tools**

**\--**

### Ruby

**Clients**

**[search-tweets-ruby](https://github.com/twitterdev/search-tweets-ruby)**

A client supporting v2, Premium v1.1 and Enterprise search

**SDKs / Libraries**

**\--**

**Tools**

**\--**

### Additional official resources

The tools below can also be useful when working with the Twitter API.

Looking for even more code? You can find examples on our [GitHub](https://github.com/twitterdev), and on [Glitch](https://glitch.com/@twitter).

**[twemoji](https://twemoji.twitter.com/)**

Twitter’s free, open source emoji character set, including a JavaScript library for cross-platform support.

**[twitter-text](https://github.com/twitter/twitter-text)**

A collection of libraries to standardize parsing and tokenization of Tweet text.

Available for Java, JavaScript, Objective-C & Ruby.

[Learn more about counting characters in Tweets](https://developer.twitter.com/en/docs/counting-characters).

**[OpenAPI specification](https://api.twitter.com/2/openapi.json)**

Use this specification to exercise the v2 API with tools like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/products/core).

**[twurl](https://github.com/twitter/twurl)**

A command-line tool (CLI) for interacting with the Twitter API, including OAuth authentication.

Requires a Ruby runtime.

**[Postman collection](https://t.co/twitter-api-postman)** 

Explore the v2 API endpoints using Postman, the visual REST client.

Community tools and libraries
-----------------------------

These are some of the many community-supported libraries that cover the Twitter API, across several programming languages and platforms. Note that these resources may not all have been tested by the Twitter team.

The libraries listed here should implement most features of the Standard API v1.1, unless otherwise noted - check with the authors for details, and for additional support.  
  
If you have built a library that supports Twitter API v2, please let us know about it [via our community forums](https://twittercommunity.com/c/libraries-and-sdks/63), for possible addition to this page. You can also use the forums to let us know about any changes to the listings on this page.

If you're missing a library or tool for your favorite programming language, let us know via the [feedback platform](https://twitterdevfeedback.uservoice.com/), where you can also vote for ideas, or get inspired to build and submit something new.

### .NET

### (ASP, C#, VB)

**Clients**

**[ASPTwitter](http://www.timacheson.com/Blog/2013/jun/asptwitter)**

by [@timacheson](https://twitter.com/timacheson)

**SDKs / Libraries**

**[LINQ2Twitter](https://github.com/JoeMayo/LinqToTwitter)**

by [@JoeMayo](https://twitter.com/JoeMayo) (v2)

**[SocialOpinion](https://github.com/jamiemaguiredotnet/SocialOpinion-Public)**

by [@jamie\_maguire1](https://twitter.com/jamie_maguire1) (v2)

**[Tweetinvi](https://github.com/linvi/tweetinvi)**

by [@TweetinviApi](https://twitter.com/TweetinviApi) (v2)

**[CoreTweet](https://coretweet.github.io/)**

by [@CoreTweet](https://github.com/CoreTweet/) (v2)

**Tools**

**\--**

### C++

**Clients**

**\--**

**SDKs / Libraries**

**[Twitter-API-C-Library](https://github.com/a-n-t-h-o-n-y/Twitter-API-C-Library)**

by [@a-n-t-h-o-n-y](https://github.com/a-n-t-h-o-n-y)

**Tools**

**\--**

### Clojure

**Clients**

**\--**

**SDKs / Libraries**

**[twitter-api](https://github.com/adamwynne/twitter-api)**

by [@adamjwynne](https://twitter.com/adamjwynne) / [@StreamScience](https://twitter.com/streamscience)

**[twttr](https://github.com/chbrown/twttr)**

by [@chbrown](https://github.com/chbrown/)

**Tools**

**\--**

### ColdFusion

**Clients**

**\--**

**SDKs / Libraries**

**[MonkehTweets](https://github.com/coldfumonkeh/monkehTweets)**

by [@coldfumonkeh](https://twitter.com/coldfumonkeh)

**Tools**

**\--**

### Dart

**Clients**

**\--**

**SDKs / Libraries**

**[dartTwitterAPI](https://github.com/stefanuros/dartTwitterAPI)**

by [@stefanuros](https://github.com/stefanuros)

**[twitter.dart](https://github.com/sh4869/twitter.dart)**

by [@sh4869sh](https://twitter.com/sh4869sh)

**[dart\_twitter\_api](https://github.com/robertodoering/twitter_api)**

by [@robertodoering](https://github.com/robertodoering)

**Tools**

**\--**

### Elixir

**Clients**

**\--**

**SDKs / Libraries**

**[extwitter](https://github.com/parroty/extwitter)**

by [@parroty](https://github.com/parroty)

**Tools**

**\--**

### Erlang

**Clients**

**\--**

**SDKs / Libraries**

**[ErlyBird](https://github.com/igb/ErlyBird)**

by [@igb](https://twitter.com/igb)

**[yatael](https://github.com/tgrk/yatael)**

by [@tajgur](https://twitter.com/tajgur)

**Tools**

**\--**

### Go

**Clients**

**[twty](https://github.com/mattn/twty)**

A command-line client tool written in Go, by [@mattn](https://github.com/mattn)

**SDKs / Libraries**

**[go-twitter](https://github.com/g8rswimmer/go-twitter)**

by [@g8rswimmer](https://github.com/g8rswimmer) (v2)

**[twittergo](https://github.com/kurrik/twittergo)**

by [@kurrik](https://twitter.com/kurrik)

**[go-twitter](https://github.com/dghubble/go-twitter)**

by [@dghubble](https://twitter.com/dghubble)

**[Anaconda](https://github.com/ChimeraCoder/anaconda)**

by [@chimeracoder](https://twitter.com/chimeracoder)

**Tools**

**[tw-oob-oauth-cli](https://github.com/smaeda-ks/tw-oob-oauth-cli)**

A small PIN-based OAuth tool to retrieve tokens, by [@smaeda-ks](https://github.com/smaeda-ks)

### Haskell

**Clients**

**\--**

**SDKs / Libraries**

**[twitter-conduit](https://github.com/himura/twitter-conduit)**

by [@himura](https://github.com/himura)

**Tools**

**[twitter-types](https://github.com/himura/twitter-types)**

by [@himura](https://github.com/himura)

### Java

**Clients**

**\--**

**SDKs / Libraries**

**[twittered](https://github.com/redouane59/twittered)**

by [@redouanebali](https://twitter.com/redouanebali) (v2, Premium v1.1 support)

**[JTwitter](https://github.com/winterstein/JTwitter)**

by [@winterwellassoc](https://twitter.com/winterwellassoc)

**[Twitter4J](https://github.com/Twitter4J/Twitter4J)**

by [@yusuke](https://twitter.com/yusuke)

**Tools**

**\--**

### JavaScript / Node.js

**Clients**

**\--**

**SDKs / Libraries**

[**twitter-v2**](https://github.com/HunterLarco/twitter-v2)

by [@HunterLarco](https://github.com/HunterLarco) (v2)

[**twitter-lite**](https://github.com/draftbit/twitter-lite)

by [@dandv](https://twitter.com/dandv) and [@peterpm](https://twitter.com/peterpme)

**Tools**

[**twitter-error-handler**](https://github.com/shalvah/twitter-error-handler)

by [@shalvah](https://github.com/shalvah)

[**twittersignin**](https://github.com/shalvah/twittersignin)

A wrapper around Twit to simplify signin, by [@shalvah](https://github.com/shalvah)

### Julia

**Clients**

**\--**

**SDKs / Libraries**

**[Twitter.jl](https://github.com/randyzwitch/Twitter.jl)**

by [@randyzwitch](https://twitter.com/randyzwitch)

**Tools**

**\--**

### Kotlin

**Clients**

**\--**

**SDKs / Libraries**

**[Tweedle](https://github.com/tyczj/Tweedle)**

by [@tyczj](https://github.com/tyczj) (v2 in alpha)

**Tools**

**\--**

### Lua

**Clients**

**\--**

**SDKs / Libraries**

**[lua-twitter](https://github.com/leafo/lua-twitter)**

by [@moonscript](https://twitter.com/moonscript)

**Tools**

**\--**

### Objective-C

**Clients**

**\--**

**SDKs / Libraries**

**[STTwitter](https://github.com/nst/STTwitter)**

by [@nst021](https://twitter.com/nst021)

**Tools**

**\--**

### Perl

**Clients**

**\--**

**SDKs / Libraries**

**[Twitter::API](https://github.com/semifor/Twitter-API)**

by [@semifor](https://twitter.com/semifor)

**Tools**

**\--**

### PHP

**Clients**

**\--**

**SDKs / Libraries**

**[twitter-labs](https://github.com/spatie/twitter-labs)**

by [@spatie\_be](https://twitter.com/spatie_be) (Labs)

**[TwitterOAuth](https://twitteroauth.com/)**

by [@Abraham](https://twitter.com/Abraham)

**[codebird-php](https://github.com/jublo/codebird-php)**

by [@jublo](https://twitter.com/jublo)

**[Twitter-API-PHP](https://github.com/J7mbo/twitter-api-php)**

by [@j7mbo](https://twitter.com/J7mbo/)

**[phirehose](https://github.com/fennb/phirehose)**

by [@fennb](https://twitter.com/fennb)

**[twitter-streaming-api](https://github.com/spatie/twitter-streaming-api)**

by [@spatie\_be](https://twitter.com/spatie_be)

**Tools**

**\--**

### PowerShell

**Clients**

**\--**

**SDKs / Libraries**

**\--**

**Tools**

**[PSTwitterAPI](https://github.com/mkellerman/PSTwitterAPI)**

by [@mkellerman](https://twitter.com/)

### Python

**Clients**

**[TwitterSearch](https://github.com/ckoepp/TwitterSearch)**

by [@ckoepp](https://github.com/ckoepp)

**[tweetget](https://github.com/gnascimento/tweeget)**

by [@gnascimento](https://github.com/gnascimento). A search client library for Premium v1.1.

**SDKs / Libraries**

**[TwitterAPI](https://github.com/geduldig/TwitterAPI)**

by [@geduldig](https://github.com/geduldig). Includes v2, Premium v1.1 and Labs support.

**[python-twitter](https://python-twitter.readthedocs.io/en/latest/)**

by [the Python-Twitter Developers](https://github.com/bear/python-twitter)

**[tweepy](https://github.com/tweepy/tweepy)**

by [the tweepy Developers](https://github.com/tweepy). Includes Premium v1.1 support.

**[twython](https://github.com/ryanmcgrath/twython)**

by [@ryanmcgrath](https://twitter.com/ryanmcgrath) and [@mikehelmick](https://twitter.com/mikehelmick)

**Tools**

**[twitter](https://github.com/sixohsix/twitter)**

by [the Python Twitter Tools developer team](https://mike.verdone.ca/twitter/). Includes a CLI, IRC tools, and minimalist API library for v1.1

### R

**Clients**

**\--**

**SDKs / Libraries**

**[rtweet](https://docs.ropensci.org/rtweet/)**

by [@kearnymw](https://twitter.com/kearneymw). Includes Premium v1.1 search support.

**[streamr](https://github.com/pablobarbera/streamR)**

by [@p\_barbera](https://twitter.com/p_barbera)

**Tools**

**[rtweetXtras](https://github.com/Arf9999/rtweetXtras)**

Helper functions for rTweet, by [@Arf9999](https://github.com/Arf9999)

**[tweetrmd](https://github.com/gadenbuie/tweetrmd)**

Easily embed Tweets into R Markdown, by [@gadenbuie](https://github.com/gadenbuie)

### Ruby

**Clients**

**[t](https://github.com/sferik/t)**

A command-line tool by [@sferik](https://twitter.com/sferik)

**SDKs / Libraries**

[**twitter-labs-api**](https://github.com/tomholford/twitter-labs-api)

by [@tomholford](https://twitter.com/tomholford) (supports Labs)

[**twitter**](https://github.com/sferik/twitter)

by [@sferik](https://twitter.com/sferik)

**Tools**

**\--**

### Rust

**Clients**

**\--**

**SDKs / Libraries**

**[egg-mode](https://github.com/QuietMisdreavus/twitter-rs)**

by [@QuietMisdreavus](https://twitter.com/QuietMisdreavus)

**[twitter-api-rs](https://github.com/gifnksm/twitter-api-rs)**

by [@gifnksm](https://twitter.com/gifnksm)

**[twitter-stream-rs](https://github.com/tesaguri/twitter-stream-rs)**

by [@teseguri](https://github.com/tesaguri)

**Tools**

**\--**

### Scala

**Clients**

**\--**

**SDKs / Libraries**

[**twitter4s**](https://github.com/DanielaSfregola/twitter4s)

by [@danielesfregola](https://twitter.com/danielasfregola)

**Tools**

**\--**

### Shell script (Bash)

**Clients**

[**tweet.sh**](https://github.com/piroor/tweet.sh)

A simple Twitter client by [@piroor](https://github.com/piroor). Requires additional command-line tools.

**SDKs / Libraries**

**\--**

**Tools**

**\--**

### Swift

**Clients**

**\--**

**SDKs / Libraries**

**[Swifter](https://github.com/mattdonnelly/Swifter)**

by [@mattdonnelly](https://github.com/mattdonnelly)

  

**Tools**

**\--**

### TypeScript

**Clients**

**\--**

**SDKs / Libraries**

**[twitter-api-ts](https://github.com/OliverJAsh/twitter-api-ts)**

by [@OliverJAsh](https://twitter.com/oliverjash)

**Tools**

**[twitter-d](https://github.com/abraham/twitter-d)**

TypeScript definitions for v1.1 Twitter API objects, by [@Abraham](https://twitter.com/Abraham)

Overview

Introduction
------------

A software development kit (SDK) is a set of software tools and programs tailored for a specific platform or API. The purpose of an SDK is to build or extend functionality of applications by providing libraries or codebases that developers can use within their applications, efficiently and with minimal coding. This significantly speeds up the development process, saving time, money, and effort.

The Twitter Developer Platform now offers 2 official SDKs for those who develop in TypeScript/Javascript and Java. These will allow developers to build more effectively by eliminating the need to manually program the complexities around the Twitter API v2, utilizing the pre-built functions for all available v2 endpoints as well as simplifying the authentication process. As these are built and maintained by the Developer Platform team, they will always be up to date with future releases to the Twitter API v2

Since these SDKs wrap the Twitter API, you must have a [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info) to authenticate requests using the credentials from a [developer App](https://developer.twitter.com/en/docs/apps), located within a [Project](https://developer.twitter.com/en/docs/projects).

#### Installing

* [Java](#item0)
* [TypeScript](#item1)

Java

TypeScript

There are a few ways to install the Java package (requires Java 1.8+)  

* Maven users - add this dependency to your project's POM file:

      `<dependency>   <groupId>com.twitter</groupId>   <artifactId>twitter-api-java-sdk</artifactId>   <version>1.1.4</version> </dependency>`
    

* Grade users - add this dependency to your project's build file:

                implementation "com.twitter:twitter-api-java-sdk:1.1.4"

* Others - first generate the JAR by running the following command

                mvn clean package

                Then manually install the following JARs:

                        target/twitter-api-java-sdk-1.1.4.jar

                        target/lib/\*.jar

This package supports Node.js 14+, to install, run the following command in the directory of the Node project:

                npm install twitter-api-sdk

#### Client basics

Import the classes (Java) and package (TypeScript) at the top of a working file to gain access to the authentication and library clients. In order to use the methods from the library client, authentication credentials must be passed, this could either be Bearer Token (App-only) or client id/client secret if authenticating with OAuth 2.0 user context.

Here are examples of how this would look:

Java TypeScript

      `// Import classes: import com.twitter.clientlib.ApiClient; import com.twitter.clientlib.ApiException; import com.twitter.clientlib.Configuration; import com.twitter.clientlib.auth.*; import com.twitter.clientlib.model.*; import com.twitter.clientlib.TwitterCredentialsBearer; import com.twitter.clientlib.api.TwitterApi;  // Instantiate library client TwitterApi apiInstance = new TwitterApi();   // Instantiate auth credentials (App-only example) TwitterCredentialsBearer credentials = new TwitterCredentialsBearer(System.getenv("APP-ONLY-ACCESS-TOKEN"));   // Pass credentials to library client apiInstance.setTwitterCredentials(credentials);`
    

      `//Import package import { Client, auth } from "twitter-api-sdk";   // Initialize auth client first const authClient = new auth.OAuth2User({  client_id: process.env.CLIENT_ID as string,  client_secret: process.env.CLIENT_SECRET as string,  callback: "YOUR-CALLBACK",  scopes: ["tweet.read", "users.read", "offline.access"], });   // Pass auth credentials to the library client   const twitterClient = new Client(authClient);`
    

#### Authentication Flow

If you are using the application only option to authenticate the SDKs, you will only need to provide the token and the library client will be ready to use the endpoint methods right away. Keep in mind, application only tokens cannot be used on endpoints that require user context authentication.

OAuth 2.0 user context authentication requires a few extra steps after creating the auth client. 

* Generate authorization URL
* Authorize the application from the authorization URL
* Redirects to callback (this should be matching the callback URL set in the auth settings page in the Developer Portal).
* Parse code verifier to exchange for access token

The SDKs provide methods on the auth client that simplifies these steps. For a full example of how to make a request authenticating with OAuth 2.0 user context, check out the GitHub repositories.

* [TypeScript](https://github.com/twitterdev/twitter-api-typescript-sdk/blob/main/examples/oauth2-callback_pkce_s256.ts)
    
* [Java](https://github.com/twitterdev/twitter-api-java-sdk/blob/main/examples/src/main/java/com/twitter/clientlib/auth/OAuth20GetAccessToken.java)
    

#### Endpoint methods

The methods provided within the library client are clearly named to correspond with every endpoint and all parameters are passed in as arguments.

Here is an example of Tweet lookup by ID:

Java TypeScript

      `String id = "1511757922354663425"; // String | A single Tweet ID. Set<String> expansions = new HashSet<>(Arrays.asList("author_id")); // Set<String> | A comma separated list of fields to expand. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at", "lang", "context_annotations")); // Set<String> | A comma separated list of Tweet fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at", "description", "name")); // Set<String> | A comma separated list of User fields to display.   try {  SingleTweetLookupResponse result = apiInstance.tweets().findTweetById(id, expansions, tweetFields, userFields, null, null, null);  System.out.println(result); } catch (ApiException e) {  System.err.println("Exception when calling TweetsApi#findTweetById");  System.err.println("Status code: " + e.getCode());  System.err.println("Reason: " + e.getResponseBody());  System.err.println("Response headers: " + e.getResponseHeaders());  e.printStackTrace(); }`
    

      `const lookupTweetById = await client.tweets.findTweetById(   // Tweet ID   "1511757922354663425",   {     // Optional parameters     expansions: ["author_id"],     "user.fields": ["created_at", "description", "name"],   } );`