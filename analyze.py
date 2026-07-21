"""
analyze.py
AIJobAssistant
Version : v2.0.0
"""

from modules.analyze_service import AnalyzeService


def main():

    report = AnalyzeService().run()

    if report is None:
        return

    print()
    print("Analysis completed.")
    print(report)


if __name__ == "__main__":
    main()