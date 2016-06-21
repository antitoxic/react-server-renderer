const zmq = require('zmq');
const renderToString = require('react-dom/server').renderToString;
const App  = require('components/app').App; // replace this with your root component
const Helmet = require("react-helmet");
const channel = zmq.socket('rep');
const [doctype, constantHead, endOfBody] = require('index.html').split(/<html.+<head>|<!--REACT-->/);

channel.connect('ipc:///tmp/myapp');
channel.on('message', state => {
    state = JSON.parse(state);
    let content = renderToString(<App state={state}></App>);
    let head = Helmet.rewind();
    channel.send(`
        ${doctype}<html ${head.htmlAttributes.toString()}><head>
        ${head.title.toString()}
        ${head.meta.toString()}
        ${head.link.toString()}
        ${constantHead}${content}${endOfBody}
    `);
});
