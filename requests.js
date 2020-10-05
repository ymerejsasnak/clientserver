
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
        XHR.open("POST", url);
        XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        XHR.send(JSON.stringify(data));
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

        // setup and send request
        let url = 'http://localhost:8080/stocks/api/v1.0/getStock/' + ticker;
        XHR.open('GET', url);
        XHR.send();
    }

    // attach the function to the button
    readButton.addEventListener( 'click', function() {
        let ticker = readTicker.value;
        readItem(ticker);
    } );



    /*
     *  UPDATE
     */
    const updateButton = document.getElementById('update_button');
    const updateTicker = document.getElementById('update_ticker');
    const updateKey = document.getElementById('update_key');
    const updateValue = document.getElementById('update_value');

    function updateItem(ticker, data) {
        console.log('Sending PUT request');

        const XHR = new XMLHttpRequest();

        // Define what happens on successful data submission
        XHR.addEventListener('load', function(event) {
            setMessage(XHR.response);
        } );

        // Define what happens in case of error
        XHR.addEventListener('error', function(event) {
            setMessage('something went wrong');
        } );

        // setup and send PUT request
        let url = 'http://localhost:8080/stocks/api/v1.0/updateStock/' + ticker;
        XHR.open("PUT", url);
        XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        XHR.send(JSON.stringify(data));
    }

    // attach the function to the button
    updateButton.addEventListener( 'click', function() {
        let ticker = updateTicker.value;
        let key = updateKey.value;
        let value = updateValue.value;
        updateItem(ticker, {key, value});
    } );



    /*
     *  DELETE
     */
    const deleteButton = document.getElementById('delete_button');
    const deleteTicker = document.getElementById('delete_ticker');

    function deleteItem(ticker) {
        console.log('Sending DELETE request');

        const XHR = new XMLHttpRequest();

        // Define what happens on successful data submission
        XHR.addEventListener( 'load', function(event) {
            setMessage(XHR.response);
        } );

        // Define what happens in case of error
        XHR.addEventListener( 'error', function(event) {
            setMessage('something went wrong');
        } );

        // setup and send request
        let url = 'http://localhost:8080/stocks/api/v1.0/deleteStock/' + ticker;
        XHR.open('DELETE', url);
        XHR.send();
    }

    // attach the function to the button
    deleteButton.addEventListener( 'click', function() {
        let ticker = deleteTicker.value;
        deleteItem(ticker);
    } );







}
