from ..exception.exception import BaseExceptionParent


class SupplyCreationException(BaseExceptionParent):
    """Raised when creating a supply fails."""

    def __init__(self, message="Failed to create supply."):
        super().__init__(message)


class SupplyEditException(BaseExceptionParent):
    """Raised when editing a supply fails."""

    def __init__(self, message="Failed to edit supply."):
        super().__init__(message)


class SupplyDeleteException(BaseExceptionParent):
    """Raised when deleting a supply fails."""

    def __init__(self, message="Failed to delete supply."):
        super().__init__(message)
