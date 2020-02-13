Title: AngularJS Grunt Production Build
date: 2018-01-18 09:48:23 -0400
Tags: rg-archetype-j2ee-angularjs, angularjs, grunt

I created a project on github called [rg-archetype-j2ee-angularjs](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs){:target="_blank"}.  This project utilizes Grunt to construct a production ready AngularJS client app, meaning the source code is minimized and obfuscated for faster download and thus better user experience.
<!-- PELICAN_END_SUMMARY -->

To learn more about the Grunt configuration for this project, find the Grunt task ```build-app``` in the [configuration file](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/build/Gruntfile.js){:target="_blank"} and inspect each dependency task.

A couple of things to take note of:

## Entry Point

Each entry point file ([public](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/index-app-public.tpl.jsp){:target="_blank"} and [secure](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/index-app-secure.tpl.jsp){:target="_blank"}) has a template file associated with it.  This was to facilitate generating a development index file, to be used in development mode, and a production index file for production deployments.  [The Grunt configuration](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/build/Gruntfile.js){:target="_blank"} has a ```preprocess``` configuration point, for development and production, to generate the index entry point from the template index entry point.

[gist:id=0dc4c027aeb67bab75de4e44f75d53ee]

## Boot file

Under [```WebContent\client\src\assets\js```](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/tree/master/WebContent/client/src/assets/js){:target="_blank"} are the boot files.  Notice the files prefixed with ```prod-```, these files contain a references to the concatenated and minified application javascript file.  This compressed file contains all vendor and custom developed source code for the application.  Contrast this with the non prefixed boot files for comparison.  When Grunt performs a production build, the ```prod-``` file gets copied into the ```compile``` build folder and then ultimately copied to the ```dist``` folder to where the [index entry point file](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/16d2ea24a5907219828ed04701b124eaa35f9c21/WebContent/client/src/index-app-public.tpl.jsp#L41){:target="_blank"} will be looking for it.  Below is a snippet of the Grunt configuration point that generates the boot file in the ```dist``` location.

[gist:id=e338159094ee4aecfae04dd0fb6bf06d]


## Mode: Development/Production

To toggle between development and production mode, change the environment type value in [```AppServletContextListener```](https://github.com/rossgodwin/rg-archetype-j2ee-angularjs/blob/master/src/org/rg/archetype/web/servlet/AppServletContextListener.java){:target="_blank"}.

Notice the difference in the network traffic for the login page between [development mode]({filename}/images/blog/j2ee-angularjs-starter-project-grunt/development-network.png){:target="_blank"} and [production mode]({filename}/images/blog/j2ee-angularjs-starter-project-grunt/production-network.png){:target="_blank"}.  Keep in mind that in development mode, requirejs is only downloading modules and partial templates as needed.  The download size of the login page in development mode is 498KB.  In production mode, that size is down to 361KB however that size includes the entire single page application so in this case the login page as well as the sign up page.  This is well over a 40% reduction in size.  This can be accounted for by minification performed by the grunt task ```uglify```.  Further notice how in [development mode]({filename}/images/blog/j2ee-angularjs-starter-project-grunt/development-console.png){:target="_blank"} the partial templates are downloaded as they are needed, whereas in [production mode]({filename}/images/blog/j2ee-angularjs-starter-project-grunt/production-console.png){:target="_blank"} there are no partial templates downloaded because they are packaged into javascript code.

## Build
Here are instructions on how to build the release application:

### Step 1

Install [npm](https://docs.npmjs.com/cli/install){:target="_blank"}.

### Step 2

Change to the following directory, ```{project root}\WebContent\client\build``` and execute the following command: ```npm install```.

This will download the dependency modules into ```{project root}\WebContent\client\build\node_modules```, including [Grunt](https://gruntjs.com){:target="_blank"}.

### Step 3

Execute the primary grunt task to create the production ready angularjs application ```grunt build-app```.

This will generate the following folders under ```{project root}\WebContent\client```: ```compile``` and ```dist```.

### Step 4

Execute a clean ```grunt prod-clean``` to remove everything but the release directory ```dist```.

Follow other writings on this project [here](/tag/rg-archetype-j2ee-angularjs).