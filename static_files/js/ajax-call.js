function filter(e){
    var csrf_token = $(e).data("csrf-token");
    var arr = Array()
    $('input:checkbox.checkbox').each(function () {
       var val = (this.checked ? $(this).val() : "");
       if (val){
        arr.push(val);
       }
    
  });
  console.log(arr);

      $.ajax({
        type:'POST',
        url: "ajax/filter-image/",
        data : {'cat':arr},
        success: function (resp) {
            console.log(resp)
            $("#image-card-id").html('');
            if (resp.length>0){
                for (var i=0; i<resp.length; i++){
                  console.log(resp[i]['image'])
                  innerHTML = `<li class="cards_item">
                                <div class="card">
                                  <div class="card_image image-fluid"><img src="${resp[i]['image']}"></div>
                                  <div class="card_content">
                                    <button type="button" class="btn card_btn">${resp[i]['title']}</button>
                                  </div>
                                </div>
                              </li>`
                   $("#image-card-id").append(innerHTML);
                }
              }else{
                innerHTML = `No Image Found, Please upload it !`
                 $("#image-card-id").append(innerHTML);
              }
             
            
        },
        error: function(err) {
            console.log(err);
        }
      });
}