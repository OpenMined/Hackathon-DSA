::: {._4-u3 ._588p}
The following is an examples are submissions of a new malicious domain
to ThreatExchange. In each example, we define which members of
ThreatExchange are allowed to see the data.

### Controlling visibility using the UI {#visible}

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/73042650_894706234256259_718260484855300096_n.png?_nc_cat=110&ccb=1-7&_nc_sid=f537c7&_nc_ohc=Lj8Dl-HRJG0AX-U7amZ&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBjQoMgcaPy47UrNq9I2dEj3jRkFpodG7V9JOivtjGhIA&oe=65A92C0B){.img
srcset="https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/73042650_894706234256259_718260484855300096_n.png?_nc_cat=110&ccb=1-7&_nc_sid=f537c7&_nc_ohc=Lj8Dl-HRJG0AX-U7amZ&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBjQoMgcaPy47UrNq9I2dEj3jRkFpodG7V9JOivtjGhIA&oe=65A92C0B"}
:::

### Allowing all members access using the API {#visible}

``` {._5s-8 .prettyprint .lang-code}
POST https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=VISIBLE
```

### Limiting privacy to a privacy group using the API {#privacygroup}

``` {._5s-8 .prettyprint .lang-code}
POST https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=HAS_PRIVACY_GROUP
&amp;privacy_members=123456789
```

### Limiting privacy To select members using the API {#whitelist}

``` {._5s-8 .prettyprint .lang-code}
POST https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=HAS_WHITELIST
&amp;privacy_members=123456789,9012345678
```

### Limiting privacy to only your app using the API {#onlyme}

``` {._5s-8 .prettyprint .lang-code}
POST https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=HAS_WHITELIST
&amp;privacy_members=555
```
:::
