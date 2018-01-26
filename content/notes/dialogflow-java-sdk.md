Title: Dialogflow Java SDK
date: 2018-01-25 09:48:23 -0400
Tags: dialogflow

Download the [java source code](https://github.com/dialogflow/dialogflow-java-client){:target="_blank"} into ```{source root}```.
<!-- PELICAN_END_SUMMARY -->

On Windows, open a command line window and set the ```JAVA_HOME``` environment variable if need be i.e. ```set JAVA_HOME="C:\dev\Java\jdk1.8.0_77"```.  Change directories to the ```{source root}``` folder and package the source via the maven command, ```mvn -X package```.

Include the following jar files in the project class path in order to create a Dialogflow webhook.  ```{source root}\libai\target\libai.jar``` and ```{source root}\web\servlet\target\libai-web-servlet-X.X.X.jar```.