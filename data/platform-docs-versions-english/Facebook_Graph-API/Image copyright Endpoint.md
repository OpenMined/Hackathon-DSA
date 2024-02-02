Image Copyright
===============

Reading
-------

Represents a copyright on an image asset.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bimage-copyright-id%7D&version=v19.0)

    GET /v19.0/{image-copyright-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{image-copyright-id}',
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

    /* make the API call */
    FB.api(
        "/{image-copyright-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{image-copyright-id}",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{image-copyright-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the object |
| `artist`<br><br>string | Artist/Photographer related the reference asset, user providedNote that the "Creator" field is used for image agencies or partners. |
| `copyright_monitoring_status`<br><br>enum | The status of the copyright reference file. It is used to determine if the match should be skipped. |
| `creation_time`<br><br>datetime | Creation time provided by TAO Server |
| `creator`<br><br>string | Creator of the reference asset, user provided |
| `custom_id`<br><br>string | Custom Id for reference asset, user provided |
| `description`<br><br>string | Description for reference asset, user provided |
| `filename`<br><br>string | Filename for reference asset, user provided |
| `image`<br><br>[Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) | The underlying image asset for the copyright |
| `matches_count`<br><br>unsigned integer | The number of matches for this copyright that are displayed in Rights Manager |
| `original_content_creation_date`<br><br>datetime | Date the reference asset was created, user provided |
| `ownership_countries`<br><br>VideoCopyrightGeoGate | Countries of included or excluded ownership for the given image copyright |
| `tags`<br><br>list<string> | Tags for the reference asset |
| `title`<br><br>string | The title of the copyright, generated from the reference asset |
| `update_time`<br><br>datetime | Update time provided by TAO Server |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can make a POST request to `image_copyrights` edge from the following paths:

* [`/{page_id}/image_copyrights`](https://developers.facebook.com/docs/graph-api/reference/page/image_copyrights/)

When posting to this edge, an [ImageCopyright](https://developers.facebook.com/docs/graph-api/reference/image-copyright/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `artist`<br><br>string | Artist/Photographer related to the copyright |
| `attribution_link`<br><br>string | The link to the rights holder where viewer can license the images. |
| `creator`<br><br>string | For agencies |
| `custom_id`<br><br>string | Any ID used internally by the copyright holder |
| `description`<br><br>string | Description of the copyrighted image |
| `filename`<br><br>string | Filename of the copyrighted image<br><br>Required |
| `geo_ownership`<br><br>list<enum {AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TP, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW}> | In which territories the copyright on the image is held<br><br>Required |
| `original_content_creation_date`<br><br>int64 | When the copyrighted image was created |
| `reference_photo`<br><br>numeric string or integer | ID of the uploaded image to be protected. This must be an unpublished, temporary photo. Please refer to the [photo documentation](https://developers.facebook.com/docs/graph-api/reference/page/photos) on how to create unpublished, temporary photos.<br><br>Required |
| `title`<br><br>string | Title of the copyrighted image |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Updating
--------

You can update an [ImageCopyright](https://developers.facebook.com/docs/graph-api/reference/image-copyright/) by making a POST request to [`/{image_copyright_id}`](https://developers.facebook.com/docs/graph-api/reference/image-copyright/).

### Parameters

| Parameter | Description |
| --- | --- |
| `artist`<br><br>string | Artist/Photographer related to the copyright |
| `creator`<br><br>string | For agencies |
| `description`<br><br>string | Description of the copyrighted image |
| `geo_ownership`<br><br>list<enum {AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TP, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW}> | In which territories the copyright on the image is held |
| `original_content_creation_date`<br><br>int64 | When the copyrighted image was created |
| `title`<br><br>string | Title of the copyrighted image |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)