# coding=utf-8
# Script: Taller de introduccion a Python - PageRank
# Descripcion: ---
# Autor: Marcos Manuel Ortega
# Fecha: 04/2016
# Repositorio: ---


import os
import random
import string
import json


PLANTILLA_HTML = 'plantilla_web.html'
HTML_DIR = 'html_webs'
WEBS = ['web1.com', 'web2.com', 'web3.com']


def url2path(url):
	return HTML_DIR + '/' + url.replace('/', '_') + '.html'


def generar_url(url):
	url += '/' + ''.join(random.choice(string.ascii_letters + string.digits)
	                     for _ in xrange(random.randrange(4, 10)))

	return url


def pag_factorial(url, nivel, u_dict, u_list):
	u_li = []

	if nivel <= 3:
		for _ in range(random.randrange(1, 5 - nivel)):
			u = generar_url(url)

			u_li.append(u)
			u_list.append(u)
			u_dict[url] = u_dict.get(url, []) + [u]

			pag_factorial(u, nivel + 1, u_dict, u_list)

	with open(url2path(url), 'w') as f:
		with open(PLANTILLA_HTML, 'r') as f_plantilla:
			plantilla = f_plantilla.read()

		url_li = '\n'.join(['<li><a href="{0}">{0}</a></li>'.format(u) for u in u_li])

		html = plantilla.replace('__url_list__', url_li)

		f.write(html)

	return u_dict


url_dict = {}
url_list = []

for w in WEBS:
	i = 0

	pag_factorial(w, i, url_dict, url_list)

print(json.dumps(url_dict, sort_keys=True, indent=4))


files = [HTML_DIR + '/' + f for f in os.listdir(HTML_DIR) if os.path.isfile(os.path.join(HTML_DIR, f))]

for file_ in files:
	with open(file_, 'r+') as f:
		html = f.read()

		f.seek(0)

		n_urls = random.randrange(6)
		u_li = []
		while len(u_li) < n_urls:
			u = random.choice(url_list)

			if u.split('/')[0] == file_.split('/')[1].split('_')[0]:
				continue

			u_li.append(u)

		url_li = '\n'.join(['<li><a href="{0}">{0}</a></li>'.format(u) for u in u_li])

		html = html.replace('__external_url_list__', url_li)

		f.write(html)
