API Overview - ThreatExchange - Documentation - Meta for Developers

ThreatExchange* Get Started
* Get Access
* Best Practices
* UI Overview
* UI Reference
* API Overview
* API Examples
* API Structure
* API Reference
* Privacy Controls
* Submitting Data
* Editing Existing Data
* Delete Data
* Re-sharing
* React to Data
* Submit Connections
* Integrations
* Webhooks
* FAQ
* Webinar
* Changelog
Graph API Versionv19.0ThreatExchange API Overview
===========================
Authenticate via an Access Token
--------------------------------
The ThreatExchange APIs perform authentication via access tokens. After Facebook notifies you that your App can access ThreatExchange, use the access token tool to get an **App Token**. *Please note, app tokens give access to sensitive details to your app and should be treated like a password.*
With the access token, test your access to ThreatExchange by retrieving the list of members in the exchange:

```
https://graph.facebook.com/threat_exchange_members?access_token=<access_token>
```
If this request does not return an error, you are now ready to begin exploring the ThreatExchange API!
Searching Data Using the API
----------------------------
With your newly activated access token, perform a search for malicious URLs added in the last week:

```
https://graph.facebook.com/threat_descriptors?type=URI&amp;status=MALICIOUS&amp;since=a week ago&amp;access_token=<access_token>
```
Please note that not all fields are returned by default. Consult the reference documentation and specify the fields you are looking to read by appending the fields parameter. See the Graph API guide for more details.
Publishing Data Using the API
-----------------------------
**Test publish** a domain, `my-test-example.com`, ensuring only you are able to see the data:

```
https://graph.facebook.com/threat_descriptors
POST DATA
type=DOMAIN
indicator=my-test-example.com
privacy_type=HAS_WHITELIST
status=UNKNOWN
description=Test data publishing
share_level=RED
privacy_members=<your_app_id>
access_token=555|1235
```
The return value will be a JSON map with a success or failure code and, if the call is successful, the unique ThreatExchange ID for the descriptor you published!
**Publish** a descriptor for your own domain, `my-company-domain.com`, and share it with Facebook's app ID, `820763734618599`:

```
https://graph.facebook.com/threat_descriptors
POST DATA
type=DOMAIN
indicator=my-company-domain.com
privacy_type=HAS_WHITELIST
status=NON_MALICIOUS
description=The domain owned by <your_app_id>
share_level=WHITE
privacy_members=820763734618599
access_token=555|1235
```
More API Examples
-----------------
**Search** for all compromised credentials found on the Internet within the last day:

```
https://graph.facebook.com/v19.0/threat_indicators?type=COMPROMISED_CREDENTIAL&since=yesterday&access_token=555|1235]
```
**Find** the unique ThreatExchange ID for a specific indicator, such as `facebook.com`:

```
https://graph.facebook.com/v19.0/threat_indicators?text=facebook.com&access_token=555|1235
```
**Explore** related indicators for a specific indicator with ThreatExchange ID `898557073557972`:

```
https://graph.facebook.com/898557073557972/descriptors?access_token=555|1235
```
**Explore** all of the descriptors for a specific indicator with ThreatExchange ID `898557073557972`:

```
https://graph.facebook.com/898557073557972/descriptors?access_token=555|1235
```
See more examples on our Github, or on the endpoint pages for threat indicators, threat descriptors.
Python/Ruby/Java/Curl wrappers
------------------------------
The above snippets showed you some examples of the bare REST API. For an easier path to integration please see our Python wrapper.

 Please also see our descriptor-focused reference designs in Ruby, Java, and
bare-curl. 