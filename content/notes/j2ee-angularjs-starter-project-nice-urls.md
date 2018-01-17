Title: J2EE AngularJS Nice Urls
date: 2018-01-14 09:48:23 -0400
Tags: rg-archetype-j2ee-angularjs, angularjs, ui-router, rewrite

I created a project on github called [rg-archetype-j2ee-angularjs](https://github.com/gwnio/rg-archetype-j2ee-angularjs){:target="_blank"}.  This project can be thought of as being two single page applications, a public domain module (i.e. login, signup, forget password screens, etc.) and a secure domain module containing functionality requiring login credentials.  I did this for faster loading of the login and signup screens, hopefully making for a slightly better user experience.  Also logically, I just like to think of this app as two single page applications.  This can easily be converted to one single page application if desired.  Each main domain module has their own index page, one for [public](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/index-app-public.jsp){:target="_blank"} and another for [secure](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/index-app-secure.jsp){:target="_blank"}.

Because this project's index pages are jsps, the context path from the ```javax.servlet.http.HttpServletRequest``` object is used to set the [```<base href=".../">```](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/index-app-public.jsp#L6){:target="_blank} for relative links:

[gist:id=7ad8a23a0b394e312e70ad619710d0f4]

Each of these applications uses [HTML5 mode](https://docs.angularjs.org/guide/$location#html5-mode){:target="_blank"}.  Note that this application does not handle HTML5 fallback mode, hashbang mode.  Each of the single page application's main modules are configured to use HTML5 mode, here is the [public module](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/app/app-public.js#L13){:target="_blank"} with the configuration and here is the [secure module](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/app/app-secure.js#L13){:target="_blank"}:

[gist:id=2a8cc7761ae041940b5c609665bee22d]

In order to perform [server-side url rewriting](https://docs.angularjs.org/guide/$location#server-side){:target="_blank"}, I used a open source url rewriting micro libary called [rewrite](https://www.ocpsoft.org/rewrite){:target="_blank"}.  When thinking of rewrite versus redirect, a rewrite happens on the server so that the client browser is never aware.  Whereas a redirect is a response from the server to the client, the client's url is updated and then another request is made for the new url.  The instructions on how to include rewrite in your project is simple, but below is this project's implementation of the [rewrite configuration provider](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/master/src/org/rg/archetype/web/UrlRewriteConfigurationProvider.java){:target="_blank"}.  Notice how urls not requiring login credentials get forwarded to the angular public entry point and the urls requiring login get forwarded to the secure entry point:

[gist:id=e844781ce8987d43f588df40faa229d4]

Lastly, this project uses [ui-router](https://github.com/angular-ui/ui-router){:target="_blank"} so here is the public single page app's [route configuration](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/app/public/MainModule.js#L29){:target="_blank"}:

[gist:id=dcfc29df2bc4bd7293934c9db9a09f4b]


 