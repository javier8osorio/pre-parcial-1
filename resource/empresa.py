from flask_restful import Resource, reqparse
from logic.empresa_logic import EmpresaLogic


class empresa(Resource):
    def __init__(self):
        self.empresa_put_args = self.createParser()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombre", type=str, help="nombre de la empresa")
        args.add_argument(
            "email de contacto", type=str, help="contacto email de la empresa"
        )
        args.add_argument("ingresos", type=int, help="ingresos de la empresa")
        args.add_argument("egresos", type=int, help="egresos de la empresa")
        return args

    def get(self, id):
        logic = EmpresaLogic()
        result = logic.getEmpresaId(id)
        if len(result) == 0:
            return {}

        return result[0], 200

    def post(self, id):
        logic = EmpresaLogic()
        result = logic.getEmpresaId(id)
        if len(result) == 0:
            return {}

        return result[0], 200

    def put(self, id):
        logic = EmpresaLogic()
        empresa = self.empresa_put_args.parse_args()
        rows = logic.insertEmpresa(empresa)
        return {"RowsAffected": rows}, 200

    def patch(self, id):
        logic = EmpresaLogic()
        empresa = self.empresa_put_args.parse_args()
        rows = logic.updateEmpresa(id, empresa)
        return {"RowsAffected": rows}, 200

    def delete(self, id):
        logic = EmpresaLogic()
        rows = logic.deleteEmpresa(id)
        return {"RowsAffected": rows}, 200