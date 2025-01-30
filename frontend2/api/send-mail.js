// api/send-mail.js
export default async function handler(req, res) {
    if (req.method === 'POST') {
        const { input } = req.body;

        try {
            const response = await fetch("https://mail-agent.onrender.com/send-mail", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ input })
            });

            const result = await response.json();
            res.status(200).json(result);
        } catch (error) {
            console.error("Error:", error);
            res.status(500).json({ error: "Something went wrong!" });
        }
    } else {
        // Handle unsupported HTTP methods
        res.status(405).json({ error: 'Method Not Allowed' });
    }
}
