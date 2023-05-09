$('.plus-cart').click(function(){
  var id=$(this).attr("pid").toString();
  var eml = this.parentNode.children[2]
  console.log("pid =",id)
  $.ajax({
    type:"GET",
    url:"/pluscart",
    data:{
      prod_id:id
    },
    success:function(data){
      console.log("data =",data);
      eml.innerText=data.quantity
      document.getElementById("amount").innerText=data.amount
      document.getElementById("totalamount").innerText=data.totalamount
    }
  })
})

$('.minus-cart').click(function(){
  var id=$(this).attr("pid").toString();
  var eml = this.parentNode.children[2]
  $.ajax({
    type:"GET",
    url:"/minuscart",
    data:{
      prod_id:id
    },
    success:function(data){
      eml.innerText=data.quantity
      document.getElementById("amount").innerText=data.amount
      document.getElementById("totalamount").innerText=data.totalamount
    }
  })
})

$('.remove-cart').click(function(index, element){
  var id = $(this).attr("pid", id.toString());
  console.log("Product ID: ", id);
  
  var eml = this;
  
  $.ajax({
    type: "GET",
    url: "/removecart",
    data: {
      prod_id: id
    },
    success: function(data){
      console.log("AJAX Success:", data);
      
      document.getElementById("amount").innerText = data.amount;
      console.log("Updated amount:", data.amount);
      
      document.getElementById("totalamount").innerText = data.totalamount;
      console.log("Updated total amount:", data.totalamount);
      
      eml.parentNode.parentNode.parentNode.parentNode.remove();
      console.log("Removed element:", eml);
    },
    error: function(xhr, status, error) {
      console.log("AJAX Error:", error);
    }
  });
});









     