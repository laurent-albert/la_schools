# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "la_schools"
app_title = "LA Schools"
app_publisher = "LA"
app_description = "LA extensions for Schools"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "la@la.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/la_schools/css/la_schools.css"
# app_include_js = "/assets/la_schools/js/la_schools.js"

# include js, css files in header of web template
# web_include_css = "/assets/la_schools/css/la_schools.css"
# web_include_js = "/assets/la_schools/js/la_schools.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "la_schools.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "la_schools.install.before_install"
# after_install = "la_schools.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "la_schools.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"la_schools.tasks.all"
# 	],
# 	"daily": [
# 		"la_schools.tasks.daily"
# 	],
# 	"hourly": [
# 		"la_schools.tasks.hourly"
# 	],
# 	"weekly": [
# 		"la_schools.tasks.weekly"
# 	]
# 	"monthly": [
# 		"la_schools.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "la_schools.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "la_schools.event.get_events"
# }

