from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader


def get_fluent_localization() -> FluentLocalization:
    locale_dir = Path(__file__).parent.joinpath("l10n")
    if not locale_dir.exists():
        error = "'l10n' directory not found"
        raise FileNotFoundError(error)
    if not locale_dir.is_dir():
        error = "'l10n' is not a directory"
        raise NotADirectoryError(error)
    locale_file = Path(locale_dir, "locale.ftl")
    if not locale_file.exists():
        error = "locale.ftl file not found"
        raise FileNotFoundError(error)
    
    commands_file = Path(locale_dir, "commands.ftl")
    if not commands_file.exists():
        error = "commands.ftl file not found"
        raise FileNotFoundError(error)

    l10n_loader = FluentResourceLoader(
        [
            str(locale_file.absolute()),
            str(commands_file.absolute()),
        ]
    )
        
    return FluentLocalization(
        locales=["ru"],
        resource_ids=[str(locale_file.absolute()), str(commands_file.absolute())],
        resource_loader=l10n_loader
    )