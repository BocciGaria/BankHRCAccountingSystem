from Interface.fields import IField
from Interface.models import IModel


class ClubMemberModel(IModel):
    """クラブ会員クラス

    クラブに入会している利用者を実装します。
    """

    __columns: tuple[IField] = ()
    __primarykey: tuple[IField] = ()


if __name__ == "__main__":
    m1 = ClubMemberModel()
    print(m1.__dict__)
