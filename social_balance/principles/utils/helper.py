

def get_result_accomplishment(dict_object_value):
    """
    Populate the input dictionary with the result and
    accomplishment in the case of
    division or equal operation.
    :param dict_object_value: dict
    :return: dict
    """
    target = dict_object_value["idobjectivo"]
    operation = target.idindicador.operacion
    numerator = dict_object_value["idnumerador"]
    result = None
    if operation == "División":
        denominator = dict_object_value["iddenominador"]
        try:
            numerator_value = float(numerator.valor)
            denominator_value = float(denominator.valor)

            result = numerator_value / denominator_value * 100

            dict_object_value["cumplimiento"] = result > float(target.meta)

        except (ValueError, TypeError):
            dict_object_value["cumplimiento"] = False

    elif operation == "Igual":
        result = numerator.valor

    elif operation == "Cumplimiento":
        dict_object_value["cumplimiento"] = True if numerator.valor == "Si" else False

    dict_object_value["resultado"] = result

    return dict_object_value