Title: GXT3 window masked behind GXT2 window
Date: 2014-08-29 11:10:23 -0400
Tags: sencha, gxt3, gxt2

<!-- PELICAN_BEGIN_SUMMARY -->
I ran into a little issue at work today and wanted to enter a brief write up on it. One of our web application's user interface is built on Sencha's GXT3 (com.sencha) and GXT2 (com.extjs) frameworks. Our new and improved UI uses GXT3 and we maintained legacy layouts and components (developed using GXT2) to permit a transition period for established users.
<!-- PELICAN_END_SUMMARY -->
As a general rule, we are not adding new features to the legacy UI and really aren't supporting that anymore. However in my case today I just finished developing a feature enhancement which was written in GXT3. This included a new presenter (MVP design pattern) and some new GXT3 components, a window being one of them. Because this new component did everything the component in the old layout did, I was thinking I'd do a little code refactoring and replace the GXT2 components with the new GXT3 components. That way I could remove some old deprecated code and clean up the package structure a little, and users still on the legacy UI would have access to this enhancement. Win, win. Generally when I add a GXT3 component to a GXT2 view I'll perform GWT code splitting to reduce the amount of code needed to be brought down on entry point load. Below is a little snippet.

[gist:id=b1e4ecd44c3e96e471a64c38d044d1e1]

I located the old GXT2 component which happened to be launched from another GXT2 window and plugged in the new GXT3 presenter. I go to test, open the GXT2 window to click a button that would launch my new component and bam...my window stack is messed up. The GXT3 window opens but is masked behind the GXT2 window. To summarize the situation, I'm trying to launch 2 windows from 2 different GXT code environments. My first futile attempt to fix this involved changing the z-index value for both components. After digging around some, I found that both GXT environments have their own z-index management ```XDOM.getTopZIndex()```. So the problem was that these 2 windows don't know anything about each other and thus the window display queue is incorrect. Turns out this is a documented bug by Sencha (EXTGWT-2994) and their fix is to allow the developer to wire the z-index code to a different source. This enables the GXT3 framework z-index to use the GXT2's z-index. Now the ideal solution is to migrate the GXT2 components to GXT3, but that can be a slow process and low priority when you have a lot of irons in the fire.

If you decide to overwrite GXT3's z-index handling, here is a couple of snippets of code I found from a GXT dev team member.

Subclass ```XDOMImpl``` and place in your package somewhere:

[gist:id=a3e9a4b2a04d1970d0a9ff38212e602f]

Then in the ```.gwt.xml``` file, bind this new class to the GXT3 default usage like so:

[gist:id=5f0e17ce03762dde26af843e01123a11]

The ```XDOMImpl``` class is part of Sencha's 3.1 release (release notes) so if you are on a older version of GXT you will need to upgrade. Be aware of any "Breaking" API changes depending on the version you are using.


