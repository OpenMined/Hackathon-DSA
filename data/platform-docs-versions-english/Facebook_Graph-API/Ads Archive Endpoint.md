Ad Library API
==============

Reading
-------

Returns archived ads based on your search.

  

Reading with the API returns [archived ads](https://developers.facebook.com/docs/graph-api/reference/archived-ad/) from the [Meta Ad Library](https://www.facebook.com/ads/library) based on keyword searches of text, images, audio from video, and the call-to-action button. **Note that we do not translate your keyword searches**, therefore you should write them in the language of the ads you are searching. For example, if you are searching Spanish language ads you should write your search string in Spanish.

Learn more about the [Ad Library API](https://www.facebook.com/ads/library/api).

### End of Results

The ad objects are returned in `data`. If you paginate through results and reach a point where `data` contains no values, this means you have reached the end of the result set.

### Search by Page

You can request archived ads for up to 10 Facebook Page IDs at once by using the search parameter `search_page_ids`.

### Filters

You can use filters in your search query to return only certain types of ads. See `bylines` and `publisher_platforms` below.

### Examples

To return archived ads related to social issues, elections and politics that contain the word 'california' and reached an audience in the US:

cURL

    curl -G \
    -d "search_terms='california'" \
    -d "ad_type=POLITICAL_AND_ISSUE_ADS" \
    -d "ad_reached_countries=['US']" \
    -d "access_token=<ACCESS_TOKEN>" \
    "https://graph.facebook.com/<VERSION>/ads_archive"

  
Show Response

### Parameters

| Parameter | Description |
| --- | --- |
| `ad_active_status`<br><br>enum {ACTIVE, ALL, INACTIVE} | Search for ads based on the status. Defaults to `ACTIVE` for all ads that are eligible for delivery. Set `INACTIVE` for ads ineligible for delivery, and `ALL` for both types. |
| `ad_delivery_date_max`<br><br>string | Search for ads delivered before the date (inclusive) you provide. The date format should be YYYY-mm-dd. |
| `ad_delivery_date_min`<br><br>string | Search for ads delivered after the date (inclusive) you provide. The date format should be YYYY-mm-dd. |
| `ad_reached_countries`<br><br>array<enum {ALL, BR, IN, GB, US, CA, AR, AU, AT, BE, CL, CN, CO, HR, DK, DO, EG, FI, FR, DE, GR, HK, ID, IE, IL, IT, JP, JO, KW, LB, MY, MX, NL, NZ, NG, NO, PK, PA, PE, PH, PL, RU, SA, RS, SG, ZA, KR, ES, SE, CH, TW, TH, TR, AE, VE, PT, LU, BG, CZ, SI, IS, SK, LT, TT, BD, LK, KE, HU, MA, CY, JM, EC, RO, BO, GT, CR, QA, SV, HN, NI, PY, UY, PR, BA, PS, TN, BH, VN, GH, MU, UA, MT, BS, MV, OM, MK, LV, EE, IQ, DZ, AL, NP, MO, ME, SN, GE, BN, UG, GP, BB, AZ, TZ, LY, MQ, CM, BW, ET, KZ, NA, MG, NC, MD, FJ, BY, JE, GU, YE, ZM, IM, HT, KH, AW, PF, AF, BM, GY, AM, MW, AG, RW, GG, GM, FO, LC, KY, BJ, AD, GD, VI, BZ, VC, MN, MZ, ML, AO, GF, UZ, DJ, BF, MC, TG, GL, GA, GI, CD, KG, PG, BT, KN, SZ, LS, LA, LI, MP, SR, SC, VG, TC, DM, MR, AX, SM, SL, NE, CG, AI, YT, CV, GN, TM, BI, TJ, VU, SB, ER, WS, AS, FK, GQ, TO, KM, PW, FM, CF, SO, MH, VA, TD, KI, ST, TV, NR, RE, LR, ZW, CI, MM, AN, AQ, BQ, BV, IO, CX, CC, CK, CW, TF, GW, HM, XK, MS, NU, NF, PN, BL, SH, MF, PM, SX, GS, SS, SJ, TL, TK, UM, WF, EH}> | Search ALL or by [ISO country code](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.iso.org%2Fiso-3166-country-codes.html&h=AT0CSX1B9qvXpHMJongJU0L_R58voRgzy0ylIhSN52OKMydbbZTJ9_D_iaB_lyvpfdn7nZDpSO04FeVbb31kVa73NkjUGF80wBHBXdK2YyK6YdwPJabc5SgjerSSwZ6TEdCfPKGifKZyBWxh) to return ads that reached specific countries or locations. Note: Ads that did not reach any location in the EU will only return if they are about [social issues, elections or politics](https://www.facebook.com/business/help/167836590566506).<br><br>Required |
| `ad_type`<br><br>enum {ALL, CREDIT\_ADS, EMPLOYMENT\_ADS, HOUSING\_ADS, POLITICAL\_AND\_ISSUE\_ADS} | Default value: `"ALL"`<br><br>Search by type of ad. You can use this to narrow your results to ads in [special ad categories](https://www.facebook.com/business/help/298000447747885#): CREDIT\_ADS returns ads related to financial products or institutions. EMPLOYMENT\_ADS returns ads related to job listings or employment opportunities. HOUSING\_ADS returns housing or real estate ads. POLITICAL\_AND\_ISSUE\_ADS returns ads about [social issues, elections or politics](https://www.facebook.com/business/help/167836590566506). ALL returns ads on all topics. |
| `bylines`<br><br>array<string> | Filter results for ads with a _paid for by disclaimer_ byline, such as political ads that reference “immigration” paid for by “ACLU”. Provide a JSON array to search for a byline without a comma _or_ one with a comma. For instance `?bylines=["byline, with a comma,","byline without a comma"]` returns results with either text variation. You must list the complete byline. For example, 'Maria' would not return ads with the byline 'Maria C. Lee for America.' **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `delivery_by_region`<br><br>array<string> | View ads by the region (such as state or province) where [Accounts Center accounts](https://www.facebook.com/business/help/283579896000936) were based or located when an ad was displayed to them. You can provide a comma-separated list of regions. For instance `?delivery_by_region=['California', 'New York']`. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `estimated_audience_size_max`<br><br>int64 | Search for ads with a maximum estimated audience size. Must be one of these range boundaries: 1000, 5000, 10000, 50000, 100000, 500000, 1000000. Leave empty for no maximum boundary. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `estimated_audience_size_min`<br><br>int64 | Search for ads with a minimum estimated audience size. Must be one of these range boundaries: 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000. Leave empty for no minimum boundary. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `languages`<br><br>array<string> | Search for ads based on the language(s) contained in the ad. Language codes are based on the [ISO 639-1 language codes](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.iso.org%2Fstandard%2F22109.html&h=AT2OKqhtWmuztmLHkTLigG6dFl1lzSaZKLtTir1Eh9Easlpls69k4_JnzpEw1pEo8CXK_ramjhRDRh9fwk8aCicve3-UxZS-YF9X0tYdDZVeEalVoH-pwlXtYh8-xaOG3WmdVNlQEOfK7dTZ) and also includes ISO 639-3 language codes CMN and YUE.<br><br>For instance `?languages=['es', 'en']`. |
| `media_type`<br><br>enum {ALL, IMAGE, MEME, VIDEO, NONE} | Search for ads based on whether they contain a specific type of media, such as an image or video. |
| `publisher_platforms`<br><br>array<enum {FACEBOOK, INSTAGRAM, AUDIENCE\_NETWORK, MESSENGER, WHATSAPP, OCULUS}> | Search for ads based on whether they appear on a particular Meta technology, such as Instagram or Facebook. You can provide one technology or a comma-separated list of technologies. |
| `search_page_ids`<br><br>array<int64> | Search for archived ads based on specific Facebook Page IDs. You can provide up to ten IDs, separated by commas. |
| `search_terms`<br><br>string | Default value: `""`<br><br>The terms to search for in your query. We treat a blank space as a logical `AND` and search for both terms and no other operators. The limit of your string is 100 characters or less. Use `search_type` to adjust the type of search to use. |
| `search_type`<br><br>enum {KEYWORD\_UNORDERED, KEYWORD\_EXACT\_PHRASE} | Default value: `KEYWORD_UNORDERED` The type of search to use for the `search_terms` field. `KEYWORD_UNORDERED` will treat each word in `search_terms` individually, and return results that contain these words in any order. `KEYWORD_EXACT_PHRASE` will treat the words in `search_terms` as a single phrase, and only return results that match that exact phrase. To search for multiple phrases at once, separate groups of words in `search_terms` by commas. This will retrieve results that contain an exact match for every phrase. |
| `unmask_removed_content`<br><br>boolean | Default value: `false`<br><br>Specify whether you would like your results to reveal content that was removed for violating our standards. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ArchivedAd](https://developers.facebook.com/docs/marketing-api/reference/archived-ad/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 1009 | Failed to pass parameter validation. |
| 200 | Permissions error |

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)