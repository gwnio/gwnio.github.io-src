Title: Wildfly Quartz 2.2x Setup
Date: 2016-12-15 11:10:23 -0400
Summary: This explains how to setup Quartz scheduler with Wildfly.
Tags: wildfly, quartz

## Step 1

Download ```quartz-2.2.3``` and extract using 7-zip

## Step 2

Dependencies

For slf4j quartz depends on ```slf4j-api-1.7.7.jar``` and ```slf4j-log4j12-1.7.7.jar```.
Wildfly does contain the slf4j module ```{wildfly home}\modules\system\layers\base\org\slf4j```.
In my version of wildfly it was ```1.7.7.jbossorg-1``` so I went with this.  To do so I updated the deployment dependencies in ```WebRoot/WEB-INF/jboss-deployment-structure.xml``` to include ```<module name="org.slf4j" />```

The documentation mentions "If you want to store your scheduling data in a database then you will also need the c3p0 library." so I went ahead and included the version that came with quartz.

And then of cource the quartz jars: ```quartz-2.2.3.jar``` and ```quartz-jobs-2.2.3.jar```

## Step 3

```quartz.properties```

I placed mine in ```WILDFLY_HOME\bin\conf```.  The documentation also specifies you can place it under ```WEB-INF```.

[gist:id=b6028016e9f55c67bbc2984019cbcc54]

Note: You can find the jndi name of your datasource under the datasources tag in your Wildfly ```standalone.xml```.
Note: If you have multiple wildfly instances running, [Quartz can be configured for clustering](http://www.quartz-scheduler.org/documentation/quartz-2.2.x/configuration/ConfigJDBCJobStoreClustering.html){:target="_blank"}.

## Step 4

Under ```{QUARTZ Root}\docs\dbTables``` they provide the table creation scripts for several databases.  Go ahead and create the tables for your database.

## Step 5

I initialized the scheduler within a [servlet container](http://quartz-scheduler.org/documentation/quartz-2.2.x/cookbook/ServletInitScheduler){:target="_blank"}

## Step 6

You can get access to ```org.quartz.impl.StdSchedulerFactory``` as a attribute in ```javax.servlet.GenericServlet#getServletContext()```

```StdSchedulerFactory factory = (StdSchedulerFactory) getServletContext().getAttribute(QuartzInitializerServlet.QUARTZ_FACTORY_KEY);```