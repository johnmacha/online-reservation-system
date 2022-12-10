
carts = document.querySelectorAll('.add-cart'); 

 goods = [
    {
        name: 'Gas Cooker',
        tag:'gas cooker',
        price:27500,
        inCart:0
    },

    {
        name: 'Radio',
        tag:'bluetooth radio',
        price:23000,
        inCart:0
    },

    {
        name: 'Iron Box',
        tag:'iron box',
        price:17000,
        inCart:0
    },

    {
        name: 'Fridge',
        tag:'fridge',
        price:30000,
        inCart:0
    }
]


for (let i=0; i < carts.length; i++){
carts[i].addEventListener('click' ,() => {
    cartNumbers(goods[i]);
    totalCost(goods[i]);
})

}

function onLoadCartNumbers(){
    let productNumbers = localStorage.getItem('cartNumbers');

    if(productNumbers){
    document.querySelector('.count span').textContent = productNumbers;
    }
}

function cartNumbers(good){

    let productNumbers = localStorage.getItem('cartNumbers');
    productNumbers = parseInt(productNumbers);

    if(productNumbers) {
        localStorage.setItem('cartNumbers', productNumbers+1);
        document.querySelector('.count span').textContent = productNumbers+1;
    }
     else{
        localStorage.setItem('cartNumbers', 1);
        document.querySelector('.count span').textContent = 1;
     }

setItems(good);

}

function setItems(good){
let cartItems = localStorage.getItem('goodsinCart');
cartItems = JSON.parse(cartItems);


if(cartItems != null){ //when not null

if(cartItems[good.tag] == undefined){
cartItems= {
    ...cartItems,
    [good.tag]:good

}
}
cartItems[good.tag].inCart +=1;
}

else { //when null

    good.inCart = 1;

    cartItems = {
       [good.tag]:good
   }
}

localStorage.setItem("goodsinCart",JSON.stringify(cartItems ));
  
}

function totalCost(good){
//console.log("The item price is ",good.price);
let itemCost = localStorage.getItem('totalCost');
console.log("My cartCost is ",itemCost);
console.log(typeof itemCost);

if(itemCost !=null) {//when not null
    itemCost = parseInt (itemCost);

localStorage.setItem("totalCost" ,itemCost + good.price)
}
else{ //when null
    localStorage.setItem("totalCost",good.price);

}

}
function displayCart() {
let cartItems = localStorage.getItem("goodsinCart");
cartItems = JSON.parse(cartItems);
let productContainer = document.querySelector(".product");
let itemCost = localStorage.getItem('totalCost');


console.log(cartItems);

if( cartItems && productContainer ){
productContainer.innerHTML = ''; //initially empty
Object.values(cartItems).map(item => {
productContainer.innerHTML += 
// use back-ticks
      `
<div class="product">
 <img id="remove" style="width:20px;height:20px;margin-left:10px;margin-right:10px;cursor:pointer;" src="./images/closebtn.png" class="remove">
<img style="width:65%; height:65%;" src="./images/${item.tag}.jpg">
<span>${item.name}</span>
</div>

<div  class="quantity">
<img style="cursor:pointer;" src="decrease.png" class="lessBtn">
<span>${item.inCart}</span>
<img style="cursor:pointer;" src="increase.png" class="addBtn">

</div>

<div class="total">
Sh.${item.inCart*item.price}.00
</div>
     `;
});

productContainer.innerHTML += `
<div class="cartTotalContainer">
<h4 class="cartTotalTitle">
Cart Total  
</h4>
<h4 class="cartTotal">   
Sh.${itemCost}.00
</h4>
`
}

}
//click events to remove items from list

function deleteItem(){
    let cart= JSON.parse(localStorage.getItem('cartItem'));
    let newcart = cart.filter((goods) => item.inCart !=goods );
    localStorage.setItem('cartItem',JSON.stringify(newcart));
    updateCart() ;

}
    
onLoadCartNumbers() ;
displayCart();

//let counter = document.querySelector('');
//let count = 1;

//setInterval(()=>{
//counter.innerText = count;
//count++

//}, 1000)

