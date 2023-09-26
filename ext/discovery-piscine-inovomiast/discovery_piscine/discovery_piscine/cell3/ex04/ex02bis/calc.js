//Calculator (With JQuery). By INovomiast

$(document).ready(function() {
    // Función para calcular el resultado
    function calcular() {
      var operador = $("#operador").val();
      var num1 = parseInt($("#num1").val());
      var num2 = parseInt($("#num2").val());
      var resultado;

      if (isNaN(num1) || isNaN(num2) || num1 < 0 || num2 < 0) {
        alert("Error :(");
        return;
      }

      switch (operador) {
        case "+":
          resultado = num1 + num2;
          break;
        case "-":
          resultado = num1 - num2;
          break;
        case "*":
          resultado = num1 * num2;
          break;
        case "/":
          // Verificar división por cero
          if (num2 === 0) {
            alert("It's over 9000!");
            return;
          }
          resultado = num1 / num2;
          break;
        case "%":
          // Verificar módulo por cero
          if (num2 === 0) {
            alert("It's over 9000!");
            return;
          }
          resultado = num1 % num2;
          break;
        default:
          alert("Error :(");
          return;
      }

      alert("El resultado es: " + resultado);
      console.log("El resultado es: " + resultado);
    }
    //Evento al hacer click
    $("#calcular").click(function(event) {
      event.preventDefault();
      calcular();
    });
});