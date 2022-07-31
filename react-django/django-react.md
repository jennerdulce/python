- Reference: [Django CRUD](https://www.youtube.com/watch?v=GieYIzvdt2U&list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60&index=2&ab_channel=TraversyMedia)
- Reference: [ValentinoG](https://www.valentinog.com/blog/drf/)

- At root `pipenv shell`
- cd in app
- `python manage.py startapp frontend`
- Create directories that React can live in
- mkdir src > components
- static > frontend
- templates > frontend
- install webpacker
    - `cd ..` to get to the root
    - `npm init -y`
        - Creates `package.json` for dependencies
    - npm i -D webpack webpack-cli
- install babel
    - `npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties`
- install react
    - `npm i react react-dom prop-types`

- Package.json should like like this

```
{
  "name": "lead_manager",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@babel/core": "^7.18.9",
    "@babel/preset-env": "^7.18.9",
    "@babel/preset-react": "^7.18.6",
    "babel-loader": "^8.2.5",
    "babel-plugin-transform-class-properties": "^6.24.1",
    "webpack": "^5.74.0",
    "webpack-cli": "^4.10.0"
  },
  "dependencies": {
    "prop-types": "^15.8.1",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

- In order to use presets
    - In root create new file: `.babelrc`

```
{
    "presets": ["@babel/preset-env", "@babel/preset-react"],
    "plugins": ["transform-class-properties"]
}
```

- Create` webpack.config.js` file in root
- loads babel loader
```
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
}
```

- need to complie react application
- in package.json
```
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "webpack --mode development --watch ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js",
    "build": "webpack --mode production ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js"
  }
```

- Create index.js
- frontend > src > index.js

