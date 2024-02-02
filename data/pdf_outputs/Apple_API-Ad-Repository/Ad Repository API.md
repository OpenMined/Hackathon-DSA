## Ad Repository API

January 2024

###### Contents

* Getting Started................
* 3 Versioning
* 3 Usability
* 3 Get a list of app and developer names
* 4 Request example
* 4 Request parameters
* 4 Response example
* 5 Response properties
* 6 Get a list of countries or regions
* 7 Response example
* 7 Response properties
* 8 Get a list of ads
* 9 Request example
* 9 Request parameters
* 9 Response example
* 10 Response properties
* 11 Get ad variations
* 14 Request parameters
* 14 Response example
* 15 Response properties
* 17 Get advertising-restrictions
* 20 Request example
* 20 Request parameters
* 20 Response example
* 21 Response properties
* 22 Response properties
* 22 Changelog

## Getting Started

Use the Ad Repository API to look up Apple-delivered advertising on the App Store in select European countries and regions as well as information about qualifying advertising restrictions. You can manage API calls programmatically using API tools and programs of your choice.

### Versioning

The current version of the API is v1.

### Usability

* Communication with the web service must use HTTPS.
* RSQL query patterns are supported in some endpoints.
* The API doesn't accept headers with */*. Disallow Accept */* in your cURL commands.
* API responses will have a header Content-Type: application/json.

## Get a list of app and developer names

GET [https://adrepository.apple.com/api/v1/ad-repository-entities](https://adrepository.apple.com/api/v1/ad-repository-entities)

Use this endpoint to return list of app and developer names based on custom query parameter input. A developer name refers to the developer as identified on the App Store, which is the entity on whose behalf the subject advertising was presented. Only apps that have been advertised in countries or regions in the European Union in which Apple-delivered advertising is available on the App Store are searchable.

### Request example

GET -/api/v1/ad-repository-entities?name={URL encoded search input text}  &types==APP  &offset=0  &limit=10

### Request parameters

\begin{tabular}{|l|c|c|c|} \hline
**Parameter** & **Type** & **Required** & **Description** \\ \hline name & string & yes & Custom query for app and developer names with a minimum of 2 characters required. \\ \hline  & & & Values are: \\ types & string & no & DEVELOPER \\  & & & APP, DEVELOPER (The default value or blank which returns all types.) \\ \hline offset & integer & no & The offset pagination that limits the number of returned records. The default is 0. \\ \hline limit & integer & no & The maximum number of entries to return per page. The default is 50. \\ \hline \end{tabular}

Response example The AdRepositoryEntity object is returned:

{  "data": [  "id": 1582276305,  "name": "TripTrek",  "type": "App"  },  {  "id": 819221,  "name": "TripTrek, Inc.",  "type": "DEVELOPER"  },  "pagination": {  "totalResults": 2,  "startIndex": 0,  "itemsPerPage": 15  } } ```

Ad Repository API January 2024Response properties

**Parameter** & **Type** & **Description**

id & integer & A unique identifier. If the type is APP, the id will be an appId. If the type is DEVELOPER, the id is a developerId. name & string & The entity name on whose behalf the advertising was presented. type & string & Values are APP, DEVELOPER

pagination & integer & Returned pagination results. totalResults: The total number of entries that return for the operation. startIndex: Specifies the position of the first element in the results. The default is zero. itemsPerPage: Specifies how many items is displayed per page.

### Get a list of countries or regions

Use this endpoint to get a list of countries or regions in the European Union in which Apple-delivered advertising is available on the App Store. Use the country codes returned in the response in the Get a list of ads call.

#### Request example

GET [https://adrepository.apple.com/api/v1/countries-or-regions](https://adrepository.apple.com/api/v1/countries-or-regions)

#### Response example

{  "data": [  {  "name": "Austria",  "code": "AT"  },  {  "name": "Belgium",  "code": "BE"  },  {  "name": "Croatia",  "code": "HR"  },  {  "name": "Czech Republic",  "code": "CZ"  },  {  "name": "Denmark",  "code": "DK"  },  {  "name": "Finland",  "code": "FI"  },  {  "name": "France",  "code": "FR"  },  {  "name": "Germany",  "code": "DE"  },  {  "name": "Greece",  "code": "GR"  },  {  "name": "Hungary",  "code": "HU"  },  {  "name": "Ireland",  "code": "IE"  },  {  "name": "Italy","code":"IT"  },  {  "name":"Netherlands",  "code":"NL"  },  {  "name":"Poland",  "code":"PL"  },  {  "name":"Portugal",  "code":"PT"  },  {  "name":"Romania",  "code":"RO"  },  {  "name":"Spain",  "code":"ES"  },  {  "name":"Sweden",  "code":"SE"  }  } }

Response properties

ParameterType

Description

namestring

The name of the country or region in the European Union in which Apple-delivered advertising is available on the App Store. For example: "Sweden".

codestring

The ISO 3166-1 alpha-2 two-letter country code of the country or region in the European Union in which Apple-delivered advertising is available on the App Store. For example: ES, SE, DE.

## Get a list of ads

Use this endpoint to return ad metadata and an adId to use in the Get Ad Variations call.

GET [https://adrepository.apple.com/api/v1/ad-repository-ads](https://adrepository.apple.com/api/v1/ad-repository-ads)

### Request example

* Use ql= URL encoded RSQL filter to allow special characters.
* You can have both id or countryOrRegion or either in a request. If id is used then type must also be present.

GET -/api/v1/ad-repository-ads ?ql=  type==APP;  id==1582276305;  countryOrRegion=in=(FR,DE);  datePreset==LAST_90_DAYS; &offset=0  &limit=50

### Request parameters

\begin{tabular}{|l|c|c|c|} \hline
**Parameter** & **Type** & **Required** & **Description** \\ \hline type & string & yes & Values are APP, DEVELOPER. \\ \hline id & string & yes & A unique identifier. If the type is APP, the id is an appl. If the type is DEVELOPER, the id is a developerId. \\ \hline countryOrRegion & string & yes & A country or region in the European Union in which Apple-delivered advertising is available on the App Store, expressed in ISO 3166-1 alpha-2 format. For example: ES, SE, DE. \\ \hline datePreset & string & no & The date range of the request. Values are \\  & & & Last_90_DAYS,LAST_YEAR. \\  & & & The default isLAST_90_DAYS. \\ \hline limit & integer & no & The maximum number of entries to return per page. The default is 50. \\ \hline offset & integer & no & The offset pagination that limits the number of returned records. The default is 0. \\ \hline \end{tabular}

### Response example

The AdRepositoryAd object is returned.

{  "data": [  {  "adId": "76324182",  "appId": 1582276305,  "appName": "TripTrek - travel app",  "developerId": 819221,  "developerName": "Apple Inc",  "legalName": "Apple Inc.",  "placement": "APPSTORE_SEARCH_RESULT",  "format": "Icon Ad",  "countryOrRegion": "es",  "audienceRefinement": {  "ageTarget": "false",  "genderTarget": "false",  "locationTarget": "true",  "customerTypeTarget": "false"  },  "firstImpressionDate": "2022-08-25",  "lastImpressionDate": "2023-04-01",  "defaultLanguageTag": "es-ES",  "defaultLanguageDisplayName": "Spanish (Spain)",  "defaultPreviewDevice": "iPhone_6.5",  "adBanner": {  "joeColor": "b:ff4c00p:04@404s:17lc@1t:361303q:452501",  "iconPictureUrl": "",  "subtitle": "Planifique sus viajes con confianza.",  "primaryCategory": "viajar",  "inAppurchases": "false",  "promotionalText": "Descripcion de la aplicacion mostrada en la App Store.",  "editorialBadge": "false"  "shortDescription": "una descripcion de la aplicacion asociada con el anuncio."  },  "adAssets": [  {  "videoUrl": "https://...x.png",  "pictureUrl": "null",  "order": 1,  "height": 1920,  "width": 1080,  "orientation": "LANDSCAPE"  }  ],  "appIconVariations": [],  "adLocaleVariations": []  }  ],  "dataStartDate": "2023-01-01",  "dataEndDate": "2023-04-01",  "pagination": {  "totalResults": 330,  "startIndex": 0,  "itemsPerPage": 15  }  }

## Response properties

\begin{tabular}{|p{113.8pt}|p{113.8pt}|p{113.8pt}|} \hline
**Parameter** & **Type** & **Description** \\ \hline adId & string & A unique ad identifier. Use adId as a resource in the ad variations call. \\ \hline appId & integer & The unique identifier of the app associated with an ad. \\ \hline appName & string & The name of the app associated with an ad. \\ \hline developerId & integer & The unique identifier of the developer identified on the App Store. \\ \hline developerName & string & The developer name refers to the developer as identified on the App Store which is the entity on whose behalf the subject advertising was presented. In some instances, the developerName may be different from the legalName field for the same entity. \\ \hline legalName & string & The legal name of the person or entity identified under the seller field on the App Store. In some instances, the legalName may be different from the developerName for the same entity. \\ \hline placement & string & The placement of the ad on the App Store. Values are APPSTORE_SEARCH_RESULTS, APPSTORE_TODAY_TAB, APPSTORE_SEARCH_TAB \\ \hline format & string & The format of the ad. Values are Icon Ad, Icon + Asset Ad. \\ \hline countryOrRegion & string & A country or region in the European Union in which Apple-delivered advertising is available on the App Store, expressed in ISO 3166-1 alpha-2 format. For example: ES, SE, DE. \\ \hline audienceRefinement & object & Audience refinement criteria used in an ad campaign. \\ \hline ageTarget & boolean & Indicates if age parameters are used in an ad campaign. \\ \hline genderTarget & boolean & Indicates if gender parameters are used in an ad campaign. \\ \hline locationTarget & boolean & Indicates if country or region parameters are used in an ad campaign. \\ \hline customerTypeTarget & boolean & Indicates app downloaded type. Values are: ALL_USERS NEW_USERS RETURNING_USERS USERS_OF_MY_OTHER_APPS \\ \hline \end{tabular}

[MISSING_PAGE_EMPTY:12]

[MISSING_PAGE_FAIL:13]

### Get ad variations

Use this endpoint to return ad variations by date range. Use the adId returned in the Get a list of ads call as a resource identifier in the URI.

GET [https://adrepository.apple.com/api/v1/ad-repository-ads/](https://adrepository.apple.com/api/v1/ad-repository-ads/){adId}? datePreset=LAST_90_DAYS

### Request parameters

[0.5cm] ParameterType Required Description adId string yes A unique resource ad identifier.

[0.5cm] The date range of the request. Values are LAST_90_DAYS, LAST_180_DAYS, LAST_YEAR. The default is LAST_90_DAYS.

### Response example

The AdRepositoryAd object is returned.

{  "data": {  "adId": "397563857",  "appld": 1582276305,  "apName": "TriPrek - travel app",  "developerId": 819221,  "developerName": "Apple Inc.",  "legalName": "Apple Inc.",  "placement": "APPSTORE_SEARCH_RESULTS",  "format": "Icon Ad",  "countryMregion": "Spain",  "audienceRefinement": {  "ageTarget": "true",  "genderTarget": "false",  "locationTarget": "true",  "customerTypeTarget": "false"  },  "firstImpressionDate": "2022-08-25",  "lastImpressionDate": "2023-04-01",  "defaultLanguageTag": "es-ES",  "defaultLanguageDisplayName": "Spanish (Spain)",  "defaultPreviewDevice": "iPhone_6.5",  "adBanner": {  "joeColor": "b:ff4c0@p0:04@4@4s:17lc01t:361303q:452501",  "iconPictureUr1": "https//...x_png/x.png",  "subtitle": "Plamiqique sus viajes con confinara.",  "primaryCategory": "viajar",  "inAppPurchases": "false",  "promotionalText": "Texto promocional que se muestra en la App Store.",  "editorialBadge": "false"  "shortDescription": "una descripcion de la aplicacion asociada con el anuncio."  },  "adAssets": [  {  "videoUrl": "https://...x_png/x.png",  "pictureUrl": "null",  "order": "l",  "height": "1920",  "width": "1080",  "orientation": "PORTRAIT"  },  "appIconVariations": [  "https://..._png/x.png, https://...\(x\).png/x.png"  ],  "adLocalevariations": [  {  "languageTag": "en-GB",  "languageDisplayName": "English (Great Britain)",  "appName": "TriPrek",  "subTitle": "Plan your trips with confidence.",  "primaryCategory": "travel",  "promotionalText": "App description shown on the App Store.",  "deviceAssets": [  {  "previewDevice": "iphone_6_5",  "adAssets": [{  "videoUr1": "https...png/x.png",  "pictureurl": "null",  "order": "1",  "height": "1920",  "width": "1080",  "orientation": "PORTRAIT"  }  }  }  }  }  }  }  }  } } ```

Ad Repository API

## Response properties

\begin{tabular}{|p{142.3pt}|p{142.3pt}|p{142.3pt}|} \hline
**Parameter** & **Type** & **Description** \\ \hline adId & string & A unique ad identifier. Use adId as a resource in the ad variations call. \\ \hline appId & integer & The unique identifier of the app associated with an ad. \\ \hline appName & string & The name of the app associated with an ad. \\ \hline developerId & integer & The unique identifier of the developer as identified on the App Store. \\ \hline  & & The developer name refers to the developer as identified on the App Store which is the entity on whose behalf the subject advertising was presented. In some instances, the developerName may be different from the legalName field for the same entity. \\ \hline legalName & string & The legal name of the person or entity identified under the seller field on the App Store. In some instances, the legalName may be different from the developerName for the same entity. \\ \hline placement & string & The placement of the ad on the App Store. Values are APPSTORE_SEARCH_RESULTS, APPSTORE_TODAY_TAB, APPSTORE_SEARCH_TAB \\ \hline format & string & The format of the ad. Values are Icon Ad, Icon + Asset Ad. \\ \hline countryOrRegion & string & A country or region in the European Union in which Apple-delivered advertising is available on the App Store, expressed in ISO 3166-1 alpha-2 format. For example: ES, SE, DE. \\ \hline audienceRefinement & object & Audience refinement criteria used in an ad campaign. \\ \hline ageTarget & boolean & Indicates if age parameters are used in an ad campaign. \\ \hline genderTarget & boolean & Indicates if gender parameters are used in an ad campaign. \\ \hline locationTarget & boolean & Indicates if country or region parameters are used in an ad campaign. \\ \hline customerTypeTarget & boolean & Indicates app downloader type. Values are: \\ \hline  & & ALL_USERS NEW_USERS RETRURNING_USERS USERS_OF_MY_OTHER_APPS \\ \hline firstImpressionDate & string & The first date of the first recorded delivered impression for the subject advertising. \\ \hline \end{tabular}

\begin{tabular}{|p{142.3pt}|p{142.3pt}|p{142.3pt}|} \hline  & & The last recorded delivered impression for the subject advertising. This date will also correspond to the last impression date for advertising that was restricted but not suspended, stopped, or removed. \\ \hline defaultLanguageTag & string & The locale code and default language used in the advertiser's App Store geoterritory. For example, es-ES. \\ \hline defaultLanguageDisplayN am & string & The default language used in the advertiser's App Store geoterritory. For example, “Spanish (Spain)”. \\ \hline defaultPreviewDevice & string & The default device model used in the advertiser's App Store geoterritory. For example, “iPhone_6.5”. \\ \hline adBanner & object & The ad's App Store metadata properties. \\ \hline joeColor & string & An encoded value that defines colors for text and background of the app as it appears on the App Store. \\ \hline iconPictureUrl & string & A resolved URL of the ad icon. \\ \hline subtitle & string & The subtitle of the app as it appears on the App Store. \\ \hline primaryCategory & string & The app category on the App Store. \\ \hline inAppurchases & boolean & Indicates if the app has in-app purchases enabled. \\ \hline promotionalText & string & The app description on the App Store. \\ \hline editorialBadge & boolean & The app's App Store metadata approval shown next to the app icon. \\ \hline shortDescription & string & If promotionalText is not present, a shortDescription matching the default product page is displayed. \\ \hline adAssets & object & A array of ad assets. \\ \hline videoUrl & string & The resolved URL for a video asset. \\ \hline pictureUrl & string & The resolved URL for the image asset. \\ \hline order & integer & The order of the ad asset that was uploaded to App Store Connect. \\ \hline height & integer & The height of the ad asset that was uploaded to App Store Connect. \\ \hline width & integer & The width of the ad asset that was uploaded to App Store Connect. \\ \hline orientation & string & The orientation of the ad asset that was uploaded to App Store Connect. Values are LANDSCAPE, PORTRAIT, UNKNOWN. \\ \hline \end{tabular}

[MISSING_PAGE_EMPTY:19]

## Get advertising-restrictions

Use this endpoint to return details of advertising-restrictions applied during a date range. Ads must have at least one advertising impression to be included in the response.

GET [https://adrepository.apple.com/api/v1/restrictions](https://adrepository.apple.com/api/v1/restrictions)

### Request example

Use ql= URL encoded RSQL filter to allow special characters.

GET -/api/v1/restrictions ?ql=  actionTaken==ACTION_ADVERTISING_REMOVED;  datePreset==LAST_90_DAYS  &offset=0  &limit=50

### Request parameters

\begin{tabular}{|l|c|c|c|} \hline \multicolumn{1}{|c|}{Parameter} & \multicolumn{1}{c|}{Type} & \multicolumn{1}{c|}{Required} & \multicolumn{1}{c|}{Description} \\ \hline \multirow{2}{*}{actionTaken} & \multirow{2}{*}{string} & \multirow{2}{*}{yes} & The action taken on the restriction, Values are: \\  & & & & ACTION_ACCOUNT_SUSPENDED \\  & & & ACTION_ADVERTISING_REMOVED \\ \hline \multirow{2}{*}{datePreset} & \multirow{2}{*}{string} & \multirow{2}{*}{no} & The date range of the request. Values are \\  & & & LAST_90_DAYS, LAST_180_DAYS, LAST_YEAR. The \\  & & & default is LAST_90_DAYS. \\ \hline \multirow{2}{*}{limit} & \multirow{2}{*}{integer} & \multirow{2}{*}{no} & The maximum number of entries to return per page. \\  & & & The default is 50. \\ \hline \multirow{2}{*}{offset} & \multirow{2}{*}{integer} & \multirow{2}{*}{no} & The offset negation that limits the number of \\  & & & returned records. The default is 0. \\ \hline \end{tabular}

### Response example

The restriction object is returned.

{  "data": [  {  "actionDate": "2022-08-26",  "actionTaken": "ACTION_ADVERITISING_REMOVED",  "reason": "REASON_TOS_INCOMPATABILITY",  "basis": "Government order.",  "details": "Incompatible with Terms and Conditions.",  "firstImpressionDate": "2022-08-25",  "affectedplacements": [  {  "placement": "APPSTORE_TODAY_TAB",  "countriesOrRegions": [  "BE",  "FR"  ]  }  ],  "audienceRefinement": {  "ageTarget": true,  "genderTarget": false,  "locationTarget": true,  "customerTypeTarget": false  }  }  ],  "dataStartDate": "2022-01-01",  "dataEndDate": "2022-09-01",  "pagination": {  "totalResults": 2,  "startIndex": 0,  "itemsPerPage": 50  }  }

### Response properties

\begin{tabular}{|p{142.3pt}|p{142.3pt}|p{142.3pt}|} \hline
**Parameter** & **Type** & **Description** \\ \hline actionDate & string & The date the restriction was enforced. \\ \hline actionTaken & string & The action taken on the restriction, Values are: \(\text{ACTION\_ACCount\_SUSPENDED}\) \(\text{ACTION\_ADVERTISING\_REMOVED}\) \\ \hline reason & string & The reason on the basis of which the advertising restriction was imposed. For example: \(\text{REASON\_GOVERNMENT\_ORDER}\) \(\text{REASON\_THIRD\_PARTY\_REPORT}\) \(\text{REASON\_POLICY\_RESTRICION\_AGE}\) \(\text{REASON\_POLICY\_RESTRICITION}\) \(\text{REASON\_TOS\_INCOMPATABILITY}\) \\ \hline basis & string & The basis of the restriction. For example, "Incompatible with Terms and Conditions". \\ \hline details & string & Details of the restriction. For example, "Removed due to governmental order". \\ \hline firstImpressionDate & string & The first date of the first recorded delivered impression for the subject advertising. \\ \hline affectedPlacements & object & Metadata of the ad restriction's App Store placement. \\ \hline placement & string & The placement of the ad on the App Store. Values are \(\text{APPSTORE\_SEARCH\_RESULTS}\), \(\text{APPSTORE\_TODAY\_TAB}\), \(\text{APPSTORE\_SEARCH\_TAB}\) \\ \hline countriesOrRegions & string & Countries or regions in the European Union in which Apple-delivered advertising is available on the App Store, expressed in ISO 3166-1 alpha-2 format. For example: ES, SE, DE. \\ \hline audienceRefinement & object & Audience refinement criteria used in an ad campaign. \\ \hline ageTarget & boolean & Indicates if age parameters are used in the ad campaign. \\ \hline genderTarget & boolean & Indicates if gender parameters are used in the ad campaign. \\ \hline locationTarget & boolean & Indicates if country or region parameters are used in the ad campaign. \\ \hline customerTypeTarget & boolean & Indicates app downloader type. Values are: \(\text{ALL\_USERS}\) \(\text{NEW\_USERS}\) \(\text{RETURNING\_USERS}\) \(\text{USERS\_OF\_MY\_OTHER\_APPS}\) \\ \hline dataStartDate & string & Returned data is delayed by 7 days. For example, if your datePreset is the \(\text{LAST\_90\_DAYS}\), the system will fetch matching ads by factoring today (UTC) as the dataEndDate minus 7 days. The dataStartDate is reported as the dataEndDate minus 90 days. \\ \hline \end{tabular}

[MISSING_PAGE_EMPTY:23]

[MISSING_PAGE_EMPTY:25]