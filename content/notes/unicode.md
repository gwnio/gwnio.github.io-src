Title: Character encoding
Subtitle: ASCII, ANSI, Unicode, UTF-8
date: 2017-03-11 09:48:23 -0400
Summary: Just some simple notes on character encodings.
Tags: tech, ascii, ansi, unicode, utf-8

## Table of contents

1. [ASCII](#ascii)
2. [ANSI Standard](#ansi_standard)
3. [Unicode](#unicode)
4. [Encodings](#encodings)
    1. [UTF-8](#utf-8)

### ASCII <a name="ascii"></a>

Represents every character using a number between 32 and 127, 32 is space "A" is 65.  Can be stored in 7 bits.  Old 8 bit computers could store all possible characters.  Codes below 32 called unprintable or control characters i.e. 7 would make computer beep.  B/c 8 bits in byte people began using codes 128 - 255.  PCs in Russia might have a different symbol at character code 120 than a PC sold in Israel.  This led to ANSI standard.

### ANSI Standard <a name="ansi_standard"></a>

Everybody agreed on character code below 128 which was basically ASCII.  From 128 and up was handled differently depending on where you lived and these different systems were called code pages. i.e. Israel DOS used a code page called 862 while Greek users used 737.  In Asia the alphabet had thousands of letters so they had to a system called DBCS "double byte character set".  Some letters were stored in 1 byte and others it took 2.  But still, most people just pretended that a byte was a character and a character was 8 bits and as long as you never moved a string from one computer to another, or spoke more than one language, it would sort of always work.

### Unicode <a name="unicode"></a>

A single character set that includes every reasonable writing system in the world.
* a letter maps to a code point (which is just a concept)
* platonic letter i.e. A is different than B and different from a but the same for different fonts
* every platonic letter is assigned a number by the Unicode consortium called a code point (character map). i.e. the English letter A character map is U+0041.  A hexadecimal number, U means "Unicode".
* "Hello" in Unicode equals U+0048 U+0065 U+006C U+006C U+006F

### Encodings <a name="encodings"></a>

#### UTF-8 <a name="utf-8"></a>

Another system for storing your string of Unicode code points (U+ numbers) in memory using 8 bits.  Code points 0-127 stored in 1 bytes, everything above stored in 2, 3 and up to 6 bytes.

Instead of "Hello" being U+0048 U+0065 U+006C U+006C U+006F its stored as 48 65 6C 6C 6F which is the same as its stored in ASCII and ANSI.  If using accented letters, Greek letters, etc. you will have to use several bytes to store a single code point.

So you have platonic letters represented by Unicode code points, these code points can be encode in any scheme: old school ASCII, old OEM Greek Encoding, Hebrew ANSI Encoding, or several hundred encodings.

A popular encoding for English text is ISO-8859-1 aka Latin-1.

Single most important fact about encodings is it doesn't make sense to have a string without know its encoding.  Plain text doesn't exist.  If you have a string in memory, in a file, or in a email email you have to know its encoding in order to display it correctly to the users.

You need to preserve the encoding a string uses:
So in the email header:

```
Content-Type: text/plain; charset="UTF-8"
```

A html page should have the encoding in the header, the browser reads the meta tag, stops parsing the page, and starts over reinterpreting the page:

```
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
```

Internet Explorer if it doesn't find the content type, tries to guess the encoding based on the frequency bytes appear in typical text in typical encodings of various languages.