import os
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

from django.http import HttpResponse
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage
import requests
from rest_framework.exceptions import APIException

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

    context = {"Author": "Carlos",
               "data": report_docx_dic
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
            width=Mm(150),
            height=Mm(75)
        )
    else:
        raise APIException(f"Failed to retrieve the image from S3. Status code: {response.status_code}")

    dict_indicators["graficocontenido"] = imagen

    dict_indicators["table"] = False
