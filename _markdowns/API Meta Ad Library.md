













Ad Library API


Ad LibraryAd Library ReportAd Library APIBranded Content​Sign inAd LibraryAd Library ReportAd Library APIBranded Content

---

Access the APIView release notesSystem statusSubscribe to email updatesAbout ads and data usePrivacyTermsCookiesAccess the APIRelease notesMeta Ad Library APIThe Ad Library API helps you perform customized searches of the Ad Library for:* Ads about social issues, election or politics that were delivered anywhere in the world during the past 7 years
* Ads of any type that were delivered to the European Union during the past year
To use the API, it helps to be a little familiar with programming. For a simpler research solution, you may want to start with our Ad Library Report.To search for all ads currently running across Meta technologies, please use the Ad Library.Ready to get started?To get authorized to use the API, you'll need a Facebook account.Step 1: Confirm your identity and locationGo to Facebook.com/ID and follow the confirmation process required to run ads about social issues, elections or politics. It can take a few days to confirm the information you submit.Step 2: Create a Meta for Developers accountVisit Meta for Developers and select **Get Started**. As part of account creation, you'll need to agree to our Platform Policy.Step 3: add a new appOnce you have an account, return to this webpage and select **Access the API**. You can then create a new app by selecting **My Apps > Create App**.When your app is ready, you can begin using the Ad Library API* You can learn more about creating queries and using the Graph API environment from the Meta for Developers documentation
* If you're an experienced API developer, you may instead want to visit Meta's Ad Library API Script Repository on Github, which includes code examples and a simple command-line interface
What you can search for through the APIAll available ads will have:* Library ID
* Content of the ad creative (subject to our Terms of Service)
* Page name and Page ID associated with the ad
* Ad delivery dates
* Where the ad appeared (Facebook, Instagram, etc.)
Ads about social issues, elections or politics will also have:* Total amount spent (range)
* Total impressions received (range)
* Demographic information on ad reach, such as age, gender and location (%)
Ads that were delivered to the European Union will also have:* Total impressions an ad received in the EU (estimated)
* Targeting and reach demographic information specific to the EU (estimated)
* Beneficiary and payer information
In the case of estimated values, aggregated demographic data is based on a number of factors, including age and gender information users provide in their Facebook profile.An example query and responseTo retrieve data on ads about social issues, elections or politics that contain the term "**california**" and that reached an audience in the United States, you could enter this query:`curl -G \``-d "search_terms='california'" \``-d "ad_type=POLITICAL_AND_ISSUE_ADS" \``-d "ad_reached_countries=['US']" \``-d "access_token=<ACCESS_TOKEN>" \``"https://graph.facebook.com/<API_VERSION>/ads_archive"`Which would return a response like this:{
 "data": [
 {
 "page\_id": "123",
 "page\_name": "123",
 "ad\_snapshot\_url": "https://www.facebook.com/ads/archive/render\_ad/?id=123&amp;access\_token=&lt;ACCESS\_TOKEN&gt;"
 }
 ],
 "paging": {
 "cursors": {
 "before": "MAZDZD",
 "after": "MAZDZD"
 },
 "next": "https://graph.facebook.com/v3.1/ads\_archive?access\_token=&lt;ACCESS\_TOKEN&gt;&amp;fields=page\_id,page\_name,ad\_snapshot\_url&amp;search\_terms='california'&amp;ad\_type=POLITICAL\_AND\_ISSUE\_ADS&amp;ad\_reached\_countries=['US']&amp;limit=25&amp;after=MAZDZD"
 }
}Search parameters you can use to find ads:Note that some parameters are only valid for certain types of ads, as indicated in the parameter description.

| Name | Description |
| --- | --- |
| `ad_active_status`enum {ACTIVE, ALL, INACTIVE} | Search for ads based on the status. Defaults to `ACTIVE` for all ads that are eligible for delivery. Set `INACTIVE` for ads ineligible for delivery, and `ALL` for both types. |
| `ad_delivery_date_max`string | Search for ads delivered before the date (inclusive) you provide. The date format should be YYYY-mm-dd. |
| `ad_delivery_date_min`string | Search for ads delivered after the date (inclusive) you provide. The date format should be YYYY-mm-dd. |
| `ad_reached_countries`array<enum {ALL, BR, IN, GB, US, CA, AR, AU, AT, BE, CL, CN, CO, HR, DK, DO, EG, FI, FR, DE, GR, HK, ID, IE, IL, IT, JP, JO, KW, LB, MY, MX, NL, NZ, NG, NO, PK, PA, PE, PH, PL, RU, SA, RS, SG, ZA, KR, ES, SE, CH, TW, TH, TR, AE, VE, PT, LU, BG, CZ, SI, IS, SK, LT, TT, BD, LK, KE, HU, MA, CY, JM, EC, RO, BO, GT, CR, QA, SV, HN, NI, PY, UY, PR, BA, PS, TN, BH, VN, GH, MU, UA, MT, BS, MV, OM, MK, LV, EE, IQ, DZ, AL, NP, MO, ME, SN, GE, BN, UG, GP, BB, AZ, TZ, LY, MQ, CM, BW, ET, KZ, NA, MG, NC, MD, FJ, BY, JE, GU, YE, ZM, IM, HT, KH, AW, PF, AF, BM, GY, AM, MW, AG, RW, GG, GM, FO, LC, KY, BJ, AD, GD, VI, BZ, VC, MN, MZ, ML, AO, GF, UZ, DJ, BF, MC, TG, GL, GA, GI, CD, KG, PG, BT, KN, SZ, LS, LA, LI, MP, SR, SC, VG, TC, DM, MR, AX, SM, SL, NE, CG, AI, YT, CV, GN, TM, BI, TJ, VU, SB, ER, WS, AS, FK, GQ, TO, KM, PW, FM, CF, SO, MH, VA, TD, KI, ST, TV, NR, RE, LR, ZW, CI, MM, AN, AQ, BQ, BV, IO, CX, CC, CK, CW, TF, GW, HM, XK, MS, NU, NF, PN, BL, SH, MF, PM, SX, GS, SS, SJ, TL, TK, UM, WF, EH}> | Search ALL or by ISO country code to return ads that reached specific countries or locations. Note: Ads that did not reach any location in the EU will only return if they are about social issues, elections or politics.RequiredThis parameter is required. |
| `ad_type`enum {ALL, CREDIT\_ADS, EMPLOYMENT\_ADS, HOUSING\_ADS, POLITICAL\_AND\_ISSUE\_ADS} | Default value: `"ALL"`Search by type of ad. You can use this to narrow your results to ads in special ad categories: CREDIT\_ADS returns ads related to financial products or institutions. EMPLOYMENT\_ADS returns ads related to job listings or employment opportunities. HOUSING\_ADS returns housing or real estate ads. POLITICAL\_AND\_ISSUE\_ADS returns ads about social issues, elections or politics. ALL returns ads on all topics. |
| `bylines`array<string> | Filter results for ads with a *paid for by disclaimer* byline, such as political ads that reference “immigration” paid for by “ACLU”. Provide a JSON array to search for a byline without a comma *or* one with a comma. For instance `?bylines=["byline, with a comma,","byline without a comma"]` returns results with either text variation. You must list the complete byline. For example, 'Maria' would not return ads with the byline 'Maria C. Lee for America.' **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `delivery_by_region`array<string> | View ads by the region (such as state or province) where Accounts Center accounts were based or located when an ad was displayed to them. You can provide a comma-separated list of regions. For instance `?delivery_by_region=['California', 'New York']`. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `estimated_audience_size_max`int64 | Search for ads with a maximum estimated audience size. Must be one of these range boundaries: 1000, 5000, 10000, 50000, 100000, 500000, 1000000. Leave empty for no maximum boundary. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `estimated_audience_size_min`int64 | Search for ads with a minimum estimated audience size. Must be one of these range boundaries: 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000. Leave empty for no minimum boundary. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `languages`array<string> | Search for ads based on the language(s) contained in the ad. Language codes are based on the ISO 639-1 language codes and also includes ISO 639-3 language codes CMN and YUE.For instance `?languages=['es', 'en']`. |
| `media_type`enum {ALL, IMAGE, MEME, VIDEO, NONE} | Search for ads based on whether they contain a specific type of media, such as an image or video. |
| `publisher_platforms`array<enum {FACEBOOK, INSTAGRAM, AUDIENCE\_NETWORK, MESSENGER, WHATSAPP, OCULUS}> | Search for ads based on whether they appear on a particular Meta technology, such as Instagram or Facebook. You can provide one technology or a comma-separated list of technologies. |
| `search_page_ids`array<int64> | Search for archived ads based on specific Facebook Page IDs. You can provide up to ten IDs, separated by commas. |
| `search_terms`string | Default value: `""`The terms to search for in your query. We treat a blank space as a logical `AND` and search for both terms and no other operators. The limit of your string is 100 characters or less. Use `search_type` to adjust the type of search to use. |
| `search_type`enum {KEYWORD\_UNORDERED, KEYWORD\_EXACT\_PHRASE} | Default value: `KEYWORD_UNORDERED`
The type of search to use for the `search_terms` field.
`KEYWORD_UNORDERED` will treat each word in `search_terms` individually, and return results that contain these words in any order.
`KEYWORD_EXACT_PHRASE` will treat the words in `search_terms` as a single phrase, and only return results that match that exact phrase.
To search for multiple phrases at once, separate groups of words in `search_terms` by commas. This will retrieve results that contain an exact match for every phrase. |
| `unmask_removed_content`boolean | Default value: `false`Specify whether you would like your results to reveal content that was removed for violating our standards. |

Data fields you can include in your search results:Note that some fields will only return data for certain types of ads and/or particular delivery locations, as indicated in the field description.

| Name | Description |
| --- | --- |
| `id`numeric string | The Library ID of the ad object. |
| `ad_creation_time`string | The UTC date and time when someone created the ad. This is not the same time as when the ad ran. Includes date and time separated by `T`. Example: `2019-01-24T19:02:04+0000`, where `+0000` is the UTC offset. |
| `ad_creative_bodies`list<string> | A list of the text which displays in each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards each with their own unique text. See Reference, Ad Creative. |
| `ad_creative_link_captions`list<string> | A list of the captions which appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards each with their own unique text that appears in the link. |
| `ad_creative_link_descriptions`list<string> | A list of text descriptions which appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards each with their own unique text describing the link. |
| `ad_creative_link_titles`list<string> | A list of titles which appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards each with their own unique title text about the link. |
| `ad_delivery_start_time`string | Date and time when an advertiser wants to start delivering an ad. Provided in UTC as in `ad_creation_time`.DefaultThis field is default. |
| `ad_delivery_stop_time`string | The time when an advertiser wants to stop delivery of their ad. If this is blank, the ad will run until the advertiser stops it or they spend their entire campaign budget. In UTC.DefaultThis field is default. |
| `ad_snapshot_url`string | String with URL link which displays the archived ad. This displays uncompressed images and videos from the ad. While you cannot currently download a batch of archived ads, you can download ad creative such as images and text for an individual ad. If you do so, it must be for analysis and you must comply with the data storage terms in our Terms of Service.DefaultThis field is default. |
| `age_country_gender_reach_breakdown`list<AgeCountryGenderReachBreakdown> | The demographic distribution of Accounts Center accounts in the EU reached by the ad. **Available only for ads delivered to the EU** |
| `beneficiary_payers`list<BeneficiaryPayer> | The reported beneficiaries and payers for this ad. **Available only for ads delivered to the EU** |
| `bylines`string | A string containing the name of the person, company, or entity that provided funding for the ad. Provided by the purchaser of the ad. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `currency`string | The currency used to pay for the ad, as an ISO currency code. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `delivery_by_region`list<AudienceDistribution> | Regional distribution of Accounts Center accounts reached by the ad. Provided as a percentage and where regions are at a sub-country level. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `demographic_distribution`list<AudienceDistribution> | The demographic distribution of Accounts Center accounts reached by the ad. Provided as age ranges and gender. Age ranges: Can be one of 18-24, 25-34, 35-44, 45-54, 55-64, 65+. Gender: Can be the following strings: "Male", "Female", "Unknown". **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `estimated_audience_size`InsightsRangeValue | Estimated Audience Size generally estimates how many Accounts Center accounts meet the targeting and ad placement criteria that advertisers select while creating an ad. Learn more. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `eu_total_reach`int32 | The estimated combined ad reach for all locations inside the European Union. **Available only for ads delivered to the EU** |
| `impressions`InsightsRangeValue | A string containing the number of times the ad created an impression. In ranges of: <1000, 1K-5K, 5K-10K, 10K-50K, 50K-100K, 100K-200K, 200K-500K, >1M. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `languages`list<string> | The list of languages contained within the ad. These are displayed in ISO 639-1 language codes. |
| `page_id`numeric string | ID of the Facebook Page that ran the ad.DefaultThis field is default. |
| `page_name`string | Name of the Facebook Page which ran the ad. |
| `publisher_platforms`list<enum> | A list of Meta technologies where the archived ad appeared, such as Facebook or Instagram. |
| `spend`InsightsRangeValue | A string showing the amount of money spent running the ad, as specified in `currency`. This is reported in ranges: <100, 100-499, 500-999, 1K-5K, 5K-10K, 10K- 50K, 50K-100K, 100K-200K, 200K-500K, >1M. **Available only for POLITICAL\_AND\_ISSUE\_ADS** |
| `target_ages`list<numeric string> | The age ranges selected for ad targeting in the EU. The lowest age that can be returned is 13; the highest is 65+. **Available only for ads delivered to the EU** |
| `target_gender`enum | The genders selected for ad targeting in the EU. Possible values: “Women”, “Men” or “All”. **Available only for ads delivered to the EU** |
| `target_locations`list<TargetLocation> | The locations included or excluded for ad targeting in the EU. **Available only for ads delivered to the EU** |

Frequently asked questionsWhere is the API available?Do I need an access token?How do I get data using the Graph API?How do I use the Graph API Explorer?Where can I find additional developer documentation?Why are some fields and parameters only available for certain types of ads?What does error 1357045 mean?Are there any unique identifiers provided for individual ads?How are ad start dates determined?What is the maximum number of ads a search can return?How can I learn more about ads about social issues, elections or politics?Can I publish an article or research findings about using the API?Can I share data obtained from the API with other researchers or journalists?I have a question not answered here. Where can I find help?System status* About ads and data use
* Privacy
* Terms
* Cookies

Meta © 2024 | English (US)
































