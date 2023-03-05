$(document).ready(function() {
    $('#boton-ejecutar').click(function() {
      var archivo = $('#archivo-python')[0].files[0];
      var comando = 'python ' + archivo.name;
      $.ajax({
        url: '/ejecutar',
        type: 'POST',
        data: {comando: comando},
        success: function(response) {
          alert(response);
        }
      });
    });
  });
  