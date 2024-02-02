::: {._4-u3 ._588p}
The following query parameters are available (bold parameters are
required):

-   **` access_token `** - The key for authenticating to the API.

-   **` text `** - Freeform text field with a value to search for. This
    value should describe a broader type or class of attack you are
    interested in.

-   ` fields ` - A list of fields to return in the response

-   ` subscribed ` - when POSTing to a specific tag, will subscribe you
    to a tag for Webhooks

Example query for all tags which start with ` malware ` :

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v18.0/threat_tags?access_token=555|aSdF123GhK&text=malware
```

``` {._5s-8 .prettyprint .lang-code}
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

``` {._5s-8 .prettyprint .lang-code}
curl -i -X GET \
 "https://graph.facebook.com/v14.0/threat_tags?access_token=555|7C1234&amp;text=malware"
```

The same query in Python:

``` {._5s-8 .prettyprint .lang-code}
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

Example query for tags which start with ` ducks ` and fetching the
tagged objects.

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v18.0/threat_tags/?access_token=555|aSdF123GhK&text=ducks&fields=id,text,tagged_objects
```

Data returned:

``` {._5s-8 .prettyprint .lang-code}
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
:::
