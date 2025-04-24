//document.getElementById('connectFormId').addEventListener('submit', function(event) {
//    event.preventDefault();
//});

function isNumberKey(evt) {
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}

function isNotNumber(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    if (charCode >= 48 && charCode <= 57) {
        return false;
    }
    return true;
}

var image = document.querySelector('.image');

image.addEventListener(click, function() {
  image.classList.toggle('show');
});
