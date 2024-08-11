const loadAllProduct = (search = '') => {
    console.log(search);
    const parent = document.getElementById("products")
    parent.innerHTML = ""
    fetch(`https://fakestoreapi.com/products`)
        .then((res) => res.json())
        .then((data) => {
            const filteredProducts = data.filter(product => 
                product.title && product.title.toLowerCase().includes(search.toLowerCase())
            );
            displayAllProduct(filteredProducts);
        })
};

const displayAllProduct = (products) =>{
    console.log(products)
    products?.forEach((product)=>{
        const parent = document.getElementById("products")
        const div = document.createElement("div")
        div.classList.add("pro-card")
        div.innerHTML=`
                <div class="wsk-cp-product">
                    <div class="wsk-cp-img">
                        <img src="${product.image}" />
                    </div>
                    <div class="wsk-cp-text">
                        <div class="category">
                            <span>${product.category}</span>
                        </div>
                        <div class="title-product">
                            <h3>${product.title}</h3>
                        </div>
                        <div class="description-prod">
                            <p>${product.description.slice(0,70)}</p>
                        </div>
                        <div class="card-footer">
                            <div class="wcf-left"><span class="price"><strong>Price: </strong> ${product.price}</span></div>
                            <div class="wcf-right"><a target="_blank" href="details.html?productId=${product.id}" class="buy-btn">Details</a></div>
                        </div>
                    </div>
                </div>

        `
        parent.appendChild(div)
    })
}


const handleSearch = () => {
    const value = document.getElementById("search-bar").value;
    loadAllProduct(value);
};

const loadAllCategories = () =>{
    fetch('https://fakestoreapi.com/products/categories')
            .then(res=>res.json())
            .then(json=>displayAllCategories(json))
}

const displayAllCategories = (categories) =>{
    console.log(categories)
    categories?.forEach((category)=>{
        const parent = document.getElementById("categories")
        const div = document.createElement("div")
        div.classList.add("cat-btn-div")
        div.innerHTML=`
            <button onclick="loadCategoryWise('${category.replace(/'/g, "\\'")}')" class="cat-btn">${category}</button>
        `
        parent.appendChild(div)
    })
}

const loadCategoryWise = (search) =>{
    console.log(search)
    const parent = document.getElementById("products")
    parent.innerHTML = ""
    fetch(`https://fakestoreapi.com/products/category/${search}`)
        .then(res=>res.json())
        .then(json=> displayCategoryWise(json))     
}

const displayCategoryWise = (products) =>{
    console.log(products)
    const parent = document.getElementById("products")
    parent.innerHTML = ""
    products?.forEach((product)=>{
        const parent = document.getElementById("products")
        const div = document.createElement("div")
        div.classList.add("pro-card")
        div.innerHTML=`
                <div class="wsk-cp-product">
                    <div class="wsk-cp-img">
                        <img src="${product.image}" />
                    </div>
                    <div class="wsk-cp-text">
                        <div class="category">
                            <span>${product.category}</span>
                        </div>
                        <div class="title-product">
                            <h3>${product.title}</h3>
                        </div>
                        <div class="description-prod">
                            <p>${product.description.slice(0,70)}</p>
                        </div>
                        <div class="card-footer">
                            <div class="wcf-left"><span class="price"><strong>Price: </strong> ${product.price}</span></div>
                            <div class="wcf-right"><a target="_blank" href="details.html?productId=${product.id}" class="buy-btn">Details</a></div>
                        </div>
                    </div>
                </div>
        `
        parent.appendChild(div)
    })
}

loadAllProduct();
loadAllCategories();
