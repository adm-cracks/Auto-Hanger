function che(x) {

    if (x <= 0) {
        alert("Plese Select minium 1 quatity")
        document.getElementById("cheout").disabled = true;
        var con = document.getElementById("cheout");
        con.style.backgroundColor = "whitesmoke";
        con.style.color = "black";
        con.style.cursor = "not-allowed";

    } else {
        document.getElementById("cheout").disabled = false;
        var con = document.getElementById("cheout");
        con.style.backgroundColor = "royalblue";
        con.style.color = "white";
        con.style.cursor = "pointer";

    }
}