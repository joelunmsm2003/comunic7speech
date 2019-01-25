

function closeSelf(){
  self.close();
  return true;
}

function traeinfomoto(){

    var x = document.getElementById("atiende").value;
   
    document.getElementById('wnumero').value=x ; 
   
    console.log('atiende..',x)
   }
   
   function cal() {
   
   
     try {
   
       console.log('entre oibches.......')
     
   
       var a = parseInt(document.getElementById("inputPrecio").value),
           cant= parseInt(document.getElementById("inputP").value),
           b = parseInt(document.getElementById("inputDesc").value),
           n=100,
   
           c = parseInt(document.getElementById("inputP").value);
   
   
           // console.log ('descuentasosss',des=(a-((b/n)*a)))
   
           console.log ('descuentasosss',des=((a-b)*c))
           //gmail= 'https://www.google.com/maps/search/'
           
       
       console.log(a,b,c)
   
          console.log ('total',des)
   
       document.getElementById("inputTotal").value =des;
       //document.getElementById("Map").value =gmail;
     } catch (e) {
     }
   }
   

   
   function traemodelos() {
   
   
         var x = document.getElementById("marca").value;
         var modelo_v = document.getElementById("modelo").value;      
         var cliente = document.getElementById("cliente").value;
         var apellido_p = document.getElementById("apellido_p").value;
         var apellido_m = document.getElementById("apellido_m").value;
         var dni = document.getElementById("dni").value;
         var telefono_1 = document.getElementById("telefono_1").value;
         var telefono_2 = document.getElementById("telefono_2").value;
         var version = document.getElementById("inputVersion").value;
         var audio = document.getElementById("audio").value;
         var anio = document.getElementById("inputAnio").value;
         var color = document.getElementById("inputColor").value;
   
         var cilindrada = document.getElementById("inputCili").value;
         var kilom = document.getElementById("inputkilo").value;
         var placa = document.getElementById("inputZip").value;
         var cant_ba = document.getElementById("inputP").value;
         var modelo = document.getElementById("modelo_b").value;
         var marca_b = document.getElementById("marca_b").value;
         var status = document.getElementById("status").value;
         var mapa = document.getElementById("Map").value;
        
         // var direccion = document.getElementById("direccion").value;
   
        
   
       window.location.href = "/colasIN/dashboard/?marca="+x+'&modelo_v='+modelo_v+'&cliente='+
       cliente+'&apellido_p='+apellido_p+'&apellido_m='+apellido_m+'&dni='+dni+'&telefono_1='+telefono_1+'&telefono_2='+telefono_2+
       '&marca_b='+marca_b+'&version='+version+'&anio='+anio+
       '&color='+color+'&cilindrada='+cilindrada+'&kilometraje='+kilom+
       '&placa='+placa+'&cant_ba='+cant_ba+'&modelo='+modelo+'&status='+status+
       '&mapa='+mapa+'&audio='+audio;
       $("#modelo").focus(); 
   
       }


      
       $(document).ready(function(){
        $("#modelo").click(function(){
    
          $("#inputVersion").focus();
        });
      });
   

  
      $(document).ready(function(){
        $(".opt").click(function(){
    
          $("cantidad").focus();
        });
      });
   
   
   
   function guardadireccion(){
   
   
      try {
     var direccion=document.getElementById("inpuguardatRF").value;
     var gmail=document.getElementById("Map").value;
   
   
     console.log(direccion)
   
     
           
           // console.log ('descuentasosss',des=(a-((b/n)*a)))
   
     console.log ('descuentasosss',direccion)
     gmail= 'https://www.google.com/maps/search/'+direccion
           
       
      
   document.getElementById("Map").value =gmail;
   
     } catch (e) {
     }
   }
   
  
   

   
   
     $(document).ready(function(){
       $("#bboleta").click(function(){
   
         $('#ffactura1').hide()
         $('#descripcion').hide()
          $('#bboleta1').show()
          $('#descripcion').show()
          $('#modal').show()
       });
     });
   
   
   
     $(document).ready(function(){
       $("#ffactura").click(function(){
   
           $('#bboleta1').hide()
           $('#ffactura1').hide()
          $('#descripcion').show()
          $('#ffactura1').show()
          $('#descripcion').show()
          $('#modal').show()
       });
   
     });
   
   //con esto le quitas accion a la tecla enter
   $(document).ready(function() {
       $("#formulario").keypress(function(e) {
           if (e.which == 13) {
               return false;
           }
       });
   });
   
   
   //CON ESTO ASE Q CILINDRADA TE DE PUNTOS DE  SEPARADOR DE MILL
$(document).ready(function(){
   $("#inputCili").on({
     "focus": function(event) {
       $(event.target).select();
     },
     "keyup": function(event) {
       $(event.target).val(function(index, value) {
         return value.replace(/\D/g, "")
           .replace(/([0-9])([0-9]{3})$/, '$1.$2')
           .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
       });
     }
   });
   });


$(document).ready(function(){   
   $("#inputkilo").on({
     "focus": function(event) {
       $(event.target).select();
     },
     "keyup": function(event) {
       $(event.target).val(function(index, value) {
         return value.replace(/\D/g, "")
           .replace(/([0-9])([0-9]{3})$/, '$1.$2')
           .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
       });
     }
   });
   
 });  
   $(document).ready(function(){
     $('#boton').click(function() {
     var a =(document.getElementById("inputime").value);
     var b = 5
     console.log('hola...q tal',a)
   
     // hora a convertir
   var t = a;
   
   
   // creamos una fecha genérica con tu tiempo
   var d = new Date("2010-01-01T"+t);
   
   
   minutos=(d.getMinutes()+5).toString()
   
   horas=(d.getHours().toString())
   
   // aumenta 5 min
   
   if (d.getMinutes()+5>=60){
   
     minutos='00:00'
   
     horas = d.getHours()+1
   
     if (horas>=24){
   
       console.log('ENtre............')
   
       horas=0
     }
   
     horas = horas.toString()
   
   }
   
   console.log('HORAS.....',d.getHours())
   
   // pinta el input
   
   if (horas.length==1){
   
       horas = '0'+horas
   }
   
    var h_exacta =horas+':'+minutos
   
   if (minutos.length==1){
   
       var h_exacta =horas+':0'+minutos
   
   }
   console.log('h_exacta',horas,minutos,h_exacta)
   
   // calculamos los minutos a partir de las horas y minutos de la fecha creada
   // var minutos = d.getHours() * 60 + d.getMinutes();
   
   // var horas= d.getHours()
   // var minutos=d.getMinutes()
   // var suma=minutos+5
   
   // console.log('horasss',horas)
   // console.log('minutitos',minutos)
   // console.log('suma',suma)
   // var h_exacta=minutos+':'+suma
   // console.log('hecho',minutos+':'+suma)
   
   
   document.getElementById("inputime").value =h_exacta;
   
   }); 
   
   }); 
   
   
   
   
   
   $(document).ready(function(){     

   $("#llmapa").click(function(){
   var mapa=document.getElementById("Map").value
      
     
       console.log('ppppppppppppp',mapa)
   
       document.getElementById("llmapa").href=mapa;
       
   });
   });
   
   
   
   
   //fechasssss
   // Para este script funcione debe útilizar las últimas librerías de jquery y jquery UI
   //CON ESTE ESCRIP ISE PARA PONER LA FECHA ACTUAL  EN UN IMPUT
  
   
    //$( "#inputFI" ).datepicker().val(fechatotal);
   // FINN CON ESTE ESCRIP ISE PARA PONER LA FECHA ACTUAL  EN UN IMPUT
   
   
   
   
$(document).ready(function(){
   $( "#gridCheck" ).click(function() {
   
     
     var nombre=document.getElementById("cliente").value+' '+document.getElementById("apellido_p").value+' '+document.getElementById("apellido_m").value;
    //  var apellido_1=document.getElementById("apellido_p").value;
    //  var apellido_2=document.getElementById("apellido_m").value;
     var dni_1=document.getElementById("dni").value;
     //var text = $('#cliente').text();
     //var text = $('#dni').text();
     
     $( "#inputNombre" ).val(nombre);
     //$( "#inputApellido_p" ).val("{{apellido_p}}");
    //  $( "#inputApellido_p" ).val(apellido_1);
   
     //$( "#inputNombre" ).val(nombre);
     //$( "#inputApellido_m" ).val("{{apellido_m}}");
    //  $( "#inputApellido_m" ).val(apellido_2);
     //$( "#inputDNI" ).val("{{dni}}");
     $( "#inputDNI" ).val(dni_1);
   console.log('patitos',nombre)
   });
  });
   
   
   
   
  
 

     $(document).ready(function(){
       $("#boleta").click(function(){
           $('#factura1').hide()
           $('#boleta1').show()
       });
      
   
   
     });
   
   
   $(document).ready(function(){
       $("#botom").click(function(){
   
         
          $('#fact').show()
       });
      
   
   
     });
   
   
   function redirect_blank(url) {
     var a = document.createElement('a');
     a.target="_blank";
     a.href=url;
     a.click();
   }
   
   function whatsApp() {
     //Sacando la fecha de hpoy 
     // var f = new Date();
     // fecha=(f.getDate() + "/" + (f.getMonth() +1) + "/" + f.getFullYear());
     // cad=f.getHours()+":"+f.getMinutes()+":"+f.getSeconds(); 
    //Sacando la fecha de hpoy 
     
     numero = $("#wnumero").val();
   
     //servicio = $("#status").val();
     marca = $("#marca").val();
     modelo = $("#modelo").val();
     //anio = $("#inputAnio").val();
   
     //color = $("#inputColor").val();
     cilindrada = $("#inputCili").val();
     inputime = document.getElementById("inputime").value;
       
     placa= $("#inputZip").val();
     cantidad = $("#inputP").val();
     bateria = $("#marca_b").val();
     modelo1 = $("#modelo_b").val();
     precio = $("#inputTotal").val();
     cliente = $("#cliente").val();
    //  apellido_p =$("#apellido_p").val();
    //  apellido_m =$("#apellido_m").val();
     dni = $("#dni").val();
     telefono_1= $("#telefono_1").val();
     telefono_2= $("#telefono_2").val();
     direccion = $("#inpuguardatRF").val();
     referencia = $("#inputRef").val();
     //pago = $("#comprobante").val();
     //documento = $("#inputRef").val();
     ruc = $("#inputRUC").val();
     razon_s = $("#inputRazon").val();
     direccion_rs = $("#inputDrs").val();
   
     direccion_1 = $("#inputDrs").val();
     nom_cli = $("#inputNombre").val();
     apellido_1 = $("#inputApellido_p").val();
     apellido_2 = $("#inputApellido_m").val();
     dni_1 = $("#inputDNI").val();
     fecha_in= $("#inputFI").val();
     gmaps = $("#Map").val();
     //atiende = $("#atiende").val();
     //almacen = $("#almacen").val();
     var anio = $("#inputAnio option:selected").text();
     var servicio = $("#status option:selected").text();
     var color = $("#inputColor option:selected").text();
     var pago = $("#comprobante option:selected").text();
     var atiende = $("#atiende option:selected").text();
     var almacen = $("#almacen option:selected").text();
    
   var documento='';
   
   
   if(ruc === ''){
       documento='Boleta'
      
   }else{
     documento='Factura'
    //Las validaciones que necesitas hacer
   }
     d = new Date(fecha_in);
   
   var day = d.getDate()+1;
   var month = d.getMonth()+1;
   var year = d.getFullYear();
     
     
       var url='https://wa.me/'
       +numero+'?text=FECHA++++++++:++++++++'+day+"/"+month+"/"+year+'%0D%0A'+
       '%20HORA++++++++:++++++++'+inputime+'%0D%0A'+
       '%20SERVICIO++++++++:++++++++'+servicio+'%0D%0A'+
       '%20VEHICULO++++++++:++++++++'+marca+'%0D%0A'+
       '%20MODELO++++++++:++++++++'+modelo+'%0D%0A'+
       '%20AÑO++++++++:++++++++'+anio+'%0D%0A'+
       '%20COLOR++++++++:++++++++'+color+'%0D%0A'+
       '%20MOTOR++++++++:++++++++'+cilindrada+'%0D%0A'+
       '%20PLACA++++++++:++++++++'+placa+'%0D%0A'+
       '%20CANTIDAD++++++++:++++++++'+cantidad+'%0D%0A'+
       '%20BATERIA++++++++:++++++++'+bateria+'%0D%0A'+
       '%20MODELO++++++++:++++++++'+modelo1+'%0D%0A'+
       '%20PRECIO++++++++:++++++++'+precio+'%0D%0A'+
       '%20CLIENTE++++++++:++++++++'+cliente+'%0D%0A'+
       '%20DNI++++++++:++++++++'+dni+'%0D%0A'+
       '%20TELEFONOS++++++++:++++++++'+telefono_1+'%20  %20'+telefono_2+'%0D%0A'+
       '%20DIRECCION++++++++:++++++++'+direccion+'%0D%0A'+
       '%20REFERENCIA++++++++:++++++++'+referencia+'%0D%0A'+
       '%20PAGO++++++++:++++++++'+pago+'%0D%0A'+
       '%20DOCUMENTO++++++++:++++++++'+documento+'%0D%0A'+
       '%20RUC++++++++:++++++++'+ruc+'%0D%0A'+
       '%20RAZON+SOCIAL++++++++:++++++++'+razon_s+'%0D%0A'+
       '%20DIRECCION_RAZON_SOCIAL++++++++'+direccion_rs+'%0D%0A'+
       '%20DIRECCION++++++++:++++++++'+direccion_1+'%0D%0A'+
       '%20CLIENTE++++++++:++++++++'+nom_cli+apellido_1+'%20  %20'+apellido_2+'%20  %20'+dni_1+'%0D%0A'+
       '%20GMAP++++++++:++++++++'+gmaps+'%0D%0A'+
       '%20ATIENDE++++++++:++++++++'+atiende+'%0D%0A'+
       '%20ALMACEN++++++++:++++++++'+almacen
   
       //var url='https://wa.me/'+numero+'?text=Hola%20esto%20es%20un%20mensaje%20para%3A%0A-Mi%20prima%0A-Mi%20gatito%0A-Mi%20Loquita'
       // 51994307859
       // 51994307959
   
       redirect_blank(url)
   
   
   
   }
   
   
   // $( "button" ).click(function() {
   //   var text = $( this ).text();
   //   $( "#input" ).val( text );
   // });
   
   
   
   // var today = new Date();
   
   // var day = today.getDate();
   // var month = today.getMonth() + 1;
   // var year = today.getFullYear();
   
   // if (day < 10) {
   //   day = '0' + day
   // }
   // if (month < 10) {
   //   month = '0' + month
   // }
   
   // var out = document.getElementById("output");
   
   // out.innerHTML = day + "/" + month + "/" + year;
   
   
   
   
   
   
   
   // //FECHA
   
   
   
   
   
   
   
   // $( ".rr" ).click(function() {
   //   var text = $('#inputRF').text();
   //   console.log(text) 
   // $( "#inputDirec" ).val(text);
     
   // });
   
   
   // function guardadireccion(data){
   
   
   //  console.log(data)
   
   //  var direccion=data
   
   //   $( "#gridCheckdireccion" ).click(function() {
   
   
   //   console.log('entre putitas')
   
   
   //   $( "#inputDirec" ).val(direccion);
   
   
   // }
   
   
   
   
   
   
   //   function cal() {
   
   
   //   try {
   
   //     console.log('entre oibches.......')
     
   
   //     var a = parseInt(document.getElementById("inputPrecio").value),
   //         b = parseInt(document.getElementById("inputDesc").value),
   
   //         c = parseInt(document.getElementById("inputP").value);
           
       
   //     console.log(a,b,c)      
   //     document.getElementById("inputTotal").value =(a-b)*c;
   //   } catch (e) {
   //   }
   // }
   
   
   
   
   //     function traemodelos() {
   
   
   //       var x = document.getElementById("marca").value;
   //       var cliente = document.getElementById("cliente").value;
   //       var apellido_p = document.getElementById("apellido_p").value;
   //       var apellido_m = document.getElementById("apellido_m").value;
   //       var dni = document.getElementById("dni").value;
   //       var telefono_1 = document.getElementById("telefono_1").value;
   //       var telefono_2 = document.getElementById("telefono_2").value;
   //       var direccion = document.getElementById("telefono_2").value;
        
   
   //     window.location.href = "/dashboard/?marca="+x+'&cliente='+cliente+'&apellido_p='+apellido_p+'&apellido_m='+apellido_m+'&dni='+dni+'&telefono_1='+telefono_1+'&telefono_2='+telefono_2+'&direcccion='+direccion
   
   
   
   //     }
   
   
   
   
   //   $(document).ready(function(){
   //     $("#bboleta").click(function(){
   
   //       $('#ffactura1').hide()
   //       $('#descripcion').hide()
   //        $('#bboleta1').show()
   //        $('#descripcion').show()
   
   //     });
      
   
   
   //   });
   
   //   $(document).ready(function(){
   //     $("#ffactura").click(function(){
   
   //         $('#bboleta1').hide()
   //         $('#ffactura1').hide()
   //        $('#descripcion').show()
   //        $('#ffactura1').show()
   //        $('#descripcion').show()
   //     });
      
   
   
   //   });
   