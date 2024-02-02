<div>

The status of the LiveVideo.

A ` LIVE_NOW ` LiveVideo is one that will be published to the intended
destination (Timeline, Group, Page, etc) upon receiving valid video
data, or one that is already published and actively streaming.

An ` UNPUBLISHED ` LiveVideo is in preparation; it\'s not visible to
other users, and it may be automatically deleted after several hours in
this state.

A ` SCHEDULED_UNPUBLISHED ` LiveVideo is scheduled to go live at a
future time.

A ` SCHEDULED_LIVE ` LiveVideo is one whose scheduled time has passed,
yet the stream is not yet live. Either in the process of transitioning,
or still waiting for a valid video stream.

(Consider using the ` SCHEDULED ` states to create a planned, future
LiveVideo.)

</div>
