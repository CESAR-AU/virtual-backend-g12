from config import validador
from marshmallow import fields, pre_load, validate, validates

class PaginacionRequestDTO(validador.Schema):
    page = fields.Integer(required=False, load_default=1)
    perPage = fields.Integer(required=False, load_default=10)

    '''@validates('page')
    def validate_page(self, value):
        if value <= 0:
            self.page = 1
    
    @pre_load(pass_many=True)
    def remove_envelope(self, data, many, **kwargs):
        namespace = 'results' if many else 'result'
        return data[namespace]'''