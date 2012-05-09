jQuery(function() {

   var doc = jQuery(document)
   doc.on('click', '.removebutton', function(e){
     url = jQuery(this).attr('data-url');
     id  = jQuery(this).attr('data-id');
     if (confirm(w2p_ajax_confirm_message)) {
        ajax(url, null, ":eval");
     }
   })
});
