function sendMail() {
    const input = document.getElementById("mailInput").value;
    const responseMessage = document.getElementById("responseMessage");

    responseMessage.innerText = "Processing...";

    fetch("http://127.0.0.1:5000/draft_mail", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ input })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            responseMessage.innerText = "✅ Successful: Mail drafted!";
            responseMessage.style.color = "green";
        } else {
            responseMessage.innerText = "❌ Error: " + data.error;
            responseMessage.style.color = "red";
        }
    })
    .catch(error => {
        responseMessage.innerText = "❌ Error: Unable to connect to the server.";
        responseMessage.style.color = "red";
    });
}
