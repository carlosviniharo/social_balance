import re

from rest_framework.exceptions import APIException

LOGIC_OPERATORS = {
    "greater_than": lambda x, y: x > y,
    "less_than": lambda x, y: x < y,
    "equal_greater": lambda x, y: x >= y,
    "default": lambda x, y: False,
}

#
# def get_result_accomplishment(dict_object_value):
#     """
#     Populate the input dictionary with the result and
#     accomplishment in the case of
#     division or equal operation.
#     :param dict_object_value: dict
#     :return: dict
#     """
#     target = dict_object_value["idobjectivo"]
#
#     if not target.is_applicable:
#         dict_object_value["cumplimiento"] = None
#         dict_object_value["is_complete"] = True
#         return dict_object_value
#
#     if target.meta == "N/A":
#         raise APIException("Please set up an objects after coming from 'no applicable'")
#
#     indicator = target.idindicador.descripcionindicador
#     operation = target.idindicador.operacion
#     logic_operator = target.logica
#     numerator = dict_object_value["idnumerador"]
#     pattern_search_percentage = r'\bPorcentaje\b'
#     result = []
#
#     if operation == "División":
#         denominator = dict_object_value["iddenominador"]
#         try:
#             numerator_value = float(numerator.valor)
#             denominator_value = float(denominator.valor)
#
#         except (ValueError, TypeError):
#             raise APIException(
#                     detail="Invalid numerator and denominator",
#                 )
#
#         is_percentage = re.match(pattern_search_percentage, indicator)
#
#         if is_percentage:
#             result.append(numerator_value / denominator_value * 100)
#             if denominator_value.is_integer() and numerator_value.is_integer():
#                 result.append(int(denominator_value - numerator_value))
#             else:
#                 result.append(denominator_value - numerator_value)
#             result.append(100 - result[0])
#
#         else:
#             result.append(numerator_value / denominator_value)
#
#         dict_object_value["cumplimiento"] = (
#             LOGIC_OPERATORS
#             .get(logic_operator, LOGIC_OPERATORS["default"])(result[0], float(target.meta))
#         )
#
#     elif operation == "División - 1":
#         denominator = dict_object_value["iddenominador"]
#         try:
#             numerator_value = float(numerator.valor)
#             denominator_value = float(denominator.valor)
#
#             result.append(((numerator_value / denominator_value) - 1) * 100)
#
#             dict_object_value["cumplimiento"] = (
#                 LOGIC_OPERATORS
#                 .get(logic_operator, LOGIC_OPERATORS["default"])(result[0], float(target.meta))
#             )
#
#         except (ValueError, TypeError):
#             dict_object_value["cumplimiento"] = False
#
#     elif operation == "Igual":
#         try:
#             numerator_value = float(numerator.valor)
#         except (ValueError, TypeError):
#             raise APIException(f"Invalid value for numerator as it musts be a number")
#
#         if numerator_value.is_integer:
#             result.append(int(numerator.valor))
#         else:
#             result.append(numerator_value)
#
#         dict_object_value["cumplimiento"] = (
#             LOGIC_OPERATORS
#             .get("equal_higher")(float(result[0]), float(target.meta))
#         )
#
#     elif operation in ["Selección", "Texto"]:
#         result.append(numerator.valor)
#         dict_object_value["cumplimiento"] = numerator.valor.lower() != "no"
#
#     elif operation == "Cumplimiento":
#         dict_object_value["cumplimiento"] = numerator.valor == target.meta
#
#     dict_object_value["resultado"] = result
#
#     return dict_object_value


class ResultAccomplishmentCalculator:
    """
    Handles the operations that each indicator depending on its type, being the types:
    Cumplimiento, Texto, Selección, Igual, División - 1 and División.
    """
    pattern_search_percentage = r'\bPorcentaje\b'

    def __init__(self, dict_object_value):
        self.dict_object_value = dict_object_value
        self.target = dict_object_value["idobjectivo"]
        self.logic_operator = self.target.logica
        self.indicator = self.target.idindicador.descripcionindicador
        self.proportion_operator = self.target.idindicador.relacionproporcion
        self.result = []

    def handle_division_operation(self, numerator):
        denominator = self.dict_object_value["iddenominador"]
        try:
            numerator_value = float(numerator.valor)
            denominator_value = float(denominator.valor)

        except (ValueError, TypeError):
            raise APIException(
                    detail="Invalid numerator and denominator",
                )

        if self.proportion_operator == "Porcentaje":
            self.result.append(numerator_value / denominator_value * 100)
            if denominator_value.is_integer() and numerator_value.is_integer():
                self.result.append(int(denominator_value - numerator_value))
            else:
                self.result.append(denominator_value - numerator_value)
            self.result.append(100 - self.result[0])

        elif self.proportion_operator == "Promedio":
            self.result.append(numerator_value / denominator_value)

        elif self.proportion_operator == "Promedio_Procentaje":
            self.result.append((numerator_value / denominator_value) * 100)

        self.dict_object_value["cumplimiento"] = (
            LOGIC_OPERATORS
            .get(self.logic_operator, LOGIC_OPERATORS["default"])(self.result[0], float(self.target.meta))
        )

    def handle_division_minus_1_operation(self, numerator):
        denominator = self.dict_object_value["iddenominador"]
        try:
            numerator_value = float(numerator.valor)
            denominator_value = float(denominator.valor)

            self.result.append(((numerator_value / denominator_value) - 1) * 100)

            self.dict_object_value["cumplimiento"] = (
                LOGIC_OPERATORS
                .get(self.logic_operator, LOGIC_OPERATORS["default"])(self.result[0], float(self.target.meta))
            )

        except (ValueError, TypeError):
            self.dict_object_value["cumplimiento"] = False

    def handle_equal_operation(self, numerator):
        try:
            numerator_value = float(numerator.valor)
        except (ValueError, TypeError):
            raise APIException(f"Invalid value for numerator as it musts be a number")

        if numerator_value.is_integer:
            self.result.append(int(numerator.valor))
        else:
            self.result.append(numerator_value)

        self.dict_object_value["cumplimiento"] = (
            LOGIC_OPERATORS
            .get("equal_higher")(float(self.result[0]), float(self.target.meta))
        )

    def handle_selection_or_text_operation(self, numerator):
        self.result.append(numerator.valor)
        self.dict_object_value["cumplimiento"] = numerator.valor.lower() != "no"

    def handle_cumplimiento_operation(self, numerator):
        self.dict_object_value["cumplimiento"] = numerator.valor == self.target.meta

    def get_result_accomplishment(self):
        if not self.target.is_applicable:
            self.dict_object_value["cumplimiento"] = None
            self.dict_object_value["is_complete"] = True
            return self.dict_object_value

        if self.target.meta == "N/A":
            raise APIException("Please set up an object after coming from 'no applicable'")

        operation_handlers = {
            "División": self.handle_division_operation,
            "División - 1": self.handle_division_minus_1_operation,
            "Igual": self.handle_equal_operation,
            "Selección": self.handle_selection_or_text_operation,
            "Texto": self.handle_selection_or_text_operation,
            "Cumplimiento": self.handle_cumplimiento_operation
        }

        operation = self.target.idindicador.operacion
        numerator = self.dict_object_value["idnumerador"]

        if operation in operation_handlers:
            operation_handlers[operation](numerator)
        else:
            raise APIException(f"Unsupported operation: {operation}")

        self.dict_object_value["resultado"] = self.result
        return self.dict_object_value

