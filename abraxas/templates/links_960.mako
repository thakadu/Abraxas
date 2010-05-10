<%inherit file="base_960.mako"/>

<%def name="title()">
Abraxas
</%def>

## --------------------- 
<%def name="body()">

${self.page_nav()}

${self.render_subs()}

${self.page_nav()}

</%def>
## ----------------------------------------------------------------


<%def name="page_nav()">
<div class="grid_11 pg">
% if c.page_numeric > 0:
<a class="nav" href="/${c.view}/${c.page_numeric-1}">&laquo;&nbsp;previous</a>
% endif
##% if c.totlinks > (c.page_numeric +1) * c.pagesize:
## Poor mans pagination below...(need to replace at some point) 
## If there are less links than the current pagesize then obviously
## there are no more links. If there are exactly pagesize links
## then there *could* be more so we display a next>> link...
% if len(c.links) == c.pagesize:
<a class="nav" href="/${c.view}/${c.page_numeric+1}">next&nbsp;&raquo;</a>
% endif
</div><!-- page_nav -->
</%def>



