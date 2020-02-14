Title: Hibernate Notes
date: 2017-03-11 09:48:23 -0400
Tags: hibernate

The following are some quotes and notes from taken from Hibernate 5.0 documentation.

<!-- PELICAN_END_SUMMARY -->

## Quotes
<!-- -->
> A SessionFactory is an expensive-to-create, threadsafe object, intended to be shared by all application threads. It is created once, usually on application startup, from a Configuration instance.

<!-- -->
> A Session is an inexpensive, non-threadsafe object that should be used once and then discarded for: a single request, a conversation or a single unit of work. A Session will not obtain a JDBC Connection, or a Datasource, unless it is needed. It will not consume any resources until used.

<!-- -->
> Do not use the session-per-operation antipattern: do not open and close a Session for every simple database call in a single thread.

<!-- -->
> The most common pattern in a multi-user client/server application is session-per-request.

<!-- -->
> In this model, a request from the client is sent to the server, where the Hibernate persistence layer runs. A new Hibernate Session is opened, and all database operations are executed in this unit of work. On completion of the work, and once the response for the client has been prepared, the session is flushed and closed.

<!-- -->
> Starting with version 3.0.1, Hibernate added the SessionFactory.getCurrentSession() method. Initially, this assumed usage of JTA transactions, where the JTA transaction defined both the scope and context of a current session. Given the maturity of the numerous stand-alone JTA TransactionManager implementations, most, if not all, applications should be using JTA transaction management, whether or not they are deployed into a J2EE container. Based on that, the JTA-based contextual sessions are all you need to use.

## Transaction
* unit of work, if onen step fails the whole unit of work must fail (atomicity all operations are executed as an atomic unit)
* keeps data clean and in consistant state by keeping it hidden from other transactions
* sql statements execute inside a transaction

## Programmatic transaction demarcation
* you begin the transaction and commit or rollback
* transaction interfaces
* java.sql.Connection - direct usage of JDBC transactions in hibernate is discouraged b/c it binds your application to JDBC environment
* org.hibernate.Transaction - works in nonmanaged plain JDBC environment and in an application server with JTA (Java Transaction API) as system transaction service
* javax.transaction.UserTransaction - should be primary choice whenever you have JTA-compatible transaction service
* javax.persistence.EntityTransaction - interface for programmatic transaction control in Java SE applications that use Java Persistence

## Declarative transaction demarcation
* you declare when you want to work inside a transaction, then the runtime environment handles this concern
* EJB container provides declarative transaction services in Java; called container-managed transactions (CMT)

## 10.1.2 on
* Programmatic transactions in Java SE
* A hibernate session is lazy, so it won't consume any resources unless they're needed.  A JDBC connection is obtained only when a transaction begins.
* beginTransaction() equivalent to setAutoCommit(false)
* NOTE: starting in Hibernate 3 all exceptions thrown are subtypes of the unchecked RuntimeException, before all exceptions thrown by Hibernate were checked
* All Hibernate exceptions are fatal