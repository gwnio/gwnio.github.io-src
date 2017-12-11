Title: JBoss4 Quartz 2.2x Setup
Date: 2015-12-18 11:10:23 -0400
Summary: This explains how to setup Quartz scheduler with JBoss4.
Tags: tech, howto, jboss, quartz

## Step 1

quartz-2.2.1-distribution.zip\quartz-2.2.1\lib

Place the jar files in your project under WEB-INF/lib.  Make sure the same jar files but with different versioning does not already exist.

## Step 2

Remove quartz jar files that came with jboss to avoid version conflict on server startup

	* JBOSS_HOME\server\default\deploy\quartz-ra.rar
	* JBOSS_HOME\server\default\lib\quartz.jar

## Step 3

quartz.properties

I placed mine in JBOSS_HOME\bin\conf.  The documentation also specifies you can place it under WEB-INF.

[gist:id=9f08014e03d372d30ff533ff76c34c33]

## Step 4

Under {QUARTZ Root}\docs\dbTables they provide the table creation scripts for several databases.  Go ahead and create the tables for your database.

## Step 5

I initialized the scheduler within a [servlet container](http://quartz-scheduler.org/documentation/quartz-2.2.x/cookbook/ServletInitScheduler){:target="_blank"}

## Step 6

Do you need to use hibernate in your implementation of org.quartz.Job?

If so then start a transaction.

<div class="wordwrap" markdown=1>
```
HibernateSessionFactory.getSessionFactory().getCurrentSession().beginTransaction();
```
</div>

## Step 7

Remember to handle misfires

According to Quartz documentation "A misfire occurs if a persistent trigger "misses" its firing time because of the scheduler being shutdown (in our case maybe a server restart), or because there are no available threads in Quartz's thread pool for executing the job."

I've set the misfire instruction to fire now so when the scheduler is restarted or a thread becomes available the trigger should immediately fire.

[Triggers](http://quartz-scheduler.org/documentation/quartz-2.x/tutorials/tutorial-lesson-04){:target="_blank"}