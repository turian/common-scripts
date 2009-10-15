Update:
    Use --force-output yes in tidy, instead of removing errant tags.


We assume that everything is in UTF-8 encoding.

html2text.pl
    = ./remove-errant-tags.pl | tidy -quiet | html2text -nobs -style pretty  -rcfile html2textrc

Here is a general procedure for converting HTML to text:

    cat foo.html | ./htmldecode.pl | ./remove-errant-tags.pl | tidy -quiet | html2text -nobs -style pretty  -rcfile html2textrc > output.txt

    remove-errant-tags.pl   - Remove instances of <lj-embed ...> and
                    other bizarre tags, which trip up tidy.
                    TODO: Remove this script, instead have tidy just
                    skip bizarre tags.
    htmlencode.pl and htmldecode.pl are part of common-scripts:
        http://github.com/turian/common-scripts/blob/master/htmldecode.pl
        http://github.com/turian/common-scripts/blob/master/htmlencode.pl
    tidy        -   Clean up HTML.
    html2text   -   Final html2text conversion.

We can also prepend:
    ./remove-nonascii-characters.pl     - Remove non-ASCII characters

TODO!
    * Remove ./remove-errant-tags.pl, instead have tidy just remove HTML
    tags its never heard of

REQUIREMENTS:
    * HTML tidy
    * html2text:  http://userpage.fu-berlin.de/~mbayer/tools/html2text.html
    * HTML::Entities perl module
        for htmldecode.pl

==================================================

NOTES ON DEVELOPING THE ABOVE METHODOLOGY

Analysis initially done using tiergroup-13/Aug/14/part-8.xml.gz
and later done using tiergroup-1/Aug/06/part-29.xml.gz

==================================================

Here are some of the different HTML 2 text

Different options:
    lynx -dump
    html2text       -   1.32, http://userpage.fu-berlin.de/~mbayer/tools/html2text.html
    html2text.py    -   http://www.aaronsw.com/2002/html2text/
    pandoc
    tidy

=====

SYMBOL CONVERSION

In first step, want to convert symbols like &lt;
We use unquote.pl, which uses perl's HTML::Entities::decode_entities().
unquote.pl also removes non-ASCI characters.

lynx, and the two h2t options work fine. pandoc and tidy do not do what is desired.
lynx -dump adds some extra indentation.
h2t.py is SLOW

h2t.py is slightly preferable to h2t, insofar as it is slightly more
parsimonious with word-breaking. lynx is also parsimonious.

h2t:
< sub-
< woofer,
---
h2t.py:
> sub-woofer,

h2t
< ABS(4-
< WHEEL),
---
h2t.py
> ABS(4-WHEEL),

All three seem to exhibit problems in splitting links:

original:
&lt;br&gt;
&lt;a
href=&quot;http://s180.photobucket.com/albums/x246/UNITEDAUTO1983/DODGE%202500%20PU%2097/&quot;
rel=&quot;n
ofollow&quot;&gt;http://s180.photobucket.com/albums/x246/UNITEDAUTO1983/DODGE%202500%20PU%2097/&lt;/a&gt;
&lt;br&gt;

h2t:
<br> <br> <br> <a href="http://s180.photobucket.com/
albums/x246/UNITEDAUTO1983/DODGE%202500%20PU%2097/" rel="nofollow">http://
s180.photobucket.com/albums/x246/UNITEDAUTO1983/DODGE%202500%20PU%2097/</a>

h2t.py:
<br> <br> <br> <a href="http://s180.photobucket.com/albums/x246/UNIT
EDAUTO1983/DODGE%202500%20PU%2097/" rel="nofollow">http://s180.photobucket.com
/albums/x246/UNITEDAUTO1983/DODGE%202500%20PU%2097/</a> <br> <br> <br> <br>

lynx:
   <br> <br> <br> <a
   href="http://s180.photobucket.com/albums/x246/UNITEDAUTO1983/DODGE%2025
   00%20PU%2097/"
   rel="nofollow">http://s180.photobucket.com/albums/x246/UNITEDAUTO1983/D
   ODGE%202500%20PU%2097/</a> <br> <br> <br> <br>

All these programs want to split lines at a particular linewidth, roughly 80
columns. This is not necessary, and can introduce small noise.
For the remaining, we use unquote for the first step.

=================

h2tpy can crash on output (using h2t above, not unquote):
UnicodeDecodeError: 'utf8' codec can't decode bytes in position 21620-21621: invalid data

h2t at this point produces blank output.

A subsequent 'tidy' step will concat broken URLs, as well as convert & back to &amp;

=================

'pandoc' converts to markdown, meaning we get the following sort of things for images:
[![image](http://feeds.chicagotribune.com/~a/chicagotribune/news/local?i=jPLVjl)](http://feeds.chicagotribune.com/~a/chicagotribune/news/local?a=jPLVjl)

h2tpy crashed on tidy output:
UnicodeDecodeError: 'utf8' codec can't decode byte 0xc3 in position 0: unexpected end of data

h2t takes 93 seconds to convert 700K of HTML.
Unless we use '-style pretty', in which case conversion takes roughly 1 second
(!?).

We use the following options:
 html2text -nobs -style pretty

'-style pretty' works better, because it actually turns out to be more compact
that '-style compact', and strips links:

47,53c47,51
< 253-9977 [http://i353.photobucket.com/albums/r379/lorina8n/
< joannejustinelorri.jpg] This is from the 1800's and either English or Scottish.
< We bought in Canada over 28 years ago for a T.V.- Bedroom dresser. It has
< served us well and we are downsizing, so no longer need. It is now used as
< office storage. Many uses. It measures 52" wide X 80" high and comes in 2
< pieces. Beautiful piece. Asking $1000.00 or will trade for Cherrywood high
< dresser. Light cherry! Hello:
---
> 253-9977  This is from the 1800's and either English or Scottish. We bought in
> Canada over 28 years ago for a T.V.- Bedroom dresser. It has served us well and
> we are downsizing, so no longer need. It is now used as office storage. Many
> uses. It measures 52" wide X 80" high and comes in 2 pieces. Beautiful piece.
> Asking $1000.00 or will trade for Cherrywood high dresser. Light cherry! Hello:

One problem with html2text is that it can lay out tables in ways that are not
counterintuitive, e.g.:

BEFORE html2text:
<td align="center"><font color="#810952" size="+2"><span>or please
call Auto Warehouse of San Jose<br>
@ (408) 885-9600 for more information!<br>
<br>
Auto Warehouse..1660 W. San Carlos St..San Jose,
CA..95128<br></span></font></td>
<td align="center"><font color="#810952" size="+2"><span>BIG SALE
GOING ON NOW!! * Upgrade stereo<br>
* 6 CD changer<br>
* Casette player<br>
* 184K miles<br>
* New tires<br>
* Extra: Yakima bike/kayak rack<br>

AFTER html2text:
       or please call                                                                           I have the following seats for the 2008-09 season:
       Auto Warehouse                                                                                      4 seats in Section 328, row 5
         of San Jose                                                                                       2 seats in Section 307, row 9
Click   @ (408) 885-                                                                     2 seats in Section 307, row 10 (right behind the seats in row 9)
 here   9600 for more
 for    information!    Prices start at $25 per ticket. Email or call me if youÂre interested in buying tickets for games this season or have further questions. Tickets for Opening Night against the Cleveland Cavaliers
 more                                                                                                             have been sold.
 info       Auto
 and   Warehouse..1660                                                                                                 Mike
photos  W. San Carlos                                                                                              559-313-4316
        St..San Jose,                                                                                    2004Â JeepÂ Â  WranglerÂ Rubicon
          CA..95128                                                                                                     Â 
