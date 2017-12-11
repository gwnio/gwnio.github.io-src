Title: Xcode upgrade to 7.2.1
date: 2016-06-03 09:48:23 -0400
Tags: tech, howto, ios, xcode

I upgrade Xcode to 7.2.1 which also required a OS update to OS X Yosemite (10.10.5).  When building and running against a software version of 8.2 or less, the app runs fine.  As soon as I switch simulator versions to 9.2 I encountered a couple of problems.  Below is a short writeup on how I resolved my issues.

<!-- PELICAN_END_SUMMARY -->

## Issue 1

[gist:id=f2d422a658c76236d19ccc6444b8dbf1]

For our dev and production environments we always run through https so I went ahead and adjusted my project .plist file to include the following property:

[gist:id=f2e65402943a622cb14d0a9bce32be5a]

## Issue 2

[I found the following post very helpful for the libraries issue.](https://forums.developer.apple.com/message/8609#8609){:target="_blank"}

> As all wonderful iOS and OS X developers have found in Xcode 7, dynamic libraries are no longer xx.dylib. They are now xx.tbd. According to an Apple staff member, the .tbd files are new "text-based stub libraries", that provide a much more compact version of the stub libraries for use in the SDK, and help to significantly reduce its download size. My best assumption is that this is part of the "App Thinning" and how they are able to reduce iOS 9 and OS X by so much.

If Xcode is not able to find a referenced file/library/etc in the Project Navigator, then the text will be highlighted red.  In my case I had some .dylib files that could not be found.  So I replaced the .dylib with the corresponding .tdb.

Now on the 9.2 simulator the app runs without a problem but as soon as I attempt to deploy the app to a physical device I begin running into library issues.

[gist:id=4b1839f1c38f1f1109252d9fb979f7bb]

I had a project and also a dependency sub project that were referencing the following:

* libc++.dylib
* libicucore.dylib
* libz.dylib

In the subproject Targets -> Build Phases under 'Link Binary With Libraries' I went ahead and deleted these 3 dynamic libraries.
Then in Targets -> Build Settings under 'Other Linker Flags' I added:

* -lc++
* -lz
* -licucore

In the primary project under 'Frameworks' I removed the following dynamic libraries.  This automatically removes them from 'Link Binary With Libraries':

* libz.tbd
* libicucore.tbd
* libc++.tbd

Then in Targets -> Build Settings under 'Other Linker Flags' I added...

* -lc++
* -lz
* -licucore

## Issue 3
I tried to run the app again on the device a received the following error

[gist:id=d4ec302d4b5aa25f620fb49aa6f2850f]

Under Targets -> Build Settings I had to change the 'Enable Bitcode' option to no.

This now enabled me to build and run on the iOS device.  Also regression run of the app on older version in the simulator seem to work.

I should also mention that Xcode version 7.3.1 was available at the time but it did require a OS update to El Capitan (10.11).  Because Apple indicated several times in the 7.x builds they would fix the above issue I went ahead and tried the link option.