Title: How To Style a Markdown Table in Pelican
date: 2017-11-17 09:48:23 -0400
Summary: This explains how to style a markdown table in the static site generator pelican.
Tags: tech, howto, pelican, markdown, css

In your style sheet define a custom class that styles a HTML table.

[gist:id=70eb1c973aca53a594e39c35a10fd320]

Then in your markdown file wrap the table syntax with a HTML div tag that includes your custom css class.

[gist:id=c66cc4e9fac6ee0658372e8d8a6842d4]

Here is a example...

<div class="article_content_table0" markdown=1>
Header 1 | | Footer
---|---|---
Row 1 | |
 | Row 2 |
 | | Row 3
</div>

Booyah!