#!/usr/bin/env python3

# export FLASK_ENV=development
# export FLASK_APP=main.py
#	 flask run

from flask import Flask, render_template
app = Flask(__name__)

import os
import base64
import yaml
from github import Github


@app.route('/')
def home():

	# Github setup
	token = os.environ['GITHUB_TOKEN']
	g = Github(token)

	repo = g.get_repo("alphagov/gsp-teams")
	contents = repo.get_contents("clusters")

	clusters = []

	for file in contents:
		decoded = base64.b64decode(file.content)
		yamled = yaml.safe_load(decoded)
		clusters.append(yamled)

	return render_template('home.html', clusters=clusters)


# This is if a separate details page is required

# @app.route('/<clustername>')
# def show_cluster_info(clustername):
#
# 	# Github setup
# 	token = os.environ['GITHUB_TOKEN']
# 	g = Github(token)
#
# 	repo = g.get_repo("alphagov/gsp-teams")
# 	file = repo.get_contents("clusters/" + clustername + ".yaml")
# 	decoded = base64.b64decode(file.content)
# 	cluster = yaml.safe_load(decoded)
#
# 	return render_template('detail.html', cluster=cluster)
