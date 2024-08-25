const loadUserDetails = () => {
  const user_id = localStorage.getItem("user_id");
  console.log(user_id);

  fetch(`http://127.0.0.1:8000/users/${user_id}`)
    .then((res) => res.json())
    .then((data) => {
      localStorage.setItem("username", data.username);
      // console.log(data)
      document.getElementById(
        "profile-username"
      ).innerText = `${data.first_name} ${data.last_name}`;
      const parent = document.getElementById("profile-details");
      const div = document.createElement("profile-all");
      div.classList.add("profile-all");
      div.innerHTML = `
                <div class="user-img">
                    <img id="profile-card-img" src="" alt="" />
                </div>
                <div class="m-5 font-mono  ">
                    <h2 class="text-4xl mb-5 text-center my-2">${data.first_name} ${data.last_name}</h2>
                    <h6 class="leading-none  text-lg text-gray-900 "><strong>Username:</strong> ${data.username}</h6>
                    <h4 class="m-2" ><strong>Email:</strong> ${data.email}</h4>
                    <h4 class="m-2" ><strong>Balance:  $ </strong><span class="font-bold" id="balance"></span></h4>
                </div>      
        
        `;
      parent.appendChild(div);
    });
  const customer_id = localStorage.getItem("customer_id");
  fetch(`http://127.0.0.1:8000/customer/list/${customer_id}`)
    .then((res) => res.json())
    .then((data) => {
      // console.log(data)
      document.getElementById("balance").innerText = `${data.balance}`;
      document.getElementById("profile-img").src = `${data.image}`;
      document.getElementById("profile-card-img").src = `${data.image}`;
    });
};
const loadCustomerId = () => {
  const user_id = localStorage.getItem("user_id");
  fetch(`http://127.0.0.1:8000/customer/list/?search=${user_id}`)
    .then((res) => res.json())
    .then((data) => localStorage.setItem("customer_id", data[0].id));
};
const changePass = (event) => {
  event.preventDefault();

  const oldPassword = document.getElementById("old_password").value;
  const newPassword = document.getElementById("new_password").value;
  const token = localStorage.getItem("token");
  console.log(token);
  const data = {
    old_password: oldPassword,
    new_password: newPassword,
  };
  console.log(data);

  fetch("http://127.0.0.1:8000/customer/pass_change/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`,
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((data) => (window.location.href = "./profile.html"));
};

const deposit = (event) => {
  event.preventDefault();
  alert("Not working");
  const form = document.getElementById("deposit-form");
  const formData = new FormData(form);
  const data = {
    amount: formData.get("deposit"),
  };

  console.log(data);
  const token = localStorage.getItem("token");
  console.log(token);
  console.log("Deposit function called");
  fetch("http://127.0.0.1:8000/transaction/deposit/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`,
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      alert("Message sent successfully!");
      // window.location.href = "./profile.html";
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("There was a problem sending your message.");
    });
};
document.getElementById("deposit-form").addEventListener("submit", deposit);

loadUserDetails();
loadCustomerId();
// document.querySelector('[data-drawer-show="drawer-navigation"]').click();
document.addEventListener("DOMContentLoaded", function () {
  const drawerButton = document.querySelector(
    '[data-drawer-show="drawer-navigation"]'
  );
  if (drawerButton) {
    drawerButton.click();
  } else {
    console.error(
      "Element with data-drawer-show='drawer-navigation' not found."
    );
  }
});
