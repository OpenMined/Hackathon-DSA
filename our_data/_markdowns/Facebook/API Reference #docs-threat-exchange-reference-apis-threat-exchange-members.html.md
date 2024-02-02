/threat\_exchange\_members - ThreatExchange - Documentation - Meta for Developers

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
Graph API Versionv19.0/threat\_exchange\_members
==========================
Returns a list of current members of the ThreatExchange, alphabetized by application name. Each application may also include an optional contact email address. You can set this address, if desired, under the settings panel for your application. See here.
Parameters
----------
The following query parameter is required:
* **`access_token`** - The key for authenticating to the API. It is a concatenation of <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
* `fields` - A list of fields to return in the response
Example query:

```
https://graph.facebook.com/v2.8/threat_exchange_members?access_token=555|aSdF123GhK
```
Data returned:

```
{
  "data": [
    {
      "id": "820763734618599",
      "email": "threatexchange@support.facebook.com",
      "name": "Facebook ThreatExchange"
    },
    ...
  ]
}
```
The same query using cURL:

```
curl -i -X GET \
 "https://graph.facebook.com/v2.8/threat_exchange_members?access_token=555%7C1234"
```
The same query using Python:

```
import requests
import json
import ast
import urllib
app_id = '555' # Replace this with your app ID
app_secret = '1234' # Replace this with your app secret
query_params = urllib.urlencode({
    'access_token' : app_id + '|' + app_secret,
    })
r = requests.get('https://graph.facebook.com/v2.8/threat_exchange_members?' + query_params)
print json.dumps(ast.literal_eval(r.text), sort_keys=True,indent=4,separators=(',', ': '))
```