Title: Configure Apache to Host Multiple Sites
date: 2018-01-02 09:48:23 -0400
Tags: tech, apache

This provides a brief explanation on how to configure your apache server to host multiple web sites.
<!-- PELICAN_END_SUMMARY -->

First thing I did was under _{apache home}/conf_ I created a custom httpd conf file named my-httpd.conf.  I did this to keep my custom changes separate from Apache's out-of-the-box configuration.  To use this configuration, at the bottom of _{apache home}/conf/httpd.conf_ add the following line _Include conf/my-httpd.conf_.  In this custom configuration, add a virtual host for each domain apache will be serving content for.

So let's say you have the following 2 domains: **www.mypersonalsite.com** and **www.cheapthycable.com**.  Under _{apache home}/htdocs_, create a separate folder for each domain, _{apache home}/htdocs/mypersonalsite.com_ and _{apache home}/htdocs/cheapthycable.com_.  I would recommend doing the same in the logs directory, _{apache home}/logs/mypersonalsite.com_ and _{apache home}/logs/cheapthycable.com_.  Then the _my-httpd.conf_ would look as follows:

[gist:id=d9616fca9447078e426dfb0debb6643d]

Now certainly there are other configuration adjustments that you can make but this a jump start for Apache hosting multiple sites.  One other thing I will add, is what if you are on a Windows environment and you want to test this locally?  First would be to modify your Windows host file located at _C:\Windows\System32\drivers\etc\host_.  Find out what you local machine's ip address is and add a couple of domains like so.

[gist:id=86196a105871cfaf345d2ec0fd9f7063]

Then adjust _my-httpd.conf_ to look as follows:

[gist:id=537f647a12a1d3d5dc31a00404677859]

Restart Apache and test it out.