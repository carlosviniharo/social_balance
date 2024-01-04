

def get_result_accomplishment(dict_object_value):
    """
    Populate the input dictionary with the result and
    accomplishment in the case of
    division or equal operation.
    :param dict_object_value: dict
    :return: dict
    """
    denominator = dict_object_value["iddenominador"]
    numerator = dict_object_value["idnumerador"]
    target = dict_object_value["idobjectivo"]
    operation = target.idindicador.operacion

    if denominator.tipovalor and numerator.tipovalor == 'number':
        try:
            numerator_value = float(numerator.valor)
            denominator_value = float(denominator.valor)

            if operation == 'División':
                result = numerator_value / denominator_value * 100
            elif operation == 'Igual':
                result = numerator_value

            dict_object_value["cumplimiento"] = result > target.meta
            dict_object_value["resultado"] = result

        except (ValueError, TypeError):
            dict_object_value["cumplimiento"] = False
            dict_object_value["resultado"] = None

        return dict_object_value
