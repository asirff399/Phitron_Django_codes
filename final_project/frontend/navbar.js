fetch("navbar.html")
.then(res => res.text())
.then((data) => {
    document.getElementById("navbar").innerHTML= data;
	// Assign navElement
	const navElement = document.getElementById("nav-element")

		const token = localStorage.getItem("token")
		// console.log(token)

		if(token){
			navElement.innerHTML=`
				<a href="./profile.html" class="text-xl font-mono text-center m-3 hover:border-b-4 hover:border-black p-1 font-extrabold ">Profile</a>
			`
			
		}
		else{
			navElement.innerHTML=`
				<div class="flex font-semibold ">
						<a href="./login.html" class=" text-xl font-mono text-center m-3 hover:border-b-4 hover:border-black p-1 font-extrabold ">LOGIN</a>
						<a href="./registration.html" class=" text-xl font-mono text-center m-3 hover:border-b-4 hover:border-black p-1 font-extrabold ">REGISTER</a>
				</div>
			`
		}

})

function closeOpenDropdowns(e) {
	let openDropdownEls = document.querySelectorAll("details.dropdown[open]");

	if (openDropdownEls.length > 0) {
		// If we're clicking anywhere but the summary element, close dropdowns
		if (e.target.parentElement.nodeName.toUpperCase() !== "SUMMARY") {
			openDropdownEls.forEach((dropdown) => {
				dropdown.removeAttribute("open");
			});
		}
	}
}

document.addEventListener("click", closeOpenDropdowns);


let dropdownToggle = document.getElementById('dropdownToggle');
let dropdownMenu = document.getElementById('dropdownMenu');

function handleClick() {
    if (dropdownMenu.className.includes('block')) {
        dropdownMenu.classList.add('hidden')
        dropdownMenu.classList.remove('block')
    } else {
        dropdownMenu.classList.add('block')
        dropdownMenu.classList.remove('hidden')
    }
}

dropdownToggle.addEventListener('click', handleClick);





