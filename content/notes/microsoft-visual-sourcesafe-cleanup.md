Title: Microsoft Visual SourceSafe cleanup in Windows
date: 2017-11-14 09:48:23 -0400
Tags: tech, microsoft, vss

I was migrating some old source code that was version controlled in Microsoft Visual SourceSafe (or vss) into Subversion.  I wanted to cleanup the files and subfolders in the project root.  By cleanup, I mean get rid of the vss metadata and reset the file permissions.  Vss adds a .scc file and sets all the files to read-only.

<!-- PELICAN_END_SUMMARY -->

Below are a couple of Windows commands, don't forget to change to project root folder:

__Remove microsoft source safe files__

```
del /S *.scc
```
 
__Change all files to not be read-only__

```
attrib -r .\*.* /s
```