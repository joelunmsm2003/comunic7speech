
  function cal() {
  try {
    var precio = parseInt(document.f.precio.value),
        descuento= parseInt(document.f.Descuento.value),
        cantidad = parseInt(document.f.cantidad.value);
    document.f.precio_total.value = (precio-descuento)cantidad;
  } catch (e) {
  }
}

