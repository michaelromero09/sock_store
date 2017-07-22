$(document).ready(function(){
    var quantity = 1;
    console.log('ready to go!')
    $('.quantity-right-plus').click(function(e){
        console.log('Test')
        e.preventDefault();
        var quantity = parseInt($('#quantity').val());
            $('#quantity').val(quantity + 1)
            console.log($('#quantity').val())
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