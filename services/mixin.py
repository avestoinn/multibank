from .interfaces import RepositoryManager, ServiceManager


def get_services(repo_manager: RepositoryManager) -> ServiceManager:
    return ServiceManager(
        repo_manager=repo_manager
    )