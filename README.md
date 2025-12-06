sale_cookies

Módulo personalizado para gestionar ventas de emprendimientos pequeños de galletas.
Actualmente permite registrar ventas con todos los datos necesarios y una buena base para crecer con nuevas funcionalidades.

Este módulo es creado principalmente para llevar un control de las ventas en un emprendimiento pequeño de galletas. No se utiliza el módulo sale que viene estandar de odoo ya que se busca una personalización versátil ajustada a cada emprendimiento, en este caso aplicado a el mío propio, manteniendo registros simples y puntuales.

Características Actuales:

Registro de ventas con campos esenciales (cliente, producto, cantidad, gramaje, precio unitario, fecha, total).

Campo computado que calcula el total de la venta multiplicando la cantidad por el precio unitario, el cual varía según el gramaje. Ej: 100g = 2$, 50g = 1$.

Interfaz simple con vista tipo list y form.

Control básico de estado: pendiente o pagado.

Estructura Técnica 

Modelos:
`models/sale_cookies.py`: Modelo principal para órdenes de venta.

Vistas:
`views/sale_cookies_view.xml`: Vistas list y form.

Datos:
`data/sale_cookies_menus.xml`:
Menu.

Seguridad:
`security/ir.model.access.csv`: Permisos.

Manifest:
`__manifest__.py`: Dependencias, metadata y carga del módulo.

Instalación:

1. Clonar o copiar el módulo en la carpeta `addons`.
2. Actualizar lista de módulos en Odoo.
3. Buscar “Sale Cookies” y activar.
4. Verificar permisos y acceso.

Autor:
Manuel Jauregui
