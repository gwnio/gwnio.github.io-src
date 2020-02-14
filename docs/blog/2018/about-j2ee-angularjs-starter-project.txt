Title: About J2EE AngularJS Starter Project
date: 2018-01-13 09:48:23 -0400
Tags: rg-archetype-j2ee-angularjs, wildfly, angularjs, ui-router, requirejs, headjs, bootstrap

I created a project on github called [rg-archetype-j2ee-angularjs](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs){:target="_blank"}.  This is a J2EE project with a AngularJS front end that is intended to be a starter kit for someone interested in creating a AngularJS single page application.  This project, out of the box, comes with a fully functional login screen, signup screen and basic dashboard screen.  
<!-- PELICAN_END_SUMMARY -->

Briefly about the application:

* Its based on AngularJS 1.5.8

* It applies bootstrap 3.3.6 styling

* It uses [ui-router 0.3.1](https://github.com/angular-ui/ui-router){:target="_blank"}

* All vendor related source code used can be found under [WebContent\client\vendor](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/tree/master/WebContent/client/vendor){:target="_blank"}.

* The client side single page app is segregated into two parts: a public app, which contains the login and signup screens, and a secure app, like the dashboard screen.

* It uses [requirejs](http://requirejs.org){:target="_blank"}, a modular script loader, and [headjs](http://headjs.com){:target="_blank"}.  For more on requirejs, [see here](/blog/2017/ng-conf-thomas-burleson-angular-and-requirejs-talk-notes.html)

* The app also has pretty url handling; meaning the login screen can be accessed by specifying ```{app context}/login```, the signup screen can be accessed through the address ```{app context}/signup``` and the app via ```{app context}/app```.  This is possible through a OSS called [rewrite](http://www.ocpsoft.org/rewrite){:target="_blank}.

* It also [utilizes](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/tree/master/WebContent/client/build){:target="_blank"} [Grunt](https://gruntjs.com/){:target="_blank"} to build a production ready distributable app.

Follow other writings on this project [here](/tag/rg-archetype-j2ee-angularjs).