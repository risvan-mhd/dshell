from pathlib import Path
import cmd


ESC = "\033["  # ] (NVIM)
BLUE = f"{ESC}34m"
RESET = f"{ESC}0m"


class Shell(cmd.Cmd):
    @property
    def prompt(self) -> str:  # type: ignore
        return f"\n{BLUE}{Path.cwd().name}{RESET} $ "

    # TODO: add args
    def do_ls(self, _: str) -> None:  # We don't care about the args yet
        items = [item.resolve() for item in Path.cwd().iterdir()]
        items.sort(key=lambda item: (not item.is_dir(), item.name.lower()))
        for item in items:
            color = BLUE if item.is_dir() else ""
            print(f"{color}{item.name}{RESET}")


def main() -> None:
    try:
        Shell().cmdloop()
    except KeyboardInterrupt:
        print("\nquit")


if __name__ == "__main__":
    main()
