from dialogs.dialog_menu import show_menu
from services.test_case_service import TestCaseService
from repository.test_case_repository import TestCaseRepository
from models.test_case import TestCase
from models.test_steps import TestSteps

def main():
    repository = TestCaseRepository()
    service = TestCaseService(repository)

    while True:
        choice = show_menu()

        if choice == "1":
            print("\n### Lägg till ett testfall ###")
            tc_id = input ("Ange id (t.ex. TC-01): ")
            title = input ("Ange titel: ")
            data = input ("Ange testdata: ")

            steps = []
            while True:
                step_instructions = input ("Ange steg i instruktionen (eller tryck Enter för att avsluta): ")
                if not step_instructions:
                    break
                step_expected_result = input ("Ange förväntat resultat för detta steg: ")

                new_step = TestSteps(instructions=step_instructions, expected_result=step_expected_result)                
                steps.append(new_step)
                print("Steg tillagt!\n")

            new_tc = TestCase(
                id=tc_id,
                title=title,
                data=data,
                steps=steps
            )

            service.try_add_test_case(new_tc)
            print(f"Testfall '{title}' har sparats med {len(steps)} st teststeg!\n")
            input("Tryck Enter för att fortsätta till menyn...")

        elif choice == "2":
            print("\n### Visa testfallen ###")
            cases = service.get_all_test_cases()

            if not cases:
                print("Inga testfall sparade ännu.")
            else:
                for tc in cases:
                    print(tc)

            input("Tryck Enterför att fortsätta tillmenyn...")

            for tc in cases:
                print(tc)

        elif choice == "3":
            print("\n### Uppdatera testfall ###")
            tc_id = input("Ange ID på det testfall du vill uppdatera: ")

            existing_tc = service.get_by_id(tc_id)
            if existing_tc:
                print(f"Hittade testfall {existing_tc.title}")
                new_title = input("Ange ny titel: ")
                new_data = input("Ange ny testdata: ")

                updated_tc = TestCase(
                    id=tc_id,
                    title=new_title,
                    data=new_data,
                    steps=existing_tc.steps
                )

                service.update_test_case(tc_id, updated_tc)
                print(f"Testfall {tc_id} har uppdaterats!\n")
            else:
                print(f"Hittade inget testfall med ID {tc_id}.\n")

            input("tryck Enter för att fortsätta till menyn.")

        elif choice == "4":
            print("\n### Ta bort testfall ###")
            tc_id = input("Ange ID på det testfall som du vill ta bort: ")

            existing_tc = service.get_by_id(tc_id)
            if existing_tc:
                service.delete_test_case(tc_id)
                print(f"Testfall {tc_id} har tagits bort!\n")
            else:
                print(f"Hittade inget testfall med ID {tc_id}.\n")

            input("tryck Enter för att fortsätta till menyn.")

        elif choice == "0":
            print("\nAvsluta programmet")
            break

        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()
