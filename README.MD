# Restaurante App (version 4)

## Estudiante
Gordon Ortega Henri Daniel

## Descripción

Aplicación desarrollada en Python utilizando Programación Orientada a Objetos para administrar productos y clientes de un restaurante mediante un menú interactivo ejecutado desde consola.

## Estructura del proyecto

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

## Constructor

La clase Producto utiliza el constructor tradicional `__init__()` para inicializar sus atributos.

## Uso de @property y @setter

Se emplean para controlar y validar el acceso a los atributos nombre, categoría y precio.

## Uso de @dataclass

La clase Cliente utiliza `@dataclass`, permitiendo generar automáticamente métodos especiales.

## Menú interactivo

Permite registrar, listar y buscar productos y clientes desde consola.

## Reflexión

La creación de objetos mediante datos ingresados por el usuario permite construir aplicaciones más dinámicas y cercanas a situaciones reales, aplicando correctamente los principios de encapsulación y organización modular.
