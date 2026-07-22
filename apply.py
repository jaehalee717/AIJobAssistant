"""
apply.py

AIJobAssistant
Version : v4.0.0
"""

from modules.apply_service import ApplyService


def main():

    print("=" * 80)
    print("AIJobAssistant v4.0 - Apply Workflow")
    print("=" * 80)

    ApplyService().run()

    print()
    print("=" * 80)
    print("Apply Workflow Completed")
    print("=" * 80)


if __name__ == "__main__":
    main()