$(document).ready(function(){
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    // console.log(csrftoken);
});

function startView(button){
    var row = $(button).closest('tr');
    var id = row.find('input[name="id"]').val();
    // console.log(id);

    // adding new lines

    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    var userId = id; 

    $.ajax({
        url: 'entry-get',
        type: 'POST',
        data: {'id': userId},
        dataType: 'json',
        headers: {'X-CSRFToken': csrftoken},
        success: function(data) {
            data = JSON.parse(data.data);
            // console.log(data);  // Access the serialized data under the 'data' key
            if (Array.isArray(data) && data.length > 0) {
                const fields = data[0].fields;
            
                // Access individual values
                const uid = fields.uid;
                const title = fields.title;
                const uname = fields.uname;
                const password = fields.password;
                const url = fields.url;
                const expire = fields.expire;
                const notes = fields.notes;
            
                $('#form6Example3').val(title);
                $('#form6Example1').val(uname);
                $('#password').val(password);
                $('#form6Example4').val(url);
                // $('#form6Example5').val(entryData.tags);
                $('#form6Example6').val(expire);
                $('#form6Example7').val(notes);
                showdiv();
            } 

            // $('#form6Example3').val("hai");
            // showdiv();

            // if (data && data.length > 0) {
            //     var entryData = data[0].fields;
    
            //     // Set the values of the form elements
            //     console.log("hai".entryData.title);
            //     
            // }
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });

}

// $(document).ready(function(){
//     var csrftoken = $("[name=csrfmiddlewaretoken]").val();
//     var userId = 2; 

//     $.ajax({
//         url: 'entry-get',
//         type: 'POST',
//         data: {'id': userId},
//         dataType: 'json',
//         headers: {'X-CSRFToken': csrftoken},
//         success: function(data) {
//             console.log(data.data);  // Access the serialized data under the 'data' key
//         },
//         error: function(error) {
//             console.log('Error:', error);
//         }
//     });
// });
