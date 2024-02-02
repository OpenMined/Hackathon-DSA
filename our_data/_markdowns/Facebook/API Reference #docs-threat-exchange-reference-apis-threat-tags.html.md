/threat\_tags - ThreatExchange - Documentation - Meta for Developers

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
Graph API Versionv19.0/threat\_tags
=============
This API call enables searching for tags in ThreatExchange. With this call you can search for ThreatTag objects by text.
Parameters
----------
The following query parameters are available (bold parameters are required):
* **`access_token`** - The key for authenticating to the API.
* **`text`** - Freeform text field with a value to search for. This value should describe a broader type or class of attack you are interested in.
* `fields` - A list of fields to return in the response
* `subscribed` - when POSTing to a specific tag, will subscribe you to a tag for Webhooks
Example query for all tags which start with `malware`:

```
https://graph.facebook.com/v19.0/threat_tags?access_token=555|aSdF123GhK&text=malware
```
```
{
  "data": [
    {
      "id": "1318516441499594",
      "text": "malware"
    },
    {
      "id": "1104531542952223",
      "text": "malwaresite"
    },
    ...
}
```
The same query using a cURL:

```
curl -i -X GET \
 "https://graph.facebook.com/v14.0/threat_tags?access_token=555|7C1234&amp;text=malware"
```
The same query in Python:

```
import requests
import json
import ast
import urllib
app_id = '555' # Replace this with your app ID
app_secret = '1234' # Replace this with your app secret
text = 'malware'
query_params = urllib.urlencode({
    'access_token' : app_id + '|' + app_secret,
    'text' : text
    })
r = requests.get('https://graph.facebook.com/v14.0/threat_tags?' + query_params)
print json.dumps(ast.literal_eval(r.text), sort_keys=True,indent=4,separators=(',', ': '))
```
Example query for tags which start with `ducks` and fetching the tagged objects.

```
https://graph.facebook.com/v19.0/threat_tags/?access_token=555|aSdF123GhK&text=ducks&fields=id,text,tagged_objects
```
Data returned:

```
{
  "data": [
    {
      "id": "501159930008561",
      "text": "ducks"
      "tagged_objects": {
        "data": [
          {
            "id": "1162586023812794",
            "type": "THREAT_DESCRIPTOR",
            "name": "test1469481750.evilevillabs.com"
          },
          ...
        ]
      },
    }
  ]
}
```