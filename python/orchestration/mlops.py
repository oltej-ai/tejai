from orchestration import OrchestrationBase


class MLOPS(OrchestrationBase):
    def __init_subclass__(OrchestrationBase) -> None:
        pass

    def get_connector():
        pass

    def get_definitions():
        pass

    def get_workflow():
        pass
