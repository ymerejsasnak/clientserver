
window.onload = function() {



    function setMessage(message) {
        const messageLabel = document.getElementById('message');
        messageLabel.innerHTML = '\n\n' + message;
    }



    const readButton = document.getElementById('read_button');
    const readTicker = document.getElementById('read_ticker');

    function readItem(ticker) {
        console.log( 'Sending GET request' );

        const XHR = new XMLHttpRequest();

        // Define what happens on successful data submission
        XHR.addEventListener( 'load', function(event) {
            //console.log( XHR.response );
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

     readButton.addEventListener( 'click', function() {
        // get entered ticker
        let ticker = readTicker.value;
        readItem(ticker);
    } );






    const createButton = document.getElementById('create_button');
    const createTicker = document.getElementById('create_ticker');
    const createKey = document.getElementById('create_key');
    const createValue = document.getElementById('create_value');


    function createItem(ticker, data) {
        setMessage( 'Sending POST request' );

        const XHR = new XMLHttpRequest();

        let urlEncodedData = "",
        urlEncodedDataPairs = [],
        name;

        // Turn the data object into an array of URL-encoded key/value pairs.
        for(name in data) {
            urlEncodedDataPairs.push(encodeURIComponent(name) + '=' + encodeURIComponent(data[name]));
        }

        // Combine the pairs into a single string and replace all %-encoded spaces to
        // the '+' character; matches the behaviour of browser form submissions.
        urlEncodedData = urlEncodedDataPairs.join('&').replace(/%20/g, '+');

        // Define what happens on successful data submission
        XHR.addEventListener('load', function(event) {
            //console.log( XHR.response );
            setMessage(XHR.response);
        } );

        // Define what happens in case of error
        XHR.addEventListener('error', function(event) {
            setMessage('something went wrong');
        } );

        let url = 'http://localhost:8080/stocks/api/v1.0/createStock/' + ticker;

        // Set up our request
        XHR.open('POST', url);

        // Add the required HTTP header for form data POST requests
        XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        console.log(urlEncodedData);

        // Finally, send our data.
        XHR.send(urlEncodedData);
    }

     createButton.addEventListener( 'click', function() {
        // get entered ticker
        let ticker = createTicker.value;
        let key = createKey.value;
        let value = createValue.value;
        createItem(ticker, {key, value});
    } );



}
