$(document).ready(function(){
    console.log('ready to go!')
    $('.quantity-right-plus').click(function(e){
        e.preventDefault();
        var quantity = parseInt($('#quantity').val());
            $('#quantity').val(quantity + 1)
            $('#quantity').change(cart[key] =) 
            // FIX TO ADJUST QUANTITY USING AJAX!!!!!
    })

    $('.quantity-left-minus').click(function(e){
        e.preventDefault();
        var quantity = parseInt($('#quantity').val());
        if (quantity > 0) {
            $('#quantity').val(quantity - 1)
            console.log($('#quantity').val())
        }
    })
})