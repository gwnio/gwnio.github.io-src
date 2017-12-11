Title: Wildfly JSF Configuration
Date: 2017-06-14 11:10:23 -0400
Tags: tech, howto, wildfly

1. [Intro](#intro)
2. [Installing a new JSF implementation manually](#install_implementation)
3. [Changing the default JSF implementation](#change_default_implementation)
4. [Configuring a JSF app to use a non-default JSF implementation](#configure_non_default_implementation)

### Intro <a name="intro"></a>

<!-- PELICAN_BEGIN_SUMMARY -->
The following is documentation for adding Mojarra or MyFaces JSF implementation as a subsystem in Wildfly 10.
<!-- PELICAN_END_SUMMARY -->
The below is taken verbatim from the [jboss documentation](https://docs.jboss.org/author/display/WFLY10/JSF+Configuration){:target="_blank"} and is authored by Farah Juma.  This person did an incredible job.  The instructions were detailed so well that following it to the script resulted in getting the Apache MyFaces implementation installed as a subsystem in Wildfly without any deviation.  Documentation of that quality is rare so I wanted to have this documentation in case they ever removed this page.

### Installing a new JSF implementation manually <a name="install_implementation"></a>

A new JSF implementation can be manually installed as follows:

#### Add a module slot for the new JSF implementation JAR

Create the following directory structure under the __WILDFLY_HOME/modules__ directory:
<div class="wordwrap" markdown=1>
```
WILDFLY_HOME/modules/com/sun/jsf-impl/<JSF_IMPL_NAME>-<JSF_VERSION>
```
</div>

For example, for Mojarra 2.2.11, the above path would resolve to:
<div class="wordwrap" markdown=1>
```
WILDFLY_HOME/modules/com/sun/jsf-impl/mojarra-2.2.11
```
</div>

Place the JSF implementation JAR in the __`<JSF_IMPL_NAME>`-`<JSF_VERSION>`__ subdirectory. In the same subdirectory, add a module.xml file similar to the Mojarra or MyFaces template examples. Change the resource-root-path to the name of your JSF implementation JAR and fill in appropriate values for ${jsf-impl-name} and ${jsf-version}

#### Add a module slot for the new JSF API JAR

Create the following directory structure under the __WILDFLY_HOME/modules__ directory:
<div class="wordwrap" markdown=1>
```
WILDFLY_HOME/modules/javax/faces/api/<JSF_IMPL_NAME>-<JSF_VERSION>
```
</div>

Place the JSF API JAR in the __`<JSF_IMPL_NAME>`-`<JSF_VERSION>`__ subdirectory. In the same subdirectory, add a module.xml file similar to the Mojarra or MyFaces template examples. Change the resource-root-path to the name of your JSF API JAR and fill in appropriate values for ${jsf-impl-name} and ${jsf-version}.

#### Add a module slot for the JSF injection JAR

Create the following directory structure under the __WILDFLY_HOME/modules__ directory:
<div class="wordwrap" markdown=1>
```
WILDFLY_HOME/modules/org/jboss/as/jsf-injection/<JSF_IMPL_NAME>-<JSF_VERSION>
```
</div>

Copy the wildfly-jsf-injection JAR and the weld-core-jsf JAR from __WILDFLY_HOME/modules/system/layers/base/org/jboss/as/jsf-injection/main__ to the __`<JSF_IMPL_NAME>`-`<JSF_VERSION>`__ subdirectory.

In the __`<JSF_IMPL_NAME>`-`<JSF_VERSION>`__ subdirectory, add a module.xml file similar to the Mojarra or MyFaces template examples and fill in appropriate values for ${jsf-impl-name}, ${jsf-version}, ${version.jboss.as}, and ${version.weld.core}. (These last two placeholders depend on the versions of the wildfly-jsf-injection and weld-core-jsf JARs that were copied over in the previous step.)

#### For MyFaces only - add a module for the commons-digester JAR

Create the following directory structure under the __WILDFLY_HOME/modules__ directory:
<div class="wordwrap" markdown=1>
```
WILDFLY_HOME/modules/org/apache/commons/digester/main
```
</div>

Place the commons-digester JAR in __WILDFLY_HOME/modules/org/apache/commons/digester/main__. In the main subdirectory, add a module.xml file similar to this template. Fill in the appropriate value for ${version.commons-digester}.

#### Start the server

After starting the server, the following CLI command can be used to verify that your new JSF implementation has been installed successfully. The new JSF implementation should appear in the output of this command.

<div class="wordwrap" markdown=1>
```
[standalone@localhost:9990 /] /subsystem=jsf:list-active-jsf-impls()
```
</div>

### Changing the default JSF implementation <a name="change_default_implementation"></a>

The following CLI command can be used to make a newly installed JSF implementation the default JSF implementation used by WildFly:

<div class="wordwrap" markdown=1>
```
/subsystem=jsf/:write-attribute(name=default-jsf-impl-slot,value=`<JSF_IMPL_NAME>`-`<JSF_VERSION>`)
```
</div>

A server restart will be required for this change to take effect.

### Configuring a JSF app to use a non-default JSF implementation <a name="configure_non_default_implementation"></a>

A JSF app can be configured to use an installed JSF implementation that's not the default implementation by adding a org.jboss.jbossfaces.JSF_CONFIG_NAME context parameter to its web.xml file. For example, to indicate that a JSF app should use MyFaces 2.2.12 (assuming MyFaces 2.2.12 has been installed on the server), the following context parameter would need to be added:

[gist:id=a7fb7b89ddf74c131490cd994734a04c]

If a JSF app does not specify this context parameter, the default JSF implementation will be used for that app.