document.querySelector("form").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const formData = {
        name: document.querySelector("input[name='name']").value,
        email: document.querySelector("input[name='email']").value,
        message: document.querySelector("textarea[name='message']").value
    };

    const response = await fetch("http://127.0.0.1:5000/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    });

    const result = await response.json();
    alert(result.message);
    this.reset();
});