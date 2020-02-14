Title: AngularJS Starter Project Bootstrap
date: 2018-01-17 09:48:23 -0400
Tags: rg-archetype-j2ee-angularjs, angularjs, requirejs

I created a project on github called [rg-archetype-j2ee-angularjs](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs){:target="_blank"}.  The following is a explanation about how this AngularJS app starts up.  This starter project is essentially two single page applications, one for portions of the sight that do not require login credentials (i.e. public) and the remainder for parts that does require a login (i.e. secure).  In this project, there are three main components to the AngularJS application loading: the entry point, boot file and main module file. 
<!-- PELICAN_END_SUMMARY -->

## Entry point [```index-app-public.jsp```](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/index-app-public.jsp){:target="_blank"}

This file contains the root element on which the application will be "bound", ```<div ui-view>```, and a reference to the javascript boot file, ```boot-public.js```.

## Boot file [```boot-public.js```](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/assets/js/boot-public.js){:target="_blank"}

The boot file uses [requirejs](http://requirejs.org){:target="_blank"} to perform all the dependency resolving and loading, which is triggered by a call to ```require()```.

## Main module [```app-public.js```](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/app/app-public.js){:target="_blank"}

The main module file contains the angular code to build the main module and submodules and then bootstrap, or start, the application by invoking [```angular.bootstrap()```](https://docs.angularjs.org/api/ng/function/angular.bootstrap){:target="_blank"}.

Follow other writings on this project [here](tag/rg-archetype-j2ee-angularjs).