import re

from rest_framework.exceptions import APIException


def get_result_accomplishment(dict_object_value):
    """
    Populate the input dictionary with the result and
    accomplishment in the case of
    division or equal operation.
    :param dict_object_value: dict
    :return: dict
    """
    target = dict_object_value["idobjectivo"]

    if not target.is_applicable:
        dict_object_value["cumplimiento"] = None
        return dict_object_value
    if target.meta == "N/A":
        raise APIException("Please set up an objects after coming from 'no applicable'")

    indicator = target.idindicador.descripcionindicador
    operation = target.idindicador.operacion
    numerator = dict_object_value["idnumerador"]
    pattern_search_percentage = r'\bPorcentaje\b'
    result = []

    if operation == "División":
        denominator = dict_object_value["iddenominador"]
        try:
            numerator_value = float(numerator.valor)
            denominator_value = float(denominator.valor)

        except (ValueError, TypeError):
            raise APIException(
                    detail="Invalid numerator and denominator",
                )

        is_percentage = re.match(pattern_search_percentage, indicator)

        if is_percentage:
            result.append(numerator_value / denominator_value * 100)
            if denominator_value.is_integer() and numerator_value.is_integer():
                result.append(int(denominator_value - numerator_value))
            else:
                result.append(denominator_value - numerator_value)
            result.append(100 - result[0])

        else:
            result.append(numerator_value / denominator_value)

        dict_object_value["cumplimiento"] = result[0] > float(target.meta)

    elif operation == "División - 1":
        denominator = dict_object_value["iddenominador"]
        try:
            numerator_value = float(numerator.valor)
            denominator_value = float(denominator.valor)

            result.append(((numerator_value / denominator_value) - 1) * 100)

            dict_object_value["cumplimiento"] = result[0] > float(target.meta)

        except (ValueError, TypeError):
            dict_object_value["cumplimiento"] = False

    elif operation == "Igual":
        try:
            numerator_value = float(numerator.valor)
        except (ValueError, TypeError):
            raise APIException(f"Invalid value for numerator as it musts be a number")

        if numerator_value.is_integer:
            result.append(int(numerator.valor))
        else:
            result.append(numerator_value)

        dict_object_value["cumplimiento"] = float(result[0]) >= float(target.meta)

    elif operation in ["Selección", "Texto"]:
        result.append(numerator.valor)
        dict_object_value["cumplimiento"] = numerator.valor.lower() != "no"

    elif operation == "Cumplimiento":
        dict_object_value["cumplimiento"] = numerator.valor == target.meta

    dict_object_value["resultado"] = result

    return dict_object_value
