function formatDate2(dateStr) {
    const date = new Date(dateStr);
    const options = { 
        day: 'numeric', 
        month: 'long', 
        year: 'numeric', 
        hour: 'numeric', 
        minute: 'numeric',
        hour12: true 
    };
    return date.toLocaleString('en-US', options).replace(" at", "");
}

const getParams = ()=>{
    const param = new URLSearchParams(window.location.search).get("pet_id")
    localStorage.setItem("pet_id",param)
    
    fetch(`http://127.0.0.1:8000/pet/list/${param}`)
    .then((res)=>res.json())
    .then((data)=> {
        console.log(data)
        const formattedDate2 = formatDate2(data.created_on);

        document.getElementById("pd-image").src = data.image
        document.getElementById("pd-name").innerText = data.name
        document.getElementById("pd-adoption-status").innerText = data.adoption_status
        document.getElementById("pd-pet-type").innerText = data.pet_type
        document.getElementById("pd-gender").innerText = data.gender
        document.getElementById("pd-age").innerText = data.age
        document.getElementById("pd-price").innerText = data.price
        document.getElementById("pd-description").innerText = data.description
        document.getElementById("pd-author").innerText = data.author
        document.getElementById("pd-created-on").innerText = data.created_on

            // const parent = document.getElementById("pet-details-container")
            // const div = document.createElement("div")
            // div.classList.add("pet-datils")
            // div.innerHTML=`
                    

            // `
            // parent.appendChild(div)
    })
    
}
const loadReview = () =>{
    const param = new URLSearchParams(window.location.search).get("pet_id")
    fetch(`http://127.0.0.1:8000/customer/review/?search=${param}`)
    .then((res)=>res.json())
    .then((data)=> {
        data.forEach((review) =>{
            console.log(review)
            const parent = document.getElementById("pet-all-review")
            const div = document.createElement("div")
            div.classList.add("review")
            div.innerHTML =`
                   
                    
                        <div class="bg-white shadow-[0_4px_12px_-5px_rgba(0,0,0,0.4)] px-6 py-8 w-full max-w-sm rounded-lg font-[sans-serif] overflow-hidden mx-auto mt-4">
                        <h3 class="text-xl font-bold flex-1 text-gray-800">Reviews</h3>
                            <div class="flex flex-wrap items-center gap-4">
                                <div>
                                    <div class="flex flex-wrap items-center cursor-pointer shadow-[0_2px_6px_-1px_rgba(0,0,0,0.3)] rounded-lg w-full p-4">
                                        <img src='https://readymadeui.com/profile_4.webp' class="w-10 h-10 rounded-full" />
                                    <div class="ml-4 flex-1">
                                            <p class="text-sm text-gray-800 font-semibold">${review.reviewer}</p>
                                            <p class="text-xs text-gray-500 mt-0.5">${review.body}</p>
                                            <p class="text-xs text-gray-500 mt-0.5">${review.rating}</p>
                                            <p class="text-xs text-gray-500 mt-0.5">${review.created_on}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

            `
            parent.appendChild(div)
        })
    })
}


// document.addEventListener("DOMContentLoaded", () => {
//     const token = localStorage.getItem("token");
//     const userName = localStorage.getItem("username");
//     const petId = localStorage.getItem("pet_id");

//     const detailsBTN = document.getElementById("details-btn")
//     console.log(detailsBTN); // Check if the element exists

//     // Fetch pet details
//     fetch(`http://127.0.0.1:8000/pet/post/${petId}/`, {
//         method: "GET",
//         headers: {
//             "Content-Type": "application/json",
//             "Authorization": `Token ${token}`,
//         }
//     })
//     .then((res) => res.json())
//     .then((data) => {
//         if (data.author === userName) {
//             console.log("Usernames match. Displaying buttons.");
//             detailsBTN.innerHTML = `
//                 <a href="./editPost.html?pet_id=${data.id}" id="edit-pet" class=" text-xl font-mono text-center m-3 border-b-4 border-black hover:border-gray-200 p-1 font-extrabold">Edit</a>
//                 <a href="./addpost.html" class=" text-xl font-mono text-center m-3 border-b-4 border-black hover:border-gray-200 p-1 font-extrabold ">Add New</a>
//                 <button type="submit" onclick="deletePet()" id="delete-pet" class=" text-xl font-mono text-center text-red-700 m-3 border-b-4 border-black hover:border-red-700 p-1 font-extrabold ">Delete</button>             
//             `
//         } else {
//             console.log("Usernames do not match. Hiding buttons.");
//             detailsBTN.innerHTML=`
//                 <a href="./addpost.html" class=" text-xl font-mono text-center m-3 border-b-4 border-black hover:border-gray-200 p-1 font-extrabold ">Add New</a>

//             `
//         }
//     })
//     .catch((error) => {
//         console.error("Error fetching pet details:", error);
//     });
// });


getParams()
loadReview()