from core.pyba_logic import PybaLogic


class EmpresaLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertEmpresa(self, empresa):
        database = self.databaseObj
        sql = (
            "INSERT INTO `progra`.`empresa` (`id`, `nombre`, `email`,`ingresos`,`egresos`)"
            + f"VALUES (0, '{empresa['nombre']}', '{empresa['email']}', {empresa['ingresos']}, {empresa['egresos']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getEmpresaId(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM progra.empresa where id = {id};"
        result = database.executeQuery(sql)
        return result

    def updateEmpresa(self, id, empresa):
        database = self.databaseObj
        sql = (
            "UPDATE `progra`.`empresa`"
            + f"SET `nombre` = '{empresa['nombre']}', `email` = '{empresa['email']}', `ingresos` = {empresa['ingresos']}, `egresos` = {empresa['egresos']}"
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteEmpresa(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `progra`.`empresa` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows
