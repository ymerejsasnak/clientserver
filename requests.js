
window.onload = function() {



    function setMessage(message) {
        const messageLabel = document.getElementById('message');
        messageLabel.innerHTML = '\n\n' + message;
    }



    const readButton = document.getElementById('read_button');
    const readTicker = document.getElementById('read_ticker');

    function readItem(ticker) {
        setMessage( 'Sending GET request for ' + ticker );

        const XHR = new XMLHttpRequest();

        // Define what happens on successful data submission
        XHR.addEventListener( 'load', function(event) {
            //console.log( XHR.response );
            setMessage(XHR.response);
        } );

        // Define what happens in case of error
        XHR.addEventListener( 'error', function(event) {
            setMessage('something went wrong' + event);
        } );

        let request = 'http://localhost:8080/stocks/api/v1.0/getStock/' + ticker;

        XHR.open('GET', request);
        XHR.send();
    }

     readButton.addEventListener( 'click', function() {
        // get entered ticker
        let ticker = readTicker.value;
        readItem(ticker);
    } );



  /*

    function sendData( data ) {
        console.log( 'Sending data' );

        const XHR = new XMLHttpRequest();

        let urlEncodedData = "",
            urlEncodedDataPairs = [],
            name;

        // Turn the data object into an array of URL-encoded key/value pairs.
        for( name in data ) {
            urlEncodedDataPairs.push( encodeURIComponent( name ) + '=' + encodeURIComponent( data[name] ) );
        }

        // Combine the pairs into a single string and replace all %-encoded spaces to
        // the '+' character; matches the behaviour of browser form submissions.
        urlEncodedData = urlEncodedDataPairs.join( '&' ).replace( /%20/g, '+' );

        // Define what happens on successful data submission
        XHR.addEventListener( 'load', function(event) {
            alert( 'Yeah! Data sent and response loaded.' );
        } );

        // Define what happens in case of error
        XHR.addEventListener( 'error', function(event) {
            alert( 'Oops! Something went wrong.' );
        } );

        // Set up our request
        XHR.open( 'POST', 'https://example.com/cors.php' );

        // Add the required HTTP header for form data POST requests
        XHR.setRequestHeader( 'Content-Type', 'application/x-www-form-urlencoded' );

        // Finally, send our data.
        XHR.send( urlEncodedData );
    }

    btn.addEventListener( 'click', function() {
        //sendData( {test:'ok'} );
        console.log('just a test');
    } )


*/

}