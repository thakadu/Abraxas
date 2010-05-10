<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>${self.title()}</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
<link rel="stylesheet" type="text/css" media="all" href="/static/reset.css" />
<link rel="stylesheet" type="text/css" media="all" href="/static/text.css" />
<link rel="stylesheet" type="text/css" media="all" href="/static/960.css" />
<link href="/static/styles_960.css" media="screen" rel="Stylesheet" type="text/css" />
</head>
<body>
## /--------------------- * container_16 id=container * ---------------------\
## |*------------------------_grid_16 id=banner_----------------------------*|
## || logo                                                search            ||
## |*.......................................................................*|
## |*------------------------grid_16 id=navbar------------------------------*|
## || latest about download                                                 ||
## |*.......................................................................*|
## |*----------- grid_11 id=main -------------------* *- grid_5 id=sidebar -*|
## ||*grid_1**---grid_10 class=sub-----------------*| |*--user_actions-----*||
## |||      ||Title (host)                         || ||  (or login)       |||
## |||      ||by X                                 || |*-------------------*||
## |||      ||tags etc.                            || |*----adverts--------*||
## ||*------**-------------------------------------*| ||                   |||
## ||                                               | |....................*||
## ||                                               | |*------tags---------*||
## ||                                               | ||popular tags...    |||
## ||                                               | |*-------------------*||
## |*-----------------------------------------------* *---------------------*|
## |*------------------------- grid_16 id=footer ---------------------------*|
## ||                                                                       ||
## |*-----------------------------------------------------------------------*|
## \........................................................................./
<div class="container_16" id="container">

	${self.banner()}
  <div class="clear"></div>

  <div class="grid_16" id="navbar">${self.navbar()}</div>
  <div class="clear"></div>

  <div class="grid_11" id="main">
    ${self.body()}
  </div><!--end of div id=main-->

  <div class="grid_5" id="sidebar">
    ${self.sidebar()}
  </div><!--end of div id=sidebar-->

  <div class="grid_16 spacer"></div>
  <div class="clear"></div>

  <div class="grid_16">${self.footer()}</div>
  <div class="clear"></div>

## If you want to load any jscript add them to jscripts
##  ${self.jscripts()}  

</div><!--container_16-->
</body>
</html>


## -------------------------- title ----------------------------
<%def name="title()">
Abraxas
</%def>
## -------------------------- banner ---------------------------
<%def name="banner()">
  <div class="grid_11"><img src="${c.logo_file}" alt="Logo" onclick="document.location='/'" /></div>
  <div class="grid_5">
## If you want a search form in your banner uncomment these lines 
##    <form id="banner_search" action="/search">
##      <p>
##        <input name="search"/>
##        <input type="submit" value="submit"/>
##      </p>
##    </form>
  </div>
</%def>
## -------------------------- navbar ---------------------------
<%def name="navbar()">
<%
    views = ('Latest', 'About', 'Download')
%>
<ul>
% for v in views:
    <li><a href="/${v}">${v}</a></li>
##<li><a href="/${v}">${v}</a></li>
##    % if c.view == v:
##    <li><a href="/${v}" class="current_view">${v}</a></li>
##    % else:
##    <li><a href="/${v}">${v}</a></li>
##    % endif
% endfor
</ul>
</%def>
## -------------- List of links/submissions for laying out links on all pages------
<%def name="render_subs()">
% for entry in c.links:
<div class="grid_11 alpha omega sub">
<p class="h"><span class="feed_title">${entry['feed_title']}</span>&nbsp;<span class="pubtime">${entry['pubtime'].strftime('%A, %B %d, %I:%M %p')}</span></p><br/>
<a class="l" href="${entry['url']}">${entry['title'].encode('utf-8','ignore')}</a><br/>
<p class="l">${human_age(entry['pubtime'])} ago.</p>
% if entry['tags']:
${self.format_tags(entry['tags'],())}
% endif
${self.format_link_actions(entry['id'],entry)}
</div>

<div class="clear"></div>
% endfor
</%def>
## ------------- format tags in links ------------------------------
<%def name="format_tags(tags, user_tags)">
<div class="tags">
% for tag in tags.split():
<a href="/tag/${tag}">${tag}</a>
% endfor
</div>
</%def>
## ----------------- format link actions --------------------------
<%def name="format_link_actions(sbid,sub)">
<div class="link_actions">
## Add any link actions such as "email link", "Digg" etc here....
</div>
</%def>
## ------------Format Age is nice human readable form----------
<%def name="human_age(sbdatesbmt)">
<%
		import time
		def calc_age(t):
        unix_ts = time.mktime(t.timetuple())+1e-6*t.microsecond
        secs = time.time() - unix_ts
        days = int(secs/86400)
        if days == 1: return '1 day'
        if days > 1: return '%d days' % days
        hrs = int(secs/3600)
        if hrs == 1: return '1 hour'
        if hrs > 1: return '%d hours' % hrs
        mins = int(secs/60)
        if mins == 1: return '1 minute'
        if mins > 1: return '%d minutes' % mins
        if secs == 1: return '1 second'
        return '%d seconds' % secs
%>
${calc_age(sbdatesbmt)}
</%def>
## -------------------------- Sidebar --------------------------
<%def name="sidebar()">
% if c.tags:
<div id="tags">
<h1>Popular Tags</h1>
<ul>
% for tag in c.tags:
<li><a href="/tag/${tag['lower']}">${tag['lower']}</a></li>
% endfor
</ul>
</div>
% endif
<div style="text-align:center">
<img src="/static/swift_river.png" alt="Swift River" />
</div>
</%def>
## -------------------------- Adverts --------------------------
<%def name="adverts()">
<div id="adverts">
<h1>SPONSORED LINKS</h1>
## Add any adverts for your site here
</div><!-- adverts -->
</%def>
## -------------------------- footer ---------------------------
<%def name="footer()">
<div id="footer">
    <a class="banneraction" href="/about">About</a>&nbsp;|
    <a class="banneraction" href="/download">Download</a>&nbsp;
</div>
</%def>
## -------------------------- jscripts -------------------------
## Place any Javascript libraries you want to use here
<%def name="jscripts()">
##<script src="/static/jquery-1.3.min.js" charset="utf-8"></script>
##<script src="/static/scripts.js" charset="utf-8"></script>
</%def>
