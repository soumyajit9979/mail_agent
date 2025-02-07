document.getElementById("startServer").addEventListener("click", async function () {
    const startButton = document.getElementById("startServer");
    const sendButton = document.getElementById("sendMail");
    const mailInput = document.getElementById("mailInput");
    const alertDiv = document.getElementById("alert");

    alertDiv.textContent = "Starting server, please wait...";
    alertDiv.className = "alert info";
    alertDiv.style.display = "block";
    startButton.disabled = true;

    try {
        const response = await fetch("https://mail-agent.onrender.com/ping");

        if (response.ok) {
            alertDiv.textContent = "Server is ready!";
            alertDiv.className = "alert success";

            // Show the email input and "Generate Email" button
            mailInput.style.display = "block";
            sendButton.style.display = "block";
        } else {
            alertDiv.textContent = "Failed to wake up server. Try again!";
            alertDiv.className = "alert error";
            startButton.disabled = false;
        }
    } catch (error) {
        alertDiv.textContent = "Error waking up the server.";
        alertDiv.className = "alert error";
        startButton.disabled = false;
    }
});

document.getElementById("sendMail").addEventListener("click", async function () {
    const userInput = document.getElementById("mailInput").value;
    const alertDiv = document.getElementById("alert");

    if (!userInput) {
        alertDiv.textContent = "Please enter email content!";
        alertDiv.className = "alert error";
        alertDiv.style.display = "block";
        return;
    }

    try {
        const response = await fetch("https://mail-agent.onrender.com/send-mail", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ input: userInput })
        });

        const result = await response.json();

        alertDiv.textContent = result.message || result.error;
        alertDiv.className = result.message ? "alert success" : "alert error";
        alertDiv.style.display = "block";
    } catch (error) {
        alertDiv.textContent = "Something went wrong!";
        alertDiv.className = "alert error";
        alertDiv.style.display = "block";
    }
});
