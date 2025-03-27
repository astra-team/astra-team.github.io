---
layout: page
title: Team
permalink: /team/
description: 
nav: true
nav_order: 2
---

<!-- pages/team.md -->
<!-- <hr>
<p>{{ site.data.team | inspect }}</p>
<hr>
<p>{{ site.data.team | where:"position","Researcher" }}</p>
<hr>
 -->
{% assign members = site.data.team | where_exp:"item","item.alumni != true" | sort_natural: "lastname" %}

{% assign heads = members | where:"position","Head" | sort: "order" %}
{% assign administratives = members | where:"position","Administrative" %}
{% assign researchers = members | where:"position","Researcher" %}
{% assign phds = members | where:"position","PhD" %}
{% assign visitors = members | where:"position","Visitor" %}
{% assign postdocs = members | where:"position","Postdoctoral" %}
{% assign engineers = members | where:"position","Engineer" %}
{% assign interns = members | where:"position","Intern" %}

{% assign alumni = site.data.team | where_exp:"item","item.alumni == true" | sort_natural: "lastname" %}

<!-- <hr><p>{{ researchers | inspect }}</p><hr>
<hr><p>{{ phds | inspect }}</p><hr>
 -->
{% if heads.size != 0 %}
<h3>Heads of the team</h3>
<div class="team">
{% for member in heads %}
    {% include team/member.html member=member %}
{% endfor %}
</div>
{% endif %}

{% if administratives.size != 0 %}
<h3>Administratives</h3>
<div class="team">
{% for member in administratives %}
    {% include team/member.html member=member %}
{% endfor %}
</div>
{% endif %}

{% if researchers.size != 0 %}
<h3>Permanents</h3>
<div class="team">
{% for member in researchers %}
    {% if member.parttime != true %}
        {% include team/member.html member=member %}
    {% endif %}
{% endfor %}
</div>
<div class="teamsep">Associate members</div>
<div class="team">
{% for member in researchers %}
    {% if member.parttime == true %}
        {% include team/member.html member=member %}
    {% endif %}
{% endfor %}
</div>
{% endif %}

{% if postdocs.size != 0 or engineers.size != 0 or visitors.size != 0 %}
<h3>Visitors, Postdoctorals and Engineers</h3>
<div class="team">
{% for member in visitors %}
    {% include team/member.html member=member %}
{% endfor %}
{% for member in postdocs %}
    {% include team/member.html member=member %}
{% endfor %}
{% for member in engineers %}
    {% include team/member.html member=member %}
{% endfor %}
</div>
{% endif %}

{% if phds.size != 0 %}
<h3>PhDs</h3>
<div class="team">
{% for member in phds %}
    {% include team/member.html member=member %}
{% endfor %}
</div>
{% endif %}

{% if interns.size != 0 %}
<h3>Interns</h3>
<div class="team">
{% for member in interns %}
    {% include team/member.html member=member %}
{% endfor %}
</div>
{% endif %}

{% if alumni.size != 0 %}
<h3 class="alumni">Alumni</h3>
<div>
{% assign alumnipositions = alumni | group_by: "position" | reverse %}
{% for group in alumnipositions %}
    <h4>{{ group.name }}</h4>
    <div class="team alumni">
    {% for member in group.items %}
        {% include team/member.html member=member %}
    {% endfor %}
    </div>
{% endfor %}
<div>
{% endif %}