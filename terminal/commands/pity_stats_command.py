from colorama import Fore

from helpers import get_rarity_display, round_to_decimals
from models.command import Command
from models.reward_rarity import RewardRarity
from program_context import ProgramContext


class PityStatsCommand(Command):
    def __init__(self):
        super().__init__("stats", "List number of wishes since last item with rarity.", aliases=["s", "stat"])

    def print_pity_count(self):
        pity_count = ProgramContext.banner.pity_count
        epic_pity_count = pity_count[RewardRarity.epic.value]
        super_rare_pity_count = pity_count[RewardRarity.super_rare.value]
        print("--- [Pity Stats] ---")
        print(f"- You have {epic_pity_count} wishes since your last " +
              f"{get_rarity_display(RewardRarity.epic.value)} item.")
        print(f"- You have {super_rare_pity_count} wishes since your last " +
              f"{get_rarity_display(RewardRarity.super_rare.value)} item.")

    def print_probability(self):
        epic_weight = ProgramContext.banner.get_weight(RewardRarity.epic.value)
        super_rare_weight = ProgramContext.banner.get_weight(RewardRarity.super_rare.value)
        total_rarity_weight = ProgramContext.banner.total_rarity_weight
        next_epic_probability = round_to_decimals(epic_weight / total_rarity_weight * 100, 2)
        next_super_rare_probability = round_to_decimals(super_rare_weight / total_rarity_weight * 100, 2)
        print("--- [Probabilities] ---")
        print(f"- Probability of an {get_rarity_display(RewardRarity.epic.value)} item on " +
              f"your next wish is approximately {next_epic_probability}%.")
        print(f"- Probability of an {get_rarity_display(RewardRarity.super_rare.value)} item on " +
              f"your next wish is approximately {next_super_rare_probability}%.")
        print()
        print(f"{Fore.YELLOW}Notes:{Fore.RESET}")
        print("The probabilities of an epic item and a super rare item can add up to more than 100.0%.")
        print("In such case, you are guaranteed to get an epic or super rare item on your next wish.")
        print("Moreover, parts of the increased probability will be carried over to the wish after your next wish.")

    def execute(self):
        self.print_pity_count()
        self.print_probability()

