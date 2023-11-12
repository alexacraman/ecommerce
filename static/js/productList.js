
document.addEventListener('DOMContentLoaded', ()=>{
    const addToCartButtons      = document.querySelectorAll('.add-button');
    const removeFromCartButtons = document.querySelectorAll('.remove-button');
    const cartInfoElement = document.getElementById('cart-info');
    const svg = '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" /></svg>'
    addToCartButtons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const url = event.target.dataset.url;
            addItem(url);
        });
    });

    removeFromCartButtons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const url = event.target.dataset.url;
            removeItem(url);
        });
    });

    async function addItem(url){
        const csrftoken = getCookie('csrftoken')
        console.log(csrftoken)
        const options = {
            method: 'POST',
            mode: 'same-origin',
            headers: {
                'X-CSRFToken': csrftoken
            }
        }
        try{
            const response = await fetch(url, options)
            const data = await response.json()
            if (data){
                const cartCount = data.data.cart_count
                const cartCost  = data.data.cart_cost
                console.log('£', cartCost, 'item', cartCount)
                if(cartInfoElement){
                    cartInfoElement.innerHTML = `${svg} £${cartCost}  ${cartCount} item${cartCount !== 1 ? 's' : ''}, `;
                }
                
            }  
        }catch(error){
            console.error('There was an error', error)
        
        }
    }

    async function removeItem(url) {
        const csrftoken = getCookie('csrftoken');
        const options = {
            method: 'POST',
            mode: 'same-origin',
            headers: {
                'X-CSRFToken': csrftoken
            }
        };
        try {
            const response = await fetch(url, options);
            const data = await response.json();
            if (data){
                const cartCount = data.data.cart_count
                const cartCost  = data.data.cart_cost
                console.log('£', cartCost, 'item', cartCount)
                cartInfoElement.innerHTML = `${svg} £${cartCost}  ${cartCount} item${cartCount !== 1 ? 's' : ''}, `;
            } 
        } catch (error) {
            console.error('There was an error', error);
        }
    }
})
