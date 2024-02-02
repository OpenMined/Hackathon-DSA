<div>

::: c01-rich-text-editor
Returns a map of the available size variations of the specified user\'s
profile banner. If the user has not uploaded a profile banner, a HTTP
404 will be served instead. This method can be used instead of string
manipulation on the ` profile_banner_url ` returned in user objects as
described in [Profile Images and
Banners](/en/docs/accounts-and-users/user-profile-images-and-banners) .

The profile banner data available at each size variant\'s URL is in PNG
format.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/users/profile_banner.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   180
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- -------------------------------------------------------------------------------------------------------------------------------- --------------- -----------
  Name          Required   Description                                                                                                                      Default Value   Example
  user_id       optional   The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name.                      *12345*
  screen_name   optional   The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID.                   *noradio*
  ------------- ---------- -------------------------------------------------------------------------------------------------------------------------------- --------------- -----------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/users/profile_banner.json?screen_name=twitterapi `

## Example Response [¶](#example-response){.headerlink}

    {
      "sizes": {
        "ipad": {
          "h": 313,
          "w": 626,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/ipad"
        },
        "ipad_retina": {
          "h": 626,
          "w": 1252,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/ipad_retina"
        },
        "web": {
          "h": 260,
          "w": 520,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/web"
        },
        "web_retina": {
          "h": 520,
          "w": 1040,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/web_retina"
        },
        "mobile": {
          "h": 160,
          "w": 320,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/mobile"
        },
        "mobile_retina": {
          "h": 320,
          "w": 640,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/mobile_retina"
        },
        "300x100": {
          "h": 100,
          "w": 300,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/300x100"
        },
        "600x200": {
          "h": 200,
          "w": 600,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/600x200"
        },
        "1500x500": {
          "h": 500,
          "w": 1500,
          "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/1500x500"
        }
      }
    }
:::

</div>
