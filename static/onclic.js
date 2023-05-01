function testConnection() {
    var host_name = document.getElementById("host_name").value;
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var database_name = document.getElementById("database_name").value;
  
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
      }
    };
    xhttp.open("GET", "/test-connection?host=" + host_name + "&username=" + username + "&password=" + password + "&database_name=" + database_name, true);
    xhttp.send();
  }