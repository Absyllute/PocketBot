from typing import Optional, Tuple, List

def init_db() -> None: ...

def setup_join_links(
    guild_id: int,
    java_link: str,
    bedrock_link: str,
    bedrock_port: int,
    embed_title: str,
    embed_desc: str,
) -> None: ...

def remove_join_links(guild_id: int) -> None: ...

def check_join_links(
    guild_id: int,
) -> Optional[
    Tuple[
        Optional[str],
        Optional[str],
        Optional[int],
        str,
        Optional[str],
    ]
]: ...

def add_modrole(guild_id: int, role_id: int) -> None: ...

def remove_modrole(guild_id: int, role_id: int) -> None: ...

def check_modroles(guild_id: int) -> List[int]: ...