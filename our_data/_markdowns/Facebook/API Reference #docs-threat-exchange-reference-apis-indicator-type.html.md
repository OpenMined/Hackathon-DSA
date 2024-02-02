IndicatorType - ThreatExchange - Documentation - Meta for Developers

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
Graph API Versionv19.0IndicatorType
=============
The kind of indicator being described by a ThreatIndicator object. Despite the name IndicatorType, these values can also be used as values for ThreatDescriptor's`type` field.
.
Values
------

Name
 | 
Description
 | 
Type
 | 
Example
 || `ADJUST_TOKEN` | A modification to token permissions in the Windows operating system | `string` | `'Debug'` |
| `API_KEY` | An API key being used within malware | `string` | `'JH52anj9snaQ'` |
| `AS_NUMBER` | An autonomous system number | `number`, `valid ASN` | `'32934'` |
| `BANNER` | A banner reply from a server | `string` | `'Apache/2.2.22 (Ubuntu) Server at localhost Port 80'` |
| `CMD_LINE` | A command line executed in an operating system | `string` | `'cmd.exe C:\tmp\malware.exe'` |
| `COOKIE_NAME` | The name of an HTTP cookie used. | `string` | `'login_name'` |
| `CRX` | A Google Chrome extension ID | `string` | `'aohghmighlieiainnegkcijnfilokake'` |
| `DEBUG_STRING` | A text string found in a binary file | `string` | `'d:\admin\projects\test\test.pdb'` |
| `DEST_PORT` | Network port for the destination host | `number`, bounded to 1-65536 | `'443'` |
| `DIRECTORY_QUERIED` | A string of a file path queried by a process | `string` | `'C:\Windows\tmp'` |
| `DOMAIN` | A valid Internet domain name | `string` | `'facebook.com'` |
| `EMAIL_ADDRESS` | A valid email address | `string` | `'postmaster@facebook.com'` |
| `FILE_CREATED` | File created by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_DELETED` | File deleted by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_MOVED` | File moved by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_NAME` | A file name on a system, can include the path | `string` | `'C:\Temp\bot.exe'` |
| `FILE_OPENED` | File opened by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_READ` | File read by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_WRITTEN` | File written by a process | `string` | `'C:\Temp\bot.exe'` |
| `GET_PARAM` | An HTTP GET query parameter name | `string` | `'search'` |
| `HASH_IMPHASH` | The PE Import hash of a Portable Executable file | `string` | `'17de70812f274b0edd9d0afe69bc7fe2'` |
| `HASH_MD5` | An MD5 hash of a file, string, etc | `string` | `286755fad04869ca523320acce0dc6a4` |
| `HASH_PDQ` | A PDQ hash of an image | `string` | `064bc5ede01712654843fe46b16de93956fae0153baba5d47ac31ef8a5905ec0`
See also
https://github.com/facebook/ThreatExchange/tree/master/hashing/pdq |
| `HASH_TMK` | A TMK hash of a video | `string` | Binary format documented at
https://github.com/facebook/ThreatExchange/tree/master/hashing/tmk |
| `HASH_SHA1` | A SHA1 hash of a file, string, etc. | `string` | `c8fed00eb2e87f1cee8e90ebbe870c190ac3848c` |
| `HASH_SHA256` | A SHA256 hash of a file, string, etc. | `string` | `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` |
| `HASH_SSDEEP` | An SSDeep hash of a file. See http://www.forensicswiki.org/wiki/Ssdeep for more details. | `string` | `768:ZY1jwLjYVmvZDnaB86WaRgAnL4PaxsJc2U0YjpsqANH+Y3b/JgKDiip47502Do1:ZY18LjYUvZDkIrPaxsJ3bxgPcP1` |
| `HASH_VIDEO_MD5` | An MD5 Hash of a video file. | `string` | `460ecaeb03f4870b1db43eda1c7faed7` |
| `HTML_ID` | The value of an ID attribute on an HTML or XHTML tag that identifies malicious or injected markup. | `string` | `my-injected-ad` |
| `HTTP_REQUEST` | The raw DELETE, GET, HEAD or POST. | `string` | `GET /index.html HTTP/1.1` |
| `IP_ADDRESS` | An IP address, version agnostic. | `string` | `127.0.0.1` or `fe80::202:c9ff:fe54:5952` |
| `IP_SUBNET` | A CIDR Mask, version agnostic. | `string` | `128.0.0.0/24` or `fe80::202:c9ff:fe54:5952/64` |
| `ISP` | An Internet service provider. | `string` | `MyInternetServiceProvider Inc.` |
| `LATITUDE` | The latitude for a location, as degrees dotted decimal. | `float` | `37.484924` |
| `LAUNCH_AGENT` | The name of a LaunchAgent on OS X. | `string` | `/System/Library/LaunchAgents/com.apple.quicklook.plist` |
| `LOCATION` | The name of a physical location. Note that there is a separate field `COUNTRY`. | `string` | `Menlo Park, CA` |
| `LONGITUDE` | The longitude for a location, as degrees dotted decimal. | `float` | `-122.148287` |
| `MALWARE_NAME` | The common name for a piece of malware. | `string` | `Zeus` |
| `MEMORY_ALLOC` | The process file name that had memory allocated. | `string` | `C:\Temp\bot.exe` |
| `MEMORY_PROTECT` | The process file name that had memory permissions altered. | `string` | `C:\Temp\bot.exe` |
| `MEMORY_WRITTEN` | The process file name that had its memory written to. | `string` | `C:\Temp\bot.exe` |
| `MUTANT_CREATED` | Mutex created by a process. | `string` | `bot-installed` |
| `MUTEX` | A symbol defined in an OS for synchronization. | `string` |  |
| `NAME_SERVER` | The host name that belongs to a name server. | `string` | `ns1.facebook.com` |
| `OTHER_FILE_OP` | Miscellaneous operations performed on a file. | `string` | `C:\Temp\bot.exe` |
| `PASSWORD` | A password value, **must** be provided as an MD5 hash. | `string` |  |
| `PASSWORD_SALT` | A salt for hashing a password. | `string` |  |
| `PAYLOAD_DATA` | A piece of malicious content (e.g. an image or a document), Base64 encoded. | `string` |  |
| `PAYLOAD_TYPE` | The MIME type format of the content in the PAYLOAD\_DATA field. | `string` | `image/jpeg` |
| `POST_DATA` | Data sent in a POST request. | `string` | `bot_id=1234&field2=Microsoft%20Windows` |
| `PROTOCOL` | The type of data protocol. | `string` | `tcp`, `ftp` |
| `REFERER` | The URI appearing in an HTTP referrer header. | `string` | `http://www.facebook.com/` |
| `REGISTRAR` | The registrar for a domain. | `string` | `REGISTER.COM, INC.` |
| `REGISTRY_KEY` | The name of a registry key in Microsoft Windows. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_CREATED` | Registry key created. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_DELETED` | Registry key deleted. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_ENUMERATED` | Registry key enumerated by a process. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_MONITORED` | Registry key monitored. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_OPENED` | Registry key opened. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_VALUE_CREATED` | Registry key value created. | `string` | `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| `REG_KEY_VALUE_DELETED` | Registry key value deleted. | `string` | `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| `REG_KEY_VALUE_MODIFIED` | Registry key value modified. | `string` | `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| `REG_KEY_VALUE_QUERIED` | Registry key value queried. | `string` | `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| `SIGNATURE` | The signature string for detecting a threat. | `string` |  |
| `SOURCE_PORT` | Network port of the originating host. | `integer` | `13456` |
| `TELEPHONE` | The full, international version of a telephone number | `string` | `+12225551212` |
| `TEXT_STRING` | A string to match text content | `string` | `This is some text that might be harmful` |
| `TREND_QUERY` | Rules to match text. JSON serialized string. Once deserialized,* `"and"` is a list of conditions, ALL of which should match
* each AND condition is a JSON object with a single `"or"` key.
* The value of the `"or"` key is a list of keywords or Regular expressions, ANY of these causes a match.
* Regular expressions begin with `"regex-"`, all other terms are keywords.
* `"not"`is a list of keywords, ANY of which should prevent a match.
Example: The sample to the right would match content that either contains the substring `foo` or matches the regular expression `.*bar.*`, and also contains the substring `zed` but does not contain either the substring `baz` or `ler` | JSON-Serialized `string` | 
```
{
    "and": [
        {"or": ["foo", "regex-/.*bar.*/"]},
        {"or": ["zed"]},
    ],
    "not": [
        "baz",
        "ler",
    ]
}
```
 |
| `URI` | An uniform resource identifier. | `string` | `http://www.facebook.com/some_page.php?test=yes` or `/index.html` |
| `USER_AGENT` | A browser`s user agent string. | `string` | `Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0` |
| `VOLUME_QUERIED` | Volume query action by a process. | `string` |  |
| `WEBSTORAGE_KEY` | The name of a key used in HTML5 local or session storage. | `string` | `malware_session_data` |
| `WEB_PAYLOAD` | The base64 encoded raw payload of a web request, with headers. | `Base64 string` | `R0VUIGh0dHA6Ly9za2V0Y2h5LWRvbWFpbi5iaXovaW1nLTcxNzAwMy5qcGcgSFRUUC8xLjEKSG9zdDogc2tldGNoeS1kb21haW4uYml6ClVzZXItQWdlbnQ6IHdlYmNvbGxhZ2UvMS4xMzVhCgp0ZXN0IGRhdGEK` |
| `WHOIS_NAME` | The name in whois information. | `string` | `Domain Administrator` |
| `WHOIS_ADDR1` | The first address line in whois information. | `string` | `1601 Willow Road` |
| `WHOIS_ADDR2` | The second address line in whois information. | `string` | `Menlo Park, CA 94025` |
| `XPI` | A Firefox addon ID. | `string` | `{e968fc70-8f95-4ab9-9e79-304de2a71ee1}` |