from .interfaces import RepositoryManager


def get_memory_repos() -> RepositoryManager:
    from .bank import MemoryBankRepository, MemoryAccountRepository
    from .card import MemoryCardRepository

    return RepositoryManager(
        bank_r=MemoryBankRepository(),
        account_r=MemoryAccountRepository(),
        card_r=MemoryCardRepository(),
    )