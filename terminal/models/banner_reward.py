from models.item_name import ItemName
from models.reward_rarity import RewardRarity


class BannerReward:
    """
    Represent one banner reward.
    """
    name: str
    quantity: int
    weight: int
    rarity: str

    def __init__(self, name: ItemName, quantity: int = 1, weight: int = 1, rarity: str = RewardRarity.common):
        self.name = name.value
        self.quantity = quantity
        self.weight = weight
        self.rarity = rarity

    def __str__(self):
        return f"{self.name}, {self.quantity}, {self.rarity}"