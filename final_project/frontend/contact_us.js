const contactUs = (event) => {
    event.preventDefault(); 

    const form = document.getElementById("contact-us");
    const formData = new FormData(form);
    const postData = {
        name: formData.get("name"),
        email: formData.get("email"),
        problem: formData.get("message"),
    };

    console.log(postData); 
    const token = localStorage.getItem("token")
    console.log(token)
    fetch("http://127.0.0.1:8000/contact_us/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization : `Token ${token}`,

        },
        body: JSON.stringify(postData),
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
        alert("Message sent successfully!");
        window.location.href = "./index.html";
    })
    .catch((error) => {
        console.error("Error:", error); 
        alert("There was a problem sending your message.");
    });
};
