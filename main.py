from pathlib import Path
import cmd


ESC = "\033["
BLUE = f"{ESC}34m"
RESET = f"{ESC}0m"


class Shell(cmd.Cmd):
    @property
    def prompt(self) -> str:  # type: ignore
        return f"{BLUE}{Path.cwd().name}{RESET} $ "


def main() -> None:
    try:
        Shell().cmdloop()
    except KeyboardInterrupt:
        print("\nquit")


if __name__ == "__main__":
    main()
