# Github Trending API

Get top trending repositories

Start server:

```
$ python trending.py
```

Make request:

```
http://localhost:4999/github/trending
```

Response:

```
  [{
    "title": "wiki",
    "description": "Wiki.js | A modern, lightweight and powerful wiki app built on Node.js",
    "stars": "9,447",
    "language": "Vue",
    "url": "https://github.com/Requarks/wiki"
  },
  {
    "title": "storybook",
    "description": "📓 The UI component workshop. Develop, document, & test for React, Vue, Angular, Ember, Web Components, & more!",
    "stars": "50,577",
    "language": "TypeScript",
    "url": "https://github.com/storybookjs/storybook"
  },
  ...
  ]
  ```
