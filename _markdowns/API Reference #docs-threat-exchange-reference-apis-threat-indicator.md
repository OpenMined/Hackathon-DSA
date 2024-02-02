<div>

Example query for descriptors related to a specific indicator:
852121234856016

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v18.0/852121234856016/descriptors/?access_token=555|aSdF123GhK
```

``` {._5s-8 .prettyprint .lang-code}
 {
   "data": [
  {
    "id": "811927545529339",
    "indicator": {
      "indicator": "test1434227164.evilevillabs.com",
      "type": "DOMAIN",
      "id": "852121234856016"
    },
    "owner": {
      "id": "588498724619612",
      "name": "Facebook CERT ThreatExchange"
    },
    "type": "DOMAIN",
    "raw_indicator": "test1434227164.evilevillabs.com",
    "description": "This is our test domain. It's harmless",
    "status": "NON_MALICIOUS"
  },
  {
    "id": "799906626794304",
    "indicator": {
      "indicator": "test1434227164.evilevillabs.com",
      "type": "DOMAIN",
      "id": "852121234856016"
    },
    "owner": {
      "id": "682796275165036",
      "name": "Facebook Site Integrity ThreatExchange"
    },
    "type": "DOMAIN",
    "raw_indicator": "test1434227164.evilevillabs.com",
    "description": "Malware command and control",
    "status": "MALICIOUS"
  }
],
"paging": {
  "cursors": {
    "before": "ODExOTI3NTQ1NTI5MzM5",
    "after": "Nzk5OTA2NjI2Nzk0MzA0"
  }
}
```

</div>
