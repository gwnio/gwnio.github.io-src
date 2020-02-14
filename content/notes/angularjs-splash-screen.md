Title: AngularJS Splash Screen
date: 2018-01-17 09:48:23 -0400
Tags: rg-archetype-j2ee-angularjs, angularjs, splash screen

The following is a explanation of how to create a splash screen for a AngularJS client, with references to example code from a [J2EE AngularJS starter project](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs){:target="_blank"} I created.
<!-- PELICAN_END_SUMMARY -->

The first thing I did was to define the html/css content for the splash screen content in the [entry point index page](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/index-app-secure.jsp){:target="_blank"}.

[gist:id=2b51dd400db9a8bbf881324a80b91aca]

This div tag contains the image element referencing the splash image and also contains inline css styling.  This splash display will be the only thing the user sees until the ```<div>``` element is removed.  The div element can be removed when the app is bootstrapped and the module gets built and run.  [See here](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/app/app-secure.js){:target="_blank"} for a example of this.

Notice a couple of things:

* I let the splash screen [display for a couple of seconds](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/app/app-secure.js#L27){:target="_blank"} before bootstrapping the app.  This is certainly optional, but let's the user absorb your nice logo briefly.

* ```function removeSplash()``` removes the splash html element containing the splash content.  This gets invoked when the main module is run ```module.run()``` but [after the initial route state is called](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/app/app-secure.js#L23){:target="_blank"}.

Follow other writings on this project [here](tag/rg-archetype-j2ee-angularjs).