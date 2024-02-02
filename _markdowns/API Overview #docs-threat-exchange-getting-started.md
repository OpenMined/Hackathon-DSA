<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
ThreatExchange is a simple-to-use platform that supports signal sharing
among predefined groups of members in a secure, privacy-compliant, and
automated way. Today, ThreatExchange (aka TX or TE) is used by multiple
companies to share signals on a variety of topics intended to prevent
real world harm. Some examples of how TX is currently used include
sharing malware, phishing scams, and terrorism signals with the goal of
helping all participating organizations tackle these problems based on
their terms of service.

ThreatExchange is built on these core concepts:

These concepts allow a group of ThreatExchange members to share signals,
[react
to](https://developers.facebook.com/docs/threat-exchange/reference/reacting)
and describe signals other members upload, and decide individually on
how a signal aligns with their policies.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Signal sharing is a tactic to prevent harm on the internet where
platforms work together to combat global threats like malware,
terrorism, and other harmful content. Platforms help each other by
sharing signals from content that they found and labeled on their
platform. For example, Platform A might find a video of terrorism on
their platform. By sharing the hash of that video (a type of signal)
with Platform B, Platform B can find and review that video, which they
might have otherwise missed. By sharing signals, the platforms can
compound their individual trust & safety efforts and prevent more harm
faster.

Signal Sharing is **not** a way for platforms to align on content
policies or to coordinate on what content they remove. Each platform
reviews content independently according to its own community standards
policies and takes actions according to those standards.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
There are many problems in the Trust & Safety space that affect all
platforms jointly, and lead to real world harm. Signal sharing on
ThreatExchange tries to reduce this harm by helping platforms find and
remove more harmful content. Platforms come in all shapes and sizes, and
not all can afford to hire a myriad of reviewers or invest millions in
specialized machine learning models. For these platforms, investing in
ThreatExchange can be an effective way to use their trust and safety
resources.

Even for platform's which already have robust trust and safety programs,
there are still tangible benefits to joining and contributing to
ThreatExchange. Namely, the harmful content found on those platform
often doesn't go away, it just goes somewhere else. A rising tide lifts
all boats, and by all pitching in, we can improve the baseline safety
level for the entire internet. Even if you aren't uploading new signals
to ThreatExchange simply confirming (or disputing!) labels will improve
that baseline, build trust in our platforms, and help make the internet
safer.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
In ThreatExchange, we refer to the signals being shared as
[Indicators](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/)
. Over 80 types of Indicators can be shared on ThreatExchange and the
full list can be found
[here](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type)
. There are, however, a few data types that are particularly common.

### Indicator Types

::: _57-c
Match Text
:::
:::
:::

</div>

</div>

Indicator Type

Raw Text

` TEXT_STRING `

Trend Queries (keywords+regex)

` TREND_QUERY `

::: _57-c
Match URLs
:::

Indicator Type

URLs

` URI `

Domains

` DOMAIN `

::: _57-c
Match Photos
:::

Indicator Type

PDQ Hashes
[details](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fpdq&h=AT04zdQw1m0wu_8mlBgqvngVFjYTbMMP5Nz5RZNjEn_8Q1m_7ft0DCI9aKaIhONN8bOQ6WhYicJYOHpqhVCvvEcuyjOMCeq_izzBxlPeyApwY14eQL7nfrm7FGvBZrTGKpKQzuDrFVjVsIeW)

` HASH_PDQ `

PDQ Hashes +
[OCR](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOptical_character_recognition&h=AT1uuibT72UWAPuLSxo8vPIKQuUiEhtiFxNn9oMEqlpt85fKlYXvnPxTwPy-JC8RnGhwdDji0pslsxf4SHQCUpiwBOdzjtl9HQE6pkSaw_gnVoj8xsVq5IRF-AwQcaNDilrAjhpCZCfNIqnO)
Text

` HASH_PDQ_OCR `

::: _57-c
Match Videos
:::

Indicator Type

MD5 Hash
[details](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMD5&h=AT3KTFnw7xZXk5QkRppj6leaf-7Xdz3Zlh1ASRFUr0Z0j_hyHxd7LWF21WkFNOhZ4U10ZVinHBDcICuE4VYVvwf0mKGCkJ3KkmIR4DzOAhtqWTAjMLvVuRPb6c9DmJ6D7usqzHwEdosnfPPt)

` HASH_MD5 `

TMK+PDQF Hash
[details](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Ftmk&h=AT3Ihm4wwEIJjmqX2IZzgYRUqpBTPQUzP29R22XMBVtyG9z1rSyOTgSoOvQ9VTCd04WEJOprQu1yRIWuwV8pMRW9TRCweZ_H027RqO5FbauqTt1_zIIvh0H9kqmBuSkL_tYW6WgWUfbwrFTe)

` HASH_TMK `

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Partners who have onboarded have reported the process takes take 1-2
weeks of engineering time to get a basic integration plus another 1-2
weeks for fully automated ingestion and contribution. The cost will vary
by company and will depend on a number of factors including the maturity
of internal systems and the number of signal types you are attempting to
use.

Some questions that might be useful in determining how long it will take
your company to integrate are:

-   Which of the above signal types are you planning to integrate with?
    (Text tends to be quick, photos moderate)
-   Can you currently search your platform for matches of those signal
    types? (You can likely piggyback on existing infrastructure, saving
    time)
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Here are the ways to share signals on ThreatExchange:

-   **UI** : ThreatExchange has a graphical user interface you can use
    to quickly and interactively do things like read and share signals
    and run queries. This is the best place to quickly explore the data
    in ThreatExchange. Learn more about
    [ThreatExchange](https://developers.facebook.com/docs/threat-exchange/ui)
    .

-   **Python** : To build an inital integration and to preform
    validation we recommend using the python [open source
    library](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fpython-threatexchange&h=AT22unYY_pituBKadb-EScGZerV-EGeuF0oO9hKHtPwHvOFrpmfoaj66Y_6kMzgy4BLmKbBpWFMxWhC5lQ2JgJjgTW6XgLHoACcmcqSTnJk6c158Te8KQBvdu7VOihUi1gIUJ2fS12bBXHyUJpc1CeNcuJpLSQ)
    we've developed. This allows you fetch a copy of shared signals in a
    simple format.

-   **API** : Lastly, there is also a powerful HTTP API which has
    greater functionality than the python wrapper for an advanced
    integration. Learn more about these
    [APIs](https://developers.facebook.com/docs/threat-exchange/reference/apis)
    .

To use any of these methods you will first need to get access to
ThreatExchange. ThreatExchange requires you (or someone on your team) to
have a Facebook account, or to create one, and then will require
creating a new application. Afterwards, you can apply for access to
ThreatExchange, which requires you to confirm that your application
belongs to your business. After that, you can add more accounts to the
application, or store a token to gain access to the API.

Follow [these
steps](https://developers.facebook.com/docs/threat-exchange/reference/ui/app-review)
to create an App and get access to ThreatExchange.
:::
:::
