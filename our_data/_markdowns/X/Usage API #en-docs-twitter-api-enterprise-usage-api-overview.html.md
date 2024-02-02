
Usage API | Twitter API | Docs | Twitter Developer Platform 

Overview

Overview
--------

Enterprise

The Usage API is a free REST API that provides programmatic access and visibility into activity consumption across products for your enterprise account. It is the most important and *best* tool for helping to monitor and manage usage across the different APIs under your account.

**Important Disclaimer:**

The usage counts returned from the Usage API may not match those on a billing invoice due to trials and other billing adjustments. All numbers are based on deduped activities consumed within a given day (in UTC).

### Features

* Programmatically retrieving usage data that is available in the console.gnip.com UI
* Stream level usage data - provides usage data at the stream level (e.g., dev and prod) in addition to the product level
* Granular and descriptive data - search "requests" are broken out by Full-Archive and 30-Day Search products
* Historical PowerTrack “days” and “jobs”

Supported APIs
--------------

Below is a list of the APIs currently supported by the Usage API:

* PowerTrack API enterprise
* 30-Day Search API enterprise
* Full-Archive Search API enterprise
* Historical PowerTrack enterprise

Limitations
------------

* The Usage API allows you to access usage data since May 1, 2018.  After July 1, 2019 Usage API allows you to access usage data for the **trailing 13 calendar months**
* You have the ability to access usage data in **three month intervals** defined with a fromDate and toDate

See below for a request & response:

```
      curl -u<username>:<password> \
"https://gnip-api.twitter.com/metrics/usage/accounts/<account-name>.json?bucket=month"
```

Code copied to clipboard

```
      {
  "account": {
    "name": "accountnamehere"
  },
  "publishers": [
    {
      "type": "twitter",
      "used": [
        {
          "timePeriod": "201805010000",
          "activities": 1235,
          "searchRequests30Day": 3,
          "searchRequestsFullArchive": 19,
          "historicalPowertrackDays": 0,
          "historicalPowertrackJobs": 0
        },
        {
          "timePeriod": "201806010000",
          "activities": 23467,
          "searchRequests30Day": 0,
          "searchRequestsFullArchive": 66,
          "historicalPowertrackDays": 0,
          "historicalPowertrackJobs": 0
        },
        {
          "timePeriod": "201807010000",
          "activities": 431,
          "searchRequests30Day": 11,
          "searchRequestsFullArchive": 4,
          "historicalPowertrackDays": 0,
          "historicalPowertrackJobs": 0
        }
      ],
      "projected": {
        "timePeriod": "201807010000",
        "activities": 803,
        "searchRequests30Day": 20,
        "searchRequestsFullArchive": 7,
        "historicalPowertrackDays": 0,
        "historicalPowertrackJobs": 0
      },
      "products": [
        {
          "type": "Historical PowerTrack Subscription",
          "used": [
            {
              "timePeriod": "201805010000",
              "activities": 0,
              "days": 0,
              "jobs": 0
            },
            {
              "timePeriod": "201806010000",
              "activities": 0,
              "days": 0,
              "jobs": 0
            },
            {
              "timePeriod": "201807010000",
              "activities": 0,
              "days": 0,
              "jobs": 0
            }
          ],
          "projected": {
            "timePeriod": "201807010000",
            "activities": 0,
            "days": 0,
            "jobs": 0
          }
        },
        {
          "type": "PowerTrack",
          "used": [
            {
              "timePeriod": "201805010000",
              "activities": 267
            },
            {
              "timePeriod": "201806010000",
              "activities": 3
            },
            {
              "timePeriod": "201807010000",
              "activities": 32
            }
          ],
          "projected": {
            "timePeriod": "201807010000",
            "activities": 59
          },
          "endpoints": [
            {
              "type": "PowerTrack 2.0",
              "label": "actformat",
              "used": [
                {
                  "timePeriod": "201805010000",
                  "activities": 0
                },
                {
                  "timePeriod": "201806010000",
                  "activities": 0
                },
                {
                  "timePeriod": "201807010000",
                  "activities": 0
                }
              ],
              "projected": {
                "timePeriod": "201807010000",
                "activities": 0
              }
            },
              {
              "type": "PowerTrack Replay 2.0",
              "label": "ogformat",
              "used": [
                {
                  "timePeriod": "201805010000",
                  "activities": 0
                },
                {
                  "timePeriod": "201806010000",
                  "activities": 0
                },
                {
                  "timePeriod": "201807010000",
                  "activities": 0
                }
              ],
              "projected": {
                "timePeriod": "201807010000",
                "activities": 0
              }
            }
          ]
        },
        {
          "type": "Search API (30-Day) 2.0",
          "used": [
            {
              "timePeriod": "201805010000",
              "activities": 10,
              "searchRequests30Day": 3
            },
            {
              "timePeriod": "201806010000",
              "activities": 0,
              "searchRequests30Day": 0
            },
            {
              "timePeriod": "201807010000",
              "activities": 23,
              "searchRequests30Day": 11
            }
          ],
          "projected": {
            "timePeriod": "201807010000",
            "activities": 42,
            "searchRequests30Day": 20
          },
          "endpoints": [
            {
              "type": "Search API (30-Day) 2.0",
              "label": "ogformat",
              "used": [
                {
                  "timePeriod": "201805010000",
                  "activities": 10,
                  "searchRequests30Day": 3
                },
                {
                  "timePeriod": "201806010000",
                  "activities": 0,
                  "searchRequests30Day": 0
                },
                {
                  "timePeriod": "201807010000",
                  "activities": 21,
                  "searchRequests30Day": 10
                }
              ],
              "projected": {
                "timePeriod": "201807010000",
                "activities": 39,
                "searchRequests30Day": 18
              }
            }
          ]
        },
        {
          "type": "Search API (Full-Archive)",
          "used": [
            {
              "timePeriod": "201805010000",
              "activities": 961,
              "searchRequestsFullArchive": 19
            },
            {
              "timePeriod": "201806010000",
              "activities": 23466,
              "searchRequestsFullArchive": 66
            },
            {
              "timePeriod": "201807010000",
              "activities": 379,
              "searchRequestsFullArchive": 4
            }
          ],
          "projected": {
            "timePeriod": "201807010000",
            "activities": 706,
            "searchRequestsFullArchive": 7
          },
          "endpoints": [
            {
              "type": "Search API (Full-Archive)",
              "label": "actformat",
              "used": [
                {
                  "timePeriod": "201805010000",
                  "activities": 1,
                  "searchRequestsFullArchive": 3
                },
                {
                  "timePeriod": "201806010000",
                  "activities": 0,
                  "searchRequestsFullArchive": 0
                },
                {
                  "timePeriod": "201807010000",
                  "activities": 2,
                  "searchRequestsFullArchive": 1
                }
              ],
              "projected": {
                "timePeriod": "201807010000",
                "activities": 3,
                "searchRequestsFullArchive": 1
              }
            },
            {
              "type": "Search API (Full-Archive)",
              "label": "ogformat",
              "used": [
                {
                  "timePeriod": "201805010000",
                  "activities": 961,
                  "searchRequestsFullArchive": 16
                },
                {
                  "timePeriod": "201806010000",
                  "activities": 23466,
                  "searchRequestsFullArchive": 66
                },
                {
                  "timePeriod": "201807010000",
                  "activities": 379,
                  "searchRequestsFullArchive": 3
                }
              ],
              "projected": {
                "timePeriod": "201807010000",
                "activities": 706,
                "searchRequestsFullArchive": 5
              }
            }
          ]
        }
      ]
    }
  ],
  "bucket": "month",
  "fromDate": "201805010000",
  "toDate": "201808010000"
}
```

Sample Payload
--------------

Below is a sample of the payload:

```
      {
  "account": {
    "name": "gnip-username"
  },
  "bucket": "month",
  "publishers": [
    {
      "type": "automattic",
      "used": [
        {
          "activities": 0,
          "timePeriod": "201603010000"
        }
      ],
      "projected": {
        "activities": 0,
        "timePeriod": "201603010000"
      },
      "products": [
        {
          "type": "PowerTrack",
          "used": [
            {
              "timePeriod": "201603010000",
              "activities": 0
            }
          ],
          "projected": {
            "timePeriod": "201603010000",
            "activities": 0
          },
          "endpoints": [
            {
              "type": "PowerTrack",
              "label": "dev",
              "used": [
                {
                  "timePeriod": "201603010000",
                  "activities": 0
                }
              ],
              "projected": {
                "timePeriod": "201603010000",
                "activities": 0
              }
            }
          ]
        }
      ]
    },
    {
      "type": "twitter",
      "used": [
        {
          "activities": 84,
          "searchRequests30Day": 4,
          "searchRequestsFullArchive": 0,
          "historicalPowertrackDays": 0,
          "historicalPowertrackJobs": 0,
          "timePeriod": "201603010000"
        }
      ],
      "projected": {
        "activities": 0,
        "searchRequests30Day": 0,
        "searchRequestsFullArchive": 0,
        "historicalPowertrackDays": 0,
        "historicalPowertrackJobs": 0,
        "timePeriod": "201601010000"
      },
      "products": [
        {
          "type": "Historical PowerTrack 2.0",
          "used": [
            {
              "timePeriod": "201511010000",
              "activities": 11884,
              "days": 5,
              "jobs": 5
            },
            {
              "timePeriod": "201512010000",
              "activities": 0,
              "days": 0,
              "jobs": 0
            },
            {
              "timePeriod": "201601010000",
              "activities": 0,
              "days": 0,
              "jobs": 0
            }
          ]
        },
        {
          "type": "PowerTrack",
          "used": [
            {
              "timePeriod": "201511010000",
              "activities": 0
            },
            {
              "timePeriod": "201512010000",
              "activities": 27456
            },
            {
              "timePeriod": "201601010000",
              "activities": 0
            }
          ],
          "projected": {
            "timePeriod": "201601010000",
            "activities": 0
          },
          "endpoints": [
            {
              "type": "PowerTrack",
              "label": "devel",
              "used": [
                {
                  "timePeriod": "201511010000",
                  "activities": 0
                },
                {
                  "timePeriod": "201512010000",
                  "activities": 2930
                },
                {
                  "timePeriod": "201601010000",
                  "activities": 0
                }
              ],
              "projected": {
                "timePeriod": "201601010000",
                "activities": 0
              }
            },
            {
              "type": "PowerTrack 2.0",
              "label": "devel-v2",
              "used": [
                {
                  "timePeriod": "201511010000",
                  "activities": 0
                },
                {
                  "timePeriod": "201512010000",
                  "activities": 24542
                },
                {
                  "timePeriod": "201601010000",
                  "activities": 0
                }
              ],
              "projected": {
                "timePeriod": "201601010000",
                "activities": 0
              }
            },
            {
              "type": "PowerTrack 2.0",
              "label": "devel-v2-1",
              "used": [
                {
                  "timePeriod": "201511010000",
                  "activities": 0
                },
                {
                  "timePeriod": "201512010000",
                  "activities": 0
                },
                {
                  "timePeriod": "201601010000",
                  "activities": 0
                }
              ],
              "projected": {
                "timePeriod": "201601010000",
                "activities": 0
              }
            }
          ]
        },
        {
          "type": "Search API",
          "used": [
            {
              "timePeriod": "201511010000",
              "activities": 0,
              "searchRequests30Day": 0
            },
            {
              "timePeriod": "201512010000",
              "activities": 0,
              "searchRequests30Day": 0
            },
            {
              "timePeriod": "201601010000",
              "activities": 0,
              "searchRequests30Day": 0
            }
          ],
          "projected": {
            "timePeriod": "201601010000",
            "activities": 0,
            "searchRequests30Day": 0
          },
          "endpoints": [
            {
              "type": "Search API",
              "label": "devel",
              "used": [
                {
                  "timePeriod": "201511010000",
                  "activities": 0,
                  "searchRequests30Day": 0
                },
                {
                  "timePeriod": "201512010000",
                  "activities": 0,
                  "searchRequests30Day": 0
                },
                {
                  "timePeriod": "201601010000",
                  "activities": 0,
                  "searchRequests30Day": 0
                }
              ],
              "projected": {
                "timePeriod": "201601010000",
                "activities": 0,
                "searchRequests30Day": 0
              }
            }
          ]
        },
        {
          "type": "Search API (30-Day)",
          "used": [
            {
              "timePeriod": "201511010000",
              "activities": 0,
              "searchRequests30Day": 0
            },
            {
              "timePeriod": "201512010000",
              "activities": 0,
              "searchRequests30Day": 0
            },
            {
              "timePeriod": "201601010000",
              "activities": 0,
              "searchRequests30Day": 0
            }
          ],
          "projected": {
            "timePeriod": "201601010000",
            "activities": 0,
            "searchRequests30Day": 0
          },
          "endpoints": [
            {
              "type": "Search API (30-Day)",
              "label": "devel",
              "used": [
                {
                  "timePeriod": "201511010000",
                  "activities": 0,
                  "searchRequests30Day": 0
                },
                {
                  "timePeriod": "201512010000",
                  "activities": 0,
                  "searchRequests30Day": 0
                },
                {
                  "timePeriod": "201601010000",
                  "activities": 0,
                  "searchRequests30Day": 0
                }
              ],
              "projected": {
                "timePeriod": "201601010000",
                "activities": 0,
                "searchRequests30Day": 0
              }
            }
          ]
        },
        {
          "type": "Search API (Full-Archive)",
          "used": [
            {
              "timePeriod": "201511010000",
              "activities": 0,
              "searchRequestsFullArchive": 0
            },
            {
              "timePeriod": "201512010000",
              "activities": 0,
              "searchRequestsFullArchive": 0
            },
            {
              "timePeriod": "201601010000",
              "activities": 0,
              "searchRequestsFullArchive": 0
            }
          ],
          "projected": {
            "timePeriod": "201601010000",
            "activities": 0,
            "searchRequestsFullArchive": 0
          },
          "endpoints": [
            {
              "type": "Search API (Full-Archive)",
              "label": "devel",
              "used": [
                {
                  "timePeriod": "201511010000",
                  "activities": 0,
                  "searchRequestsFullArchive": 0
                },
                {
                  "timePeriod": "201512010000",
                  "activities": 0,
                  "searchRequestsFullArchive": 0
                },
                {
                  "timePeriod": "201601010000",
                  "activities": 0,
                  "searchRequestsFullArchive": 0
                }
              ],
              "projected": {
                "timePeriod": "201601010000",
                "activities": 0,
                "searchRequestsFullArchive": 0
              }
            }
          ]
        }
      ]
    }
  ]
}
```

Developer policy and terms

Follow @XDevelopers

Subscribe to developer news

#### 
 X platform

* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app

#### 
 X Corp.

* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors

#### 
 Help

* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us

#### 
 Developer resources

* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms

#### 
 Business resources

* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy

 © 2024 X Corp.

Cookies

Privacy

Terms and conditions

**Did someone say … cookies?**  

 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.

* Accept all cookies
* Refuse non-essential cookies