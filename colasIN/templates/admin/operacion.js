
  function cal() {
  try {
    var a = parseInt(document.f.precio.value),
        b = parseInt(document.f.Descuento.value),
        c = parseInt(document.f.cantidad.value);
    document.f.precio_total.value = a+b;
  } catch (e) {
  }
}

