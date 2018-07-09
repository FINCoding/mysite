$(document).ready(function(){
    var form = $('#form-test')
    console.log(form)
    form.on('submit', function(e){
        e.preventDefault();
    })
})