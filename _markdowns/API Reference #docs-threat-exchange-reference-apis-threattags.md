::: {._4-u3 ._588p}
::: _57-c
Name
:::
:::

Description

Type

` tagged_objects `

The objects tagged with this text.

` Malware ` , ` ThreatDescriptor ` , ` MalwareFamily `

The following query parameters are available:

-   ` tagged_since ` - Fetches all objects that have been tagged since
    this time (inclusive).

-   ` tagged_until ` - Fetches all objects that have been tagged until
    this time (inclusive).

Tagged objects are returned in the order based on when the tag was
applied, ascending. This timestamp is currently not exposed by the API,
but is the same one used by ` tagged_since ` and ` tagged_until ` .
While this API can be used to create a copy of data in ThreatExchange,
the
[threat_updates](/docs/threat-exchange/reference/apis/threat-updates/v10.0)
API may be better suited for your usecase.

### Sample Usage {#connections_usage}

Example of tagged objects for a specific ThreatTag: 908180082612873

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v2.7/908180082612873/tagged_objects/?access_token=555|aSdF123GhK
```

Data returned:

``` {._5s-8 .prettyprint .lang-code}
{
  "data": [
    {
      "id": "1039423046092869",
      "type": "THREAT_DESCRIPTOR",
      "name": "test1464195852.evilevillabs.com"
    },
    ...
  ]
}
```

Example of tagged objects for a ThreatTag with the text \'ducks\'

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v2.7/threat_tags/?access_token=555|aSdF123GhK&amp;text=ducks&amp;fields=id,text,tagged_objects
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
