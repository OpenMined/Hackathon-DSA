
Post - Documentation - Meta for Developers












Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
Graph API Versionv19.0Page Post
=========

A Post that was published on a Facebook Page.


Reading
-------


 A Post that has been published or is scheduled to be published on a Facebook Page.
 ### Permissions

The `source` field will not be returned for Page-owned videos unless the User making the request is an admin of the owning Page.

### Limitations

* If a Post has expired, you will no longer be able to view the content using the Graph API.
* This endpoint does not return Reels. To get a list of Reels published to your Page, use the Page VideoReels edge.
### New Page Experience

This endpoint is supported for New Page Experience.### Feature Permissions



| Name | Description |
| --- | --- |
| Page Public Content Access | This feature permission may be required. |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURLGraph API Explorer
```
GET /v19.0/{page-id}_{post-id}/ HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{page-id}_{post-id}/',
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```

```
/* make the API call */
FB.api(
    "/{page-id}_{post-id}/",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{page-id}_{post-id}/",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{page-id}_{post-id}/"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

```
curl -X GET -G \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/{page-id}_{post-id}/
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

This endpoint doesn't have any parameters.### Fields



| Field | Description |
| --- | --- |
| `id`token with structure: Post ID | The post ID
 |
| `actions`list | Action links
 |
| `admin_creator`BusinessUser|User|Application | The admin creator of a Page Post. Only available if there exists more than one admin for the page.
 |
| `allowed_advertising_objectives`list<string> | Objectives under which this post can be advertised
 |
| `application`Application | Information about the app this post was published by.
 |
| `backdated_time`datetime | The backdated time for backdate post. For regular post, this field will be set to null.
 |
| `call_to_action`struct with keys: type, value | The call to action type used in any Page posts for mobile app engagement ads.
 |
| `can_reply_privately`bool | Whether the page viewer can send a private reply to this post
 |
| `child_attachments`list | Sub-shares of a multi-link share post
 |
| `comments_mirroring_domain`string | If comments are being mirrored to an external site, this function returns the domain of that external site.
 |
| `coordinates`struct with keys: checkin\_id, author\_uid, page\_id, target\_id, target\_href, coords, tagged\_uids, timestamp, message, target\_type | An array of information about the attachment to the post
 |
| `created_time`datetime | The time the post was published, expressed as UNIX timestamp
Default |
| `event`Event | If this Post has a place, the event associated with the place
 |
| `expanded_height`unsigned int32 | An array of information about the attachment to the post
 |
| `expanded_width`unsigned int32 | An array of information about the attachment to the post
 |
| `feed_targeting`struct with keys: country, cities, regions, genders, age\_min, age\_max, education\_statuses, college\_years, relationship\_statuses, interests, interested\_in, user\_adclusters, locales, countries, geo\_locations, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, industries, politics, ethnic\_affinity, generation, fan\_of, relevant\_until\_ts | Object that controls Feed targeting for this post. Anyone in these groups will be more likely to see this post, others will be less likely, but may still see it anyway. Any of the targeting fields shown here can be used, none are required (applies to Pages only).
 |
| `from`User|Page | The ID of the user, page, group, or event that published the post
 |
| `full_picture`string | Full size picture from attachment
 |
| `height`unsigned int32 | An array of information about the attachment to the post
 |
| `icon`string | A link to an icon representing the type of this post.
 |
| `is_app_share`bool | Whether or not the post references an app
 |
| `is_eligible_for_promotion`bool | Whether the post is eligible for promotion.
 |
| `is_expired`bool | Whether the post has expiration time that has passed
 |
| `is_hidden`bool | Whether a post has been set to hidden
 |
| `is_inline_created`bool | Returns True if the post was created inline when creating ads.
 |
| `is_popular`bool | Whether the post is currently popular. Based on whether the total actions as a percentage of reach exceeds a certain threshold
 |
| `is_published`bool | Indicates whether a scheduled post was published (applies to scheduled Page Post only, for users post and instanlty published posts this value is always true)
 |
| `is_spherical`bool | Whether the post is a spherical video post
 |
| `message`string | The message written in the post
Default |
| `message_tags`list | Profiles tagged in message. This is an object with a unique key for each tag in the message
 |
| `multi_share_end_card`bool | Whether display the end card for a multi-link share post
 |
| `multi_share_optimized`bool | Whether automatically select the order of the links in multi-link share post when used in an ad
 |
| `parent_id`token with structure: Post ID | The ID of a parent post for this post, if it exists. For example, if this story is a 'Your Page was mentioned in a post' story, the parent\_id will be the original post where the mention happened
 |
| `permalink_url`uri | The permanent static URL to the post on www.facebook.com. Example: https://www.facebook.com/FacebookforDevelopers/posts/10153449196353553
 |
| `place`Place | ID of the place associated with the post
 |
| `privacy`Privacy | The privacy settings for a post
 |
| `promotable_id`token with structure: Post ID | ID of post to use for promotion for stories that cannot be promoted directly
 |
| `properties`list | A list of properties for any attached video, for example, the length of the video.
 |
| `scheduled_publish_time`float | UNIX timestamp of the scheduled publish time for the post
 |
| `shares`struct with keys: count | Number of times the post has been shared
 |
| `status_type`string | Description of the type of a status update.
 |
| `story`string | Text of stories not intentionally generated by users, such as those generated when two users become friends. You must have the "Include recent activity stories" migration enabled in your app to retrieve this field
Default |
| `story_tags`list | The list of tags in the post description
 |
| `subscribed`bool | Whether user is subscribed to the post
 |
| `target`Profile | The profile this was posted on if different from the author
 |
| `targeting`struct with keys: country, cities, regions, zips, genders, college\_networks, work\_networks, age\_min, age\_max, education\_statuses, college\_years, college\_majors, political\_views, relationship\_statuses, interests, keywords, interested\_in, user\_clusters, user\_clusters2, user\_clusters3, user\_adclusters, excluded\_user\_adclusters, custom\_audiences, excluded\_custom\_audiences, locales, radius, connections, excluded\_connections, friends\_of\_connections, countries, excluded\_user\_clusters, adgroup\_id, user\_event, qrt\_versions, page\_types, user\_os, user\_device, action\_spec, action\_spec\_friend, action\_spec\_excluded, geo\_locations, excluded\_geo\_locations, targeted\_entities, conjunctive\_user\_adclusters, wireless\_carrier, site\_category, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, behaviors, travel\_status, industries, politics, markets, income, net\_worth, home\_type, home\_ownership, home\_value, ethnic\_affinity, generation, household\_composition, moms, office\_type, interest\_clusters\_expansion, dynamic\_audience\_ids, product\_audience\_specs, excluded\_product\_audience\_specs, exclusions, flexible\_spec, engagement\_specs, excluded\_engagement\_specs | Object that limited the audience for this content. Anyone not in these demographics will not be able to view this content. This will not override any Page-level demographic restrictions that may be in place.
 |
| `timeline_visibility`string | Timeline visibility information of the post
 |
| `updated_time`datetime | The time the post was last updated, which occurs when a user comments on the post.
 |
| `via`User|Page | ID of the user or Page the post was shared from
 |
| `width`unsigned int32 | An array of information about the attachment to the post
 |

### Edges



| Edge | Description |
| --- | --- |
| `attachments` | Any attachments that are associated with the story
 |
| `comments` | Comments made on this
 |
| `dynamic_posts` | All dynamic ad creatives
 |
| `insights` | Insights for this post (only for Pages).
 |
| `likes` | People who like this
 |
| `reactions` | People who reacted on this
 |
| `sharedposts` | Shared posts
 |
| `sponsor_tags` | An array sponsor pages tagged in the post
 |
| `to` | Profiles mentioned or targeted in this post.
 |

### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 190 | Invalid OAuth 2.0 Access Token |
| 210 | User not visible |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 459 | The session is invalid because the user has been checkpointed |
| 3001 | Invalid query |
| 2500 | Error parsing graph query |

Creating
--------

You can't perform this operation on this endpoint.Updating
--------

You can update a PagePost by making a POST request to `/{page_post_id}`.### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURLGraph API Explorer
```
POST /v19.0/{page-id}_{post-id}/ HTTP/1.1
Host: graph.facebook.com

message=This+is+a+test+value
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{page-id}_{post-id}/',
    array (
      'message' => 'This is a test value',
    ),
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```

```
/* make the API call */
FB.api(
    "/{page-id}_{post-id}/",
    "POST",
    {
        "message": "This is a test value"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
Bundle params = new Bundle();
params.putString("message", "This is a test value");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{page-id}_{post-id}/",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
NSDictionary *params = @{
  @"message": @"This is a test value",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{page-id}_{post-id}/"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

```
curl -X POST \
  -F 'message="This is a test value"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/{page-id}_{post-id}/
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters



| Parameter | Description |
| --- | --- |
| `attached_media`list<Object> | attached\_media
 |
| `media_fbid`numeric string |  |
| `message`UTF-8 string | Supports Emoji |
| `backdated_time`datetime | SELF\_EXPLANATORY
 |
| `backdated_time_granularity`enum{year, month, day, hour, min, none} | Default value: `none`SELF\_EXPLANATORY
 |
| `composer_session_id`string | composer\_session\_id
 |
| `direct_share_status`int64 | The status to allow sponsor directly boost the post.
 |
| `explicitly_added_mentionee_ids`list<int64> | List of IDs that were explicitly mentioned by the user (i.e. typed) rather than auto-populated by the product.
 |
| `feed_story_visibility`enum{hidden, visible} | SELF\_EXPLANATORY
 |
| `is_approved`boolean | SELF\_EXPLANATORY
 |
| `is_explicit_location`boolean | is\_explicit\_location
 |
| `is_hidden`boolean | SELF\_EXPLANATORY
 |
| `is_pinned`boolean | SELF\_EXPLANATORY
 |
| `message`UTF-8 string | SELF\_EXPLANATORY
Supports Emoji |
| `og_action_type_id`numeric string or integer | SELF\_EXPLANATORY
 |
| `og_hide_object_attachment`boolean | SELF\_EXPLANATORY
 |
| `og_icon_id`numeric string or integer | SELF\_EXPLANATORY
 |
| `og_object_id`OG object ID or URL string | SELF\_EXPLANATORY
 |
| `og_phrase`string | SELF\_EXPLANATORY
 |
| `og_set_profile_badge`boolean | og\_set\_profile\_badge
 |
| `og_suggestion_mechanism`string | SELF\_EXPLANATORY
 |
| `place`place tag | SELF\_EXPLANATORY
 |
| `privacy`Privacy Parameter | SELF\_EXPLANATORY
 |
| `product_item`Object | SELF\_EXPLANATORY
Supports Emoji |
| `title`string | Supports Emoji |
| `price`float |  |
| `currency`string | Default value: `USD` |
| `retail_price`float |  |
| `shipping_price`float |  |
| `condition`string | Default value: `used` |
| `description`string | Default value: Supports Emoji |
| `pickup_delivery_info`string | Default value:  |
| `location_page_id`string | Default value:  |
| `price_type`string | Default value: `fixed` |
| `multiple_item_type`string | Default value: `SINGLE_ITEM` |
| `category_id`numeric string or integer |  |
| `category_source`enum {TEXT, IMAGE, IMAGE\_TEXT, IMAGE\_TEXT\_DOCNN, PAGE\_ID, TITLE\_REGEX, CLASSIFY\_RULE, CATALOG\_BERT\_CLASSIFY\_RULE, HUMAN\_VERIFIED, SELLER\_SELECTED, USE\_EXISTING\_PRODUCT, COMPOSER, HUMAN\_MAPPING, PARTNER\_INGESTION, MERCHANT\_GOOGLE\_CATEGORY, BUSINESS\_DIRECT, MEGA\_TAXON, SHOPS, MOTORS\_ATTRIBUTES\_C2C, CATALOG\_BERT, CATALOG\_BERT\_ONLINE, ATTR\_GENDER\_F249720567, JOBS\_TITLE\_TAXONOMY\_MAPPING, CATALOG\_BERT\_FULL\_FPT, CATALOG\_BERT\_I18N, CATALOG\_MMF\_FULL\_FPT, SCALE\_AI, CATALOG\_MMF\_FULL\_FPT\_WITH\_OVERRIDE} |  |
| `predict_category_id`numeric string or integer |  |
| `predict_leaf_category_id`numeric string or integer |  |
| `sherlock_image_model_signature`string | Default value:  |
| `sherlock_model_id`integer | Default value: `0` |
| `sherlock_used_category_feature`enum {FAILED, TEXT\_ONLY, IMAGE\_ONLY, IMAGE\_TEXT, USE\_EXISTING\_PRODUCT} |  |
| `latitude`float |  |
| `longitude`float |  |
| `quantity`int64 |  |
| `serialized_verticals_data`string | Default value:  |
| `commerce_verticals_data`Object |  |
| `autos_make`string |  |
| `autos_model`string |  |
| `autos_year`string |  |
| `autos_odometer`string |  |
| `autos_odometer_units`string | Default value:  |
| `autos_vin`string |  |
| `draft_type`enum {COMMERCE\_SELL\_OPTIONS, FOR\_SALE\_AUTO} |  |
| `is_preview`boolean | Default value: `false` |
| `status_type`enum {COMMERCE\_SELL\_OPTIONS, DRAFT} | Default value: `commerce_sell_options` |
| `original_commerce_item_id`numeric string or integer |  |
| `original_for_sale_item_id`numeric string or integer |  |
| `original_post_id`numeric string or integer |  |
| `original_product_item_id`numeric string or integer |  |
| `collection_id`numeric string or integer |  |
| `graphapi_has_photo_hint_for_loki`boolean | Default value: `false` |
| `shipping_offered`boolean | Default value: `false` |
| `delivery_type`enum {IN\_PERSON, DROP\_OFF} | Default value: `in_person` |
| `delivery_types`list<enum {IN\_PERSON, DROP\_OFF, SHIPPING\_ONSITE, SHIPPING\_OFFSITE, LOCAL\_DELIVERY, IN\_PERSON\_HOLDS, LOW\_CONTACT\_EXCHANGE, DOOR\_PICKUP, DOOR\_DROPOFF, PUBLIC\_MEETUP}> |  |
| `shipping_services`list<enum {USPS\_PRIORITY, USPS\_PRIORITY\_EXPRESS, USPS\_FIRST, USPS\_PARCEL\_SELECT}> |  |
| `parcel_type`enum {USPS\_LT\_HALF\_LBS, USPS\_LT\_THREE\_LBS, USPS\_LT\_TEN\_LBS, USPS\_LT\_TWENTY\_LBS, OVERWEIGHT} |  |
| `seller_address_id`numeric string or integer |  |
| `seller_email`string | Default value:  |
| `attribute_data`JSON object |  |
| `brand`string | Default value:  |
| `color`string | Default value:  |
| `size`string | Default value:  |
| `material`string | Default value:  |
| `condition`string | Default value:  |
| `carrier`string | Default value:  |
| `internal_memory`string | Default value:  |
| `device_name`string | Default value:  |
| `platform`string | Default value:  |
| `decor_style`string | Default value:  |
| `attribute_data_freeform`dictionary { numeric string or integer : <string> } |  |
| `attribute_data_normalized`dictionary { numeric string or integer : <list<numeric string or integer>> } |  |
| `variants`list<JSON object> |  |
| `id`numeric string or integer |  |
| `index`int64 |  |
| `photo_ids`list<numeric string or integer> |  |
| `product_image_ids`list<numeric string or integer> |  |
| `price`float | Required |
| `description`string |  |
| `quantity`int64 | Required |
| `additional_variant_attributes`list<JSON object> | Required |
| `variant_label`string | Default value:  |
| `variant_value`string | Default value:  |
| `commerce_shipping_delivery_type`enum {SHIPPING, LOCAL\_DELIVERY, LOCKER} |  |
| `shipping_option_type`enum {PREPAID\_LABEL, OWN\_LABEL, LOCAL\_DELIVERY} |  |
| `shipping_options_data`list<JSON object> |  |
| `shipping_price`JSON object |  |
| `currency`string | Default value: `USD` |
| `price`float | Required |
| `shipping_label_price`JSON object |  |
| `currency`string | Default value: `USD` |
| `price`float | Required |
| `shipping_label_rate_code`string |  |
| `shipping_cost_option`string |  |
| `commerce_shipping_carrier`enum {AUSTRALIA\_POST, CANADA\_POST, CDL\_LASTMILE, DELIVER\_IT, DHL, DHL\_ECOMMERCE\_US, EAGLE, FEDEX, FEDEX\_UK, NEW\_ZEALAND\_POST, ONTRAC, POST\_DANMARK, PUROLATOR, ROYAL\_MAIL, SPEE\_DEE, TFORCE\_FINALMILE, TNT, TNT\_POST, UPS, USPS, DOORDASH, DOORDASH\_ARCHIVED, DPD\_FRANCE, LA\_POSTE, COLISSIMO, CHRONOPOST\_FRANCE, TNT\_FRANCE, COLIS\_PRIVE, GEODIS\_DISTRIBUTION\_EXPRESS, BERT\_TRANSPORT, GEODIS\_E\_SPACE, MONDIAL\_RELAY, TELIWAY\_SIC\_EXPRESS, AMAZON, APC\_OVERNIGHT, ARROW\_XL, ASENDIA\_UK, BIRDSYSTEM, BLUECARE\_EXPRESS\_LTD, COLLECT\_PLUS, DELTEC\_COURIER, DPD\_LOCAL, DPD\_LOCAL\_REFERENCE, DPD\_UK, HERMESWORLD, IMX\_MAIL, JERSEY\_POST, MYHERMES\_UK, NATIONAL\_SAMEDAY, NORSK\_GLOBAL, PANTHER, PANTHER\_ORDER\_NUMBER, PANTHER\_REFERENCE, PARCEL\_FORCE, RPD2MAN\_DELIVERIES, TNT\_UK, TNT\_UK\_REFERENCE, TUFFNELLS\_PARCELS\_EXPRESS, UK\_MAIL, WHISTL, WNDIRECT, XDP\_EXPRESS, XDP\_EXPRESS\_REFERENCE, YODEL\_DOMESTIC, YODEL\_INTERNATIONAL, AMAZON\_LOGISTICS, AO\_LOGISTICS, APC\_OVERNIGHT\_CONSIGNMENT\_NUMBER, AQUILINE, BANDH\_WORLDWIDE, CAE\_DELIVERS, DHL\_PARCEL\_UK, DMSMATRIX, EU\_FLEET\_SOLUTIONS, GBA\_SERVICES\_LTD, GEMWORLDWIDE, KNAIRLINK\_AEROSPACE\_DOMESTIC\_NETWORK, OCS\_WORLDWIDE, PARCEL2GO, SKYNET\_WORLDWIDE\_EXPRESS\_UK, TUFFNELLS\_PARCELS\_EXPRESS\_REFERENCE, XPERT\_DELIVERY, MAINWAY, INTERPARCEL\_UK, OTHER, ABF\_FREIGHT, ABX\_EXPRESS, AB\_CUSTOM\_GROUP, ACOMMERCE, ACS\_COURIER, ACS\_WORLDWIDE\_EXPRESS, ADICIONAL\_LOGISTICS, ADSONE, AIR21, AIRPAK\_EXPRESS, AIRSPEED\_INTERNATIONAL\_CORPORATION, ALFATREX, ALLIED\_EXPRESS, ALLJOY\_SUPPLY\_CHAIN\_CO\_LTD, ALPHAFAST, AMAZON\_FBA\_USA, AN\_POST, APC\_OVERNIGHT\_REFERENCE, APC\_POSTAL\_LOGISTICS, APRISA\_EXPRESS, ARAMEX, ASENDIA\_GERMANY, ASENDIA\_HK, ASENDIA\_HK\_PREMIUM\_SERVICE\_LATAM, ASENDIA\_USA, ASM, AUPOST\_CHINA, AUSTRALIA\_POST\_SFTP, AUSTRIAN\_POST\_EXPRESS, AUSTRIAN\_POST\_REGISTERED, AUPOST, DHLAU, AXLEHIRE, AXL\_EXPRESS\_LOGISTICS, A\_DUIE\_PYLE, A\_J\_EXPRESS, B2C\_EUROPE, BELPOST, BEST\_EXPRESS, BEST\_WAY\_PARCEL, BETTER\_TRUCKS, BJS\_DISTRIBUTION\_STORAGE\_COURIERS, BJS\_DISTRIBUTION\_STORAGE\_COURIERS\_FTP, BLUEDART, BLUE\_STAR, BNEED, BONDS\_COURIERS, BOXC, BPOST, BPOST\_INTERNATIONAL, BRAZIL\_CORREIOS, BRT\_BARTOLINI, BRT\_BARTOLINI\_PARCEL\_ID, BULGARIAN\_POSTS, BUYLOGIC, CAINIAO, CAMBODIA\_POST, CANPAR\_COURIER, CAPITAL\_TRANSPORT, CARRIER\_007EX, CARRIER\_17\_POST\_SERVICE, CARRIER\_2GO, CARRIER\_360\_LION\_EXPRESS, CARRIER\_4PX, CARRIER\_4\_72\_ENTREGANDO, CARRIER\_ECHO, CBL\_LOGISTICS, CELERITAS\_TRANSPORTE\_SL, CESKA\_POSTA, CHINA\_EMS\_EPACKET, CHINA\_POST, CHIT\_CHATS, CHRONOPOST\_PORTUGAL, CH\_ROBINSON\_WORLDWIDE\_INC, CITY\_LINK\_EXPRESS, CJ\_CENTURY, CJ\_CENTURY\_INTERNATIONAL, CJ\_GLS, CJ\_KOREA\_EXPRESS, CJ\_LOGISTICS\_INTERNATIONAL, CJ\_TRANSNATIONAL\_PHILIPPINES, CLEVY\_LINKS, CLOUDWISH\_ASIA, CNE\_EXPRESS, COLLECTCO, CON\_WAY\_FREIGHT, COPA\_AIRLINES\_COURIER, CORREOS\_CHILE, CORREOS\_DE\_COSTA\_RICA, CORREOS\_DE\_ESPANA, CORREOS\_DE\_MEXICO, CORREOS\_EXPRESS, CORREO\_ARGENTINO, COSMETICS\_NOW, COUREX, COURIERPOST, COURIERS\_PLEASE, COURIER\_IT, COURIER\_PLUS, CPACKET, CUCKOO\_EXPRESS, CYPRUS\_POST, DACHSER, DAWN\_WING, DAYLIGHT\_TRANSPORT\_LLC, DB\_SCHENKER, DB\_SCHENKER\_SWEDEN, DD\_EXPRESS\_COURIER, DELCART, DELHIVERY, DELIVERYONTIME\_LOGISTICS\_PVT\_LTD, DEMANDSHIP, DETRACK, DEUTSCHE\_POST\_DHL, DEUTSCHE\_POST\_MAIL, DEX\_I, DHL\_2\_MANN\_HANDLING, DHL\_ACTIVE\_TRACING, DHL\_BENELUX, DHL\_ECOMMERCE\_ASIA, DHL\_EXPRESS\_PIECE\_ID, DHL\_GLOBAL\_FORWARDING, DHL\_HONG\_KONG, DHL\_NETHERLANDS, DHL\_PARCEL\_NL, DHL\_PARCEL\_SPAIN, DHL\_POLAND\_DOMESTIC, DHL\_SPAIN\_DOMESTIC, DIMERCO\_EXPRESS\_GROUP, DIRECTLOG, DIRECT\_FREIGHT\_EXPRESS, DIRECT\_LINK, DMM\_NETWORK, DOORA\_LOGISTICS, DOTZOT, DPD, DPD\_GERMANY, DPD\_HK, DPD\_IRELAND, DPD\_POLAND, DPD\_ROMANIA, DPD\_RUSSIA, DPEX, DPEX\_CHINA, DPE\_EXPRESS, DPE\_SOUTH\_AFRICA, DSV, DTDC\_AUSTRALIA, DTDC\_EXPRESS\_GLOBAL\_PTE\_LTD, DTDC\_INDIA, DX, DX\_FREIGHT, DYNALOGIC\_BENELUX\_BV, DYNAMIC\_LOGISTICS, EASY\_MAIL, ECARGO, ECMS\_INTERNATIONAL\_LOGISTICS\_CO\_LTD, ECOM\_EXPRESS, EC\_FIRSTCLASS, EFS\_E\_COMMERCE\_FULFILLMENT\_SERVICE, EKART, ELTA\_HELLENIC\_POST, EMIRATES\_POST, EMPS\_EXPRESS, ENSENDA, ENVIALIA, EPARCEL\_KOREA, EP\_BOX, EQUICK\_CHINA, ESTAFETA, ESTES, ETOTAL\_SOLUTION\_LIMITED, EURODIS, EXPEDITORS, EZSHIP, FASTRAK\_SERVICES, FASTWAY\_AUSTRALIA, FASTWAY\_IRELAND, FASTWAY\_NEW\_ZEALAND, FASTWAY\_SOUTH\_AFRICA, FEDEX\_CROSS\_BORDER, FEDEX\_FREIGHT, FEDEX\_POLAND\_DOMESTIC, FERCAM\_LOGISTICS\_TRANSPORT, FIRST\_FLIGHT\_COURIERS, FIRST\_LOGISTICS, FLYT\_EXPRESS, GATI\_KWE, GDEX, GENIKI\_TAXYDROMIKI, GIAO\_HANG\_NHANH, GLOBEGISTICS\_INC, GLS, GLS\_CZECH\_REPUBLIC, GLS\_ITALY, GLS\_NETHERLANDS, GOFLY, GOJAVAS, GREYHOUND, GSI\_EXPRESS, HERMES\_GERMANY, HERMES\_ITALY, HOLISOL, HOMEDIRECT\_LOGISTICS, HONG\_KONG\_POST, HRVATSKA\_POSTA, HUA\_HAN\_LOGISTICS, HUNTER\_EXPRESS, ICELAND\_POST, IDEX, IMEX\_GLOBAL\_SOLUTIONS, INDIA\_POST\_DOMESTIC, INDIA\_POST\_INTERNATIONAL, INPOST\_PACZKOMATY, INSTANT\_TIONG\_NAM\_EBIZ\_EXPRESS\_SDN\_BHD, INTERNATIONAL\_SEUR, INTERNET\_EXPRESS, ISRAEL\_POST, ISRAEL\_POST\_DOMESTIC, ITALY\_SDA, I\_PARCEL, J\_T\_EXPRESS, JAM\_EXPRESS, JANCO\_ECOMMERCE, JAPAN\_POST, JAYON\_EXPRESS\_JEX, JCEX, JET\_SHIP\_WORLDWIDE, JINSUNG\_TRADING, JNE, JOCOM, JP\_BH\_POSTA, JX, J\_NET, K1\_EXPRESS, KANGAROO\_WORLDWIDE\_EXPRESS, KERRY\_EXPRESS\_HONG\_KONG, KERRY\_EXPRESS\_THAILAND, KERRY\_EXPRESS\_VIETNAM\_CO\_LTD, KGM\_HUB, KIALA, KOREA\_POST, KOREA\_POST\_EMS, KRONOS\_EXPRESS, KUEHNE\_NAGEL, LANDMARK\_GLOBAL, LAO\_POST, LASERSHIP, LBC\_EXPRESS, LHT\_EXPRESS, LIETUVOS\_PASTAS, LINE\_CLEAR\_EXPRESS\_LOGISTICS\_SDN\_BHD, LINK\_BRIDGE\_BEIJING\_INTERNATIONAL\_LOGISTICS\_COLTD, LION\_PARCEL, LOGISTIC\_WORLDWIDE\_EXPRESS, LOGWIN\_LOGISTICS, LONE\_STAR\_OVERNIGHT, MAGYAR\_POSTA, MAILAMERICAS, MAILPLUS, MAINFREIGHT, MALAYSIA\_POST\_EMS\_POS\_LAJU, MALAYSIA\_POST\_REGISTERED, MARA\_XPRESS, MATDESPATCH, MATKAHUOLTO, MDS\_COLLIVERY\_PTY\_LTD, MEGASAVE, MEXICO\_AEROFLASH, MEXICO\_REDPACK, MEXICO\_SENDA\_EXPRESS, MIKROPAKKET, MRW, MUDITA, MXE\_EXPRESS, MYPOSTONLINE, M\_XPRESS\_SDN\_BHD, NACEX\_SPAIN, NANJING\_WOYUAN, NATIONWIDE\_EXPRESS, NEWGISTICS, NEWGISTICS\_API, NEXIVE\_TNT\_POST\_ITALY, NHANS\_SOLUTIONS, NIGHTLINE, NIM\_EXPRESS, NINJA\_VAN, NINJA\_VAN\_INDONESIA, NINJA\_VAN\_MALAYSIA, NINJA\_VAN\_PHILIPPINES, NINJA\_VAN\_THAILAND, NIPOST, NOVA\_POSHTA, NOVA\_POSHTA\_INTERNATIONAL, OCA\_ARGENTINA, OLD\_DOMINION\_FREIGHT\_LINE, OMNIVA, OMNI\_PARCEL, ONE\_WORLD\_EXPRESS, PACKLINK, PAL\_EXPRESS\_LIMITED, PANDU\_LOGISTICS, PAQUETEXPRESS, PARCELLEDIN, PARCELPOINT\_PTY\_LTD, PARCEL\_POST\_SINGAPORE, PAYPAL\_PACKAGE, PFC\_EXPRESS, PICKUPP, PICK\_UPP\_MYS\_SGP, PILOT\_FREIGHT\_SERVICES, PITNEY\_BOWES, PIXSELL\_LOGISTICS, POCZTA\_POLSKA, PORTUGAL\_CTT, PORTUGAL\_SEUR, POST56, POSTEN\_NORGE\_BRING, POSTE\_ITALIANE, POSTE\_ITALIANE\_PACCOCELERE, POSTI, POSTNL\_DOMESTIC, POSTNL\_INTERNATIONAL, POSTNL\_INTERNATIONAL\_3S, POSTNORD\_DENMARK, POSTNORD\_LOGISTICS, POSTNORD\_SWEDEN, POST\_OF\_SLOVENIA, POST\_SERBIA, POS\_INDONESIA\_DOMESTIC, POS\_INDONESIA\_INTL, POSTA\_ROMANA, PROFESSIONAL\_COURIERS, PTT\_POSTA, QUALITYPOST, QUANTIUM, QXPRESS, RABEN\_GROUP, RAF\_PHILIPPINES, RAIDEREX, RAM, REDUR\_SPAIN, RED\_CARPET\_LOGISTICS, RINCOS, RL\_CARRIERS, ROADBULL\_LOGISTICS, ROCKET\_PARCEL\_INTERNATIONAL, RPX\_INDONESIA, RPX\_ONLINE, RRD\_INTERNATIONAL\_LOGISTICS\_USA, RUSSIAN\_POST, RUSTON, RZY\_EXPRESS, SAFEXPRESS, SAGAWA, SAIA\_LTL\_FREIGHT, SAILPOST, SAP\_EXPRESS, SAUDI\_POST, SCUDEX\_EXPRESS, SEINO, SEKO\_LOGISTICS, SENDING\_TRANSPORTE\_URGENTE\_Y\_COMUNICACION\_SAU, SENDIT, SENDLE, SFC\_SERVICE, SF\_EXPRESS, SF\_INTERNATIONAL, SGT\_CORRIERE\_ESPRESSO, SHANGHAI\_WISE\_SUPPLY\_CHAIN\_MANAGEMENT\_CO\_LTD, SHENZHEN\_JINGHUADA\_LOGISTICS\_CO\_LTD, SHIPPIT, SHIPTOR, SHOPFANSRU\_LLC, SHREE\_MARUTI\_COURIER\_SERVICES\_PVT\_LTD, SHREE\_TIRUPATI\_COURIER\_SERVICES\_PVT\_LTD, SHUNYOU\_POST, SIMPLYPOST, SINGAPORE\_POST, SINGAPORE\_SPEEDPOST, SIODEMKA, SKYBOX, SKYNET\_MALAYSIA, SKYNET\_WORLDWIDE\_EXPRESS, SKYNET\_WORLDWIDE\_EXPRESS\_UAE, SKYNET\_WORLD\_WIDE\_EXPRESS\_SOUTH\_AFRICA, SKYPOSTAL, SMOOTH\_COURIERS, SMSA\_EXPRESS, SOUTH\_AFRICAN\_POST\_OFFICE, SPANISH\_SEUR, SPECIALISED\_FREIGHT, SPEEDEX\_COURIER, SPEED\_COURIERS, SPOTON\_LOGISTICS\_PVT\_LTD, SRE\_KOREA, STARTRACK, STAR\_TRACK\_COURIER, STAR\_TRACK\_EXPRESS, STO\_EXPRESS, SWISHIP, SWISS\_POST, TAIWAN\_POST, TAQBIN\_HONG\_KONG, TAQBIN\_MALAYSIA, TAQBIN\_SINGAPORE, TCS, THAILAND\_THAI\_POST, THE\_COURIER\_GUY, TIKI, TIPSA, TNT\_AUSTRALIA, TNT\_CLICK\_ITALY, TNT\_ITALY, TNT\_REFERENCE, TOLL\_IPEC, TOLL\_PRIORITY, TOLOS, TOPYOU, TRAKPAK, TRANSMISSION, TRANS\_KARGO\_INTERNASIONAL, UBI\_SMART\_PARCEL, UKRPOSHTA, UNITED\_DELIVERY\_SERVICE\_LTD, UPS\_FREIGHT, UPS\_MAIL\_INNOVATIONS, VIETNAM\_POST, VIETNAM\_POST\_EMS, VIETTELPOST, WAHANA, WANBEXPRESS, WEDO\_LOGISTICS, WEPOST\_LOGISTICS, WISELOADS, WISE\_EXPRESS, WISHPOST, XEND\_EXPRESS, XL\_EXPRESS, XPOSTPH, XPRESSBEES, XQ\_EXPRESS, YAKIT, YAMATO\_JAPAN, YANWEN, YRC, YTO\_EXPRESS, YUNDA\_EXPRESS, YUN\_EXPRESS, ZEPTOEXPRESS, ZINC, ZJS\_INTERNATIONAL, ZTO\_EXPRESS, ZYLLEM, CJ\_PACKET} |  |
| `shipping_calculation_logic_version`float |  |
| `shipping_label_rate_type`string |  |
| `shipping_service_type`string |  |
| `shipping_package_weight`JSON object |  |
| `big_weight`JSON object | Required |
| `value`float | Required |
| `unit`enum {OUNCE, POUND, GRAM, KILOGRAM} | Required |
| `small_weight`JSON object | Required |
| `value`float | Required |
| `unit`enum {OUNCE, POUND, GRAM, KILOGRAM} | Required |
| `shipping_package_dimensions`JSON object |  |
| `unit`enum {INCH, CENTIMETER} | Required |
| `length`float | Required |
| `width`float | Required |
| `height`float | Required |
| `shipping_cost_range_lower_cost`JSON object |  |
| `currency`string | Default value: `USD` |
| `price`float | Required |
| `shipping_cost_range_upper_cost`JSON object |  |
| `currency`string | Default value: `USD` |
| `price`float | Required |
| `shipping_option_type`enum {PREPAID\_LABEL, OWN\_LABEL, LOCAL\_DELIVERY} |  |
| `commerce_shipping_delivery_type`enum {SHIPPING, LOCAL\_DELIVERY, LOCKER} |  |
| `nearby_locations`list<JSON object> |  |
| `name`string |  |
| `street_address`string |  |
| `latitude`float |  |
| `longitude`float |  |
| `image_url`string |  |
| `location_type`string |  |
| `location_page_id`numeric string or integer |  |
| `auto_price_drop_new_price`list<JSON object> |  |
| `date`string |  |
| `price`string |  |
| `xpost_surface`enum {MARKETPLACE\_CROSS\_POST\_SUGGESTIONS, INVENTORY\_MANAGEMENT, GROUP\_COMPOSER, MARKETPLACE\_COMPOSER, PROFILE\_SELLING\_CROSS\_POST\_SUGGESTIONS, BIZ\_ON\_MP\_SETUP\_VIEW, BSG\_ATTACHMENT\_TO\_XPOST\_TO\_MP, UNKNOWN} |  |
| `source_type`string | Default value:  |
| `surface`string | Default value:  |
| `source_post_id_during_creation`string |  |
| `xpost_target_ids`list<string> |  |
| `product_hashtag_names`list<string> |  |
| `suggested_hashtag_names`list<string> |  |
| `product_image_ids`list<string> |  |
| `created_through_nlu_conversion`boolean |  |
| `auction_duration`int64 |  |
| `auction_minimum_bid_increment`int64 |  |
| `video_ids`list<string> |  |
| `video_types`list<enum {SELLER\_ASSISTED\_VIDEO, SELLER\_CREATED\_REEL, SELLER\_CREATED\_VIDEO}> |  |
| `three_d_models_data`list<JSON object> |  |
| `asset_file_handle`string | Required |
| `preview_image_file_handle`string | Required |
| `three_d_model_ids`list<string> |  |
| `shipping_label_rate_code`string |  |
| `shipping_label_price`string |  |
| `product_group_id`numeric string or integer |  |
| `listing_type`enum {SINGLE\_ITEM, MULTI\_VARIANT} |  |
| `live_shopping_video_id`numeric string or integer |  |
| `is_live_shopping_dummy_listing`boolean |  |
| `min_acceptable_checkout_offer_price`float |  |
| `comparable_price`float |  |
| `comparable_price_type`string |  |
| `category_model_source`enum {B2C, C2C, THIRDPARTY\_INGESTION, SELLER\_SELECTED, AICOMMERCE, JOBS, NSR, INTEGRITY, OOPS, BLENDED\_MODEL, RELATED\_PRODUCTS} |  |
| `xpost_profile_audience`JSON object |  |
| `base_state`enum {EVERYONE, FRIENDS, FRIENDS\_OF\_FRIENDS, SELF} | Required |
| `allow`list<string> |  |
| `deny`list<string> |  |
| `tag_expansion_state`enum {TAGGEES, UNSPECIFIED} |  |
| `hidden_from_friends_visibility`enum {HIDDEN\_FROM\_FRIENDS, VISIBLE\_TO\_EVERYONE} |  |
| `indexed_listing_set_id`numeric string or integer |  |
| `indexed_listing_set_data`JSON object |  |
| `availability_set`list<string> | Required |
| `condition_set`list<string> |  |
| `description_set`string |  |
| `title_set`string | Required |
| `should_create_indexed_listing_set`boolean |  |
| `shipping_cost_option`string |  |
| `canonical_product_item_id`numeric string or integer |  |
| `canonical_product_item_data`JSON object |  |
| `catalog_item_clustering_usecase_id`string | Default value:  |
| `enable_reservation`boolean |  |
| `should_update_indexed_listing_set`boolean |  |
| `enable_local_explicitly`boolean |  |
| `max_additional_items`int64 |  |
| `cost_per_additional_item`string |  |
| `product_item_comments_allowed`boolean |  |
| `composer_type`enum {BULK\_COMPOSER, MINIMAL\_COMPOSER, MULTI\_ITEM\_COMPOSER, QUICK\_COMPOSER, REAL\_ESTATE\_COMPOSER, REGULAR\_COMPOSER, SKINNY\_COMPOSER, VEHICLES\_COMPOSER, VIDEO\_FIRST\_COMPOSER} |  |
| `sell_by_date`int64 |  |
| `sku`string |  |
| `commerce_shipping_carrier`enum {AUSTRALIA\_POST, CANADA\_POST, CDL\_LASTMILE, DELIVER\_IT, DHL, DHL\_ECOMMERCE\_US, EAGLE, FEDEX, FEDEX\_UK, NEW\_ZEALAND\_POST, ONTRAC, POST\_DANMARK, PUROLATOR, ROYAL\_MAIL, SPEE\_DEE, TFORCE\_FINALMILE, TNT, TNT\_POST, UPS, USPS, DOORDASH, DOORDASH\_ARCHIVED, DPD\_FRANCE, LA\_POSTE, COLISSIMO, CHRONOPOST\_FRANCE, TNT\_FRANCE, COLIS\_PRIVE, GEODIS\_DISTRIBUTION\_EXPRESS, BERT\_TRANSPORT, GEODIS\_E\_SPACE, MONDIAL\_RELAY, TELIWAY\_SIC\_EXPRESS, AMAZON, APC\_OVERNIGHT, ARROW\_XL, ASENDIA\_UK, BIRDSYSTEM, BLUECARE\_EXPRESS\_LTD, COLLECT\_PLUS, DELTEC\_COURIER, DPD\_LOCAL, DPD\_LOCAL\_REFERENCE, DPD\_UK, HERMESWORLD, IMX\_MAIL, JERSEY\_POST, MYHERMES\_UK, NATIONAL\_SAMEDAY, NORSK\_GLOBAL, PANTHER, PANTHER\_ORDER\_NUMBER, PANTHER\_REFERENCE, PARCEL\_FORCE, RPD2MAN\_DELIVERIES, TNT\_UK, TNT\_UK\_REFERENCE, TUFFNELLS\_PARCELS\_EXPRESS, UK\_MAIL, WHISTL, WNDIRECT, XDP\_EXPRESS, XDP\_EXPRESS\_REFERENCE, YODEL\_DOMESTIC, YODEL\_INTERNATIONAL, AMAZON\_LOGISTICS, AO\_LOGISTICS, APC\_OVERNIGHT\_CONSIGNMENT\_NUMBER, AQUILINE, BANDH\_WORLDWIDE, CAE\_DELIVERS, DHL\_PARCEL\_UK, DMSMATRIX, EU\_FLEET\_SOLUTIONS, GBA\_SERVICES\_LTD, GEMWORLDWIDE, KNAIRLINK\_AEROSPACE\_DOMESTIC\_NETWORK, OCS\_WORLDWIDE, PARCEL2GO, SKYNET\_WORLDWIDE\_EXPRESS\_UK, TUFFNELLS\_PARCELS\_EXPRESS\_REFERENCE, XPERT\_DELIVERY, MAINWAY, INTERPARCEL\_UK, OTHER, ABF\_FREIGHT, ABX\_EXPRESS, AB\_CUSTOM\_GROUP, ACOMMERCE, ACS\_COURIER, ACS\_WORLDWIDE\_EXPRESS, ADICIONAL\_LOGISTICS, ADSONE, AIR21, AIRPAK\_EXPRESS, AIRSPEED\_INTERNATIONAL\_CORPORATION, ALFATREX, ALLIED\_EXPRESS, ALLJOY\_SUPPLY\_CHAIN\_CO\_LTD, ALPHAFAST, AMAZON\_FBA\_USA, AN\_POST, APC\_OVERNIGHT\_REFERENCE, APC\_POSTAL\_LOGISTICS, APRISA\_EXPRESS, ARAMEX, ASENDIA\_GERMANY, ASENDIA\_HK, ASENDIA\_HK\_PREMIUM\_SERVICE\_LATAM, ASENDIA\_USA, ASM, AUPOST\_CHINA, AUSTRALIA\_POST\_SFTP, AUSTRIAN\_POST\_EXPRESS, AUSTRIAN\_POST\_REGISTERED, AUPOST, DHLAU, AXLEHIRE, AXL\_EXPRESS\_LOGISTICS, A\_DUIE\_PYLE, A\_J\_EXPRESS, B2C\_EUROPE, BELPOST, BEST\_EXPRESS, BEST\_WAY\_PARCEL, BETTER\_TRUCKS, BJS\_DISTRIBUTION\_STORAGE\_COURIERS, BJS\_DISTRIBUTION\_STORAGE\_COURIERS\_FTP, BLUEDART, BLUE\_STAR, BNEED, BONDS\_COURIERS, BOXC, BPOST, BPOST\_INTERNATIONAL, BRAZIL\_CORREIOS, BRT\_BARTOLINI, BRT\_BARTOLINI\_PARCEL\_ID, BULGARIAN\_POSTS, BUYLOGIC, CAINIAO, CAMBODIA\_POST, CANPAR\_COURIER, CAPITAL\_TRANSPORT, CARRIER\_007EX, CARRIER\_17\_POST\_SERVICE, CARRIER\_2GO, CARRIER\_360\_LION\_EXPRESS, CARRIER\_4PX, CARRIER\_4\_72\_ENTREGANDO, CARRIER\_ECHO, CBL\_LOGISTICS, CELERITAS\_TRANSPORTE\_SL, CESKA\_POSTA, CHINA\_EMS\_EPACKET, CHINA\_POST, CHIT\_CHATS, CHRONOPOST\_PORTUGAL, CH\_ROBINSON\_WORLDWIDE\_INC, CITY\_LINK\_EXPRESS, CJ\_CENTURY, CJ\_CENTURY\_INTERNATIONAL, CJ\_GLS, CJ\_KOREA\_EXPRESS, CJ\_LOGISTICS\_INTERNATIONAL, CJ\_TRANSNATIONAL\_PHILIPPINES, CLEVY\_LINKS, CLOUDWISH\_ASIA, CNE\_EXPRESS, COLLECTCO, CON\_WAY\_FREIGHT, COPA\_AIRLINES\_COURIER, CORREOS\_CHILE, CORREOS\_DE\_COSTA\_RICA, CORREOS\_DE\_ESPANA, CORREOS\_DE\_MEXICO, CORREOS\_EXPRESS, CORREO\_ARGENTINO, COSMETICS\_NOW, COUREX, COURIERPOST, COURIERS\_PLEASE, COURIER\_IT, COURIER\_PLUS, CPACKET, CUCKOO\_EXPRESS, CYPRUS\_POST, DACHSER, DAWN\_WING, DAYLIGHT\_TRANSPORT\_LLC, DB\_SCHENKER, DB\_SCHENKER\_SWEDEN, DD\_EXPRESS\_COURIER, DELCART, DELHIVERY, DELIVERYONTIME\_LOGISTICS\_PVT\_LTD, DEMANDSHIP, DETRACK, DEUTSCHE\_POST\_DHL, DEUTSCHE\_POST\_MAIL, DEX\_I, DHL\_2\_MANN\_HANDLING, DHL\_ACTIVE\_TRACING, DHL\_BENELUX, DHL\_ECOMMERCE\_ASIA, DHL\_EXPRESS\_PIECE\_ID, DHL\_GLOBAL\_FORWARDING, DHL\_HONG\_KONG, DHL\_NETHERLANDS, DHL\_PARCEL\_NL, DHL\_PARCEL\_SPAIN, DHL\_POLAND\_DOMESTIC, DHL\_SPAIN\_DOMESTIC, DIMERCO\_EXPRESS\_GROUP, DIRECTLOG, DIRECT\_FREIGHT\_EXPRESS, DIRECT\_LINK, DMM\_NETWORK, DOORA\_LOGISTICS, DOTZOT, DPD, DPD\_GERMANY, DPD\_HK, DPD\_IRELAND, DPD\_POLAND, DPD\_ROMANIA, DPD\_RUSSIA, DPEX, DPEX\_CHINA, DPE\_EXPRESS, DPE\_SOUTH\_AFRICA, DSV, DTDC\_AUSTRALIA, DTDC\_EXPRESS\_GLOBAL\_PTE\_LTD, DTDC\_INDIA, DX, DX\_FREIGHT, DYNALOGIC\_BENELUX\_BV, DYNAMIC\_LOGISTICS, EASY\_MAIL, ECARGO, ECMS\_INTERNATIONAL\_LOGISTICS\_CO\_LTD, ECOM\_EXPRESS, EC\_FIRSTCLASS, EFS\_E\_COMMERCE\_FULFILLMENT\_SERVICE, EKART, ELTA\_HELLENIC\_POST, EMIRATES\_POST, EMPS\_EXPRESS, ENSENDA, ENVIALIA, EPARCEL\_KOREA, EP\_BOX, EQUICK\_CHINA, ESTAFETA, ESTES, ETOTAL\_SOLUTION\_LIMITED, EURODIS, EXPEDITORS, EZSHIP, FASTRAK\_SERVICES, FASTWAY\_AUSTRALIA, FASTWAY\_IRELAND, FASTWAY\_NEW\_ZEALAND, FASTWAY\_SOUTH\_AFRICA, FEDEX\_CROSS\_BORDER, FEDEX\_FREIGHT, FEDEX\_POLAND\_DOMESTIC, FERCAM\_LOGISTICS\_TRANSPORT, FIRST\_FLIGHT\_COURIERS, FIRST\_LOGISTICS, FLYT\_EXPRESS, GATI\_KWE, GDEX, GENIKI\_TAXYDROMIKI, GIAO\_HANG\_NHANH, GLOBEGISTICS\_INC, GLS, GLS\_CZECH\_REPUBLIC, GLS\_ITALY, GLS\_NETHERLANDS, GOFLY, GOJAVAS, GREYHOUND, GSI\_EXPRESS, HERMES\_GERMANY, HERMES\_ITALY, HOLISOL, HOMEDIRECT\_LOGISTICS, HONG\_KONG\_POST, HRVATSKA\_POSTA, HUA\_HAN\_LOGISTICS, HUNTER\_EXPRESS, ICELAND\_POST, IDEX, IMEX\_GLOBAL\_SOLUTIONS, INDIA\_POST\_DOMESTIC, INDIA\_POST\_INTERNATIONAL, INPOST\_PACZKOMATY, INSTANT\_TIONG\_NAM\_EBIZ\_EXPRESS\_SDN\_BHD, INTERNATIONAL\_SEUR, INTERNET\_EXPRESS, ISRAEL\_POST, ISRAEL\_POST\_DOMESTIC, ITALY\_SDA, I\_PARCEL, J\_T\_EXPRESS, JAM\_EXPRESS, JANCO\_ECOMMERCE, JAPAN\_POST, JAYON\_EXPRESS\_JEX, JCEX, JET\_SHIP\_WORLDWIDE, JINSUNG\_TRADING, JNE, JOCOM, JP\_BH\_POSTA, JX, J\_NET, K1\_EXPRESS, KANGAROO\_WORLDWIDE\_EXPRESS, KERRY\_EXPRESS\_HONG\_KONG, KERRY\_EXPRESS\_THAILAND, KERRY\_EXPRESS\_VIETNAM\_CO\_LTD, KGM\_HUB, KIALA, KOREA\_POST, KOREA\_POST\_EMS, KRONOS\_EXPRESS, KUEHNE\_NAGEL, LANDMARK\_GLOBAL, LAO\_POST, LASERSHIP, LBC\_EXPRESS, LHT\_EXPRESS, LIETUVOS\_PASTAS, LINE\_CLEAR\_EXPRESS\_LOGISTICS\_SDN\_BHD, LINK\_BRIDGE\_BEIJING\_INTERNATIONAL\_LOGISTICS\_COLTD, LION\_PARCEL, LOGISTIC\_WORLDWIDE\_EXPRESS, LOGWIN\_LOGISTICS, LONE\_STAR\_OVERNIGHT, MAGYAR\_POSTA, MAILAMERICAS, MAILPLUS, MAINFREIGHT, MALAYSIA\_POST\_EMS\_POS\_LAJU, MALAYSIA\_POST\_REGISTERED, MARA\_XPRESS, MATDESPATCH, MATKAHUOLTO, MDS\_COLLIVERY\_PTY\_LTD, MEGASAVE, MEXICO\_AEROFLASH, MEXICO\_REDPACK, MEXICO\_SENDA\_EXPRESS, MIKROPAKKET, MRW, MUDITA, MXE\_EXPRESS, MYPOSTONLINE, M\_XPRESS\_SDN\_BHD, NACEX\_SPAIN, NANJING\_WOYUAN, NATIONWIDE\_EXPRESS, NEWGISTICS, NEWGISTICS\_API, NEXIVE\_TNT\_POST\_ITALY, NHANS\_SOLUTIONS, NIGHTLINE, NIM\_EXPRESS, NINJA\_VAN, NINJA\_VAN\_INDONESIA, NINJA\_VAN\_MALAYSIA, NINJA\_VAN\_PHILIPPINES, NINJA\_VAN\_THAILAND, NIPOST, NOVA\_POSHTA, NOVA\_POSHTA\_INTERNATIONAL, OCA\_ARGENTINA, OLD\_DOMINION\_FREIGHT\_LINE, OMNIVA, OMNI\_PARCEL, ONE\_WORLD\_EXPRESS, PACKLINK, PAL\_EXPRESS\_LIMITED, PANDU\_LOGISTICS, PAQUETEXPRESS, PARCELLEDIN, PARCELPOINT\_PTY\_LTD, PARCEL\_POST\_SINGAPORE, PAYPAL\_PACKAGE, PFC\_EXPRESS, PICKUPP, PICK\_UPP\_MYS\_SGP, PILOT\_FREIGHT\_SERVICES, PITNEY\_BOWES, PIXSELL\_LOGISTICS, POCZTA\_POLSKA, PORTUGAL\_CTT, PORTUGAL\_SEUR, POST56, POSTEN\_NORGE\_BRING, POSTE\_ITALIANE, POSTE\_ITALIANE\_PACCOCELERE, POSTI, POSTNL\_DOMESTIC, POSTNL\_INTERNATIONAL, POSTNL\_INTERNATIONAL\_3S, POSTNORD\_DENMARK, POSTNORD\_LOGISTICS, POSTNORD\_SWEDEN, POST\_OF\_SLOVENIA, POST\_SERBIA, POS\_INDONESIA\_DOMESTIC, POS\_INDONESIA\_INTL, POSTA\_ROMANA, PROFESSIONAL\_COURIERS, PTT\_POSTA, QUALITYPOST, QUANTIUM, QXPRESS, RABEN\_GROUP, RAF\_PHILIPPINES, RAIDEREX, RAM, REDUR\_SPAIN, RED\_CARPET\_LOGISTICS, RINCOS, RL\_CARRIERS, ROADBULL\_LOGISTICS, ROCKET\_PARCEL\_INTERNATIONAL, RPX\_INDONESIA, RPX\_ONLINE, RRD\_INTERNATIONAL\_LOGISTICS\_USA, RUSSIAN\_POST, RUSTON, RZY\_EXPRESS, SAFEXPRESS, SAGAWA, SAIA\_LTL\_FREIGHT, SAILPOST, SAP\_EXPRESS, SAUDI\_POST, SCUDEX\_EXPRESS, SEINO, SEKO\_LOGISTICS, SENDING\_TRANSPORTE\_URGENTE\_Y\_COMUNICACION\_SAU, SENDIT, SENDLE, SFC\_SERVICE, SF\_EXPRESS, SF\_INTERNATIONAL, SGT\_CORRIERE\_ESPRESSO, SHANGHAI\_WISE\_SUPPLY\_CHAIN\_MANAGEMENT\_CO\_LTD, SHENZHEN\_JINGHUADA\_LOGISTICS\_CO\_LTD, SHIPPIT, SHIPTOR, SHOPFANSRU\_LLC, SHREE\_MARUTI\_COURIER\_SERVICES\_PVT\_LTD, SHREE\_TIRUPATI\_COURIER\_SERVICES\_PVT\_LTD, SHUNYOU\_POST, SIMPLYPOST, SINGAPORE\_POST, SINGAPORE\_SPEEDPOST, SIODEMKA, SKYBOX, SKYNET\_MALAYSIA, SKYNET\_WORLDWIDE\_EXPRESS, SKYNET\_WORLDWIDE\_EXPRESS\_UAE, SKYNET\_WORLD\_WIDE\_EXPRESS\_SOUTH\_AFRICA, SKYPOSTAL, SMOOTH\_COURIERS, SMSA\_EXPRESS, SOUTH\_AFRICAN\_POST\_OFFICE, SPANISH\_SEUR, SPECIALISED\_FREIGHT, SPEEDEX\_COURIER, SPEED\_COURIERS, SPOTON\_LOGISTICS\_PVT\_LTD, SRE\_KOREA, STARTRACK, STAR\_TRACK\_COURIER, STAR\_TRACK\_EXPRESS, STO\_EXPRESS, SWISHIP, SWISS\_POST, TAIWAN\_POST, TAQBIN\_HONG\_KONG, TAQBIN\_MALAYSIA, TAQBIN\_SINGAPORE, TCS, THAILAND\_THAI\_POST, THE\_COURIER\_GUY, TIKI, TIPSA, TNT\_AUSTRALIA, TNT\_CLICK\_ITALY, TNT\_ITALY, TNT\_REFERENCE, TOLL\_IPEC, TOLL\_PRIORITY, TOLOS, TOPYOU, TRAKPAK, TRANSMISSION, TRANS\_KARGO\_INTERNASIONAL, UBI\_SMART\_PARCEL, UKRPOSHTA, UNITED\_DELIVERY\_SERVICE\_LTD, UPS\_FREIGHT, UPS\_MAIL\_INNOVATIONS, VIETNAM\_POST, VIETNAM\_POST\_EMS, VIETTELPOST, WAHANA, WANBEXPRESS, WEDO\_LOGISTICS, WEPOST\_LOGISTICS, WISELOADS, WISE\_EXPRESS, WISHPOST, XEND\_EXPRESS, XL\_EXPRESS, XPOSTPH, XPRESSBEES, XQ\_EXPRESS, YAKIT, YAMATO\_JAPAN, YANWEN, YRC, YTO\_EXPRESS, YUNDA\_EXPRESS, YUN\_EXPRESS, ZEPTOEXPRESS, ZINC, ZJS\_INTERNATIONAL, ZTO\_EXPRESS, ZYLLEM, CJ\_PACKET} |  |
| `shipping_calculation_logic_version`float |  |
| `shipping_label_rate_type`string |  |
| `shipping_service_type`string |  |
| `shipping_package_weight`JSON object |  |
| `big_weight`JSON object | Required |
| `value`float | Required |
| `unit`enum {OUNCE, POUND, GRAM, KILOGRAM} | Required |
| `small_weight`JSON object | Required |
| `value`float | Required |
| `unit`enum {OUNCE, POUND, GRAM, KILOGRAM} | Required |
| `shipping_package_dimensions`JSON object |  |
| `unit`enum {INCH, CENTIMETER} | Required |
| `length`float | Required |
| `width`float | Required |
| `height`float | Required |
| `shipping_cost_range_lower_cost`string |  |
| `shipping_cost_range_upper_cost`string |  |
| `personalization_info`string |  |
| `is_personalization_required`boolean |  |
| `relisted_from_listing_id`numeric string or integer |  |
| `commerce_shipping_carriers`list<enum {AUSTRALIA\_POST, CANADA\_POST, CDL\_LASTMILE, DELIVER\_IT, DHL, DHL\_ECOMMERCE\_US, EAGLE, FEDEX, FEDEX\_UK, NEW\_ZEALAND\_POST, ONTRAC, POST\_DANMARK, PUROLATOR, ROYAL\_MAIL, SPEE\_DEE, TFORCE\_FINALMILE, TNT, TNT\_POST, UPS, USPS, DOORDASH, DOORDASH\_ARCHIVED, DPD\_FRANCE, LA\_POSTE, COLISSIMO, CHRONOPOST\_FRANCE, TNT\_FRANCE, COLIS\_PRIVE, GEODIS\_DISTRIBUTION\_EXPRESS, BERT\_TRANSPORT, GEODIS\_E\_SPACE, MONDIAL\_RELAY, TELIWAY\_SIC\_EXPRESS, AMAZON, APC\_OVERNIGHT, ARROW\_XL, ASENDIA\_UK, BIRDSYSTEM, BLUECARE\_EXPRESS\_LTD, COLLECT\_PLUS, DELTEC\_COURIER, DPD\_LOCAL, DPD\_LOCAL\_REFERENCE, DPD\_UK, HERMESWORLD, IMX\_MAIL, JERSEY\_POST, MYHERMES\_UK, NATIONAL\_SAMEDAY, NORSK\_GLOBAL, PANTHER, PANTHER\_ORDER\_NUMBER, PANTHER\_REFERENCE, PARCEL\_FORCE, RPD2MAN\_DELIVERIES, TNT\_UK, TNT\_UK\_REFERENCE, TUFFNELLS\_PARCELS\_EXPRESS, UK\_MAIL, WHISTL, WNDIRECT, XDP\_EXPRESS, XDP\_EXPRESS\_REFERENCE, YODEL\_DOMESTIC, YODEL\_INTERNATIONAL, AMAZON\_LOGISTICS, AO\_LOGISTICS, APC\_OVERNIGHT\_CONSIGNMENT\_NUMBER, AQUILINE, BANDH\_WORLDWIDE, CAE\_DELIVERS, DHL\_PARCEL\_UK, DMSMATRIX, EU\_FLEET\_SOLUTIONS, GBA\_SERVICES\_LTD, GEMWORLDWIDE, KNAIRLINK\_AEROSPACE\_DOMESTIC\_NETWORK, OCS\_WORLDWIDE, PARCEL2GO, SKYNET\_WORLDWIDE\_EXPRESS\_UK, TUFFNELLS\_PARCELS\_EXPRESS\_REFERENCE, XPERT\_DELIVERY, MAINWAY, INTERPARCEL\_UK, OTHER, ABF\_FREIGHT, ABX\_EXPRESS, AB\_CUSTOM\_GROUP, ACOMMERCE, ACS\_COURIER, ACS\_WORLDWIDE\_EXPRESS, ADICIONAL\_LOGISTICS, ADSONE, AIR21, AIRPAK\_EXPRESS, AIRSPEED\_INTERNATIONAL\_CORPORATION, ALFATREX, ALLIED\_EXPRESS, ALLJOY\_SUPPLY\_CHAIN\_CO\_LTD, ALPHAFAST, AMAZON\_FBA\_USA, AN\_POST, APC\_OVERNIGHT\_REFERENCE, APC\_POSTAL\_LOGISTICS, APRISA\_EXPRESS, ARAMEX, ASENDIA\_GERMANY, ASENDIA\_HK, ASENDIA\_HK\_PREMIUM\_SERVICE\_LATAM, ASENDIA\_USA, ASM, AUPOST\_CHINA, AUSTRALIA\_POST\_SFTP, AUSTRIAN\_POST\_EXPRESS, AUSTRIAN\_POST\_REGISTERED, AUPOST, DHLAU, AXLEHIRE, AXL\_EXPRESS\_LOGISTICS, A\_DUIE\_PYLE, A\_J\_EXPRESS, B2C\_EUROPE, BELPOST, BEST\_EXPRESS, BEST\_WAY\_PARCEL, BETTER\_TRUCKS, BJS\_DISTRIBUTION\_STORAGE\_COURIERS, BJS\_DISTRIBUTION\_STORAGE\_COURIERS\_FTP, BLUEDART, BLUE\_STAR, BNEED, BONDS\_COURIERS, BOXC, BPOST, BPOST\_INTERNATIONAL, BRAZIL\_CORREIOS, BRT\_BARTOLINI, BRT\_BARTOLINI\_PARCEL\_ID, BULGARIAN\_POSTS, BUYLOGIC, CAINIAO, CAMBODIA\_POST, CANPAR\_COURIER, CAPITAL\_TRANSPORT, CARRIER\_007EX, CARRIER\_17\_POST\_SERVICE, CARRIER\_2GO, CARRIER\_360\_LION\_EXPRESS, CARRIER\_4PX, CARRIER\_4\_72\_ENTREGANDO, CARRIER\_ECHO, CBL\_LOGISTICS, CELERITAS\_TRANSPORTE\_SL, CESKA\_POSTA, CHINA\_EMS\_EPACKET, CHINA\_POST, CHIT\_CHATS, CHRONOPOST\_PORTUGAL, CH\_ROBINSON\_WORLDWIDE\_INC, CITY\_LINK\_EXPRESS, CJ\_CENTURY, CJ\_CENTURY\_INTERNATIONAL, CJ\_GLS, CJ\_KOREA\_EXPRESS, CJ\_LOGISTICS\_INTERNATIONAL, CJ\_TRANSNATIONAL\_PHILIPPINES, CLEVY\_LINKS, CLOUDWISH\_ASIA, CNE\_EXPRESS, COLLECTCO, CON\_WAY\_FREIGHT, COPA\_AIRLINES\_COURIER, CORREOS\_CHILE, CORREOS\_DE\_COSTA\_RICA, CORREOS\_DE\_ESPANA, CORREOS\_DE\_MEXICO, CORREOS\_EXPRESS, CORREO\_ARGENTINO, COSMETICS\_NOW, COUREX, COURIERPOST, COURIERS\_PLEASE, COURIER\_IT, COURIER\_PLUS, CPACKET, CUCKOO\_EXPRESS, CYPRUS\_POST, DACHSER, DAWN\_WING, DAYLIGHT\_TRANSPORT\_LLC, DB\_SCHENKER, DB\_SCHENKER\_SWEDEN, DD\_EXPRESS\_COURIER, DELCART, DELHIVERY, DELIVERYONTIME\_LOGISTICS\_PVT\_LTD, DEMANDSHIP, DETRACK, DEUTSCHE\_POST\_DHL, DEUTSCHE\_POST\_MAIL, DEX\_I, DHL\_2\_MANN\_HANDLING, DHL\_ACTIVE\_TRACING, DHL\_BENELUX, DHL\_ECOMMERCE\_ASIA, DHL\_EXPRESS\_PIECE\_ID, DHL\_GLOBAL\_FORWARDING, DHL\_HONG\_KONG, DHL\_NETHERLANDS, DHL\_PARCEL\_NL, DHL\_PARCEL\_SPAIN, DHL\_POLAND\_DOMESTIC, DHL\_SPAIN\_DOMESTIC, DIMERCO\_EXPRESS\_GROUP, DIRECTLOG, DIRECT\_FREIGHT\_EXPRESS, DIRECT\_LINK, DMM\_NETWORK, DOORA\_LOGISTICS, DOTZOT, DPD, DPD\_GERMANY, DPD\_HK, DPD\_IRELAND, DPD\_POLAND, DPD\_ROMANIA, DPD\_RUSSIA, DPEX, DPEX\_CHINA, DPE\_EXPRESS, DPE\_SOUTH\_AFRICA, DSV, DTDC\_AUSTRALIA, DTDC\_EXPRESS\_GLOBAL\_PTE\_LTD, DTDC\_INDIA, DX, DX\_FREIGHT, DYNALOGIC\_BENELUX\_BV, DYNAMIC\_LOGISTICS, EASY\_MAIL, ECARGO, ECMS\_INTERNATIONAL\_LOGISTICS\_CO\_LTD, ECOM\_EXPRESS, EC\_FIRSTCLASS, EFS\_E\_COMMERCE\_FULFILLMENT\_SERVICE, EKART, ELTA\_HELLENIC\_POST, EMIRATES\_POST, EMPS\_EXPRESS, ENSENDA, ENVIALIA, EPARCEL\_KOREA, EP\_BOX, EQUICK\_CHINA, ESTAFETA, ESTES, ETOTAL\_SOLUTION\_LIMITED, EURODIS, EXPEDITORS, EZSHIP, FASTRAK\_SERVICES, FASTWAY\_AUSTRALIA, FASTWAY\_IRELAND, FASTWAY\_NEW\_ZEALAND, FASTWAY\_SOUTH\_AFRICA, FEDEX\_CROSS\_BORDER, FEDEX\_FREIGHT, FEDEX\_POLAND\_DOMESTIC, FERCAM\_LOGISTICS\_TRANSPORT, FIRST\_FLIGHT\_COURIERS, FIRST\_LOGISTICS, FLYT\_EXPRESS, GATI\_KWE, GDEX, GENIKI\_TAXYDROMIKI, GIAO\_HANG\_NHANH, GLOBEGISTICS\_INC, GLS, GLS\_CZECH\_REPUBLIC, GLS\_ITALY, GLS\_NETHERLANDS, GOFLY, GOJAVAS, GREYHOUND, GSI\_EXPRESS, HERMES\_GERMANY, HERMES\_ITALY, HOLISOL, HOMEDIRECT\_LOGISTICS, HONG\_KONG\_POST, HRVATSKA\_POSTA, HUA\_HAN\_LOGISTICS, HUNTER\_EXPRESS, ICELAND\_POST, IDEX, IMEX\_GLOBAL\_SOLUTIONS, INDIA\_POST\_DOMESTIC, INDIA\_POST\_INTERNATIONAL, INPOST\_PACZKOMATY, INSTANT\_TIONG\_NAM\_EBIZ\_EXPRESS\_SDN\_BHD, INTERNATIONAL\_SEUR, INTERNET\_EXPRESS, ISRAEL\_POST, ISRAEL\_POST\_DOMESTIC, ITALY\_SDA, I\_PARCEL, J\_T\_EXPRESS, JAM\_EXPRESS, JANCO\_ECOMMERCE, JAPAN\_POST, JAYON\_EXPRESS\_JEX, JCEX, JET\_SHIP\_WORLDWIDE, JINSUNG\_TRADING, JNE, JOCOM, JP\_BH\_POSTA, JX, J\_NET, K1\_EXPRESS, KANGAROO\_WORLDWIDE\_EXPRESS, KERRY\_EXPRESS\_HONG\_KONG, KERRY\_EXPRESS\_THAILAND, KERRY\_EXPRESS\_VIETNAM\_CO\_LTD, KGM\_HUB, KIALA, KOREA\_POST, KOREA\_POST\_EMS, KRONOS\_EXPRESS, KUEHNE\_NAGEL, LANDMARK\_GLOBAL, LAO\_POST, LASERSHIP, LBC\_EXPRESS, LHT\_EXPRESS, LIETUVOS\_PASTAS, LINE\_CLEAR\_EXPRESS\_LOGISTICS\_SDN\_BHD, LINK\_BRIDGE\_BEIJING\_INTERNATIONAL\_LOGISTICS\_COLTD, LION\_PARCEL, LOGISTIC\_WORLDWIDE\_EXPRESS, LOGWIN\_LOGISTICS, LONE\_STAR\_OVERNIGHT, MAGYAR\_POSTA, MAILAMERICAS, MAILPLUS, MAINFREIGHT, MALAYSIA\_POST\_EMS\_POS\_LAJU, MALAYSIA\_POST\_REGISTERED, MARA\_XPRESS, MATDESPATCH, MATKAHUOLTO, MDS\_COLLIVERY\_PTY\_LTD, MEGASAVE, MEXICO\_AEROFLASH, MEXICO\_REDPACK, MEXICO\_SENDA\_EXPRESS, MIKROPAKKET, MRW, MUDITA, MXE\_EXPRESS, MYPOSTONLINE, M\_XPRESS\_SDN\_BHD, NACEX\_SPAIN, NANJING\_WOYUAN, NATIONWIDE\_EXPRESS, NEWGISTICS, NEWGISTICS\_API, NEXIVE\_TNT\_POST\_ITALY, NHANS\_SOLUTIONS, NIGHTLINE, NIM\_EXPRESS, NINJA\_VAN, NINJA\_VAN\_INDONESIA, NINJA\_VAN\_MALAYSIA, NINJA\_VAN\_PHILIPPINES, NINJA\_VAN\_THAILAND, NIPOST, NOVA\_POSHTA, NOVA\_POSHTA\_INTERNATIONAL, OCA\_ARGENTINA, OLD\_DOMINION\_FREIGHT\_LINE, OMNIVA, OMNI\_PARCEL, ONE\_WORLD\_EXPRESS, PACKLINK, PAL\_EXPRESS\_LIMITED, PANDU\_LOGISTICS, PAQUETEXPRESS, PARCELLEDIN, PARCELPOINT\_PTY\_LTD, PARCEL\_POST\_SINGAPORE, PAYPAL\_PACKAGE, PFC\_EXPRESS, PICKUPP, PICK\_UPP\_MYS\_SGP, PILOT\_FREIGHT\_SERVICES, PITNEY\_BOWES, PIXSELL\_LOGISTICS, POCZTA\_POLSKA, PORTUGAL\_CTT, PORTUGAL\_SEUR, POST56, POSTEN\_NORGE\_BRING, POSTE\_ITALIANE, POSTE\_ITALIANE\_PACCOCELERE, POSTI, POSTNL\_DOMESTIC, POSTNL\_INTERNATIONAL, POSTNL\_INTERNATIONAL\_3S, POSTNORD\_DENMARK, POSTNORD\_LOGISTICS, POSTNORD\_SWEDEN, POST\_OF\_SLOVENIA, POST\_SERBIA, POS\_INDONESIA\_DOMESTIC, POS\_INDONESIA\_INTL, POSTA\_ROMANA, PROFESSIONAL\_COURIERS, PTT\_POSTA, QUALITYPOST, QUANTIUM, QXPRESS, RABEN\_GROUP, RAF\_PHILIPPINES, RAIDEREX, RAM, REDUR\_SPAIN, RED\_CARPET\_LOGISTICS, RINCOS, RL\_CARRIERS, ROADBULL\_LOGISTICS, ROCKET\_PARCEL\_INTERNATIONAL, RPX\_INDONESIA, RPX\_ONLINE, RRD\_INTERNATIONAL\_LOGISTICS\_USA, RUSSIAN\_POST, RUSTON, RZY\_EXPRESS, SAFEXPRESS, SAGAWA, SAIA\_LTL\_FREIGHT, SAILPOST, SAP\_EXPRESS, SAUDI\_POST, SCUDEX\_EXPRESS, SEINO, SEKO\_LOGISTICS, SENDING\_TRANSPORTE\_URGENTE\_Y\_COMUNICACION\_SAU, SENDIT, SENDLE, SFC\_SERVICE, SF\_EXPRESS, SF\_INTERNATIONAL, SGT\_CORRIERE\_ESPRESSO, SHANGHAI\_WISE\_SUPPLY\_CHAIN\_MANAGEMENT\_CO\_LTD, SHENZHEN\_JINGHUADA\_LOGISTICS\_CO\_LTD, SHIPPIT, SHIPTOR, SHOPFANSRU\_LLC, SHREE\_MARUTI\_COURIER\_SERVICES\_PVT\_LTD, SHREE\_TIRUPATI\_COURIER\_SERVICES\_PVT\_LTD, SHUNYOU\_POST, SIMPLYPOST, SINGAPORE\_POST, SINGAPORE\_SPEEDPOST, SIODEMKA, SKYBOX, SKYNET\_MALAYSIA, SKYNET\_WORLDWIDE\_EXPRESS, SKYNET\_WORLDWIDE\_EXPRESS\_UAE, SKYNET\_WORLD\_WIDE\_EXPRESS\_SOUTH\_AFRICA, SKYPOSTAL, SMOOTH\_COURIERS, SMSA\_EXPRESS, SOUTH\_AFRICAN\_POST\_OFFICE, SPANISH\_SEUR, SPECIALISED\_FREIGHT, SPEEDEX\_COURIER, SPEED\_COURIERS, SPOTON\_LOGISTICS\_PVT\_LTD, SRE\_KOREA, STARTRACK, STAR\_TRACK\_COURIER, STAR\_TRACK\_EXPRESS, STO\_EXPRESS, SWISHIP, SWISS\_POST, TAIWAN\_POST, TAQBIN\_HONG\_KONG, TAQBIN\_MALAYSIA, TAQBIN\_SINGAPORE, TCS, THAILAND\_THAI\_POST, THE\_COURIER\_GUY, TIKI, TIPSA, TNT\_AUSTRALIA, TNT\_CLICK\_ITALY, TNT\_ITALY, TNT\_REFERENCE, TOLL\_IPEC, TOLL\_PRIORITY, TOLOS, TOPYOU, TRAKPAK, TRANSMISSION, TRANS\_KARGO\_INTERNASIONAL, UBI\_SMART\_PARCEL, UKRPOSHTA, UNITED\_DELIVERY\_SERVICE\_LTD, UPS\_FREIGHT, UPS\_MAIL\_INNOVATIONS, VIETNAM\_POST, VIETNAM\_POST\_EMS, VIETTELPOST, WAHANA, WANBEXPRESS, WEDO\_LOGISTICS, WEPOST\_LOGISTICS, WISELOADS, WISE\_EXPRESS, WISHPOST, XEND\_EXPRESS, XL\_EXPRESS, XPOSTPH, XPRESSBEES, XQ\_EXPRESS, YAKIT, YAMATO\_JAPAN, YANWEN, YRC, YTO\_EXPRESS, YUNDA\_EXPRESS, YUN\_EXPRESS, ZEPTOEXPRESS, ZINC, ZJS\_INTERNATIONAL, ZTO\_EXPRESS, ZYLLEM, CJ\_PACKET}> |  |
| `include_listing_info_in_rating`enum {ENABLE\_INCLUDE\_LISTING\_INFO\_IN\_RATING, DISABLE\_INCLUDE\_LISTING\_INFO\_IN\_RATING} |  |
| `has_multiple_items`boolean |  |
| `public_meetup_location_page_ids`list<string> |  |
| `is_meetup_location_public`boolean |  |
| `listing_email_id`numeric string or integer |  |
| `scheduled_publish_time`int64 | SELF\_EXPLANATORY
 |
| `should_sync_product_edit`boolean | should\_sync\_product\_edit
 |
| `source_type`string | source\_type
 |
| `sponsor_id`numeric string or integer | Facebook Page id that is tagged as sponsor in the Feed post
 |
| `sponsor_relationship`int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith
 |
| `tags`list<int> | SELF\_EXPLANATORY
 |
| `text_format_preset_id`numeric string or integer | text\_format\_preset\_id
 |
| `timeline_visibility`enum{hidden, normal, forced\_allow} | SELF\_EXPLANATORY
 |
| `tracking`JSON-encoded string | SELF\_EXPLANATORY
 |

### Return Type

This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 210 | User not visible |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

Deleting
--------


 Only select developers can perform this operation using the API. You can use the Business Manager to delete posts.

You can delete a PagePost by making a DELETE request to `/{page_post_id}`.### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURLGraph API Explorer
```
DELETE /v19.0/{page-id}_{post-id}/ HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->delete(
    '/{page-id}_{post-id}/',
    array (),
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```

```
/* make the API call */
FB.api(
    "/{page-id}_{post-id}/",
    "DELETE",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{page-id}_{post-id}/",
    null,
    HttpMethod.DELETE,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{page-id}_{post-id}/"
                                      parameters:params
                                      HTTPMethod:@"DELETE"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```

```
curl -X DELETE -G \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/{page-id}_{post-id}/
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

This endpoint doesn't have any parameters.### Return Type

 Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |



































