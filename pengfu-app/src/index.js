import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// import App from './App';
// import AppRouter from './AppRouter'
// import JokeList from './components/jokeList'
import Person from './components/test2'
import * as serviceWorker from './serviceWorker';
import './style/common.css'
// import './a.less'
// import './b.scss'
ReactDOM.render(<Person />, document.getElementById('root'),function () {
  console.log('渲染完成')
});

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
