Ad Repository API



November 2023



Version 1.0

Getting Started.................................................................................................................................................3



Versioning ....................................................................................................................................................3



Usability .......................................................................................................................................................3



Get a list of app and developer names.............................................................................................................4



Request example .........................................................................................................................................4



Request parameters ....................................................................................................................................4



Response example.......................................................................................................................................5



Response properties....................................................................................................................................6



Get a list of countries or regions ......................................................................................................................7



Response example.......................................................................................................................................7



Response properties....................................................................................................................................8



Get a list of ads ................................................................................................................................................9



Request example .........................................................................................................................................9



Request parameters ....................................................................................................................................9



Response example .....................................................................................................................................10



Response properties...................................................................................................................................11



Get ad variations ............................................................................................................................................14



Request parameters...................................................................................................................................14



Response example .....................................................................................................................................15



Response properties ..................................................................................................................................17



Get advertising-restrictions ...........................................................................................................................20



Request example .......................................................................................................................................20



Request parameters ..................................................................................................................................20



Response example .....................................................................................................................................21



Response properties..................................................................................................................................22



Changelog......................................................................................................................................................24



Ad Repository API November 2023 2



Contents

Getting Started

Use the Ad Repository API to look up Apple-delivered advertising on the App Store inselect European countries and regions as well as information about qualifyingadvertising restrictions. You can manage API calls programmatically using API tools andprograms of your choice.

Versioning

The current version of the API is v1 .

Usability

• Communication with the web service must use HTTPS.• RSQL query patterns are supported in some endpoints.• The API doesn’t accept headers with

 \*/\*. Disallow Accept \*/\* in your cURLcommands.• API responses will have a header

 Content-Type: application/json.



Ad Repository API November 2023 3

Get a list of app and developer names



GET https://adrepository.apple.com/api/v1/ad-repository-entities

Use this endpoint to return list of app and developer names based on custom query

parameter input. A developer name refers to the developer as identified on the App

Store, which is the entity on whose behalf the subject advertising was presented. Only

apps that have been advertised in countries or regions in the European Union in which

Apple-delivered advertising is available on the App Store are searchable.



Request example



GET ~/api/v1/ad-repository-entities?name={URL encoded search input text}

\&types==APP

\&offset=0

\&limit=10



Request parameters



Parameter Type Required Description



name string yes Custom query for app and developer names with a

minimum of 2 characters required.



types string no



Values are:



APP

DEVELOPER

APP,DEVELOPER (T he default value or blank which

returns all types.)



offset integer no The offset pagination that limits the number of returned

records. The default is 0.



limit integer no The maximum number of entries to return per page. The

default is 50.



Ad Repository API November 2023 4

Response example

The AdRepositoryEntity object is returned:



{

"data": [

{

"id": 1582276305,

"name": "TripTrek",

"type": "APP"

},

{

"id": 819221,

"name": "Trip Trek, Inc.",

"type": "DEVELOPER"

}

],

"pagination": {

"totalResults": 2,

"startIndex": 0,

"itemsPerPage": 15

}

}



Ad Repository API November 2023 5

Response properties



Parameter Type Description



id integer A unique identifier. If the type is APP , the id will be an appId . If

the type is DEVELOPER, the id is a developerId.



name string The entity name on whose behalf the advertising was presented.



type string Values are APP , DEVELOPER



pagination integer Returned pagination results.



totalResults: The total number of entries that return for the

operation.



startIndex: Specifies the position of the first element in the

results. The default is zero.



itemsPerPage: Specifies how many items is displayed per page.



Ad Repository API November 2023 6

Get a list of countries or regions

Use this endpoint to get a list of countries or regions in the European Union in which

Apple-delivered advertising is available on the App Store. Use the country codes

returned in the response in the Get a list of ads call.

Request example

GET https://adrepository.apple.com/api/v1/countries-or-regions



Response example



{

"data": [

{

"name": "Austria",

"code": "AT"

},

{

"name": "Belgium",

"code": "BE"

},

{

"name": "Croatia",

"code": "HR"

},

{

"name": "Czech Republic",

"code": "CZ"

},

{

"name": "Denmark",

"code": "DK"

},

{

"name": "Finland",

"code": "FI"

},

{

"name": "France",

"code": "FR"

},

{

"name": "Germany",

"code": "DE"

},

{

"name": "Greece",

"code": "GR"

},

{

"name": "Hungary",

"code": "HU"

},

{

"name": "Ireland",

"code": "IE"

},

{

"name": "Italy",



Ad Repository API November 2023 7

"code": "IT"

},

{

"name": "Netherlands",

"code": "NL"

},

{

"name": "Poland",

"code": "PL"

},

{

"name": "Portugal",

"code": "PT"

},

{

"name": "Romania",

"code": "RO"

},

{

"name": "Spain",

"code": "ES"

},

{

"name": "Sweden",

"code": "SE"

}

]

}



Response properties



Parameter Type Description



name string

The name of the country or region in the European Union in which

Apple-delivered advertising is available on the App Store. For

example: " Sweden".



code string

The ISO 3166-1 alpha-2 two-letter country code of the country or

region in the European Union in which Apple-delivered advertising

is available on the App Store. For example: ES, SE, DE.



Ad Repository API November 2023 8

Get a list of ads



Use this endpoint to return ad metadata and an adId to use in the Get Ad Variations call.



GET https://adrepository.apple.com/api/v1/ad-repository-ads



Request example

• Use ql= URL encoded RSQL filter to allow special characters.

• You can have both id or countryOrRegion or either in a request. If id is used

then type must also be present.

GET ~/api/v1/ad-repository-ads

?ql=

type==APP;

id==1582276305;

countryOrRegion=in=(FR,DE);

datePreset==LAST_90_DAYS;

\&offset=0

\&limit=50



Request parameters



Parameter Type Required Description



type string yes Values are APP , DEVELOPER.



id string yes

A unique identifier. If the type is APP , the id is an

appId . If the type is DEVELOPER, the id is a

developerId.



countryOrRegion string yes

A country or region in the European Union in

which Apple-delivered advertising is available on

the App Store, expressed in ISO 3166-1 alpha-2

format. For example: ES, SE, DE.



datePreset string no

The date range of the request. Values are

LAST_90_DAYS, LAST_180_DAYS, LAST_YEAR.

The default is LAST_90_DAYS.



limit integer no The maximum number of entries to return per

page. The default is 50.



offset integer no The offset pagination that limits the number of

returned records. The default is 0.



Ad Repository API November 2023 9

Response example

The AdRepositoryAd object is returned.



{

"data": [

{

"adId": "76324182",

"appId": 1582276305,

"appName": "TripTrek - travel app",

"developerId": 819221,

"developerName": "Apple Inc",

"legalName": "Apple Inc.",

"placement": "APPSTORE_SEARCH_RESULT",

"format": "Icon Ad",

"countryOrRegion": "ES",

"audienceRefinement": {

"ageTarget": "false",

"genderTarget": "false",

"locationTarget": "true",

"customerTypeTarget": "false"

},

"firstImpressionDate": "2022-08-25",

"lastImpressionDate": "2023-04-01",

"defaultLanguageTag": "es-ES",

"defaultLanguageDisplayName": "Spanish (Spain)",

"defaultPreviewDevice": "iPhone_6.5",

"adBanner": {

"iconPictureUrl": "",

"subtitle": "Planifique sus viajes con confianza.",

"primaryCategory": "viajar",

"inAppPurchases": "false",

"promotionalText": "Descripción de la aplicación mostrada en la App

Store.",

"editorialBadge": "false"

"shortDescription": "una descripción de la aplicación asociada con el

anuncio."

},

"adAssets": [

{

"videoUrl": "https://...x.png",

"pictureUrl": "null",

"order": 1,

"height": 1920,

"width": 1080,

"orientation": "LANDSCAPE"

}

],

"appIconVariations": [],

"adLocaleVariations": []

}

],

"dataStartDate": "2023-01-01",

"dataEndDate": "2023-04-01",

"pagination": {

"totalResults": 330,

"startIndex": 0,

"itemsPerPage": 15

}

}



Ad Repository API November 2023 10

Response properties



Parameter Type Description



adId string A unique ad identifier. Use adId as a resource in

the ad variations call.



appId integer The unique identifier of the app associated with

an ad.



appName string The name of the app associated with an ad.



developerId integer The unique identifier of the developer identified

on the App Store.



developerName string



The developer name refers to the developer as

identified on the App Store which is the entity on

whose behalf the subject advertising was

presented. In some instances, the

developerName may be different from the

legalName field for the same entity.



legalName string



The legal name of the person or entity identified

under the seller field on the App Store. In some

instances, the legalName may be different from

the developerName for the same entity.



placement string

The placement of the ad on the App Store.

Values are APPSTORE_SEARCH_RESULTS,

APPSTORE_TODAY_TAB, APPSTORE_SEARCH_TAB



format string The format of the ad. Values are Icon Ad, Icon

+ Asset Ad.



countryOrRegion string

A country or region in the European Union in

which Apple-delivered advertising is available on

the App Store, expressed in ISO 3166-1 alpha-2

format. For example: ES, SE, DE.



audienceRefinement object Audience refinement criteria used in an ad

campaign.



ageTarget boolean Indicates if age parameters are used in an ad

campaign.



genderTarget boolean Indicates if gender parameters are used in an ad

campaign.



locationTarget boolean Indicates if country or region parameters are

used in an ad campaign.



customerTypeTarget boolean



Indicates app downloader type. Values are:

ALL_USERS

NEW_USERS

RETURNING_USERS

USERS_OF_MY_OTHER_APPS



Ad Repository API November 2023 11

firstImpressionDate string The first date of the first recorded delivered

impression for the subject advertising.



lastImpressionDate string



The last recorded delivered impression for the

subject advertising. This date will also

correspond to the last impression date for

advertising that was restricted but not

suspended, stopped, or removed.



defaultLanguageTag string

The locale code and default language used in the

advertiser's App Store geoterritory. For example,

es-ES .



defaultLanguageDisplay

Name string

The default language used in the advertiser's

App Store geoterritory. For example, "Spanish

(Spain)".



defaultPreviewDevice string

The default device model used in the advertiser's

App Store geoterritory. For example,

"iPhone_6.5".



adBanner object The ad's App Store properties.



iconPictureUrl string A resolved URL of the ad icon.



subtitle string The subtitle of the app that appears on the App

Store.



primaryCategory string The app category on the App Store.



inAppPurchases boolean Indicates if the app has in-app purchases

enabled.



promotionalText string The app description on the App Store.



editorialBadge boolean The app's App Store metadata approval shown

alongside the app icon.



shortDescription string

If promotionalText is not present, a

shortDescription matching the default

product page is displayed.



adAssets object A array of ad assets.



videoUrl string The resolved URL for a video asset.



pictureUrl string The resolved URL for the image asset.



order integer The order of the ad asset that was uploaded to

App Store Connect.



height integer The height of the ad asset that was uploaded to

App Store Connect.



width integer The width of the ad asset that was uploaded to

App Store Connect.



orientation string

The orientation of the ad asset that was

uploaded to App Store Connect. Values are

LANDSCAPE, PORTRAIT, UNKNOWN.



Ad Repository API November 2023 12

appIconVariations object The URL of the app icon on the App Store.



adLocaleVariations object The language metadata of ad variations on the

App Store.



dataStartDate string



Returned data is delayed by 7 days. For example,

If your datePreset is the LAST_90_DAYS, the

system will fetch matching ads by factoring

today (UTC) as the dataEndDate minus 7 days.

The dataStartDate is reported as the

dataEndDate minus 90 days.



dataEndDate string



Returned data is delayed by 7 days. For example,

If your datePreset is the LAST_90_DAYS, the

system will fetch matching ads by factoring

today (UTC) as the dataEndDate minus 7 days.

The dataStartDate is reported as the

dataEndDate minus 90 days.



pagination integer



Returned pagination results.



totalResults: The total number of entries that

return for the operation.



startIndex: Specifies the position of the first

element in the results. The default is zero.



itemsPerPage: Specifies how many items is

displayed per page.



Ad Repository API November 2023 13

Get ad variations

Use this endpoint to return ad variations by date range. Use the adId returned in

the Get a list of ads call as a resource identifier in the URI.



GET https://adrepository.apple.com/api/v1/ad-repository-ads/{adId}?

datePreset=LAST_90_DAYS



Request parameters



Parameter Type Required Description



adId string yes A unique resource ad identifier.



datePreset string no

The date range of the request. Values are

LAST_90_DAYS, LAST_180_DAYS, LAST_YEAR.

The default is LAST_90_DAYS.



Ad Repository API November 2023 14

Response example

The AdRepositoryAd object is returned.



{

"data": {

"adId": "397563857",

"appId": 1582276305,

"appName": "TripTrek - travel app",

"developerId": 819221,

"developerName": "Apple Inc.",

"legalName": "Apple Inc.",

"placement": "APPSTORE_SEARCH_RESULTS",

"format": " Icon Ad",

"countryOrRegion": "Spain",

"audienceRefinement": {

"ageTarget": "true",

"genderTarget": "false",

"locationTarget": "true",

"customerTypeTarget": "false"

},

"firstImpressionDate": "2022-08-25",

"lastImpressionDate": "2023-04-01",

"defaultLanguageTag": "es-ES",

"defaultLanguageDisplayName": "Spanish (Spain)",

"defaultPreviewDevice": "iPhone_6.5",

"adBanner": {

"iconPictureUrl": "https://...x_.png/x.png",

"subtitle": "Planifique sus viajes con confianza.",

"primaryCategory": "viajar",

"inAppPurchases": "false",

"promotionalText": "Texto promocional que se muestra en la App Store.",

"editorialBadge": "false"

"shortDescription": "una descripción de la aplicación asociada con el

anuncio."

},

"adAssets": [

{

"videoUrl": "https://...x_.png/x.png",

"pictureUrl": "null",

"order": "1",

"height": "1920",

"width": "1080",

"orientation": "PORTRAIT"

}

],

"appIconVariations": [

"https://..._.png/x.png, https://..._x_.png/x.png"

],

"adLocaleVariations": [

{

"languageTag": "en-GB",

"languageDisplayName": "English (Great Britain)",

"appName": "TripTrek",

"subTitle": "Plan your trips with confidence.",

"primaryCategory": "travel",

"promotionalText": "App description shown on the App Store.",

"deviceAssets": [

{

"previewDevice": "iphone_6_5",

"adAssets": [

{



Ad Repository API November 2023 15

"videoUrl": "https..._.png/x.png",

"pictureUrl": "null",

"order": "1",

"height": "1920",

"width": "1080",

"orientation": "PORTRAIT"

}

]

}

]

}

]

}

}



Ad Repository API November 2023 16

Response properties



Parameter Type Description



adId string A unique ad identifier. Use adId as a resource in

the ad variations call.



appId integer The unique identifier of the app associated with

an ad.



appName string The name of the app associated with an ad.



developerId integer The unique identifier of the developer as

identified on the App Store.



developerName string



The developer name refers to the developer as

identified on the App Store which is the entity on

whose behalf the subject advertising was

presented. In some instances, the

developerName may be different from the

legalName field for the same entity.



legalName string

The legal name of the person or entity identified

under the seller field on the App Store. In some

instances, the legalName may be different from

the developerName for the same entity.



placement string

The placement of the ad on the App Store.

Values are APPSTORE_SEARCH_RESULTS,

APPSTORE_TODAY_TAB, APPSTORE_SEARCH_TAB



format string The format of the ad. Values are Icon Ad, Icon

+ Asset Ad.



countryOrRegion string

A country or region in the European Union in

which Apple-delivered advertising is available on

the App Store, expressed in ISO 3166-1 alpha-2

format. For example: ES, SE, DE.



audienceRefinement object Audience refinement criteria used in an ad

campaign.



ageTarget boolean Indicates if age parameters are used in an ad

campaign.



genderTarget boolean Indicates if gender parameters are used in an ad

campaign.



locationTarget boolean Indicates if country or region parameters are

used in an ad campaign.



customerTypeTarget boolean



Indicates app downloader type. Values are:

ALL_USERS

NEW_USERS

RETURNING_USERS

USERS_OF_MY_OTHER_APPS



firstImpressionDate string The first date of the first recorded delivered

impression for the subject advertising.



Ad Repository API November 2023 17

lastImpressionDate string



The last recorded delivered impression for the

subject advertising. This date will also

correspond to the last impression date for

advertising that was restricted but not

suspended, stopped, or removed.



defaultLanguageTag string

The locale code and default language used in the

advertiser's App Store geoterritory. For example,

es-ES .



defaultLanguageDisplayN

ame string

The default language used in the advertiser's

App Store geoterritory. For example, "Spanish

(Spain)".



defaultPreviewDevice string

The default device model used in the advertiser's

App Store geoterritory. For example,

"iPhone_6.5".



adBanner object The ad's App Store metadata properties.



iconPictureUrl string A resolved URL of the ad icon.



subtitle string The subtitle of the app that appears on the App

Store.



primaryCategory string The app category on the App Store.



inAppPurchases boolean Indicates if the app has in-app purchases

enabled.



promotionalText string The app description on the App Store.



editorialBadge boolean The app's App Store metadata approval shown

next to the app icon.



shortDescription string

If promotionalText is not present, a

shortDescription matching the default

product page is displayed.



adAssets object A array of ad assets.



videoUrl string The resolved URL for a video asset.



pictureUrl string The resolved URL for the image asset.



order integer The order of the ad asset that was uploaded to

App Store Connect.



height integer The height of the ad asset that was uploaded to

App Store Connect.



width integer The width of the ad asset that was uploaded to

App Store Connect.



orientation string

The orientation of the ad asset that was

uploaded to App Store Connect. Values are

LANDSCAPE, PORTRAIT, UNKNOWN.



appIconVariations object The URL of the app icon on the App Store.



Ad Repository API November 2023 18

adLocaleVariations object The language metadata of ad variations on the

App Store.



languageTag string

The locale code of the language used in the ad

variation on the advertiser's App Store

geoterritory. For example, es-ES.



languageDisplayName string

The language used in the ad variation on the

advertiser's App Store geoterritory. "Spanish

(Spain)"



appName string The name of the app associated with an ad.



subTitle string The subtitle of the app that appears on the App

Store.



primaryCategory string The app category on the App Store.



promotionalText string The app description on the App Store.



deviceAssets object The device properties used in an ad campaign.



previewDevice string The device displaying the ad.



adAssets string The resolved URL for an ad assset.



videoUrl string The resolved URL for a video asset.



pictureUrl string The resolved URL for the screenshot or a

screenshot of the image asset.



order integer The order of the ad asset that was uploaded to

App Store Connect.



height integer The height of the ad asset that was uploaded to

App Store Connect.



width integer The width of the ad asset that was uploaded to

App Store Connect.



orientation string

The orientation of the ad asset that was

uploaded to App Store Connect. Values are

LANDSCAPE, PORTRAIT, UNKNOWN



Ad Repository API November 2023 19

Get advertising-restrictions

Use this endpoint to return details of advertising-restrictions applied during a date

range. Ads must have at least one advertising impression to be included in the

response.



GET https://adrepository.apple.com/api/v1/restrictions



Request example

Use ql= URL encoded RSQL filter to allow special characters.



GET ~/api/v1/restrictions

?ql=

actionTaken==ACTION_ADVERTISING_REMOVED;

datePreset==LAST_90_DAYS

\&offset=0

\&limit=50



Request parameters



Parameter Type Required Description



actionTaken string yes

The action taken on the restriction, Values are:

ACTION_ACCOUNT_SUSPENDED

ACTION_ADVERTISING_REMOVED



datePreset string no

The date range of the request. Values are

LAST_90_DAYS, LAST_180_DAYS, LAST_YEAR . The

default is LAST_90_DAYS.



limit integer no The maximum number of entries to return per page.

The default is 50.



offset integer no The offset pagination that limits the number of

returned records. The default is 0.



Ad Repository API November 2023 20

Response example

The restriction object is returned.



{

"data": [

{

"actionDate": "2022-08-26",

"actionTaken": "ACTION_ADVERTISING_REMOVED",

"reason": "REASON_TOS_INCOMPATABILITY",

"basis": "Government order.",

"details": "Incompatible with Terms and Conditions.",

"firstImpressionDate": "2022-08-25",

"affectedPlacements": [

{

"placement": "APPSTORE_TODAY_TAB",

"countriesOrRegions": [

"BE",

"FR"

]

}

],

"audienceRefinement": {

"ageTarget": true,

"genderTarget": false,

"locationTarget": true,

"customerTypeTarget": false

}

}

],

"dataStartDate": "2022-01-01",

"dataEndDate": "2022-09-01",

"pagination": {

"totalResults": 2,

"startIndex": 0,

"itemsPerPage": 50

}

}



Ad Repository API November 2023 21

Response properties



Parameter Type Description



actionDate string The date the restriction was enforced.



actionTaken string

The action taken on the restriction, Values are:

ACTION_ACCOUNT_SUSPENDED

ACTION_ADVERTISING_REMOVED



reason string



The reason on the basis of which the advertising

restriction was imposed. For example:

REASON_GOVERNMENT_ORDER

REASON_THIRD_PARTY_REPORT

REASON_POLICY_RESTRICTION_AGE

REASON_POLICY_RESTRICTION

REASON_TOS_INCOMPATABILITY



basis string The basis of the restriction. For example,

"Incompatible with Terms and Conditions".



details string Details of the restriction. For example, "Removed due

to governmental order".



firstImpressionDate string The first date of the first recorded delivered impression

for the subject advertising.



affectedPlacements object Metadata of the ad restriction’s App Store placement.



placement string

The placement of the ad on the App Store. Values are

APPSTORE_SEARCH_RESULTS, APPSTORE_TODAY_TAB,

APPSTORE_SEARCH_TAB



countriesOrRegions string

Countries or regions in the European Union in which

Apple-delivered advertising is available on the App

Store, expressed in ISO 3166-1 alpha-2 format. For

example: ES, SE, DE.



audienceRefinement object

array

Audience refinement criteria used in an ad campaign.



ageTarget boolean Indicates if age parameters are used in the ad

campaign.



genderTarget boolean Indicates if gender parameters are used in the ad

campaign.



locationTarget boolean Indicates if country or region parameters are used in

the ad campaign.



customerTypeTarget boolean



Indicates app downloader type. Values are:

ALL_USERS

NEW_USERS

RETURNING_USERS

USERS_OF_MY_OTHER_APPS



dataStartDate string



Returned data is delayed by 7 days. For example, if

your datePreset is the LAST_90_DAYS, the system will

fetch matching ads by factoring today (UTC) as the

dataEndDate minus 7 days. The dataStartDate is

reported as the dataEndDate minus 90 days.



Ad Repository API November 2023 22

dataEndDate string



Returned data is delayed by 7 days. For example, If

your datePreset is the LAST_90_DAYS, the system will

fetch matching ads by factoring today (UTC) as the

dataEndDate minus 7 days. The dataStartDate is

reported as the dataEndDate minus 90 days.



pagination integer



Returned pagination results.



totalResults: The total number of entries that return

for the operation.



startIndex: Specifies the position of the first element

in the results. The default is zero.



itemsPerPage: Specifies how many items is displayed

per page.



Ad Repository API November 2023 23

Changelog



Date Notes



August, 2023 Initial version.



November, 2023 Added short description field. See Get a list of ads Response properties

and Get ad variations Response properties.



Ad Repository API November 2023 24

Apple Inc.

Copyright © 2023 Apple Inc.

All rights reserved.



No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, mechanical,

electronic, photocopying, recording, or otherwise, without prior written permission of Apple Inc., with the following exceptions: Any person

is hereby authorized to store documentation on a single computer or device for personal use only and to print copies of documentation for

personal use provided that the documentation contains Apple’s copyright notice. No licenses, express or implied, are granted with respect

to any of the technology described in this document. Apple retains all intellectual property rights associated with the technology

described in this document. This document is intended to assist publishers and partners with trafficking Advertising on Apple News.



Apple Inc.

Ad Platforms

One Apple Park Way

Cupertino, CA 95014, USA



APPLE MAKES NO WARRANTY OR REPRESENTATION, EITHER EXPRESS OR IMPLIED, WITH RESPECT TO THIS DOCUMENT, ITS

QUALITY, ACCURACY, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE. AS A RESULT, THIS DOCUMENT IS PROVIDED

“AS IS,” AND YOU, THE READER, ARE ASSUMING THE ENTIRE RISK AS TO ITS QUALITY AND ACCURACY. IN NO EVENT WILL APPLE BE

LIABLE FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES RESULTING FROM ANY DEFECT, ERROR OR

INACCURACY IN THIS DOCUMENT, even if advised of the possibility of such damages. Some jurisdictions do not allow the exclusion of

implied warranties or liability, so the above exclusion may not apply to you.



Ad Repository API November 2023 25