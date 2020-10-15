/*
Jeremy Kansas
CS 499
Category 3 Artifact
*/

window.onload = function() {


    // Get UI elements
    const createButton = document.getElementById('create_button');
    const createTicker = document.getElementById('create_ticker');
    const createKey = document.getElementById('create_key');
    const createValue = document.getElementById('create_value');

    const readButton = document.getElementById('read_button');
    const readTicker = document.getElementById('read_ticker');

    const updateButton = document.getElementById('update_button');
    const updateTicker = document.getElementById('update_ticker');
    const updateKey = document.getElementById('update_key');
    const updateValue = document.getElementById('update_value');

    const deleteButton = document.getElementById('delete_button');
    const deleteTicker = document.getElementById('delete_ticker');


    /*
     *  Function setMessage
     *  Displays a string in the 'message' text label
     *  Args: message - the string to display
     */
    function setMessage(message) {
        const messageLabel = document.getElementById('message');
        messageLabel.innerHTML = '\n\n' + message;
    }

    /*
     *  Function XHR
     *  Sets up and sends an XMLHttpRequest
     *  Args:
     *        ticker: ticker symbol as string
     *        crudOp: crud operation as string
     *        data: (optional) data to send
     */
    function XHR(ticker, crudOp, data=null) {
        const XHR = XMLHttpRequest();
        const METHODS = {"create":"POST", "read":"GET", "update":"PUT", "delete":"DELETE"}

        crudOp = crudOp.toLowerCase();
        let reqMethod = METHODS[crudOp];

        // Define what happens on successful data submission
        XHR.addEventListener( 'load', function(event) {
            setMessage(XHR.response);
        } );

        // Define what happens in case of error
        XHR.addEventListener( 'error', function(event) {
            setMessage('something went wrong');
        } );

        // setup and send request
        let url = 'http://localhost:8080/stocks/api/v1.0/' + crudOp.toLowerCase() + 'Stock/' + ticker;
        XHR.open(reqMethod, url);

        if (data) {
            XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            XHR.send(JSON.stringify(data));
        } else {
            XHR.send();
        }
    }


    /*
     *  CREATE
     */
    function createItem(ticker, data) {
        console.log('Sending POST request');
        XHR(ticker, 'create', data);
    }

    // attach the function to the button
    createButton.addEventListener( 'click', function() {
        let ticker = createTicker.value;
        let key = createKey.value;
        let value = createValue.value;
        let doc = {};
        doc[key] = value;
        createItem(ticker, doc);
    } );


    /*
     *  READ
     */
    function readItem(ticker) {
        console.log( 'Sending GET request' );
        XHR(ticker, 'read');
    }

    // attach the function to the button
    readButton.addEventListener( 'click', function() {
        let ticker = readTicker.value;
        readItem(ticker);
    } );


    /*
     *  UPDATE
     */
    function updateItem(ticker, data) {
        console.log('Sending PUT request');
        XHR(ticker, 'update', data);
    }

    // attach the function to the button
    updateButton.addEventListener( 'click', function() {
        let ticker = updateTicker.value;
        let key = updateKey.value;
        let value = updateValue.value;
        let doc = {};
        doc[key] = value;
        updateItem(ticker, doc);
    } );


    /*
     *  DELETE
     */
    function deleteItem(ticker) {
        console.log('Sending DELETE request');
        XHR(ticker, 'delete');
    }

    // attach the function to the button
    deleteButton.addEventListener( 'click', function() {
        let ticker = deleteTicker.value;
        deleteItem(ticker);
    } );


}
