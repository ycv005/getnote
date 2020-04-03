$(document).ready(function(){
    $(document).on('submit',"#note-form",function(e){
        e.preventDefault();
        var modal = $("#addNoteModel");
        var form = $("#note-form");
        var url = form.attr("action");
        var httpMethod = form.attr("method");
        $.ajax({
        url: url,
        method: httpMethod,
        data: $(this).serialize(),
        success: function(data){
            document.getElementById("note-form").reset();
            modal.modal('toggle');
            var shortText = jQuery.trim(data.text).substring(0, 80)
            var shortTitle = jQuery.trim(data.title).substring(0, 21)
            // adding div element 
        // we can't include the snippet bcoz- Any jQuery calls will happen after the DOM is loaded. While any include statements will happen before.
            $(".note-list-row").prepend(
                '<div class="col-3">'+
                    '<div class="card shadow mb-3 bg-white rounded" style="width: 16rem;">'+
                        '<div class="card-body">'+
                            '<h5 class="card-title">'+shortTitle+'</h5>'+
                            '<small class="card-subtitle mb-2 pt-2 text-muted">Last mod: '+data.last_mod+'</small>'+
                            '<br>'+
                            '<p class="card-text">'+shortText+'</p>'+
                            '<button type="button" class="btn btn-outline-primary">View Card</button>'+
                        '</div>'+
                    '</div>'+
                '</div>'
            )
        },
        error: function(xhr,errmsg,err){
            console.log("below is the error msg")
            console.log(xhr.status + ": " + xhr.responseText);
        }
      })
    });
});