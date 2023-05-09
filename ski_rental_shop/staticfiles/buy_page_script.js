const checkbox = document.getElementById("delivery")
const address = document.getElementById("address")
checkbox.addEventListener("click", (e) => {
    address.hidden = !e.target.checked;
});