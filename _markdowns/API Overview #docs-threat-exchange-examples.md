::: {._4-u3 ._588p}
Example 1: A query to get all threat indicators which are IP Addresses
of proxies in ThreatExchange.

``` {._5s-8 .prettyprint .lang-code}
import requests
import json
import ast
import urllib

app_id = '555' # Replace this with your app ID
app_secret = '1234' # Replace this with your app secret
type_ = 'IP_ADDRESS'
text = 'proxy'

query_params = urllib.urlencode({
'access_token' : app_id + '|' + app_secret,
'type' : type_,
'text' : text
})

r = requests.get('https://graph.facebook.com/v2.4/threat_indicators?' + query_params)

print json.dumps(ast.literal_eval(r.text), sort_keys=True,indent=4,separators=(',', ': '))
```

Example 2: A query to get all IP Addresses of proxies uploaded by the
Facebook Administrator app in ThreatExchange.

``` {._5s-8 .prettyprint .lang-code}
import requests
import json
import ast
import urllib

app_id = '555' # Replace this with your app ID
app_secret = '1234' # Replace this with your app secret
type_ = 'IP_ADDRESS'
owner_app_id = 820763734618599
text = 'proxy'

query_params = urllib.urlencode({
'access_token' : app_id + '|' + app_secret,
'type' : type_,
'owner' : owner_app_id,
'text' : text
})

r = requests.get('https://graph.facebook.com/v2.4/threat_descriptors?' + query_params)

print json.dumps(ast.literal_eval(r.text), sort_keys=True,indent=4,separators=(',', ': '))
```
:::
