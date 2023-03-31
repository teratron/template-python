"""TODO:"""
from typing import Any


class Template:
    """TODO:
    """

    name: str = "template"

    def __init__(self, **props: Any) -> None:
        """TODO:
        :param props: properties of the template projects.
        :type props: dict[str, Any]
        :return:
        :rtype:
        """

    def __str__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

    def __repr__(self) -> str:
        return f"{self.__str__()}: {self.__dict__}"

    def __dir__(self) -> list[str]:
        return (
                ["__class__", "__doc__", "__module__"]
                + [m for cls in self.__class__.mro() for m in cls.__dict__ if m[0] != "_"]
                + [m for m in self.__dict__ if m[0] != "_"]
        )
