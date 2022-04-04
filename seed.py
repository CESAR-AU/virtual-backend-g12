from models.categorias import ModelCategoria
from config import conexion
from  sqlalchemy import or_

def categoriasSeed():
    categorias = conexion.session.query(ModelCategoria).filter(
        or_(ModelCategoria.nombre == 'OCIO', ModelCategoria.nombre == 'COMIDA', ModelCategoria.nombre == 'EDUCACION', ModelCategoria.nombre == 'VIAJES')
    ).first()

    if categorias is None:
        nombres = ['OCIO', 'COMIDA', 'EDUCACION', 'VIAJES']
        try:
            for categoria in nombres:
                nueva_categoria = ModelCategoria(nombre=categoria)
                conexion.session.add(nueva_categoria)
            conexion.session.commit()
            print('Categorias creadas exitosamente')
        except Exception as ex:
            conexion.session.rollback()
            print('Error al alimentar la db', ex.args)
