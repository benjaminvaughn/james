// on load get the data

window.onload = function () {

    $.get("/getdata", function (data) {
        console.log(data)
        var node = document.createElement("div");                 // Create a <li> node
        var textnode = document.createTextNode(data);         // Create a text node
        node.appendChild(textnode);                              // Append the text to <li>
        document.getElementById("id").appendChild(node);     // Append <li> to <ul> with id="myList" 
    })
}
// This is the function for the drop down
function sendcoin() {
    coin = document.getElementById("select").value;
    console.log(coin)
    $.ajax({
        url : "/graph",
        type: "POST",
        data : {'coin': coin},
        success: function(data, textStatus, jqXHR)
        {
            console.log(data) //this is the data python returns.
        },
        error: function (jqXHR, textStatus, errorThrown)
        {
            console.log("no reponse")
        }
    });
    
}
console.log("run")
