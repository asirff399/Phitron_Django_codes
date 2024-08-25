const loadAllService = () =>{
    fetch("http://127.0.0.1:8000/service/")
    .then((res)=>res.json())
    .then((data)=>{
        console.log(data)
        data.forEach((service)=>{
            const parent = document.getElementById("services-container")
            const div = document.createElement("div")
            div.classList.add("service")
            div.innerHTML=`
                <div class="bg-white w-full rounded-lg overflow-hidden shadow-lg" >
                    <img src=${service.image} alt="Blog Post 1" class="w-full h-52 object-cover" />
                    <div class="p-6">
                    <h3 class="text-xl font-bold text-gray-800 mb-2">${service.name}</h3>
                    <p class="text-gray-600 text-sm">${service.description.slice(0,30)}...</p>
                    <a href="service_detail.html?service_id=${service.id}" class="mt-4 inline-block text-blue-600 text-sm hover:underline">Read More</a>
                    </div>
                </div>

            `
            parent.appendChild(div)
        })
    })
}

const getParams = ()=>{
    const param = new URLSearchParams(window.location.search).get("service_id")
    console.log(param)
    
    fetch(`http://127.0.0.1:8000/service/${param}`)
    .then((res)=>res.json())
    .then((data)=> {
        console.log(data)
            const parent = document.getElementById("service-details-container")
            const div = document.createElement("div")
            div.classList.add("service-datils")
            div.innerHTML=`
                <div class="bg-gray-50 w-full rounded-lg font-[sans-serif] overflow-hidden max-w-5xl mx-auto">
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 items-center">
                        <img src=${data.image} class="w-full rounded-lg m-4 h-full object-cover shrink-0" />
                        <div class="lg:col-span-2 p-10">
                        <h1 class="text-3xl font-bold text-gray-800">${data.name}</h1>
                        <p class="mt-4 text-sm text-gray-500 leading-relaxed">${data.description}</p>

                        <button type="button"
                            class="px-6 py-3 mt-8 rounded-lg text-white text-sm tracking-wider border-none outline-none bg-black "><a href="./index.html">Back Home</a></button>
                        </div>
                    </div>
                </div>

            `
            parent.appendChild(div)
    })
    
}


getParams()
loadAllService()