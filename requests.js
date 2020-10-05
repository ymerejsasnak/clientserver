
window.onload = function() {

    function setMessage(message) {
        const messageLabel = document.getElementById('message');
        messageLabel.innerHTML = '\n\n' + message;
    }


    /*
     *  CREATE
     */
    const createButton = document.getElementById('create_button');
    const createTicker = document.getElementById('create_ticker');
    const createKey = document.getElementById('create_key');
    const createValue = document.getElementById('create_value');

    function createItem(ticker, data) {
        console.log('Sending POST request');

        const XHR = new XMLHttpRequest();
        let urlEncodedData = "", urlEncodedDataPairs = [], name;

        // Turn the data object into an array of URL-encoded key/value pairs.
        for(name in data) {
            urlEncodedDataPairs.push(encodeURIComponent(name) + '=' + encodeURIComponent(data[name]));
        }

        // Combine the pairs into a single string and replace all %-encoded spaces to
        // the '+' character; matches the behaviour of browser form submissions.
        urlEncodedData = urlEncodedDataPairs.join('&').replace(/%20/g, '+');

        // Define what happens on successful data submission
        XHR.addEventListener('load', function(event) {
            setMessage(XHR.response);
        } );

        // Define what happens in case of error
        XHR.addEventListener('error', function(event) {
            setMessage('something went wrong');
        } );

        // setup and send POST request
        let url = 'http://localhost:8080/stocks/api/v1.0/createStock/' + ticker;
        XHR.open('POST', url);
        XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        XHR.send(urlEncodedData);
    }

    // attach the function to the button
    createButton.addEventListener( 'click', function() {
        let ticker = createTicker.value;
        let key = createKey.value;
        let value = createValue.value;
        createItem(ticker, {key, value});
    } );


    /*
     *  READ
     */
    const readButton = document.getElementById('read_button');
    const readTicker = document.getElementById('read_ticker');

    function readItem(ticker) {
        console.log( 'Sending GET request' );

        const XHR = new XMLHttpRequest();

        // Define what happens on successful data submission
        XHR.addEventListener( 'load', function(event) {
            setMessage(XHR.response);
        } );

        // Define what happens in case of error
        XHR.addEventListener( 'error', function(event) {
            setMessage('something went wrong');
        } );

        let url = 'http://localhost:8080/stocks/api/v1.0/getStock/' + ticker;
        XHR.open('GET', url);
        XHR.send();
    }

    // attach the function to the button
    readButton.addEventListener( 'click', function() {
        let ticker = readTicker.value;
        readItem(ticker);
    } );










}
