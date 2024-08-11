const handleLogout = () =>{
    const token = localStorage.getItem("token")
    fetch("https://testing-8az5.onrender.com/patient/logout",{
        method:"POST",
        headers:{
            Authorization:`Token ${token}`,
            "Context-Type":"application/json"
        }
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data)
        localStorage.removeItem("token")
        localStorage.removeItem("user_id")
    })
}
handleLogout()