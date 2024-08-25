function formatDate(dateStr) {
    const date = new Date(dateStr);
    const options = { 
        day: 'numeric', 
        month: 'long',  
    };
    return date.toLocaleString('en-US', options).replace(" at", "");
}
const loadAllPet = () =>{
    fetch("http://127.0.0.1:8000/all_pet/")
    .then((res)=>res.json())
    .then((data)=>{
        displayAllPet(data)
    })
}
const loadInitialPet = () =>{
    fetch("http://127.0.0.1:8000/all_pet/")
    .then((res)=>res.json())
    .then((data)=>{
        displayInitialPet(data.slice(0,3))
    })
}
const displayAllPet = (pets) =>{
    // console.log(pets)
    document.getElementById("all-pet").innerHTML = ""
    pets.forEach((pet)=>{
        const parent = document.getElementById("all-pet")
        const div = document.createElement("div")
        div.classList.add("pet-card")
        const formattedDate = formatDate(pet.created_on);
        div.innerHTML=`
                <div class="mx-auto bg-gray-200 mb-10 w-96 transform overflow-hidden rounded-lg bg-white dark:bg-slate-800 shadow-lg duration-300 hover:scale-105 hover:shadow-lg">
                    <img class="h-48 w-full object-cover object-center" src=${pet.image} alt="Product Image" />
                    <div class="p-4 text-center">
                        <h1 class="mb-2 text-2xl font-medium dark:text-white text-gray-900"><strong>${pet.name}</strong> </h1>
                        <p class="mb-2 text-base dark:text-gray-300 text-gray-700">${pet.description.slice(0,40)}...</p>
                        <div class="flex justify-evenly items-center">
                            <p class="mr-2 text-lg font-semibold text-gray-900 dark:text-white">$${pet.price}</p>
                            <h2 class="font-bold ">${pet.adoption_status }</h2>

                        </div>
                        <div class="flex mt-7">
                        <button type="button" class="w-1/3 focus:outline-none text-white bg-black hover:bg-yellow-500 focus:ring-4 focus:ring-yellow-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:focus:ring-yellow-900"><a href="./pet_details.html?pet_id=${pet.id}">Details</a> </button>
                        </div>
                        
                        <div>
                            <p class="text-sm mt-7">Created By <a class="text-red-500 underline" href="">${pet.author}</a> on ${formattedDate}</p>
                        </div>
                    </div>
                </div> 
        
        `
        parent.appendChild(div)
    })
}
const displayInitialPet = (pets) =>{
    // console.log(pets)
    // document.getElementById("initial-pet").innerHTML = ""
    pets.forEach((pet)=>{
        const parent = document.getElementById("initial-pet")
        const div = document.createElement("div")
        div.classList.add("pet-card")
        const formattedDate = formatDate(pet.created_on);
        div.innerHTML=`
                <div class="mx-auto mt-11 mb-10 w-96 transform overflow-hidden rounded-lg bg-white dark:bg-slate-800 shadow-lg duration-300 hover:scale-105 hover:shadow-lg">
                    <img class="h-48 w-full object-cover object-center" src=${pet.image} alt="Product Image" />
                    <div class="p-4 text-center">
                        <h1 class="mb-2 text-2xl font-medium dark:text-white text-gray-900"><strong>${pet.name}</strong> </h1>
                        <p class="mb-2 text-base dark:text-gray-300 text-gray-700">${pet.description.slice(0,50)}...</p>
                        <div class="flex justify-evenly items-center">
                            <p class="mr-2 text-lg font-semibold text-gray-900 dark:text-white">$${pet.price}</p>
                            <h2 class="font-bold ">${pet.adoption_status }</h2>
                        </div>
                        <div class="flex mt-7">
                            <button type="button" class="w-1/3 focus:outline-none text-white bg-black hover:bg-yellow-500 focus:ring-4 focus:ring-yellow-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:focus:ring-yellow-900"><a href="./pet_details.html?pet_id=${pet.id}">Details</a> </button>
                        </div>
                        <div>
                            <p class="text-sm mt-7">Created By <a class="text-red-500 underline" href="">${pet.author}</a> on ${formattedDate}</p>
                        </div>
                    </div>
                </div> 
        
        `
        parent.appendChild(div)
    })
}
const loadPetCategoryWise = (search) =>{
    // console.log(search)
    fetch(`http://127.0.0.1:8000/pet/list/?search=${search? search : "" }`)
    .then((res)=>res.json())
    .then((data)=>{
        // displayPetCategoryWise(data?.results)
        displayAllPet(data)
    })
}
const getParam = () =>{
    const param = new URLSearchParams(window.location.search).get("page")
    // console.log(param)
    loadPetPageBy(param)
}
// const loadPetPageBy = (search) =>{
//     console.log(search)
//     fetch(`http://127.0.0.1:8000/pet/list/?page=${search? search : "" }`)
//     .then((res)=>res.json())
//     .then((data)=>{
//         displayPetCategoryWise(data?.results)
//     })
// }
const displayPetCategoryWise = (pets) =>{
    // console.log(pets)
    document.getElementById("category-pet").innerHTML = ""
    pets.forEach((pet)=>{
        const parent = document.getElementById("category-pet")
        const div = document.createElement("div")
        div.classList.add("pet-card")
        div.innerHTML=`
                <div class="mx-auto bg-gray-200 mt-11 w-96 transform overflow-hidden rounded-lg bg-white dark:bg-slate-800 shadow-lg duration-300 hover:scale-105 hover:shadow-lg">
                    <img class="h-48 w-full object-cover object-center" src=${pet.image} alt="Product Image" />
                    <div class="p-4 ">
                        <h1 class="mb-2 text-lg font-medium dark:text-white text-gray-900"><strong>${pet.name}</strong> </h1>
                        <p class="mb-2 text-base dark:text-gray-300 text-gray-700">${pet.description.slice(0,50)}...</p>
                        <div class="flex justify-evenly items-center">
                            <p class="mr-2 text-lg font-semibold text-gray-900 dark:text-white">$${pet.price}</p>
                            <h2 class="font-bold ">${pet.adoption_status }</h2>
                        </div>
                        <div class="flex mt-7">
                            <button type="button" class="w-1/2 focus:outline-none text-white bg-black hover:bg-yellow-500 focus:ring-4 focus:ring-yellow-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:focus:ring-yellow-900"><a href="./pet_details.html?pet_id=${pet.id}">Details</a></button>
                        </div>
                        
                    </div>
                </div> 
        
        `
        parent.appendChild(div)
    })
}
const loadAllPetType = () =>{
    fetch("http://127.0.0.1:8000/pet/types/")
    .then((res)=>res.json())
    .then((data)=>{
        // console.log(data)
        data.forEach((type)=>{
            const parent = document.getElementById("pet-types")
            const div = document.createElement("div")
            div.classList.add("pet-ty")
            div.innerHTML=`               
                <button type="button" onclick="loadPetCategoryWise('${type.name}')"
                    class="bg-white py-2 px-7 shadow-xl shadow-purple-200 rounded-full text-black text-sm tracking-wider font-medium outline-none border border-purple-600 active:shadow-inner">${type.name}
                </button>            
            `
            parent.appendChild(div)
        })
    })
}
const loadPetTypePost = () =>{
    const token = localStorage.getItem("token")
    fetch("http://127.0.0.1:8000/pet/types/",{
        method:"GET",
        headers:{
            "Content-Type":"application/json",
            "Authorization": `Token ${token}`,}
    })
    .then((res)=>res.json())
    .then((data)=>{
        // console.log(data)
        data.forEach((item)=>{
            // console.log(item) 
            const parent = document.getElementById("pet-type")
            const option = document.createElement("option")

            option.value = item.id
            option.innerHTML = item.name

            parent.appendChild(option)
        })
    })
}
const loadPetTypeEdit = () =>{
    const token = localStorage.getItem("token")
    fetch("http://127.0.0.1:8000/pet/types/",{
        method:"GET",
        headers:{
            "Content-Type":"application/json",
            "Authorization": `Token ${token}`,}
    })
    .then((res)=>res.json())
    .then((data)=>{
        // console.log(data)
        data.forEach((item)=>{
            // console.log(item) 
            const parent = document.getElementById("ed-pet-type")
            const option = document.createElement("option")

            option.value = item.id
            option.innerHTML = item.name

            parent.appendChild(option)
        })
    })
}

const loadAllMember = () =>{
    fetch("http://127.0.0.1:8000/member/")
    .then((res)=>res.json())
    .then((data)=>{
        // console.log(data)
        data.forEach((member)=>{
            const parent = document.getElementById("team_members")
            const div = document.createElement("div")
            div.classList.add("member")
            div.innerHTML=`
                    <div class="bg-gray-200 relative rounded">
                    <img src=${member.image} class="w-32 h-32 rounded-full inline-block -mt-12" />

                    <div class="py-4">
                        <h4 class="text-gray-800 text-base font-extrabold">${member.name}</h4>
                        <p class="text-gray-800 text-xs mt-1 uppercase">${member.type}</p>

                    <div class="space-x-4 mt-4">
                            <button type="button"
                                class="w-7 h-7 inline-flex items-center justify-center rounded-full border-none outline-none bg-gray-100 hover:bg-gray-200">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12px" class="fill-gray-800" viewBox="0 0 155.139 155.139">
                                    <path
                                        d="M89.584 155.139V84.378h23.742l3.562-27.585H89.584V39.184c0-7.984 2.208-13.425 13.67-13.425l14.595-.006V1.08C115.325.752 106.661 0 96.577 0 75.52 0 61.104 12.853 61.104 36.452v20.341H37.29v27.585h23.814v70.761h28.48z"
                                        data-original="#010002" />
                                </svg>
                            </button>
                            <button type="button"
                                class="w-7 h-7 inline-flex items-center justify-center rounded-full border-none outline-none  bg-gray-100 hover:bg-gray-200">
                                <svg xmlns="http://www.w3.org/2000/svg" width="12px" class="fill-gray-800" viewBox="0 0 512 512">
                                    <path
                                        d="M512 97.248c-19.04 8.352-39.328 13.888-60.48 16.576 21.76-12.992 38.368-33.408 46.176-58.016-20.288 12.096-42.688 20.64-66.56 25.408C411.872 60.704 384.416 48 354.464 48c-58.112 0-104.896 47.168-104.896 104.992 0 8.32.704 16.32 2.432 23.936-87.264-4.256-164.48-46.08-216.352-109.792-9.056 15.712-14.368 33.696-14.368 53.056 0 36.352 18.72 68.576 46.624 87.232-16.864-.32-33.408-5.216-47.424-12.928v1.152c0 51.008 36.384 93.376 84.096 103.136-8.544 2.336-17.856 3.456-27.52 3.456-6.72 0-13.504-.384-19.872-1.792 13.6 41.568 52.192 72.128 98.08 73.12-35.712 27.936-81.056 44.768-130.144 44.768-8.608 0-16.864-.384-25.12-1.44C46.496 446.88 101.6 464 161.024 464c193.152 0 298.752-160 298.752-298.688 0-4.64-.16-9.12-.384-13.568 20.832-14.784 38.336-33.248 52.608-54.496z"
                                        data-original="#03a9f4" />
                                </svg>
                            </button>
                            <button type="button"
                                class="w-7 h-7 inline-flex items-center justify-center rounded-full border-none outline-none  bg-gray-100 hover:bg-gray-200">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14px" class="fill-gray-800" viewBox="0 0 24 24">
                                    <path
                                        d="M23.994 24v-.001H24v-8.802c0-4.306-.927-7.623-5.961-7.623-2.42 0-4.044 1.328-4.707 2.587h-.07V7.976H8.489v16.023h4.97v-7.934c0-2.089.396-4.109 2.983-4.109 2.549 0 2.587 2.384 2.587 4.243V24zM.396 7.977h4.976V24H.396zM2.882 0C1.291 0 0 1.291 0 2.882s1.291 2.909 2.882 2.909 2.882-1.318 2.882-2.909A2.884 2.884 0 0 0 2.882 0z"
                                        data-original="#0077b5" />
                                </svg>
                            </button>
                        </div>     
                    </div>
                </div>
            `
            parent.appendChild(div)
        })
    })
}

// getParam()
document.addEventListener("DOMContentLoaded", function() {
    loadInitialPet()
    loadAllPetType();
    loadAllPet()
    loadAllMember();
});
document.addEventListener("DOMContentLoaded", () => {
    loadPetTypePost();
    loadPetTypeEdit()
});
// loadPetTypePost()
// loadAllPetType()


 