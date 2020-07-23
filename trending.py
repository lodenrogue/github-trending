from flask import Flask, request, Response
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import json

BASE_URL = 'https://github.com'
TRENDING_URL = BASE_URL + '/trending'

app = Flask(__name__)
CORS(app)

@app.route('/github/trending', methods=['GET'])
def get_trending():
	req = requests.get(TRENDING_URL)
	soup = BeautifulSoup(req.content, 'html.parser')

	projects = get_projects(soup)
	js = json.dumps(projects)
	return Response(js, status=200, mimetype='application/json')


def get_projects(soup):
	projects = []

	rows = soup.find_all(class_='Box-row')

	for row in rows:
		title = get_title(row)
		description = get_description(row)

		stars = get_stars(row)
		language = get_language(row)
		url = get_url(row)

		projects.append({
			'title': title,
			'description': description,
			'stars': stars,
			'language': language,
			'url': url
		})

	return projects


def get_title(row):
	header = row.find(class_='lh-condensed')
	link = header.find('a')
	text = link.get_text()
	last_word = text.split(' ')[-1]
	return last_word.replace('\n', '')


def get_description(row):
	p = row.find('p')

	if p is None:
		return None
	else:
		text = p.getText()
		stripped = text.strip()
		return stripped.replace('\n', '')


def get_stars(row):
	f6 = row.find(class_='f6')
	links = f6.find_all('a')
	star_link = links[0]

	text = star_link.get_text()
	replaced = text.replace('\n', '')
	return replaced.strip()


def get_language(row):
	f6 = row.find(class_='f6')
	spans = f6.find_all('span')
	span = spans[0]
	language_span = span.find('span', itemprop='programmingLanguage')

	if language_span is None:
		return None
	else:
		return language_span.get_text()


def get_url(row):
	header = row.find(class_='lh-condensed')
	link = header.find('a')
	return BASE_URL + link['href']


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4999)
