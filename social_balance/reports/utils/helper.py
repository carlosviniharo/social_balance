import os
from io import BytesIO

from django.http import HttpResponse
from docxtpl import DocxTemplate


current_directory = os.getcwd()
url = os.path.join(current_directory, "reports", "templates", "docx", "socialBalanceTemplate.docx")


def create_report(principles_dict):
    # Create a Word document
    doc_social_balance = DocxTemplate(url)
    principles_maped = [
        (principle["codigoprincipio"], principle["descripcionprincipio"])
        for principle in principles_dict
    ]

    context_example = {"Author": "Carlos",
                       "principles": principles_maped
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
