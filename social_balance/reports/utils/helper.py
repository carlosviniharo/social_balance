import os
from io import BytesIO

from django.http import HttpResponse
from docxtpl import DocxTemplate


current_directory = os.getcwd()
url = os.path.join(current_directory, "reports", "templates", "docx", "socialBalanceTemplate.docx")


def create_report(principles_dict_list, objects_reports_dic_list):
    report_docx_dic = {principles_dic["descripcionprincipio"]: [{"codigoprincipio": principles_dic["codigoprincipio"]}]
                       for principles_dic in principles_dict_list}
    for objects_reports_dic in objects_reports_dic_list:
        if objects_reports_dic.get("cumplimiento") is not None:
            if report_docx_dic.get(objects_reports_dic.get("descripcionprincipio")):
                report_docx_dic[objects_reports_dic["descripcionprincipio"]].append(objects_reports_dic)

    # Create a Word document
    doc_social_balance = DocxTemplate(url)

    context_example = {"Author": "Carlos",
                       "data": report_docx_dic
                       }
    doc_social_balance.render(context_example)

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
