from django.shortcuts import render

# Create your views here.
def miTienda(request):
    return render(request,'ejercicioApp/tienda.html')


def electronica(request):
    data={
        'seccion':'Electronica',
        'productos':[
            {
                'id':1,
                'nombre':'Smartphone',
                'descripcion':'Telefono inteligente con camara de 48MP',
                'precio':'$800',
                'imagen':'https://via.placeholder.com/150/ff0000'
            },
            {
                'id':2,
                'nombre':'Smartwatch',
                'descripcion':'Reloj inteligente con gps',
                'precio':'$200',
                'imagen':'https://via.placeholder.com/150/00ff00'
            },
            {
                'id':3,
                'nombre':'Tablet',
                'descripcion':'Tablet con pantalla de 10 pulgadas',
                'precio':'$500',
                'imagen':'https://via.placeholder.com/150/0000ff'
            }
        ]
    }
    return render(request, 'ejercicioApp/seccion.html', data)


def detalleProductos(request,idProducto):
    productos=[
            {
                'id':1,
                'nombre':'Smartphone',
                'descripcion':'Telefono inteligente con camara de 48MP',
                'precio':'$800',
                'imagen':'https://via.placeholder.com/150/ff0000'
            },
            {
                'id':2,
                'nombre':'Smartwatch',
                'descripcion':'Reloj inteligente con gps',
                'precio':'$200',
                'imagen':'https://via.placeholder.com/150/00ff00'
            },
            {
                'id':3,
                'nombre':'Tablet',
                'descripcion':'Tablet con pantalla de 10 pulgadas',
                'precio':'$500',
                'imagen':'https://via.placeholder.com/150/0000ff'
            }
        ]

    producto=None
    for p in productos:
        if p['id']==idProducto:
            producto=p
            break

    
    return render(request, 'ejercicioApp/detalles.html', {'producto':producto})