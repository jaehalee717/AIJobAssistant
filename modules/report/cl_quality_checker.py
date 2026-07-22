"""
modules/report/cl_quality_checker.py

AIJobAssistant
Version : v1.0.0
"""


class CLQualityChecker:

    def __init__(
        self,
    ):
        pass


    def validate(
        self,
        document,
    ):

        if document is None:

            return False


        if not hasattr(
            document,
            "paragraphs",
        ):

            return False


        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )


        if not text.strip():

            return False


        return True


    def check(
        self,
        document,
    ):

        return self.validate(
            document,
        )