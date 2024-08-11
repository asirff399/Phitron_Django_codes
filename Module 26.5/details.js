const getparams = () =>{
    const param = new URLSearchParams(window.location.search).get("productId")
    console.log(param)
    fetch(`https://fakestoreapi.com/products/${param}`)
    .then((res) => res.json())
    .then((data) => displayDetails(data))
}


const displayDetails = (product) =>{
    console.log(product)
    const parent = document.getElementById("details")
    const div = document.createElement("div")
    div.classList.add("pro-details")
    div.innerHTML=`
        <div class="wrapper">
            <div class="product-img">
                <img src="${product.image}" alt="">
            </div>
            <div class="product-info">
                <div class="product-text">
                    <h1>${product.title}</h1>                  
                    <h3>${product.category}</h3>
                    <h2>by studio and friends</h2>
                    <p>${product.description}</p>
                    <h4><strong>Price: </strong><span>${product.price}</span>$</h4>
                </div>
                <div class="product-price-btn ">
                    <button type="button">buy now</button>
                </div> 
            </div>
        </div>

        `
        parent.appendChild(div)
}

getparams()

