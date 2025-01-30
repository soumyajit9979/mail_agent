document.getElementById("sendMail").addEventListener("click", async function () {
    const userInput = document.getElementById("mailInput").value;

    if (!userInput) {
        alert("Please enter email content!");
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
        alert(result.message || result.error);
    } catch (error) {
        console.error("Error:", error);
        alert("Something went wrong!");
    }
});
