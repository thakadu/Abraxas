<%inherit file="base_960.mako"/>

## -------------- Overide the Title -----------------------
<%def name="title()">
Abraxas Download
</%def>

## --------------  Overide the body ---------------------- 
<%def name="body()">

<h1>Abraxas</h1> 
<p>
Abraxas is a very simple blog / feed Aggregator written
in Python. It uses the Pylons web framework, the SiLCC Web Service, SQLAlchemy
and Mako templates.</p>
<p>
<p>Abraxas is very easy to customize and enhance.
Released under a BSD style license, you can download it,
or check out the source code from Github
at <a href="http://github.com/thakadu/Abraxas">Abraxas</a>.
</p>
</%def>

##------------------ Overide the sidebar ---------------------
<%def name="sidebar()">
<div style="text-align:center">
<img src="/static/pylons-powered.png" alt="Pylons" /> <br/>
<img src="/static/sqla-logo6.gif" alt="SQLAlchemy" /> <br/>
<img src="/static/makoLogo.png" alt="Mako Templates" /> <br/>
<img src="/static/python-powered-w-200x80.png" alt="Python" /> <br/>
<img src="/static/abraxas.png" alt="Abraxas" width="200"/>
<img src="/static/swift_river.png" alt="Swift River" />
</div>
</%def>

