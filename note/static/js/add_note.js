$(document).ready(function(){
    $('#addNoteModel').on('show.bs.modal', function (event) {
        var getTagList = $("#tag-list").text().split(",");
        $('[name="tags"]').tagify({
            whitelist: getTagList,
            maxTags: 10,
            dropdown: {
                // maxItems: 20,           // <- mixumum allowed rendered suggestions
                classname: "tags-look", // <- custom classname for this dropdown, so it could be targeted
                enabled: 0,             // <- show suggestions on focus
                // closeOnSelect: true,    // <- hide the suggestions dropdown once an item has been selected
                duplicates :false,
            },
        })
      })
    $(document).on('submit',"#note-form",function(e){
        e.preventDefault();
        var modal = $("#addNoteModel");
        var form = $("#note-form");
        var url = form.attr("action");
        var httpMethod = form.attr("method");
        var TagValues = JSON.parse($('[name="tags"]').tagify().val())
        var TagArray = []
        for(let i=0;i<TagValues.length;i++){
            TagArray.push(TagValues[i].value)
        }
        var dataToSend = $(this).serializeArray();
        for (let index = 0; index < dataToSend.length; ++index) {
            if (dataToSend[index].name == "tags") {
                dataToSend[index].value = TagArray;
                break;
            }
        }
        $.ajax({
        url: url,
        method: httpMethod,
        data: jQuery.param(dataToSend),
        success: function(data){
            document.getElementById("note-form").reset();
            modal.modal('toggle');
            var shortText = jQuery.trim(data.text).substring(0, 80)
            var shortTitle = jQuery.trim(data.title).substring(0, 21)
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