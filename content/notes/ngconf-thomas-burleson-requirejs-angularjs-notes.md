Title: Ng-conf Thomas Burleson Angular and RequireJS Talk Notes
Date: 2017-06-14 11:10:23 -0400
Tags: angularjs, requirejs, grunt

## Intro

<!-- PELICAN_BEGIN_SUMMARY -->
The following are notes I have taking from a talk that Thomas Burleson gave at ng-conf in 2014.
<!-- PELICAN_END_SUMMARY -->
The talk can be found [here](https://www.youtube.com/watch?v=4yulGISBF8w){:target="_blank"} and was very helpful with my angularjs project.  I did not attend this conference, rather I found this resource on Youtube.

In the below notes, I have also added links to examples in a [J2EE AngularJS starter project](https://github.com/gwnio/rg-archetype-j2ee-angularjs){:target="_blank"} I created which implements some of the concepts the speaker discusses.

### Is RequireJS needed in your Angular project? [2:17](https://www.youtube.com/watch?v=4yulGISBF8w#t=02m17s){:target="_blank"}

#### Option 1

Load code in one js file, this is ok for simple applications.

```angular.module().config().service().controller()```

#### Option 2

Organize by packages, manually load the dependencies via imports.  You have to remember the dependencies and get the order of loading right.  This is very difficult for large projects and does not scale well.

```<script src='...\sourceFile.js></script>```

### Need: package dependency manager

Manages which classes need to be loaded in what order.

### Dependency Types [4:18](https://www.youtube.com/watch?v=4yulGISBF8w#t=04m18s){:target="_blank"}

* load - which classes need to be loaded in what order
* construction - the arguments needed to instantiate classes
* runtime - functions and utilities needed post instantiation
* module (angular specific) - which modules depend on other modules

### RequireJS Features [5:04](https://www.youtube.com/watch?v=4yulGISBF8w#t=05m04s){:target="_blank"}

* package dependency manager
* class injector (not to be confused with Angular instance injection)
* js file loader
    * lazy loader of files or classes
* concatenator / uglifies

### RequireJS vs Angular [5:10](https://www.youtube.com/watch?v=4yulGISBF8w#t=05m10s){:target="_blank"}

<div class="article_content_table0" markdown=1>
Framework | Manages
--- | ---
RequireJS | load and runtime dependencies
Angular | construction and module dependencies
</div>

### RequireJS Apis [5:28](https://www.youtube.com/watch?v=4yulGISBF8w#t=05m28s){:target="_blank"}

#### **define()**

* Allows you to define factory function that gets called when your dependencies are resolved.  [See here for example](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/app/public/MainModule.js#L1){:target="_blank"}.
* Create [AMD definition](https://github.com/amdjs/amdjs-api/wiki/AMD){:target="_blank"} - allows you to load your js files in any order, but dependencies defined what triggers get pulled.
* Ready handlers
    * Called when dependencies resolve, if no dependencies are defined then the ready handler is called immediately i.e. define([], function(){})
    * Returns values stored by filename or id
    * Values are injected into ready handlers of other AMD definitions (or dependencies)
* Every file wrapped with a define()
* Every define returns a value (function, class, or instance)
* Id in the cached registry is the file name
* Builds tree of dependencies and when the handlers fire it creates a flat registry of values stored by dependency ids
    * Values are usually references to classes or functions
* BUT nothing happens until at least one call to require().  [See here for example](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/assets/js/boot-public.js#L47){:target="_blank"}.

[gist:id=80edf1a206609494a7d7befd7bece55c]

#### **require()**

* You can register a callback function that is invoked when all your dependencies have resolved.  [See here for example](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/assets/js/boot-public.js#L47){:target="_blank"}.
* Starts the cascading of triggering because the main class has other dependencies
    * cascade of define() triggers

[gist:id=8fe285cd5ba07a0d866058a9990254e6]

#### **conifg()**

* Let's you define location to sources and packages and also define aliases.  [See here for example](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/assets/js/boot-public.js#L24){:target="_blank"}.

### Use RequireJS with Angular [11:21](https://www.youtube.com/watch?v=4yulGISBF8w#t=11m21s){:target="_blank"}

* Wrap all your code with define[], this is not tedious because you are defining a contract of imports that that class requires, or dependencies it needs
    * Think of import statements in Java
* Use require() to launch code to initialize Angular app.  [See here for example](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/62336a6e6a6c4f8e234f6e52e8c07da315dc8c25/WebContent/client/src/assets/js/boot-public.js#L47){:target="_blank"}.
* **REMEMBER** RequireJS injects functions or classes, Angular injects instances of classes
* So RequireJS can define a function that gets used in the body of a Angular function i.e. ViewController.  [See here for another example](https://github.com/gwnio/rg-archetype-j2ee-angularjs/blob/master/WebContent/client/src/app/public/login/LoginController.js){:target="_blank"}.
* The below snippet of code is referred to as a constructor array.

```return ["http", "q", function(http, q) {}]```

### Grunt [14:20](https://www.youtube.com/watch?v=4yulGISBF8w#t=14m20s){:target="_blank"}

* [See here]([utilizes](https://github.com/gwnio/rg-archetype-j2ee-angularjs/tree/master/WebContent/client/build){:target="_blank"} for a example of the starter project's Grunt configuration.