
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})




setTimeout(function(){ 
  var alert = document.querySelector('.alert');
  if (alert) {
    alert.remove()
  }; }, 3000);

