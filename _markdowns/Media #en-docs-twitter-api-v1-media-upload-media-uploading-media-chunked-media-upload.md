::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: bl19-no-edit-wrap
::: {.c15-column-container .js-column-container}
::: {.container--mini .container--mobile}
::: {.column .column-6}
::: c01-rich-text-editor
::: is-table-default
Using the [chunked POST
media/upload](/en/docs/media/upload-media/api-reference/post-media-upload-init.html)
endpoints requires an adjusted workflow from single image uploads. For
video or chunked uploads, you must:

-   Initialize the upload using the INIT command
-   Upload each chunk of bytes using the APPEND command
-   Complete the upload using the FINALIZE command

See the [large video upload
sample](https://github.com/twitterdev/large-video-upload-python/) for an
example written in Python.

Below is a working example using the command-line
[twurl](https://github.com/twitter/twurl) utility. To see full headers
of the requests and responses when using twurl, use the -t option to
enable trace mode.

**INIT**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=INIT&media_type=video/mp4&total_bytes=4430752"
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "media_id": 601413451156586496,
  "media_id_string": "601413451156586496",
  "expires_after_secs": 3599
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=APPEND&media_id=601413451156586496&segment_index=0" --file /path/to/video.mp4 --file-field "media"
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
HTTP 2XX will be returned with an empty response body on successful
upload.\

**FINALIZE**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=FINALIZE&media_id=601413451156586496"
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "media_id": 601413451156586496,
  "media_id_string": "601413451156586496",
  "size": 4430752,
  "expires_after_secs": 3600,
  "video": {
    "video_type": "video/mp4"
  }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
