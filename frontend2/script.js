document.getElementById("sendMail").addEventListener("click", async function () {
    const userInput = document.getElementById("mailInput").value;
    const alertDiv = document.getElementById("alert");

    // Clear previous alerts
    alertDiv.style.display = 'none';

    if (!userInput) {
        alertDiv.textContent = "Please enter email content!";
        alertDiv.className = "alert error";
        alertDiv.style.display = 'block';
        return;
    }

    try {
        const response = await fetch("https://mail-agent.onrender.com/send-mail", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ input: userInput })  // Sending input to backend
        });

        const result = await response.json();
        
        if (result.message) {
            alertDiv.textContent = result.message;
            alertDiv.className = "alert success";
        } else if (result.error) {
            alertDiv.textContent = result.error;
            alertDiv.className = "alert error";
        }

        alertDiv.style.display = 'block';
    } catch (error) {
        console.error("Error:", error);
        alertDiv.textContent = "Something went wrong!";
        alertDiv.className = "alert error";
        alertDiv.style.display = 'block';
    }
});
