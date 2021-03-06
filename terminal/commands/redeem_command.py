from colorama import Fore

from constants.item_ids import ITEM_IDS
from models.command import Command
from program_context import ProgramContext


class RedeemCommand(Command):
    def __init__(self):
        super().__init__("redeem", "Redeem your rewards and clear your current inventory.")

    def execute(self):
        prop_map = ProgramContext.user_stats.properties

        print("--- [Redeem Commands] ---")
        for item_name, quantity in prop_map.items():
            if quantity > 0:
                print(f"habits transaction create --property-id {ITEM_IDS[item_name]} -t \"[Redeem] Wish Rewards\" " +
                      f"-a {quantity}")

        ProgramContext.user_stats.properties = {}
        ProgramContext.user_stats.audit_properties()
        ProgramContext.save_user_stats()
        print("--- [Note] ---")
        print(Fore.YELLOW + "NOTE: Your wish properties have been cleared. Be sure to copy the commands above and" +
                            " run them immediately.")
