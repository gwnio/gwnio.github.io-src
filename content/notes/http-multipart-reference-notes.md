Title: HTTP 'Content-Type' of 'multipart/form-data' Reference Notes
Date: 2015-04-06 11:10:23 -0400
Summary: These are just some basic notes that I took while doing some research on HTTP 'Content-Type' of 'multipart/form-data'.
Tags: tech

* Content type that should be used for submitting forms that contain files, non-ASCII data, and binary data
* 'multipart/form-data' message contains a series of parts, each part represents a control
* Each part sent in the order defined by the application and form as part of the multipart stream
* Each part has a 'Content-Type' defaulting to 'text/plain'
* Each part has a "Content-Disposition" header, with disposition type = "form-data"
* Each part has a control name
* If contents of a file are submitted with a form, "Content-Type" should be included
* If media type is not know then "Content-Type" set to "application/octet-stream"
* If the value of the part does not conform to 7BIT encoding, then set "Content-Transfer-Encoding"
* If multiple files are submitted, the "Content-Type" within the part should be "multipart/mixed"
* The user agent should attempt to include the filename for each submitted file

[gist:id=9d72952f07e4d39fe182bf400c28ea9e]

If the user enters a favorite color of "Red" and submits 2 files of different types, a HTTP example fragment:

[gist:id=f995333bb547c3ec5f7d9f87d9c91092]