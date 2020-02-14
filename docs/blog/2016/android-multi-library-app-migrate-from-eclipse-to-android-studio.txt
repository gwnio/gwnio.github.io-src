Title: Android (multi library) App Migrate from Eclipse to Android Studio
date: 2016-06-05 09:48:23 -0400
Tags: android, eclipse, android studio, intellij

The following is an explanation of taking a android app project developed in Eclipse that contains multiple library dependencies and migrating the project to Android Studio.  The below table list the projects and dependencies.

<!-- PELICAN_END_SUMMARY -->

<div class="article_content_table0" markdown=1>
Project | Project Type | Dependency
--- | :---: | :---:
CarPartsLib | Library |
EngineLib | Library | CarPartsLib
BodyLib | Library | CarPartsLib, EngineLib
CarApp | Application | CarPartsLib, EngineLib, BodyLib
</div>

## Import CarPartsLib library project

* Import (under Other Import Options I unchecked 'Create Gradle-style...)
* If module name is app rename module to CarPartsLibModule
* Update ```settings.gradle``` ```include 'CarPartsLibModule'```
* Update module ```build.gradle```

[gist:id=535b9fd5bbb5ba2741a075772e9b985a]

* Update project ```build.gradle``` - Comment out or remove dependencies

## Import EngineLib library project

* Import (under Other Import Options I unchecked ```Create Gradle-style...```)
* File -> Project Structure... -> Select CarPartsLib and delete
* With the project structure view selected, right-click CarPartsLib folder and choose ```Delete...```
* Rename *app* module to EngineLibModule
* Update settings.gradle

[gist:id=9e0965cbc063aff34f544425e639d274]

* Update project build.gradle - Under allprojects add ```buildDir = "E:/temp/${rootProject.name}/${project.name}"``` - this prevents from getting the file name too long on Windows error
* Update module ```build.gradle```

[gist:id=57b74842d174479e6e206af92d5f87da]

## Import BodyLib library project

* Import (under Other Import Options I unchecked ```Create Gradle-style...```)
* File -> Project Structure... -> Select CarPartsLib and delete, select EngineLib and delete
* With the project structure view selected, select CarPartsLib and EngineLib then right-click choose ```Delete...```
* Rename *app* module to BodyLibModule
* Update ```settings.gradle```

[gist:id=9fa9dc3615721139b05af78e509bb265]

* Update project build.gradle - Under allprojects add ```buildDir = "E:/temp/${rootProject.name}/${project.name}"``` - this prevents from getting the file name too long on Windows error
* Update module ```build.gradle```

[gist:id=df5daf4063edc1c697b9459c3f0c4ac3]

## Import CarApp application project

* Import (under Other Import Options I unchecked ```Create Gradle-style...```)
* File -> Project Structure... -> Select CarPartsLib and delete, select EngineLib and delete, select BodyLib and delete
* With the project structure view selected, select CarPartsLib, EngineLib, and BodyLib then right-click choose ```Delete...```
* Update ```settings.gradle```

[gist:id=dcaad67d1e5ff28b68a298edd2a08492]

* Update project ```build.gradle```

[gist:id=20393136d1fe6086c8d253bdb081ab22]

* Add ```gradle.properties``` to project root for gradle optimization

[gist:id=1e5fcb45b3114596eca91f0fa1d2da64]

* Update module ```build.gradle```

[gist:id=91ba79f121ec8a17c81f38d8db3622c6]