document.getElementById("startServer").addEventListener("click", async function () {
    const startButton = document.getElementById("startServer");
    const sendButton = document.getElementById("sendMail");
    const statusDiv = document.getElementById("serverStatus");

    statusDiv.textContent = "Starting server, please wait...";
    statusDiv.className = "alert info";
    statusDiv.style.display = "block";
    startButton.disabled = true;

    try {
        const response = await fetch("https://mail-agent.onrender.com/ping");

        if (response.ok) {
            statusDiv.textContent = "Server is ready!";
            statusDiv.className = "alert success";

            // Show "Generate Email" button when server is ready
            sendButton.style.display = "block";
        } else {
            statusDiv.textContent = "Failed to wake up server. Try again!";
            statusDiv.className = "alert error";
            startButton.disabled = false;
        }
    } catch (error) {
        statusDiv.textContent = "Error waking up the server.";
        statusDiv.className = "alert error";
        startButton.disabled = false;
    }
});

document.getElementById("sendMail").addEventListener("click", async function () {
    const userInput = document.getElementById("mailInput").value;
    const statusDiv = document.getElementById("serverStatus");

    if (!userInput) {
        statusDiv.textContent = "Please enter email content!";
        statusDiv.className = "alert error";
        statusDiv.style.display = "block";
        return;
    }

    try {
        const response = await fetch("https://mail-agent.onrender.com/send-mail", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ input: userInput })
        });

        const result = await response.json();

        statusDiv.textContent = result.message || result.error;
        statusDiv.className = result.message ? "alert success" : "alert error";
        statusDiv.style.display = "block";
    } catch (error) {
        statusDiv.textContent = "Something went wrong!";
        statusDiv.className = "alert error";
        statusDiv.style.display = "block";
    }
});
