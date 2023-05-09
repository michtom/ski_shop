function hide_question(){
    let checkbox = document.getElementById("delivery");
    let to_be_hidden = document.getElementById("address");
    let address = document.getElementById("address_value");
    if(checkbox.checked){
        to_be_hidden.style.display = 'block';
    }
    else{
        to_be_hidden.style.display = 'none';
        address.value = "Company Address, 11-111 Example City";
    }
}
function calculate_price(){
    const items_number = document.getElementById("items_number").value;
    const price = document.getElementById("price").value;
    document.getElementById("money_amount").value = price*items_number.toString();
}
function validate_address(){
    const address = document.getElementById("address_value").value;
    const regex = /[0-9][0-9]-[0-9][0-9][0-9]/g;
    if(address.match(regex) == null){
        window.alert("Address must contain a proper postal code. (XX-XXX format)");
        return false;
    }
    return true;
}
