import os
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

from django.http import HttpResponse
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage
import requests
from rest_framework.exceptions import APIException

from principles.models import Vindicators

current_directory = os.getcwd()
url = os.path.join(current_directory, "reports", "templates", "docx", "socialBalanceTemplate.docx")


def create_report(principles_dict_list, objects_reports_dic_list):

    doc_social_balance = DocxTemplate(url)
    report_docx_dic = {principles_dic["descripcionprincipio"]: {"code": principles_dic["codigoprincipio"],
                                                                "objects": []}
                       for principles_dic in principles_dict_list}

    def process_objects(objects_reports_dic):
        if objects_reports_dic.get("cumplimiento") is not None:
            principle_key = objects_reports_dic["descripcionprincipio"]
            if principle_key in report_docx_dic:
                report_docx_dic[principle_key]["objects"].append(objects_reports_dic)
                if objects_reports_dic.get("graficotipo"):
                    retrieve_image_aws(doc_social_balance, objects_reports_dic)
                else:
                    objects_reports_dic["table"] = True

    with ThreadPoolExecutor() as executor:
        executor.map(process_objects, objects_reports_dic_list)

    summary_dic = populate_table(objects_reports_dic_list)

    context = {"Author": "Carlos",
               "data_indicators": report_docx_dic,
               "data_summary": summary_dic
               }

    doc_social_balance.render(context)

    # Save the document to a BytesIO buffer
    buffer = BytesIO()
    doc_social_balance.save(buffer)

    # Create the HttpResponse object with the appropriate content type for Word documents
    response = HttpResponse(
        buffer.getvalue(),
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    response['Content-Disposition'] = 'attachment; filename=example.docx'

    # Close the buffer
    buffer.close()
    return response


def retrieve_image_aws(template, dict_indicators):

    s3_url = dict_indicators.get("graficocontenido")
    response = requests.get(s3_url)

    if response.status_code == 200:
        imagen = InlineImage(
            template,
            image_descriptor=BytesIO(response.content),
            width=Mm(130),
            height=Mm(65)
        )
    else:
        raise APIException(f"Failed to retrieve the image from S3. Status code: {response.status_code}")

    dict_indicators["graficocontenido"] = imagen

    dict_indicators["table"] = False


def populate_table(objects_reports_dic_list):

    indicators_overview = {
        "sum_values": {
            "sum_all_indicators": 0,
            "sum_indicators_not_applying": 0,
            "sum_indicators_accomplished": 0,
            "sum_indicators_failed": 0,
            "sum_accomplishment": 0.0
        }
    }

    all_indicators = Vindicators.objects.all()

    # Sum of all the indicators
    sum_all_indicators = len(all_indicators)
    indicators_overview["sum_values"]["sum_all_indicators"] = sum_all_indicators

    for indicators in all_indicators:
        indicators_overview.setdefault(
            indicators.codigoprincipio,
            {
                "total_indicators": 0,
                "indicators_not_applying": 0,
                "indicators_accomplished": 0,
                "indicators_failed": 0,
                "accomplishment_percentage": 0,
             }
        )
        indicators_overview[indicators.codigoprincipio]["total_indicators"] += 1

    for indicators_values in objects_reports_dic_list:
        codeprinciple = indicators_values.get("codigoprincipio")
        accomplishment = indicators_values.get("cumplimiento")

        if not codeprinciple:
            raise APIException("The report is empty, it does not have any record")

        if accomplishment is None:
            indicators_overview[codeprinciple]["indicators_not_applying"] += 1
            indicators_overview["sum_values"]["sum_indicators_not_applying"] += 1

        elif accomplishment is True:
            indicators_overview[codeprinciple]["indicators_accomplished"] += 1
            indicators_overview["sum_values"]["sum_indicators_accomplished"] += 1

        elif accomplishment is False:
            indicators_overview[codeprinciple]["indicators_failed"] += 1
            indicators_overview["sum_values"]["sum_indicators_failed"] += 1

        valid_indicators = (
                indicators_overview[codeprinciple]["total_indicators"] -
                indicators_overview[codeprinciple]["indicators_not_applying"]
        )
        percentage_accomplishment = (
            indicators_overview[codeprinciple]["indicators_accomplished"] /
            valid_indicators
                                    ) * 100
        indicators_overview[codeprinciple]["accomplishment_percentage"] = round(percentage_accomplishment, 2)

    all_valid_indicators = sum_all_indicators - indicators_overview["sum_values"]["sum_indicators_not_applying"]
    indicators_overview["sum_values"]["sum_accomplishment"] = round(
        (indicators_overview["sum_values"]["sum_indicators_accomplished"] / all_valid_indicators) * 100,
        2
    )

    return indicators_overview
